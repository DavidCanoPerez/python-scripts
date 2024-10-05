# -*- coding: utf-8 -*-

"""
probando speechr

pip install SpeechRecognition
pip install moviepy
install pyaudio

a partir de video, extrae audio y extrae texto

límite de 10 megas
incluir video.mp4 en el que se hable
"""

import speech_recognition as sr
import moviepy.editor as mp

clip = mp.VideoFileClip("video.mp4")
clip.audio.write_audiofile("extracted_audio.wav")

r = sr.Recognizer()

audio = sr.AudioFile("extracted_audio.wav")

with audio as source:
    r.adjust_for_ambient_noise(source)
    audio_file = r.record(source)

result = r.recognize_google(audio_file, language="es_ES")

with open('recognized_text.txt', 'w') as file:
    file.write("RECOGNIZED SPEECH: \n")
    file.write(result)

print("\n COMPLETED")