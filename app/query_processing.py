import json
from sentence_transformers import SentenceTransformer, CrossEncoder, util
import torch
import os
import itertools

def get_result_list(query):
    bi_encoder = SentenceTransformer('all-mpnet-base-v2')

    file_path_embed = os.path.join(os.path.dirname(__file__), 'index_data', 'embedding_data.json')
    data_string = open(file_path_embed)
    data = json.load(data_string)
    all_items = list(data.items())
    
    file_path_web_data = os.path.join(os.path.dirname(__file__), 'index_data', 'filtered_docs.json')
    website_data_string = open(file_path_web_data)
    website_data = json.load(website_data_string)

    all_ids = []
    for item in all_items:
        all_ids.append(item[0])

    query_embedding = bi_encoder.encode(query, convert_to_tensor=True)

    embeddings_text = []
    embeddings_title = []
    
    for _, doc_data in data.items():
        embeddings_text.append(torch.tensor(doc_data['embedding_score_html']))
        embeddings_title.append(torch.tensor(doc_data['embedding_score_headline']))

    text_hits = util.semantic_search(query_embedding, embeddings_text, top_k=len(all_items))
    title_hits = util.semantic_search(query_embedding, embeddings_title, top_k=len(all_items))

    text_hits = text_hits[0]
    title_hits = title_hits[0]
    
    recalculated_hits = {}
    
    for i in range(len(text_hits)):
        current_id = all_ids[text_hits[i]['corpus_id']]
        title_score = next((d for d in title_hits if text_hits[i].get('corpus_id') in d.values()), 0)['score']
        combined_score = (text_hits[i]['score'] + title_score) / 2
        recalculated_hits[current_id] = {
            "score": combined_score
        }
    
    recalculated_hits = dict(sorted(recalculated_hits.items(), key=lambda item: item[1]['score'], reverse=True))
    recalculated_hits = dict(itertools.islice(recalculated_hits.items(), 100))

    results = []
    
    for count, hit in enumerate(recalculated_hits.items()):
        doc_id = hit[0]
        results.append({
            "rank": count,
            "url": website_data[doc_id]['url'],
            "score": hit[1]['score'],
            "title": website_data[doc_id]['headline'],
            "preview": website_data[doc_id]['website_preview'],
        })

    return results
