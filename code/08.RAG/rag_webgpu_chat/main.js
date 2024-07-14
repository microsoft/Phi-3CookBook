import { env, AutoTokenizer,pipeline, cos_sim } from '@xenova/transformers';
import { RAG } from './rag.js';
import { Phi3SLM } from './phi3_slm.js';
import { marked } from 'marked';



const fileContents = [];
const kbContents = [];
let rag;


document.getElementById('send-button').addEventListener('click', async function() {
  const inputBox = document.querySelector('.input-box');
  const question = inputBox.value.trim();
  
  if (question) {
      const chatContainer = document.querySelector('.chat-container');
      const userMessage = document.createElement('div');
      userMessage.className = 'message question';
      userMessage.textContent = question;
      chatContainer.appendChild(userMessage);

      inputBox.value = '';

      try {
          const answer = await generateAnswer(question);

          const summary = await generativeSummary(answer);


          const botMessage = document.createElement('div');
          botMessage.className = 'message answer';
          botMessage.textContent = summary;
          chatContainer.appendChild(botMessage);


          chatContainer.scrollTop = chatContainer.scrollHeight;
      } catch (error) {
          console.error('Error fetching answer:', error);
      }
  }
});

async function generateAnswer(question) {
  
  return rag.getEmbeddings(question,kbContents);
}

async function generativeSummary(answer) {


  let prompt = `<|system|>\nYou are a friendly assistant. Help me summarize answer of the knowledge points<|end|>\n<|user|>\n${answer}<|end|>\n<|assistant|>\n`;

  let summary = await rag.generateSummaryContent(prompt);

  return summary;

}





async function getEmbeddings(content) {  


  const progressContainer = document.getElementById('progress-container');
  progressContainer.style.display = 'block';
  document.getElementById('overlay').style.display = 'none';
  document.getElementById('addMarkdown').textContent = '+';
  // progressBar.style.width = '0%';


  let prompt_template = `
  
      Extract the input according to the following conditions, keep the knowledge points, summarize the detailed content of the knowledge points and delete the content related to the picture before outputting, please keep the content related to the link when outputting

      Starting with # , ## , ### is a knowledge point, All knowledge points must be output and cannot be missing, such as

      [INPUT]
      # ABC
      ...............

      ## CDF 
      ..........
      ### GGG
      .....
      [END INPUT]

      [OUTPUT]
      [{"KB": "ABC", "Content":"..............."},{"KB": "CDF", "Content":".........."},{"KB": "GGG", "Content":"....."}]
      [END OUTPUT]

      [INPUT]
      # ABC
      ...............

      ### GGG
      .....

      ### www
      .....

      [END INPUT]

      [OUTPUT]
      [{"KB": "ABC", "Content":"..............."},{"KB": "GGG", "Content":"....."},{"KB": "www", "Content":"....."}]
      [END OUTPUT]


      [INPUT]
    ` + content 
      + 
    `
      [END INPUT]

     [OUTPUT]`;

  
  let prompt = `<|system|>\nYou are a markdown assistant. Help me to get knowledge in markdown file<|end|>\n<|user|>\n${prompt_template}<|end|>\n<|assistant|>\n`;

  let json_result = await rag.generateEmbeddingsContent(prompt);

  const jsonObject = JSON.parse(json_result);


  for(const content of jsonObject) {
    console.log(content);
    kbContents.push(content.KB+'-'+content.Content);

  }

  // alert(kbContents.length);

  if (kbContents.length > 0) {
    document.getElementById('chat-message').style.display = 'block';
    document.getElementById('progress-container').style.display = 'none';
  }

}



//
// embedding markdown content
//

document.getElementById('upload-form').addEventListener('submit', async function(event) {
  event.preventDefault();
  const fileInput = document.getElementById('file-input');
  const files = fileInput.files;

  if (files.length === 0) {
      alert('Please upload at least one file.');
      return;
  }

  for (const file of files) {
      const text = await file.text();
      fileContents.push(text);
      console.log(text);
  }

  document.getElementById('progress-container').display = 'block';

  var embeddd = await getEmbeddings(fileContents[0]);

  console.log('11234'+embeddd);


  document.getElementById('overlay').style.display = 'none';
  document.getElementById('addMarkdown').textContent = '+';

  document.getElementById('chat-message').display = 'block';
  document.getElementById('progress-container').display = 'none';

});

//
// markdown file upload
//
document.getElementById('addMarkdown').addEventListener('click', function() {
  const overlay = document.getElementById('overlay');
  if (overlay.style.display === 'none') {
      overlay.style.display = 'flex';
      this.textContent = '-';
  } else {
      overlay.style.display = 'none';
      this.textContent = '+';
  }
});


//
// Check if we have webgpu and fp16
//
async function hasWebGPU() {
  // returns 0 for webgpu with f16, 1 for webgpu without f16, 2 for no webgpu
  if (!("gpu" in navigator)) {
    return 2;
  }
  try {
    const adapter = await navigator.gpu.requestAdapter()
    if (adapter.features.has('shader-f16')) {
      return 0;
    }
    return 1;
  } catch (e) {
    return 2;
  }
}

async function Init(hasFP16) {
  try {

    if (kbContents.length === 0) {
        document.getElementById('chat-message').style.display = 'none';
    }

    rag = new RAG();
    await rag.InitPhi3SLM();
    // await rag.loadONNX();
  } catch (error) {
    console.log('InitError');
  }
}


window.onload = () => {
  hasWebGPU().then((supported) => {
    if (supported < 2) {
      if (supported == 1) {
        alert("Your GPU or Browser does not support webgpu with fp16, using fp32 instead.");
      }
      Init(supported === 0);
    } else {
      alert("Your GPU or Browser does not support webgpu");
    }
  });
}

