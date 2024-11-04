import os
import pandas as pd
from src.NewsAnalyzerAPI import LLMConnector
from src.NewsAnalyzerAPI import NewsAnalyzer
from tqdm import tqdm

from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

con = LLMConnector("http://143.107.183.116:18888/v1", api_key, "llama3.1")
analyzer = NewsAnalyzer(con)

# reading sheet file and extracting components
df = pd.read_excel("dengue_hazzards_news.xlsx")
data_list = df.to_dict(orient="list")
components_list = []
for text in tqdm(data_list["text"]):
    components = analyzer.extract_components(text)
    components_list.append(components)

# transforming components into a dataframe and writing in a spreadsheet with the new columns (predicted components)
components_df = pd.DataFrame(components_list)
df = pd.concat([df, components_df], axis=1)
df.to_excel("dengue_hazzards_pred.xlsx", index=False)
print("Success")