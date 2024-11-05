# -*- coding: utf-8 -*-
"""YouTube Transcript Summarizer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nr39rFGFfAROXr_7aqecjJgIlsUvt0nA
"""

!pip install -q transformers

!pip install -q youtube_transcript_api

from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

youtube_video = "https://www.youtube.com/watch?v=2iOlM9XdOYo"

video_id = youtube_video.split("=")[1]

video_id

from IPython.display import YouTubeVideo
YouTubeVideo(video_id)

YouTubeTranscriptApi.get_transcript(video_id)
transcript = YouTubeTranscriptApi.get_transcript(video_id)

transcript[0:5]

result = ""
for i in transcript:
  result += ' '+i['text']

print(len(result))

summarizer = pipeline('summarization')

num_iters = int(len(result)/1000)
summarized_text = []
for i in range(0,num_iters+1):
  start=0
  start = i*1000
  end = (i+1) * 1000
  out = summarizer(result[start:end])
  out = out[0]
  out = out['summary_text']
  summarized_text.append(out)

print(summarized_text)

str(summarized_text)