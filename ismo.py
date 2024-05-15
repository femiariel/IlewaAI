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


stability_apikey=st.secrets["STABILITY_API"]

client = AzureOpenAI(
  azure_endpoint = "https://azureai-models.openai.azure.com/", 
  api_key=st.secrets["API_KEY"] ,  
  api_version="2024-02-15-preview"
) 

 
specifications = """
        - You are an expert AI translator specializing in translating text from Yoruba to English.
        - I want you to send me back only the translated text, nothing more.
        -  The input sentence is in yoruba
        - Translate the input sentence from yoruba to english please
        """

# Configuration de l'audio
CHUNK = 1024  # Nombre de frames par buffer
FORMAT = pyaudio.paInt16  # Format des échantillons audio
CHANNELS = 1  # Nombre de canaux
RATE = 16000  # Taux d'échantillonnage (échantillons par seconde)
RECORD_SECONDS = 5  # Durée d'enregistrement
 
# Initialisation de PyAudio
audio = pyaudio.PyAudio()
 
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



col1, col2 = st.columns([1, 6])

with col1:
    st.image('./52148170-conception-carte-bénin-icône-vecteur.jpg')

with col2:
    st.markdown(
        """
        <style>
        .big-title {
            font-size: 65px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        '<h1 class="big-title">'
        '<span style="color: green;">I</span>'
        '<span style="color: yellow;">l</span>'
        '<span style="color: red;">e</span>'
        '<span style="color: green;">w</span>'
        '<span style="color: yellow;">a</span>'
        '<span style="color: red;">A</span>'
        '<span style="color: green;">I</span>'
        '</h1>', 
        unsafe_allow_html=True
    )



# Fonction de sauvegarde de l'audio
def save_audio(audio_data, filename):
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(audio_data.tobytes())
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
 
# Interface Streamlit

st.markdown('<p style="font-size:25px;">Select a language and an input method to begin.</p>', unsafe_allow_html=True)

# Sélection de la langue
language = st.selectbox("Select Language", ["Yoruba", "Fon"])
 
# Choix de la méthode d'entrée
input_method = st.selectbox("Select Input Method", ["Audio", "Text", "Upload File"])

if language =="Yoruba": 
    if input_method == "Audio":
        if st.button("Start Recording"):
            audio_data = record_audio()
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmpfile:
                tmpfile_name = tmpfile.name
                save_audio(audio_data, tmpfile_name)
        
            # URL de l'API selon la langue sélectionnée
            api_url = "http://yoruba-s2t-api.francecentral.azurecontainer.io/speech-to-text/" 
            transcription = send_to_api(api_url, data={}, files={'file': open(tmpfile_name, 'rb')})
            st.write("Transcription:")
            st.write(transcription)
        
            # Traduire la transcription en français
            translation = translate_to_english(transcription)
            image= image_generation(translation)
            st.write("Translation in French:")
            st.write(translation)
            st.image(image, caption=translation)
    
    elif input_method == "Text":
        text_input = st.text_area("Enter Text")
        if st.button("Submit"):
        
            # Traduire la transcription en français
            translation = translate_to_english(text_input)
            image= image_generation(translation)
            st.write("Translation in English:")
            st.write(translation)
            st.image(image, caption=translation)

    elif input_method == "Upload File":
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmpfile:
                tmpfile_name = tmpfile.name
                tmpfile.write(uploaded_file.getvalue())
        
            # URL de l'API selon la langue sélectionnée
            api_url = "http://yoruba-s2t-api.francecentral.azurecontainer.io/speech-to-text/" 
            transcription = send_to_api(api_url, data={}, files={'file': open(tmpfile_name, 'rb')})
            st.write("Transcription:")
            st.write(transcription)
        
            # Traduire la transcription en français
            translation = translate_to_english(transcription)
            image= image_generation(translation)
            st.write("Translation in French:")
            st.write(translation)
            st.image(image)
            

if language == "Fon":
    if input_method == "Audio":
        if st.button("Start Recording"):
            audio_data = record_audio()
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmpfile:
                tmpfile_name = tmpfile.name
                save_audio(audio_data, tmpfile_name)
        
            # URL de l'API selon la langue sélectionnée
            api_url = "http://fon-s2t-api.francecentral.azurecontainer.io/speech-to-text/" 
            transcription = send_to_api(api_url, data={}, files={'file': open(tmpfile_name, 'rb')})
            st.write("Transcription:")
            st.write(transcription)
            api_translation_url="http://fon-t2t-api.francecentral.azurecontainer.io/translate/"
            request_body = {
               "text": transcription
            }
            response=requests.post(api_translation_url, json=request_body)
            response_data= response.json()
            translation=response_data.get('translated_text', 'Key not found')
            st.write("Translation in French")
            st.write(translation)
            image= image_generation(translation)
            st.image(image)

    elif input_method == "Text":
        text_input = st.text_area("Enter Text")
        if st.button("Submit"):
            request_body = {
                "text": text_input
            }
            api_translation_url="http://fon-t2t-api.francecentral.azurecontainer.io/translate/"
            response=requests.post(api_translation_url, json=request_body)
            response_data= response.json()
            translation=response_data.get('translated_text', 'Key not found')
            image=image_generation(translation)
            # Traduire la transcription en français
            st.write(translation)
            st.image(image, caption=translation)

    elif input_method == "Upload File":
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmpfile:
                tmpfile_name = tmpfile.name
                tmpfile.write(uploaded_file.getvalue())
        
            # URL de l'API selon la langue sélectionnée
            api_url = "http://fon-s2t-api.francecentral.azurecontainer.io/speech-to-text/"  
            transcription = send_to_api(api_url, data={}, files={'file': open(tmpfile_name, 'rb')})
            st.write("Transcription:")
            st.write(transcription)
            api_translation_url="http://fon-t2t-api.francecentral.azurecontainer.io/translate/"
            request_body = {
               "text": transcription
            }
            response=requests.post(api_translation_url, json=request_body)
            response_data= response.json()
            translation=response_data.get('translated_text', 'Key not found')
            st.write("Translation in French")
            st.write(translation)
            image= image_generation(translation)
            st.image(image)
    