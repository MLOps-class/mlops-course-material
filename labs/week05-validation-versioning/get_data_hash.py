import yaml

def get_data_hash(dvc_file_path="loan_applications.csv.dvc"):
    """Read the DVC pointer file and return the content hash of the tracked data."""
    with open(dvc_file_path) as f:
        dvc_meta = yaml.safe_load(f)
    return dvc_meta["outs"][0]["md5"]

if __name__ == "__main__":
    print(get_data_hash())
