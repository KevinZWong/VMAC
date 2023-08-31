from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv
import os

class GoogleImageFetcher:

    def __init__(self):
        # Load env variables if .env exists
        if os.path.exists(".env"):
            load_dotenv()
        else:
            print(".env file missing, please create one with your API and CX")

        self.DK = os.environ.get('DEVELOPER_KEY')
        self.CX = os.environ.get('CX')
        
        self.spath = 'ImageQuerry/'
        
        # Create directory if it doesn't exist
        if not os.path.exists(self.spath):
            os.mkdir(self.spath)
        
        self.gis = GoogleImagesSearch(self.DK, self.CX)

    def fetch_images(self, searchfor):
        with GoogleImagesSearch(self.DK, self.CX) as gis:
            _search_params = {
                "q": searchfor,
                "num": 1,
                "safe": "high",
                "fileType": "jpg",
                "imgType": "photo",
                "rights": "cc_publicdomain",
                "imgSize": "HUGE"
            }
            self.gis.search(search_params=_search_params, path_to_dir=self.spath)
        print("Finished!")

# Usage
if __name__ == "__main__":
    fetcher = GoogleImageFetcher()
    fetcher.fetch_images("corgi")
