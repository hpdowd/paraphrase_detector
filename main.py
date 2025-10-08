from tools.parser import parse_sentence, extract_dependency_relationships

def main():

    sentence = "The quick brown fox jumps over the lazy dog."
    doc = parse_sentence(sentence)

    dependencies = extract_dependency_relationships(doc)
    print("\nDependency relationships:")
    for dep in dependencies:
        print(f"{dep['word']} --{dep['dep_type']}--> {dep['head']}")        

if __name__ == "__main__":
    main()