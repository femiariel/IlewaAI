# IlewaAI App
Benin Multimodal Hackhaton

# Projet de Génération d'Images à partir de Langues Locales
Ce projet utilise une série de technologies pour transcrire la parole en texte, traduire ce texte et générer des images à partir du texte traduit. Le pipeline complet comprend les étapes suivantes :
1. **Transcription de la parole en texte** avec [MMS (Meta Speech-to-Text)](https://github.com/facebookresearch/fairseq/tree/main/examples/mms).
2. **Traduction du texte** avec [NLLB (No Language Left Behind)](https://github.com/facebookresearch/flores).
3. **Génération d'images** à partir du texte traduit avec [Stable Diffusion](https://github.com/CompVis/stable-diffusion).
4. **Affichage de l'image générée** avec [Streamlit](https://streamlit.io/).
## Table des matières
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Technologies utilisées](#technologies-utilisées)
- [Contribution](#contribution)
- [Licence](#licence)
## Installation
Pour exécuter ce projet localement, suivez les étapes suivantes :
1. Clonez ce dépôt :
  ```bash
  git clone
https://github.com/votre-utilisateur/votre-depot.git
  cd votre-depot
  ```
2. Créez et activez un environnement virtuel :
  ```bash
  python -m venv env
  source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`
  ```
3. Installez les dépendances :
  ```bash
  pip install -r requirements.txt
  ```
## Utilisation
1. **Lancement de l'application** :
  ```bash
  streamlit run app.py
  ```
2. **Interface Utilisateur** :
  - **Upload** : Téléchargez un fichier audio contenant la parole dans la langue locale.
  - **Transcription** : Le discours est transcrit en texte à l'aide de MMS.
  - **Traduction** : Le texte est traduit dans une langue supportée par Stable Diffusion à l'aide de NLLB.
  - **Génération d'image** : Une image est générée à partir du texte traduit avec Stable Diffusion.
  - **Affichage** : L'image générée est affichée via l'interface Streamlit.
## Technologies Utilisées
- **MMS (Meta Speech-to-Text)** : Pour la transcription de la parole en texte.
- **NLLB (No Language Left Behind)** : Pour la traduction du texte.
- **Stable Diffusion** : Pour la génération d'images à partir de descriptions textuelles.
- **Streamlit** : Pour la création de l'interface utilisateur et l'affichage des résultats.
3. **Interface Utilisateur** :
  - **Interface** : Nous avons déployé l'application sur streamlit cloud: le lien pour y accéder est : https://ilewaai.streamlit.app/
  - **API** : Nous avons déployé des APIs pour chaque moèle que nous utilisons et nous faisons appel à ces fichiers dans notre ismo.py pour effectuer les transcriptions et les translations.Ces modèles ont été déployés via Azure Container Instances grace à leur image Docker. Cela permet à n'importe qui de faire fonctionner notre code meme s'il n'a pas la puissance de calcul nécessaire.
  - **Modèle de traduction fon à français**: api : 'http://fon-t2t-api.francecentral.azurecontainer.io/'  et github: 'https://github.com/Ggasyd/fon-t2t-api'
  -  **Modèle de transcription fon à français** : api : 'http://fon-s2t-api.francecentral.azurecontainer.io/' et github: 'https://github.com/Ggasyd/fon-api'
  -  **Modèle de transcription yoruba à anglais** : api : 'http://yoruba-s2t-api.francecentral.azurecontainer.io/' et github : 'https://github.com/Ggasyd/ilewa-api'
  -  **Devcontainer**: Mise en place d'un devcontainer pour s'assurer que les utilisateurs puissent avoir accès aux memes dépendances

