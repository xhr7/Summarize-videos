from flask import Flask, request, jsonify, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from moviepy.editor import VideoFileClip
import whisper
from transformers import T5ForConditionalGeneration, T5Tokenizer
import re

# Initialize the Flask application
app = Flask(__name__)

# Configuration for file upload
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'avi', 'mov'}

# Load the Whisper model for transcription
whisper_model = whisper.load_model("base")

# Load the fine-tuned T5 model for summarization
dir_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(dir_path, 'fine_tuned_t5_50k')
t5_model = T5ForConditionalGeneration.from_pretrained(model_path)
t5_tokenizer = T5Tokenizer.from_pretrained(model_path)

def allowed_file(filename):
    """Check if the file's extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def clean_text(text):
    """Clean the text for summarization."""
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def summarize_text(text):
    """Generate a summary for the provided text."""
    cleaned_text = clean_text(text)
    input_ids = t5_tokenizer.encode("summarize: " + cleaned_text, return_tensors="pt")
    summary_ids = t5_model.generate(input_ids, max_length=150, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = t5_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

@app.route('/', methods=['GET', 'POST'])
def upload_video():
    """Handle the video upload and redirect to transcription."""
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return redirect(url_for('transcribe', filename=filename))
    return render_template('upload.html')

@app.route('/transcribe/<filename>', methods=['GET'])
def transcribe(filename):
    """Transcribe the audio extracted from the video."""
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    video_clip = VideoFileClip(filepath)
    audio_path = "temp_audio.wav"
    video_clip.audio.write_audiofile(audio_path)
    transcription = whisper_model.transcribe(audio_path)['text']
    return render_template('transcription.html', transcription=transcription, filename=filename)

@app.route('/summarize/<filename>', methods=['GET'])
def show_summary(filename):
    """Display the summary of the transcription."""
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    video_clip = VideoFileClip(filepath)
    audio_path = "temp_audio.wav"
    video_clip.audio.write_audiofile(audio_path)
    transcription = whisper_model.transcribe(audio_path)['text']
    summary = summarize_text(transcription)
    return render_template('summary.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
