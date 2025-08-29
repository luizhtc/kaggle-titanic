import os
import zipfile

from kaggle.api.kaggle_api_extended import KaggleApi

def pull_data() -> None:
    download_path = os.path.join(os.getcwd(), "data")

    api = KaggleApi()
    api.authenticate()

    try:
        api.competition_download_files(
            competition="titanic",
            path=download_path,
            quiet=False,
            force=True)
        
        print("Unzipping files...")
        with zipfile.ZipFile(os.path.join(download_path, "titanic.zip"), 'r') as zip_ref:
            zip_ref.extractall(download_path)
        print("Files unzipped successfully.")
        os.remove(os.path.join(download_path, "titanic.zip"))
        os.listdir(download_path)
    except Exception as e:
        print(f"Error downloading competition files: {e}")

    