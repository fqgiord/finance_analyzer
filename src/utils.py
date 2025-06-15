import os 

def create_dirs():
    os.makedirs("data/raw", exist_ok=True)
    os.makedirs("data/process", exist_ok=True)
    