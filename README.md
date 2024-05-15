# IlewaAI App
Benin Multimodal Hackhaton

# Project for Image Generation from Local Languages
This project uses a series of technologies to transcribe speech into text, translate this text, and generate images from the translated text. The complete pipeline includes the following steps:
1. **Speech to text transcription** with [MMS (Meta Speech-to-Text)](https://github.com/facebookresearch/fairseq/tree/main/examples/mms)
2. **Text Translation** with [NLLB (No Language Left Behind)](https://github.com/facebookresearch/flores).
3. **Image generation** from translated text with [Stable Diffusion](https://github.com/CompVis/stable-diffusion).
4. **Display of the generated image** with [Streamlit](https://streamlit.io/).
## Table des matières
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Used Technologies](#used technologies)
- [Contribution](#contribution)
- [Licence](#licence)
## Installation
To run this project locally, follow the following steps: :
1. Clone this repository: :
  ```bash
  git clone
https://github.com/votre-utilisateur/votre-depot.git
  cd votre-depot
  ```
2. Create and activate a virtual environment: :
  ```bash
  python -m venv env
  source env/bin/activate  # On Windows, use `env\Scripts\activate`
  ```
3. Install the dependencies: :
  ```bash
  pip install -r requirements.txt
  ```
## Usage
1. **Launching the application:** :
  ```bash
  streamlit run ismo.py
  ```
2. **User Interface:** :
  - **Upload** : Upload an audio file containing speech in the local language.
  - **Transcription** : The speech is transcribed into text using MMS.
  - **Traduction** : The text is translated into a language supported by Stable Diffusion using NLLB.
  - **Génération d'image** : An image is generated from the translated text with Stable Diffusion.
  - **Affichage** : The generated image is displayed via the Streamlit interface.
## Used technologies
- **MMS (Meta Speech-to-Text)** :  For the transcription of speech into text..
- **NLLB (No Language Left Behind)** : For the translation of text.
- **Stable Diffusion** : For generating images from text descriptions.
- **Streamlit** : For creating the user interface and displaying the results.
3. **User Interface** :
  - **Interface** : We have deployed the application on streamlit cloud: the link to access it is : https://ilewaai.streamlit.app/
  - **API** : We have deployed APIs for each model we use and we call these files in our ismo.py to perform the transcriptions and translations. These models have been deployed via Azure Container Instances thanks to their Docker image. This allows anyone to run our code even if they do not have the necessary computing power.
  - **Fon to French translation model**: api : 'http://fon-t2t-api.francecentral.azurecontainer.io/'  and github: 'https://github.com/Ggasyd/fon-t2t-api'
  -  **Fon to French transcription model** : api : 'http://fon-s2t-api.francecentral.azurecontainer.io/' et github: 'https://github.com/Ggasyd/fon-api'
  -  **Yoruba to English transcription model** : api : 'http://yoruba-s2t-api.francecentral.azurecontainer.io/' et github : 'https://github.com/Ggasyd/ilewa-api'
  -  **Devcontainer**: Setting up a devcontainer to ensure that users can have access to the same dependencies

