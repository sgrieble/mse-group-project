import json
import re
import string
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer

bi_encoder = SentenceTransformer('all-mpnet-base-v2')

data_string = open(r"./filtered_docs.json")
data = json.load(data_string)

print(len(data))

def get_embedding_score(text):
    doc_embedding = bi_encoder.encode(text, convert_to_tensor=True, show_progress_bar=True)
    return doc_embedding

def get_html_text(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    text = soup.get_text(separator=' ', strip=True)
    normalized_text = re.sub(r'\s+', ' ', text)
    return normalized_text.strip()

def clean_string(input_str):
    translator = str.maketrans('', '', string.punctuation)
    no_punct = input_str.translate(translator)
    no_multi_spaces = re.sub(r'\s+', ' ', no_punct)
    clean_str = no_multi_spaces.strip()
    
    return clean_str

index = {}
for entry in data.items():
    index[entry[0]] = {
        'embedding_score_html': get_embedding_score(get_html_text(entry[1]['html_text'])).tolist(),
        'embedding_score_headline': get_embedding_score(clean_string(entry[1]['headline'])).tolist(),
    }

with open(r'./embedding_data.json', 'w') as json_file:
    json.dump(index, json_file, indent=4)