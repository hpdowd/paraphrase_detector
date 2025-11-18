import pandas as pd
import os

raw_data_path = "./data/raw/"
processed_data_path = "./data/processed/"

def load_msr_data(file_path):
    """Load the MSR Paraphrase Corpus from a TSV file."""
    df = pd.read_csv(file_path, sep='\t', quoting=3)  # quoting=3 for ignoring quotes
    
    print(f"Loaded {len(df)} sentence pairs")
    #print(f"Positive examples (paraphrases): {df['quality'].sum()}")
    #print(f"Negative examples: {len(df) - df['quality'].sum()}")

    return df


def save_to_pickle(df, pickle_path):
    """Save the DataFrame to a pickle file."""
    df.to_pickle(pickle_path)
    print(f"DataFrame saved to {pickle_path}")


def load_and_save_data():
    """Load paraphrase data from user input and save as pickle"""
    print("Enter current relative path to MSR Corpus\n")
    relative_path = input("./ : ").strip()
    #full_path = os.path.join(raw_data_path, relative_path)

    try:
        df = load_msr_data(relative_path)
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None
    
    pkl_save_path = input("Enter relative path to save pickle: ").strip()
    if not os.path.isdir(pkl_save_path):
        print(f"❌ Directory does not exist: ./{pkl_save_path}")
        return None
    
    pkl_filename = input("Enter pickle filename: ").strip() + ".pkl"
    full_pkl_path = os.path.join(pkl_save_path, pkl_filename)

    try:
        save_to_pickle(df, full_pkl_path)
    except Exception as e:
        print(f"❌ Error saving pickle: {e}")
        return None 

    print("✅ Data loading and saving completed successfully.")
    print(f"Pickle saved at: {full_pkl_path}")

load_and_save_data()