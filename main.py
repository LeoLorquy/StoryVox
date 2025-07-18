from vosk import Model, KaldiRecognizer
import pyaudio
import json
import time
import aiohttp
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()  # Charger les variables d'environnement depuis .env

# Accéder aux variables
api_key = os.getenv("MISTRAL_API_KEY")
model_path = os.getenv("VOSK_MODEL_PATH")

# Mistral API request function
async def send_request(question, api_key):
    try:
        url = "https://api.mistral.ai/v1/chat/completions"
        data = {
            "model": "mistral-medium-2505",
            "messages": [
                {
                    "role": "system",
                    "content": """Vous êtes un écrivain autobiographique professionnel, expert dans la création de récits fluides et immersifs. À partir des phrases ou fragments autobiographiques fournis par l’utilisateur, rédigez un texte autobiographique en français, en respectant ces consignes :  

Enrichissez chaque phrase avec des détails sensoriels, émotionnels ou descriptifs pour la rendre plus vivante et fluide, tout en restant fidèle au sens original.
Il y aura des moments ou tu ne comprend pas ce que je dit, c'est insensé, supprime, ne le mets pas.
Utilisez un ton introspectif et engageant, adapté à un public général, sauf indication contraire.  
Restez dans le présent narratif des propos de l’utilisateur, sans spéculer sur les causes, le passé ou le futur des événements décrits.  
Structurez le texte de manière thématique, en regroupant les idées similaires, sauf indication contraire. 
Exemple :
Phrase fournie : “Je marche dans la forêt.”
Phrase enrichie : “Je marche dans la forêt, où les feuilles craquent doucement sous mes pas, tandis que l’odeur humide de la mousse et le chant lointain d’un oiseau emplissent l’air d’une quiétude apaisante.”
Entrée utilisateur : [Insérez ici les phrases ou fragments fournis par l’utilisateur].
Sortie : Rédigez un texte autobiographique fluide et enrichi, respectant les consignes ci-dessus.
"""
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            "max_tokens": 700,
            "temperature": 0.9
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                url,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                },
                data=json.dumps(data)
            ) as response:
                if response.status != 200:
                    raise Exception(f"Erreur : {response.status} {response.reason}")
                result = await response.json()
                generated_text = result["choices"][0]["message"]["content"]
                return generated_text
    except Exception as error:
        print(f"Erreur lors de la requête : {error}")
        return None

# Main async function to handle voice recognition and API calls
async def main():
    # Charger le modèle Vosk
    model = Model(model_path)  # Remplacez par le chemin correct
    recognizer = KaldiRecognizer(model, 16000)

    # Initialiser PyAudio
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
    stream.start_stream()

    print("Parlez maintenant...")

    # Variables pour gérer le silence
    SILENCE_THRESHOLD = 20.0  # 60 secondes de silence
    last_speech_time = time.time()
    full_text = ""

    try:
        while True:
            data = stream.read(4096, exception_on_overflow=False)
            
            if recognizer.AcceptWaveform(data):
                # Résultat final
                result = json.loads(recognizer.Result())
                text = result.get("text", "")
                if text:
                    full_text += text + " "
                    last_speech_time = time.time()
                    print("Transcription complète :", text)

            else:
                # Résultat partiel
                partial_result = json.loads(recognizer.PartialResult())
                if partial_result.get("partial"):
                    print("Transcription partielle :", partial_result["partial"])
                    last_speech_time = time.time()
            
            # Vérifier le silence
            if time.time() - last_speech_time > SILENCE_THRESHOLD and full_text:
                print("\n=== Transcription finale ===\n", full_text.strip())
                # Call the Mistral API
                result_mistral = await send_request(full_text.strip(), api_key)
                if result_mistral:
                    print("\n=== Réponse de Mistral ===\n", result_mistral)
                full_text = ""  # Réinitialiser le texte complet
                last_speech_time = time.time()  # Réinitialiser le timer

    except KeyboardInterrupt:
        print("\nArrêt de l'enregistrement...")
        if full_text:
            print("\n=== Transcription finale ===\n", full_text.strip())
            # Call the Mistral API for the final text
            result_mistral = await send_request(full_text.strip(), api_key)
            if result_mistral:
                print("\n=== Réponse de Mistral ===\n", result_mistral)

    finally:
        # Nettoyer
        stream.stop_stream()
        stream.close()
        mic.terminate()

# Exécuter le script
if __name__ == "__main__":
    asyncio.run(main())