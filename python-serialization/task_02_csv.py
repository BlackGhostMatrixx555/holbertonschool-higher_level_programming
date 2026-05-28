import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it to JSON format, 
    saving it to 'data.json'.
    
    Args:
        csv_filename (str): The path to the input CSV file.
        
    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        data = []
        
        # Read the CSV data
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
                
        # Write the serialized JSON data
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
            
        return True
        
    except FileNotFoundError:
        return False
    except Exception:
        return False