import os
import zipfile
from pandas import DataFrame
from typing import List

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
    df['Survived'] = df['Survived'].round(0).astype('Int64')

    return df

def ktic_get_title(x, list_titles: List[str]) -> str:
    for title in list_titles:
        if title in x:
            return title
        
    return "No title."

def ktic_get_title_group(df) -> DataFrame:
    title_map = {
        "Capt.": "Millitary",
        "Col.": "Millitary",
        "Don.": "Honorary",
        "Dr.": "Honorary",
        "Jonkheer.": "Honorary",
        "Major.": "Millitary",
        "Master.": "Honorary",
        "Miss.": "Common",
        "Mlle.": "Honorary",
        "Mme.": "Honorary",
        "Mr.": "Common",
        "Mrs.": "Common",
        "Ms.": "Common",
        "Rev.": "Honorary"
    }

    df["Title_Group"] = df["Title"].map(title_map)
    return df

    