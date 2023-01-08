# -*- coding: utf-8 -*-

"""
    script text to speech para spyder 
    Hace uso del paquete de google gTTS para generar varios mp3

    pip install gTTS
    pip install playsound==1.2.2

    gTTS documentacion:
        https://github.com/pndurette/gTTS
        https://gtts.readthedocs.io/en/latest/        
        comando para ver que lenguajes soporta gtts en anaconda prompt
            gtts-cli --all
    
    No confundir
        google cloud tts
            Servicio de pago.
            Requiere registro.
            Con muchas funcionalidades y preparada para manejarse desde 
            cualquier lenguaje de programación
            doc:
                https://googleapis.dev/python/texttospeech/latest/index.html
                https://cloud.google.com/text-to-speech/docs/libraries#client-libraries-resources-python
        paquete gtts
            No es de pago
            Que se sepa, no se puede cambiar la velocidad de la voz.
            Según usuarios de stackoverflow:
                El módulo gTTS usa una API no documentada 
                relacionada con el servicio "Google Translate". 
                Esa API también puede pronunciar cosas, pero no está pensada 
                como servicio TTS por lo que no permite textos muy largos, 
                ni cambiar la velocidad, salvo entre el valor "normal" y "lento"
                No está pensada para ser usada por aplicaciones de terceros y ante
                muchas peticiones el servicio puede quedar suspendido.    
"""

from gtts import gTTS
from playsound import playsound
import os.path


# english
string_text = "Hello, this example is in english language"
obj1 = gTTS(string_text, lang='en')

# obtener directorio actual
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
print('Directorio actual: ' + CURRENT_DIR)

# guardar mp3
save_path1 = CURRENT_DIR + r'/ttsEnglish.mp3'
if os.path.isfile(save_path1):
    None
else:
    obj1.save(save_path1)

# reproducir mp3
print("Reproduce voz INGLES")
playsound(save_path1)
    
# español
string_text_es = "Hola, también funciona en español"
obj2 = gTTS(string_text_es, lang='es')

# guardar mp3
save_path2 = CURRENT_DIR + r'/ttsEsp.mp3'
if os.path.isfile(save_path2):
    None
else:
    obj2.save(save_path2)

# reproducir mp3
print("Reproduce voz ESPAÑOL")
playsound(save_path2)

print("No se borran los audios, permanecerán en el directorio indicado")






