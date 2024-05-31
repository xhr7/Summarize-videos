# Summarize-videos








In today’s fast-paced world, many individuals find it challenging to allocate time to watch lengthy videos. This difficulty results in a significant gap in accessing and utilizing information efficiently, which is critical for both personal and professional development. Additionally, people with hearing impairments encounter considerable accessibility issues with video content, as standard videos do not always include accessible features such as subtitles or sign language interpretations. These challenges underscore the urgent need for a solution that makes video content more manageable and accessible to a wider audience, ensuring that all users, regardless of their time constraints or sensory abilities, can benefit from important audiovisual information.


To address the challenges of information accessibility and consumption efficiency, my project is developing a web application that leverages advanced AI technology to enhance how users interact with video content. 

<img width="390" alt="image" src="https://github.com/xhr7/Summarize-videos/assets/102740867/1f2b7ea4-50f9-4df4-8031-4d2083e1e8ef">



# Model Development Pipeline

## Data Collection and Sources

### Data Source
- **Dataset:** CNN/DailyMail dataset from Hugging Face.
- **Content:** Over 300,000 news articles from CNN and the Daily Mail.
- **Purpose:** Ideal for training text summarization models due to diverse topics and writing styles.

### Data Structure and Content
- **ID:** Unique SHA1 hash of the article's URL.
- **Article:** Full text of the news article.
- **Highlights:** Author-written summaries of the articles, used as targets for model training.

## Data Pre-processing
- **Training Set:** 50,000 instances for diverse content exposure.
- **Validation Set:** 10,000 instances for model tuning.
- **Testing Set:** 50 instances to evaluate summarization performance.

### Pre-processing Steps
- Remove URLs: Using regex to eliminate noise from URLs.
- Normalize Whitespace: Ensuring consistency by normalizing spaces.

## Model Development Pipeline
This section details each stage of our workflow, from initial input to final output.

### Stage 1: Video to Audio Conversion
- **Input:** Video files (e.g., MP4, AVI).
- **Process:** Use FFmpeg via ffmpeg-python to convert videos to WAV audio format.
- **Output:** High-quality audio files in WAV format.

### Stage 2: Audio Transcription
- **Input:** Audio files in WAV format.
- **Process:**
  - Preprocessing the Audio: Reduce noise using the noisereduce library.
  - Transcription: Employ OpenAI's Whisper model to transcribe audio to text.
- **Output:** Text representation of the audio content.

### Stage 3: Text Summarization
- **Input:** Transcribed text.
- **Process:**
  - Text Cleaning: Remove URLs and extra whitespace.
  - Tokenization: Use the T5 tokenizer to prepare text for the model.
  - Model Training: Fine-tune the T5-small model using Hugging Face’s Trainer API.
- **Output:** Summarized text that concisely represents the original content.

### Stage 4: Interface
I used the Flask framework to build the interface. I also used CSS and HTML 

I will now attach a link to a drive in which the model has been trained for 50,000. You can now try it without retraining the model 

You just have to put it in the same flash code file and the template

https://drive.google.com/drive/folders/1xhbMRrMkBtpHghe_RDds3_INHdYszT9V?usp=sharing


### Demo

https://github.com/xhr7/Summarize-videos/assets/102740867/fd953949-c39a-4d61-ac73-8e6a0372596c


### Evaluation

The project analyses reveal that while the model successfully identifies key concepts, it significantly struggles to translate these into coherent, accurate, and fluent summaries, evidenced by consistently low recall, BLEU, and METEOR scores. The model's performance indicates a need for further tuning and training, potentially with a richer variety of source content or an enhanced focus on linguistic structure to improve its summarization capabilities. Despite accurately capturing certain elements, the summaries are notably incomplete, highlighting the system's challenge in fully encapsulating the breadth of the original content.
