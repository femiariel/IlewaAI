import streamlit as st
import pyaudio
import wave
import numpy as np
import tempfile
import requests
import openai
from openai import OpenAI
import os
from openai import AzureOpenAI
from io import BytesIO
from PIL import Image
from audio_recorder_streamlit import audio_recorder


 
# Fonction d'enregistrement audio
def record_audio(duration=RECORD_SECONDS):
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    st.write("Recording...")
    frames = [stream.read(CHUNK) for i in range(0, int(RATE / CHUNK * duration))]
    st.write("Recording finished.")
    stream.stop_stream()
    stream.close()
    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
    return audio_data

def image_generation(input):
    import requests

    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
        headers={
            "authorization": f"Bearer {stability_apikey}",
            "accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": input,
            "output_format": "jpeg",
        },
    )

    if response.status_code == 200:
    # Ouvrir l'image à partir des bytes et retourner l'objet image
        image = Image.open(BytesIO(response.content))
        return image
    else:
        raise Exception(str(response.json()))



# Fonction de sauvegarde de l'audio
def save_audio(audio_data, filename):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(audio_data.tobytes())
    wf.close()
 

def save_new(audio_data, filename):
    # Assumant que les données suivantes sont extraites ou sont connues :
    channels = 2  # Stéréo
    sampwidth = 2  # Largeur d'échantillon en octets (16 bits -> 2 octets)
    framerate = 16000  # Fréquence d'échantillonnage

    # Ouvrir le fichier en mode écriture binaire
    wf = wave.open(filename, 'wb')

    # Configurer les paramètres du fichier audio
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)

    # Écrire les données audio
    wf.writeframes(audio_data)  # Écrire directement les données audio sans traitement supplémentaire

    # Fermer le fichier
    wf.close()
  
def send_to_api_translation(url, data):
    response = requests.post(url, data=data)
    if response.status_code == 200:
        return response.json().get('translation', 'translation not found')
    else:
        return "Error in transcription"


# Fonction pour envoyer des données à l'API
def send_to_api(url, data, files=None):
    response = requests.post(url, data=data, files=files)
    if response.status_code == 200:
        return response.json().get('transcription', 'Transcription not found')
    else:
        return "Error in transcription"
 
def translate_to_english(text):
    prompt = "You are an Yoruba to English translator.You are an translation expert Yoruba English. The following sentence is in yoruba {text}.I want you to send me back only the translated text, nothing more."
    response = client.chat.completions.create(
            model= "gpt4-model",
            max_tokens=2000,
            messages=[
                {"role": "system", "content": f" Follow strictly these instructions: {specifications}"},
                {"role": "user", "content": text}
            ]
        )
    return response.choices[0].message.content
 
