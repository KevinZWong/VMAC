

from pathlib import Path
import openai
import os

class TextToSpeech:
    def __init__(self, voice="alloy"):
        self.client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.voice = voice
    def generate_speech(self, filename, text):
        file_path = filename
        response = self.client.audio.speech.create(
            model="tts-1",
            voice=self.voice,
            input=text
        )
        response.stream_to_file(file_path)

# Usage
if __name__ == "__main__":
    generator = TextToSpeech()
    file_path = generator.generate_speech("custom_speech.mp3", "The quick brown fox jumped over the lazy dog.")
    print(f"Speech file created at: {file_path}")
