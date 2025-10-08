import spacy
from tools import parser

# Load spaCy and dataset
nlp = spacy.load("en_core_web_sm")
dataset = parser.load_dataset("glue", "mrpc")

def process_sentence_pair(sentence1, sentence2):
    """Parse both sentences and extract their dependency structures"""
    
    # Parse both sentences
    doc1 = nlp(sentence1)
    doc2 = nlp(sentence2)
    
    # Extract dependency graphs
    deps1 = parser.extract_dependency_relationships(doc1)
    deps2 = parser.extract_dependency_relationships(doc2)
    
    return {
        'sentence1': sentence1,
        'sentence2': sentence2,
        'dependencies1': deps1,
        'dependencies2': deps2,
        'doc1': doc1,
        'doc2': doc2
    }

# Process a few examples from the dataset
print("Processing MRPC examples...")
for i in range(3):  # Just do first 3 examples
    example = dataset['train'][i]
    result = process_sentence_pair(example['sentence1'], example['sentence2'])
    
    print(f"\nExample {i+1}:")
    print(f"Sentence 1: {result['sentence1']}")
    print(f"Sentence 2: {result['sentence2']}")
    print(f"Label: {example['label']} (1=paraphrase, 0=not paraphrase)")
    
    print(f"\nDependencies for Sentence 1:")
    for dep in result['dependencies1'][:5]:  # Show first 5 dependencies
        print(f"  {dep['word']} --{dep['dep_type']}--> {dep['head']}")