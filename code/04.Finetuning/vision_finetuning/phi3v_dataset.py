import copy
import json
from pathlib import Path

import torch
from PIL import Image
from torch.utils.data import Dataset

IGNORE_INDEX = -100


def pad_sequence(sequences, padding_side='right', padding_value=0):
    """
    Pad a list of sequences to the same length.
    sequences: list of tensors in [seq_len, *] shape
    """
    assert padding_side in ['right', 'left']
    max_size = sequences[0].size()
    trailing_dims = max_size[1:]
    max_len = max(len(seq) for seq in sequences)
    batch_size = len(sequences)
    output = sequences[0].new_full((batch_size, max_len) + trailing_dims, padding_value)
    for i, seq in enumerate(sequences):
        length = seq.size(0)
        if padding_side == 'right':
            output.data[i, :length] = seq
        else:
            output.data[i, -length:] = seq
    return output


class Phi3VDataset(Dataset):
    def __init__(self, jsonl_file: str, image_dir: str, processor):
        self.image_dir = Path(image_dir)
        with open(jsonl_file) as f:
            self.examples = [json.loads(line) for line in f]
        self.processor = processor

    def __len__(self):
        return len(self.examples)

    def shard(self, num_shards, shard_id):
        num_data = len(self.examples)
        sharded = copy.deepcopy(self)
        sharded.examples = [self.examples[i] for i in range(shard_id, num_data, num_shards)]
        return sharded

    def _get_inputs(self, user_text, image_paths):
        images = [Image.open(self.image_dir / image_path) for image_path in image_paths]
        image_tag_text = ''.join([f'<|image_{i}|>' for i in range(1, len(images) + 1)])

        prompt_message = {'role': 'user', 'content': f'{image_tag_text}\n{user_text}'}
        prompt = self.processor.tokenizer.apply_chat_template(
            [prompt_message], tokenize=False, add_generation_prompt=True
        )
        inputs = self.processor(prompt, images, return_tensors='pt')
        return inputs

    def __getitem__(self, idx):
        example = self.examples[idx]

        all_input_ids = []
        all_labels = []
        all_pixel_values = []
        all_image_sizes = []
        for turn in example['conversations']:
            inputs = self._get_inputs(turn['user'], turn['images'])
            prompt_input_ids = inputs['input_ids']

            assistant_text = turn['assistant']
            response = f'{assistant_text}<|end|>\n<|endoftext|>'
            # Do not add bos token to answer
            response_input_ids = self.processor.tokenizer(
                response, add_special_tokens=False, return_tensors='pt'
            )['input_ids']

            input_ids = torch.cat([prompt_input_ids, response_input_ids], dim=1).squeeze(0)
            labels = torch.cat(
                [
                    torch.tensor([IGNORE_INDEX] * len(prompt_input_ids[0])),
                    response_input_ids.squeeze(0),
                ],
                dim=0,
            )

            all_input_ids.append(input_ids)
            all_labels.append(labels)
            all_pixel_values.append(inputs['pixel_values'])
            all_image_sizes.append(inputs['image_sizes'])

        input_ids = torch.cat(all_input_ids, dim=0)
        labels = torch.cat(all_labels, dim=0)
        pixel_values = torch.cat(all_pixel_values, dim=0)
        image_sizes = torch.cat(all_image_sizes, dim=0)

        return {
            'id': example['id'],  # unique identifier for the example
            'input_ids': input_ids,
            'labels': labels,
            'pixel_values': pixel_values,
            'image_sizes': image_sizes,
        }


class Phi3VDataCollator:
    def __init__(self, pad_token_id: int):
        self.pad_token_id = pad_token_id

    def __call__(self, examples):
        batch_input_ids = []
        batch_label_ids = []
        batch_pixel_values = []
        batch_image_sizes = []
        for example in examples:
            batch_input_ids.append(example['input_ids'])
            batch_pixel_values.append(example['pixel_values'])
            batch_image_sizes.append(example['image_sizes'])
            batch_label_ids.append(example['labels'])

        input_ids = pad_sequence(
            batch_input_ids, padding_side='right', padding_value=self.pad_token_id
        )
        attention_mask = input_ids != self.pad_token_id
        labels = pad_sequence(batch_label_ids, padding_side='right', padding_value=IGNORE_INDEX)
        pixel_values = torch.cat(batch_pixel_values, dim=0)
        image_sizes = torch.cat(batch_image_sizes, dim=0)

        return {
            'input_ids': input_ids,
            'labels': labels,
            'attention_mask': attention_mask,
            'pixel_values': pixel_values,
            'image_sizes': image_sizes,
        }


class Phi3VEvalDataset(Phi3VDataset):
    def __getitem__(self, idx):
        example = self.examples[idx]

        messages = []
        all_images = []
        for i, turn in enumerate(example['conversations']):
            image_paths = turn['images']
            user_text = turn['user']
            assistant_text = turn['assistant']

            images = [Image.open(self.image_dir / image_path) for image_path in image_paths]
            image_tag_text = ''.join([f'<|image_{i}|>' for i in range(1, len(images) + 1)])

            prompt_message = {'role': 'user', 'content': f'{image_tag_text}\n{user_text}'}
            messages.append(prompt_message)
            all_images.extend(images)

            if i + 1 == len(example['conversations']):
                break

            response_message = {
                'role': 'assistant',
                'content': f'{assistant_text}<|end|>\n<|endoftext|>',
            }
            messages.append(response_message)

        prompt = self.processor.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self.processor(prompt, all_images, return_tensors='pt')
        answer = example['conversations'][-1].get('assistant', None)

        return {
            'id': example['id'],  # unique identifier for the example
            'input_ids': inputs['input_ids'].squeeze(0),
            'pixel_values': inputs['pixel_values'],
            'image_sizes': inputs['image_sizes'],
            'answer': answer
        }


class Phi3VEvalDataCollator(Phi3VDataCollator):
    def __call__(self, examples):
        unique_ids = []
        batch_input_ids = []
        batch_pixel_values = []
        batch_image_sizes = []
        answers = []
        for example in examples:
            unique_ids.append(example['id'])
            batch_input_ids.append(example['input_ids'])
            batch_pixel_values.append(example['pixel_values'])
            batch_image_sizes.append(example['image_sizes'])
            answers.append(example['answer'])

        input_ids = pad_sequence(
            batch_input_ids, padding_side='left', padding_value=self.pad_token_id
        )
        attention_mask = input_ids != self.pad_token_id
        pixel_values = torch.cat(batch_pixel_values, dim=0)
        image_sizes = torch.cat(batch_image_sizes, dim=0)

        return {
            'unique_ids': unique_ids,
            'input_ids': input_ids,
            'attention_mask': attention_mask,
            'pixel_values': pixel_values,
            'image_sizes': image_sizes,
            'answers': answers,
        }
