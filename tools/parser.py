import spacy

# English model
nlp = spacy.load("en_core_web_sm")

# Parse a single sentence
def parse_sentence(sentence):
    doc = nlp(sentence)

    print("Token-by-token analysis:")
    for token in doc:
        print(f"Text: {token.text:<12} Dep: {token.dep_:<10} Head: {token.head.text:<10} POS: {token.pos_:<8}")

    return doc

def extract_dependency_relationships(doc):
    """Extract dependency relationships for graph representation"""
    dependencies = []
    
    for token in doc:
        # Skip punctuation
        if token.is_punct:
            continue
            
        dependency = {
            'word': token.text,
            'lemma': token.lemma_,
            'dep_type': token.dep_,
            'head': token.head.text,
            'head_lemma': token.head.lemma_,
            'pos': token.pos_
        }
        dependencies.append(dependency)
    
    return dependencies
