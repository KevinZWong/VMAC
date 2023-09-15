import json
import os
from pathlib import Path
from base64 import b64decode
from dotenv import load_dotenv
import openai

class ImageCreator:
    def __init__(self):
        self.data_dir = Path.cwd() / "jsonScriptFiles"
        self.image_dir = Path.cwd() / "ImageFiles"
        self.data_dir.mkdir(exist_ok=True)
        self.image_dir.mkdir(parents=True, exist_ok=True)
        self.api_key = os.getenv('OPENAI_API_KEY')

    def create_image(self, prompt):
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="b64_json",
        )

        file_name = self.data_dir / f"{response['created']}.json"

        with open(file_name, mode="w", encoding="utf-8") as file:
            json.dump(response, file)

        return self._create_png_from_json(file_name)

    def _create_png_from_json(self, json_file):
        with open(json_file, mode="r", encoding="utf-8") as file:
            response = json.load(file)

        for index, image_dict in enumerate(response["data"]):
            image_data = b64decode(image_dict["b64_json"])
            image_file = self.image_dir / f"{json_file.stem}-{index}.png"
            with open(image_file, mode="wb") as png:
                png.write(image_data)

        return image_file.as_posix()

if __name__ == "__main__":

    image_creator = ImageCreator()
    print(image_creator.create_image("cars"))
