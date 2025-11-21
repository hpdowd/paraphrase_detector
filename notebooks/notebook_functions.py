# NoteBook Functions
import spacy
from spacy import displacy
from IPython.display import display, HTML

nlp = spacy.load("en_core_web_md") # Medium model

def jaccard_similarity(sent1, sent2):
    # make lowercase and split into words
    words1 = set(sent1.lower().split())
    words2 = set(sent2.lower().split())
    intersection = words1.intersection(words2)
    union = words1.union(words2)
    return float(len(intersection)) / len(union) if union else 0.0

def sentence_similarity_avg(sent1, sent2):
    doc1 = nlp(sent1)
    doc2 = nlp(sent2)

    # Vectors for each word, filter out words without vectors (medium model)
    vecs1 = [token.vector for token in doc1 if token.has_vector]
    vecs2 = [token.vector for token in doc2 if token.has_vector]

    if not vecs1 or not vecs2:
        return 0.0

    # Average vectors
    avg1 = sum(vecs1) / len(vecs1)
    avg2 = sum(vecs2) / len(vecs2)

    #cosine similarity
    from sklearn.metrics.pairwise import cosine_similarity
    return cosine_similarity([avg1], [avg2])[0][0]

def extract_all_features(sentence_pairs):
    features = []
    for sent1, sent2 in sentence_pairs:
        feature_vector = [
            jaccard_similarity(sent1, sent2),
            sentence_similarity_avg(sent1, sent2),
            sentence_similarity_sif(sent1, sent2),
            syntactic_similarity(sent1, sent2)
        ]

def visualize_parse_tree(text):
    doc = nlp(text)
    html = displacy.render(doc, style="dep", jupyter=False, options={"distance": 100})
    display(HTML(html))