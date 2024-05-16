# IlewaAI App
Benin Multimodal Hackhaton

# Project for Image Generation from Local Languages
This project uses a series of technologies to transcribe speech into text, translate this text, and generate images from the translated text. The complete pipeline includes the following steps:
1. **Speech to text transcription** with [MMS (Meta Speech-to-Text)](https://github.com/facebookresearch/fairseq/tree/main/examples/mms)
2. **Text Translation** with [NLLB (No Language Left Behind)](https://github.com/facebookresearch/flores).
3. **Image generation** from translated text with [Stable Diffusion](https://stability.ai/).
4. **Display of the generated image** with [Streamlit](https://streamlit.io/).
## Table of Content
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Technologies](#technologies)
- [Contribution](#contribution)
- [Licence](#licence)
## Installation
To run this project locally, follow the following steps: :
1. Clone this repository: :
  ```bash
  git clone
https://github.com/femiariel/IlewaAI.git
  cd IlewaAI
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
1. **Launching the application:** 
  ```bash
  streamlit run ismo.py
  ```
2. **User Interface:**
  - **Upload or record** : Upload or record an audio containing speech in the local language (Fon or Yoruba).
  - **Transcription** : The speech is transcribed into text using MMS.
  - **Translation** : The text is translated into a language supported by Stable Diffusion using NLLB.
  - **Image generation** : An image is generated from the translated text with Stable Diffusion.
  - **Display** : The generated image is displayed via the Streamlit interface.
## Technologies
- **MMS (Meta Speech-to-Text)** :  For the transcription of speech into text.
- **NLLB (No Language Left Behind)** : For the translation of text from fon to french.
- **Docker** : To containerize our Hugging Face models and deploy them efficiently.
- **Azure Container Instances** : To host the APIs for each model.
- **GPT-4** : For the translation of text from yoruba to english.
- **Stable Diffusion** : For generating images from text descriptions.
- **Streamlit** : For creating the user interface and displaying the results.
3. **User Interface** :

  - **Application Interface**: The application is hosted on Streamlit Cloud, accessible via this link: [https://ilewaai.streamlit.app/](https://ilewaai.streamlit.app/).

  - **API Integration**: We have deployed APIs for each model we use and call these APIs in our `ismo.py` to perform transcriptions and translations. These models are hosted using Azure Container Instances with their respective Docker images, enabling anyone to run our code regardless of their local computing power.

  - **Fon to French Translation Model**: 
    - API: [http://fon-t2t-api.francecentral.azurecontainer.io/](http://fon-t2t-api.francecentral.azurecontainer.io/)
    - GitHub: [https://github.com/Ggasyd/fon-t2t-api](https://github.com/Ggasyd/fon-t2t-api)
  
  - **Fon to French Transcription Model**: 
    - API: [http://fon-s2t-api.francecentral.azurecontainer.io/](http://fon-s2t-api.francecentral.azurecontainer.io/)
    - GitHub: [https://github.com/Ggasyd/fon-api](https://github.com/Ggasyd/fon-api)
  
  - **Yoruba to English Transcription Model**: 
    - API: [http://yoruba-s2t-api.francecentral.azurecontainer.io/](http://yoruba-s2t-api.francecentral.azurecontainer.io/)
    - GitHub: [https://github.com/Ggasyd/ilewa-api](https://github.com/Ggasyd/ilewa-api)
  
  - **Devcontainer Setup**: A devcontainer is configured to ensure that all users can access the same dependencies, promoting consistency across development environments.

