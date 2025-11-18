import spacy
from spacy import displacy

# Load the model
nlp = spacy.load("en_core_web_sm")

def extract_parse_tree(text):
    """Extract basic parse tree information"""
    doc = nlp(text)
    
    print(f"Sentence: {text}")
    print("\nDependency Parse Tree:")
    print("-" * 50)
    
    for token in doc:
        print(f"{token.text:<12} {token.dep_:<12} {token.head.text:<12} {[child.text for child in token.children]}")
    
    return doc

# Test with some sentences
test_sentences = [
    "The cat sat on the mat.",
    "A quick brown fox jumps over the lazy dog.",
    "She gave him the book yesterday."
]

for sentence in test_sentences:
    doc = extract_parse_tree(sentence)
    print("\n" + "="*60 + "\n")