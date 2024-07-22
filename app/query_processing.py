import json
from sentence_transformers import SentenceTransformer, CrossEncoder, util
import torch
import os
import itertools

def get_result_list(query):
    bi_encoder = SentenceTransformer('all-mpnet-base-v2')

    file_path_embed = os.path.join(os.path.dirname(__file__), 'index_data', 'embedding_data.json')
    with open(file_path_embed, 'r') as f:
        data = json.load(f)
    all_items = list(data.items())
    
    file_path_web_data = os.path.join(os.path.dirname(__file__), 'index_data', 'filtered_docs.json')
    with open(file_path_web_data, 'r') as f:
        website_data = json.load(f)

    all_ids = [item[0] for item in all_items]

    if len(query) < 4:
        query = query + ' Tübingen'
    query_embedding = bi_encoder.encode(query, convert_to_tensor=True)

    embeddings_text = [torch.tensor(doc_data['embedding_score_html']) for _, doc_data in data.items()]
    embeddings_title = [torch.tensor(doc_data['embedding_score_headline']) for _, doc_data in data.items()]
    
    text_hits = util.semantic_search(query_embedding, embeddings_text, top_k=len(all_items))[0]
    title_hits = util.semantic_search(query_embedding, embeddings_title, top_k=len(all_items))[0]
    
    recalculated_hits = {}
    
    title_scores = {hit['corpus_id']: hit['score'] for hit in title_hits}
    recalculated_hits = {
        all_ids[hit['corpus_id']]: {
            "score": (hit['score'] + title_scores.get(hit['corpus_id'], 0)) / 2
        }
        for hit in text_hits
    }
    
    recalculated_hits = dict(sorted(recalculated_hits.items(), key=lambda item: item[1]['score'], reverse=True))
    recalculated_hits = dict(itertools.islice(recalculated_hits.items(), 100))
    
    results = [
        {
            "rank": count,
            "link": website_data[doc_id]['url'],
            "score": hit['score'],
            "title": website_data[doc_id]['headline'],
            "preview": website_data[doc_id]['website_preview'],
        }
        for count, (doc_id, hit) in enumerate(recalculated_hits.items())
    ]

    return results
