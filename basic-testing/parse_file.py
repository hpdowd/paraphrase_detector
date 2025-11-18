import pandas as pd

def load_msr_data(file_path):
    """Load the MSR Paraphrase Corpus from a TSV file."""
    df = pd.read_csv("../data/processed/msr_paraphrase_train.txt", sep='\t', quoting=3)
    return df