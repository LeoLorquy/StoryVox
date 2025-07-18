# Projet d'Écriture Autobiographique Assistée par IA

## Description
Ce projet vise à faciliter l'écriture d'un livre autobiographique grâce à l'intelligence artificielle et la transcription vocale en temps réel. En utilisant le modèle de reconnaissance vocale **Vosk** pour transcrire la voix en texte et l'API **Mistral** pour enrichir les transcriptions en un récit fluide et immersif, ce programme permet de transformer des fragments oraux en un texte digne d'un livre. Le résultat est un texte narratif enrichi de détails sensoriels et émotionnels, tout en restant fidèle aux propos de l'utilisateur.

Le projet est sous **licence MIT**, permettant une utilisation et une modification libres, sous réserve de mentionner les contributeurs originaux.

## Prérequis
Pour exécuter ce projet, vous devez installer les dépendances suivantes et configurer certains éléments.

### Dépendances Python
Les modules Python nécessaires sont listés dans le fichier `requirements.txt`. Installez-les avec la commande suivante :
```bash
pip install -r requirements.txt
```

Contenu du fichier `requirements.txt` :
- `vosk` : Pour la reconnaissance vocale.
- `pyaudio` : Pour capturer l'audio via le microphone.
- `aiohttp` : Pour effectuer des requêtes asynchrones à l'API Mistral.
- `python-dotenv` : Pour gérer les variables d'environnement dans un fichier `.env`.

### Autres prérequis
- **Modèle Vosk** : Téléchargez le modèle de reconnaissance vocale français `vosk-model-fr-0.22` depuis [le site officiel de Vosk](https://alphacephei.com/vosk/models). Placez-le dans un dossier accessible (par exemple, `../vosk-model-fr-0.22`) et mettez à jour le chemin dans le fichier `.env`.
- **Clé API Mistral** : Obtenez une clé API depuis [Mistral AI](https://mistral.ai/). Ajoutez-la dans un fichier `.env` (voir ci-dessous).
- **Système audio** : Un microphone fonctionnel est requis pour la capture audio.

### Fichier `.env`
Créez un fichier `.env` dans le répertoire racine du projet avec le contenu suivant :
```
MISTRAL_API_KEY=votre_clé_api_mistral
VOSK_MODEL_PATH=chemin/vers/vosk-model-fr-0.22
```
**Attention** : Ne partagez pas votre fichier `.env` publiquement et ajoutez-le à votre `.gitignore`.

## Installation
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   cd votre-repo
   ```

2. Créez un environnement virtuel (optionnel mais recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Téléchargez et configurez le modèle Vosk :
   - Téléchargez le modèle `vosk-model-fr-0.22` depuis [Vosk](https://alphacephei.com/vosk/models).
   - Décompressez-le dans un dossier (par exemple, `../vosk-model-fr-0.22`).
   - Mettez à jour la variable `VOSK_MODEL_PATH` dans le fichier `.env` avec le chemin correct.

5. Configurez la clé API Mistral :
   - Ajoutez votre clé API dans le fichier `.env` sous `MISTRAL_API_KEY`.

6. Exécutez le script :
   ```bash
   python votre_script.py
   ```

## Utilisation
- Lancez le script, parlez dans votre microphone, et le programme transcrira votre voix en temps réel.
- Après un silence de 20 secondes (configurable via `SILENCE_THRESHOLD`), le texte transcrit est envoyé à l'API Mistral pour être enrichi en un récit autobiographique.
- Les résultats sont affichés dans la console, avec la transcription brute et le texte enrichi.

## Communiqué de presse
**Un nouvel outil révolutionnaire pour écrire votre histoire avec l'IA**

[Date] – Nous sommes ravis d'annoncer le lancement de ce projet open-source, conçu pour transformer la manière dont les histoires personnelles sont écrites. Grâce à la puissance de la reconnaissance vocale de Vosk et à l'intelligence artificielle de Mistral, cet outil permet à quiconque de créer des récits autobiographiques immersifs à partir de simples enregistrements vocaux. Que vous soyez un écrivain en herbe ou que vous souhaitiez préserver vos souvenirs, ce projet rend l'écriture accessible, fluide et captivante.

Disponible sous licence MIT, ce projet invite les développeurs et les créateurs à contribuer à son évolution. Téléchargez-le dès aujourd'hui sur GitHub et commencez à raconter votre histoire comme jamais auparavant !

Pour plus d'informations, contactez [votre contact] ou visitez [votre site web/dépôt GitHub].

## Licence
Ce projet est distribué sous la **licence MIT**. Voir le fichier `LICENSE` pour plus de détails.

## Contribution
Les contributions sont les bienvenues ! Veuillez ouvrir une issue ou une pull request sur GitHub pour proposer des améliorations ou signaler des bugs.