from openai import OpenAI
import requests

class ImageCreator:
    def __init__(self, model='dall-e-3', size='1024x1024', quality='standard', style='vivid', n=1):
        self.client = OpenAI()
        self.model = model
        self.size = size
        self.quality = quality
        self.style = style
        self.n = n

    def generate_image_url(self, prompt):
        response = self.client.images.generate(
            model=self.model,
            prompt=prompt,
            size=self.size,
            quality=self.quality,
            style=self.style,
            n=self.n
        )
        return response.data[0].url

    def download_image(self, url, filename, max_retries=10):
        if not url:
            print("No URL provided")
            return

        attempts = 0
        while attempts < max_retries:
            response = requests.get(url)
            if response.status_code == 200:
                with open(filename, 'wb') as file:
                    file.write(response.content)
                print(f"Image downloaded successfully as {filename}")
                return 
            else:
                print(f"Failed to download the image, attempt {attempts + 1} of {max_retries}")
                attempts += 1

        print(f"Max retries reached, failed to download the image")


if __name__ == "__main__":
    downloader = ImageCreator()
    image_url = downloader.generate_image_url("corgi")
    downloader.download_image(image_url, 'downloaded_image2.jpg')
