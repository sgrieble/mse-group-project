import json
from sentence_transformers import SentenceTransformer, CrossEncoder, util
import torch
import os
def get_result_list(query):
    bi_encoder = SentenceTransformer('all-mpnet-base-v2')

    file_path_embed = os.path.join(os.path.dirname(__file__), 'index_data', 'embedding_data.json')
    data_string = open(file_path_embed)
    data = json.load(data_string)
    
    file_path_web_data = os.path.join(os.path.dirname(__file__), 'index_data', 'filtered_docs.json')
    website_data_string = open(file_path_web_data)
    website_data = json.load(website_data_string)

    all_ids = []
    for item in list(data.items()):
        all_ids.append(item[0])

    query_embedding = bi_encoder.encode(query, convert_to_tensor=True)

    embeddings = []
    for doc_id, doc_data in data.items():
        embeddings.append(torch.tensor(doc_data['embedding_score']))

    hits = util.semantic_search(query_embedding, embeddings, top_k=100)
    hits = hits[0]

    results = []

    for count, hit in enumerate(hits):
        doc_position = hit['corpus_id']
        results.append({
            "rank": count,
            "link": website_data[all_ids[doc_position]]['url'],
            "score": hit['score'],
            "title": website_data[all_ids[doc_position]]['headline'],
            "preview": website_data[all_ids[doc_position]]['website_preview'],
        })

    return results

# [{"rank": 1, "link": "https://d3rlpy.readthedocs.io/en/v2.5.0/", "score": 0.991, "title": "d3rlpy - An offline deep reinforcement learning library", "first_three_sentences": "d3rlpy provides state-of-the-art offline deep reinforcement learning algorithms through out-of-the-box scikit-learn-style APIs. Unlike other RL libraries, the provided algorithms can achieve extremely powerful performance beyond their papers via several tweaks."},
#             {"rank": 2, "link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "score": 0.901, "title": "ILIAS Uni Tübingen", "first_three_sentences": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de. Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de. Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
#             {"rank": 3, "link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "score": 0.894, "title": "ILIAS Uni Tübingen", "first_three_sentences": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
#             {"rank": 4, "link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "score": 0.762, "title": "ILIAS Uni Tübingen", "first_three_sentences": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
#             {"rank": 5, "link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "score": 0.743, "title": "ILIAS Uni Tübingen", "first_three_sentences": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
#             {"rank": 6, "link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "score": 0.698, "title": "ILIAS Uni Tübingen", "first_three_sentences": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
#             {"rank": 7, "link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "score": 0.687, "title": "ILIAS Uni Tübingen", "first_three_sentences": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},
#             {"rank": 8, "link": "https://ovidius.uni-tuebingen.de/ilias3/login.php?target=&client_id=pr02&auth_stat=", "score": 0.210, "title": "ILIAS Uni Tübingen", "first_three_sentences": "Login mit zentraler Universitäts-Kennung Sie betreten die ILIAS Plattform für Mitglieder der Universität Tübingen. Studierende finden hier Materialien für ihre Veranstaltungen. Lehrenden bietet ILIAS effektive Verwaltungs-, Kommunikations- und Kooperationswerkzeuge. Kontakt: esc@ub.uni-tuebingen.de"},]
