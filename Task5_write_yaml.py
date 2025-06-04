import yaml

def write_yaml(path, data):
    with open(path, 'w') as f:
        yaml.safe_dump(data, f)
