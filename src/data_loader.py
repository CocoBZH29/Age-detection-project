from datasets import load_dataset

def load_data():
    """Load the dataset from the HuggingFace"""
    ds = load_dataset("py97/UTKFace-Cropped")
    return ds

