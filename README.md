<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

<h1>YouTube Recapulator</h1>
<h2>An AI-Powered Video Summarization Tool</h2>
<p>
  <span class="highlight">YouTube Recapulator</span> is an AI-based application that summarizes YouTube video transcripts to provide users with concise overviews. It leverages <strong>Hugging Face's transformers</strong> for text summarization and <strong>YouTube Transcript API</strong> to retrieve video transcripts.
</p>

<h3>Features</h3>
<ul>
  <li>📄 <strong>Automated Transcript Extraction:</strong> Retrieves video transcripts from YouTube for analysis.</li>
  <li>⚡ <strong>AI-Powered Summarization:</strong> Uses advanced NLP models to summarize long videos into concise content.</li>
  <li>💼 <strong>Enhanced Viewing Experience:</strong> Saves time by providing an overview of the video’s content.</li>
  <li>📝 <strong>Text-Based:</strong> Ideal for environments where audio playback is restricted.</li>
</ul>

<div class="section">
  <h3>How It Works</h3>
  <p>
    The application performs the following steps:
  </p>
  <ul>
    <li>🔹 <strong>Extract Transcript:</strong> Extracts the transcript using the video URL.</li>
    <li>🔹 <strong>Generate Summarization:</strong> Summarizes the transcript into shorter text snippets.</li>
    <li>🔹 <strong>Display Summary:</strong> Shows the summarized content for easy reading.</li>
  </ul>
</div>

<div class="section">
  <h3>Usage</h3>
  <p>To run the application:</p>
  <h4>Prerequisites</h4>
  <p>Install the following Python libraries:</p>
  <code>pip install transformers youtube_transcript_api</code>

  <h4>Example Code</h4>
  <pre>
  <code>
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

youtube_video = "https://www.youtube.com/watch?v=2iOlM9XdOYo"
video_id = youtube_video.split("=")[1]
transcript = YouTubeTranscriptApi.get_transcript(video_id)

result = ""
for i in transcript:
  result += ' ' + i['text']

summarizer = pipeline('summarization')
num_iters = int(len(result)/1000)
summarized_text = []

for i in range(0, num_iters + 1):
  start = i * 1000
  end = (i + 1) * 1000
  out = summarizer(result[start:end])[0]['summary_text']
  summarized_text.append(out)

print(summarized_text)
  </code>
  </pre>
</div>

<div class="section">
  <h3>Sample Output</h3>
  <p>A sample output might look like:</p>
  <p><em>"The greatest treasure by Ahmed Garg: Peter found a treasure map and set off on an adventure. He made friends along the way, overcoming obstacles together, and in the end, they realized that their friendship was the greatest treasure of all."</em></p>
</div>

<div class="section">
  <h3>Future Enhancements</h3>
  <ul>
    <li>🖥️ <strong>GUI Integration:</strong> User-friendly graphical interface for input and output.</li>
    <li>🌐 <strong>Multilingual Support:</strong> Summarize content in various languages.</li>
    <li>🔊 <strong>Voice Output:</strong> Option to read out the summary.</li>
    <li>⚙️ <strong>Custom Summarization Models:</strong> Select between different summarization models.</li>
  </ul>
</div>

<div class="section">
  <h3>Technologies Used</h3>
  <ul>
    <li>🐍 <strong>Python:</strong> Core language for the application.</li>
    <li>🤗 <strong>Transformers (Hugging Face):</strong> NLP library for summarization.</li>
    <li>🎥 <strong>YouTube Transcript API:</strong> Retrieves YouTube transcripts.</li>
  </ul>
</div>

<div class="section">
  <h3>License</h3>
  <p>This project is licensed under the <strong>MIT License</strong>.</p>
</div>

</body>
</html>
