"""
modified from https://huggingface.co/docs/transformers/tasks/video_classification
and https://huggingface.co/docs/transformers/main/en/model_doc/video_llava
"""
import argparse
import json
import pathlib
import shutil
import tarfile

import av
import numpy as np
from huggingface_hub import hf_hub_download
from PIL import Image


def read_video_pyav(container, indices):
    """
    Decode the video with PyAV decoder.
    Args:
        container (`av.container.input.InputContainer`): PyAV container.
        indices (`List[int]`): List of frame indices to decode.
    Returns:
        result (np.ndarray): np array of decoded frames of shape (num_frames, height, width, 3).
    """
    frames = []
    container.seek(0)
    start_index = indices[0]
    end_index = indices[-1]
    for i, frame in enumerate(container.decode(video=0)):
        if i > end_index:
            break
        if i >= start_index and i in indices:
            frames.append(frame)
    return np.stack([x.to_ndarray(format='rgb24') for x in frames])


def video_to_images(video_path, num_images=8):
    """
    Extracts frames from a video file.
    Args:
        video_path (str): Path to the video file.
    Returns:
        List of PIL images.
    """
    container = av.open(video_path)
    total_frames = container.streams.video[0].frames
    indices = np.arange(0, total_frames, total_frames / num_images).astype(int)
    video_array = read_video_pyav(container, indices)
    images = [Image.fromarray(frame).convert('RGB') for frame in video_array]
    return images


def main(tmp_dir, out_dir):
    hf_dataset_identifier = 'sayakpaul/ucf101-subset'
    filename = 'UCF101_subset.tar.gz'
    file_path = hf_hub_download(
        repo_id=hf_dataset_identifier, filename=filename, repo_type='dataset'
    )

    tmp_path = pathlib.Path(tmp_dir)
    tmp_path.mkdir(parents=True, exist_ok=False)
    with tarfile.open(file_path) as t:
        t.extractall(tmp_path)

    dataset_root_path = tmp_path / 'UCF101_subset'
    all_video_file_paths = (
        list(dataset_root_path.glob('train/*/*.avi'))
        + list(dataset_root_path.glob('val/*/*.avi'))
        + list(dataset_root_path.glob('test/*/*.avi'))
    )

    class_labels = sorted({str(path).split('/')[-2] for path in all_video_file_paths})
    prompt = f'Classify the video into one of the following classes: {", ".join(class_labels)}.'

    # convert all videos
    split2examples = {'train': [], 'val': [], 'test': []}
    out_path = pathlib.Path(out_dir)
    out_image_path = out_path / 'images'
    for i, video_file_path in enumerate(all_video_file_paths):
        # get train/val/test
        split = video_file_path.parts[-3]
        label = video_file_path.parts[-2]
        images = video_to_images(video_file_path)

        image_path_prefix = '/'.join(video_file_path.with_suffix('').parts[-3:])
        split2examples[split].append(
            {
                'id': f'{split}-{i:010d}',
                'source': 'ucf101',
                'conversations': [
                    {
                        'images': [
                            f'{image_path_prefix}.{i}.jpg' for i in range(len(images))
                        ],
                        'user': prompt,
                        'assistant': label,
                    }
                ],
            }
        )
        (out_image_path / image_path_prefix).parent.mkdir(parents=True, exist_ok=True)
        for i, image in enumerate(images):
            image.save((out_image_path / image_path_prefix).with_suffix(f'.{i}.jpg'))

    for split, examples in split2examples.items():
        with open(out_path / f'ucf101_{split}.jsonl', 'w') as f:
            for example in examples:
                f.write(json.dumps(example) + '\n')

    # remove tmp_path recursively
    shutil.rmtree(tmp_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--tmp_dir', type=str, default='/tmp/ucf101')
    parser.add_argument('--out_dir', type=str, default='./ucf101')
    args = parser.parse_args()

    main(args.tmp_dir, args.out_dir)
