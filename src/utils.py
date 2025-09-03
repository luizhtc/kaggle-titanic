import os
import zipfile
from pandas import DataFrame

from kaggle.api.kaggle_api_extended import KaggleApi

def ktic_pull_data() -> str:
    download_path = os.path.abspath("../data")

    api = KaggleApi()
    api.authenticate()

    try:
        api.competition_download_files(
            competition="titanic",
            path=download_path,
            quiet=False,
            force=False)
        
        file_path = os.path.join(download_path, "titanic.zip")
        
        print("Unzipping files...")
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(download_path)
        print("Files unzipped successfully.")
        os.remove(file_path)
        print(os.listdir(download_path))

        return download_path
    except Exception as e:
        print(f"Error downloading competition files: {e}")

        return ""
    
def ktic_treat_data_types(df) -> DataFrame:
    df['Pclass'] = df.apply(
        lambda x: '1st' if x['Pclass'] == 1
            else '2nd' if x['Pclass'] == 2
            else '3rd', axis=1
    )
    df['Age'] = df['Age'].round(0).astype('Int64')

    return df

    