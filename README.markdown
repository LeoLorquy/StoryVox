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

# COMMUNIQUÉ DE PRESSE  
**Bordeaux, le 13 juillet 2025**  
**Léo Eyrard, étudiant à l’EGS, lance StoryVox : Écrivez un livre en 1 à 2 mois grâce à l’IA**

## Chapô  
Léo Eyrard, étudiant en licence de développeur web à l’EGS, dévoile StoryVox, un outil révolutionnaire qui permet d’écrire un livre en seulement 1 à 2 mois. En combinant la reconnaissance vocale en temps réel de Vosk et la rédaction automatisée de Mistral, StoryVox transforme vos paroles en chapitres structurés, rendant l’écriture accessible à tous.

## StoryVox : Écrire un livre n’a jamais été aussi simple  
StoryVox, lancé aujourd’hui par Léo Eyrard, étudiant en licence de développeur web à l’École de Gestion et de Commerce (EGS) de Bordeaux, est un outil innovant qui démocratise l’écriture de livres. Grâce à une interface intuitive, il suffit de brancher un micro, de parler, et l’outil fait le reste : la technologie de reconnaissance vocale Vosk transcrit vos paroles en temps réel, tandis que le modèle d’intelligence artificielle Mistral les organise en chapitres cohérents, avec un style adapté à celui d’un livre. « J’ai voulu créer un outil qui supprime les barrières de l’écriture, permettant à chacun de raconter son histoire sans effort », explique Léo Eyrard, créateur de StoryVox.

## Un outil pour les écrivains en herbe et les créateurs pressés  
StoryVox s’adresse à un large public : étudiants souhaitant rédiger des mémoires, amateurs d’écriture créative, ou professionnels désirant publier un livre blanc. En quelques minutes par jour, l’outil transforme des idées orales en un manuscrit structuré, avec une table des matières et un style narratif soigné. Testé par une dizaine d’utilisateurs, StoryVox a déjà permis à plusieurs d’entre eux de finaliser des projets en moins de deux mois. « StoryVox m’a permis de structurer mes idées sans perdre de temps à écrire », témoigne Clara, une étudiante en littérature et bêta-testeuse.

## Une innovation technologique au service de la créativité  
Développé dans le cadre de son projet de fin d’études, StoryVox combine deux technologies de pointe : Vosk pour une transcription vocale précise et Mistral pour une rédaction intelligente qui respecte les nuances littéraires. L’outil est accessible via un site web convivial, compatible avec tous les navigateurs, et propose une version gratuite pour encourager les premiers utilisateurs. Léo Eyrard prévoit d’ajouter des fonctionnalités, comme la personnalisation des styles d’écriture et l’exportation en formats eBook.

## Conclusion : Donnez vie à vos histoires avec StoryVox  
StoryVox est dès à présent disponible sur le github en libre accées. Pour plus d’informations, contactez Léo Eyrard, créateur de StoryVox, à eyrard.leo.1@gmail.com ou au [0641983518].

## Licence
Ce projet est distribué sous la **licence MIT**. Voir le fichier `LICENSE` pour plus de détails.

## Contribution
Les contributions sont les bienvenues ! Veuillez ouvrir une issue ou une pull request sur GitHub pour proposer des améliorations ou signaler des bugs.