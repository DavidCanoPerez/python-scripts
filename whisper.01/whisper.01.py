# -*- coding: utf-8 -*-

"""
 probando whisper
 
 pip install -U openai-whisper
 pip install ffmpeg
 
 a partir de audio extrae texto
"""

import whisper

model = whisper.load_model("base")
result = model.transcribe("audio.mp3")
print(result["text"])

