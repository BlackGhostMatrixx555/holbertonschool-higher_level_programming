import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.
    
    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file.
    
    Args:
        filename (str): The name of the input JSON file.
        
    Returns:
        dict: The deserialized JSON data as a Python dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)