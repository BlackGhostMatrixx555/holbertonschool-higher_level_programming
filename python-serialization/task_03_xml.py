import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.
    
    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The output XML file name.
    """
    # Create the root element
    root = ET.Element("data")
    
    # Add child elements for each key-value pair
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
        
    # Write the tree to a file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8')

def deserialize_from_xml(filename):
    """
    Reads XML data from a file and returns a deserialized dictionary.
    
    Args:
        filename (str): The input XML file name.
        
    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct the dictionary
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text
            
        return deserialized_dict
        
    except Exception:
        return None