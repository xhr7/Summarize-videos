# Summarize-videos

https://github.com/xhr7/Summarize-videos/assets/102740867/fd953949-c39a-4d61-ac73-8e6a0372596c



In today’s fast-paced world, many individuals find it challenging to allocate time to watch lengthy videos. Additionally, people with hearing impairments encounter accessibility issues due to the lack of captions or transcripts. These challenges highlight the need for a solution that makes video content more accessible, efficient, and inclusive.

This project introduces a web application that uses advanced AI models to:
- Convert video to text
- Summarize the transcribed content
- Present the result in a clean, simple interface

<img src="https://github.com/xhr7/Summarize-videos/assets/102740867/1f2b7ea4-50f9-4df4-8031-4d2083e1e8ef" width="500"/>



## Model Development Pipeline

| Stage            | Input         | Process                                                                 | Output                        |
|------------------|---------------|-------------------------------------------------------------------------|-------------------------------|
| Video to Audio   | MP4, AVI      | Convert video to WAV using `ffmpeg-python`                             | WAV audio file                |
| Audio Transcription | WAV audio   | Denoise using `noisereduce`, transcribe using OpenAI Whisper           | Raw text                      |
| Text Summarization | Transcribed text | Clean text, tokenize using T5 tokenizer, fine-tune `t5-small` model    | Concise summary               |
| Web Interface    | Final summary | Build frontend using Flask + HTML/CSS                                   | User-friendly display         |



## Data Collection

- **Dataset:** CNN/DailyMail from Hugging Face  
- **Instances:**  
  - Training: 50,000  
  - Validation: 10,000  
  - Testing: 50  
- **Data Fields:**  
  - `article`: Full news text  
  - `highlights`: Human-written summaries



## Preprocessing

- Removed URLs using regex
- Normalized whitespace for consistency
- Cleaned audio before transcription
- Used tokenizer compatible with T5 model


## Evaluation Summary

The model shows a basic ability to identify key ideas but struggles with generating fluent and complete summaries — which is expected at this stage. Due to the use of a lightweight model (T5-small) and limited fine-tuning, results often lack coherence, miss important details, and produce partial outputs. These challenges are common when working with real-world audio transcriptions and can be improved by using stronger models, more diverse training data, and better linguistic handling.






## System Stack

- Python
- Hugging Face Transformers
- T5-small model
- OpenAI Whisper
- noisereduce
- Flask
- HTML / CSS


## Getting Started

### Prerequisites

- Python 3.10+
- pip installed libraries: `transformers`, `torch`, `flask`, `ffmpeg-python`, `noisereduce`, `openai-whisper`

###  Step 1:Installation

```bash
git clone https://github.com/xhr7/Summarize-videos.git
cd Summarize-videos
```



### Step 2: Download the Pretrained Model

Before running the app, download the pretrained model from the following link:  
📦 [Google Drive – Trained Model](https://drive.google.com/drive/folders/1xhbMRrMkBtpHghe_RDds3_INHdYszT9V?usp=sharing)

> Place the downloaded files in the main project directory, next to the Flask code and templates.

---

### Step 3: Install Dependencies

Make sure you have Python 3.10+, then install all required libraries:

```bash
pip install -r requirements.txt

```

Step 4: Run the App 
```bash
python app.py
```
