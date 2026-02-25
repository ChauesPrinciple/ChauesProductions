import xml.etree.ElementTree as ET
import json
import os

kml_file = r"c:\Users\rober\.gemini\antigravity\scratch\chaues-productions\Chaues' Map of Japan.kml"
output_file = r"c:\Users\rober\.gemini\antigravity\scratch\chaues-productions\parsed_map_data.json"

def parse_kml(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    
    # KML uses a namespace usually, we need to extract it
    ns = ''
    if '}' in root.tag:
        ns = root.tag.split('}')[0] + '}'
    
    data = []
    
    # Find all Folders (categories) Option 1: Document -> Folder
    for folder in root.findall(f".//{ns}Folder"):
        folder_name_elem = folder.find(f"{ns}name")
        folder_name = folder_name_elem.text if folder_name_elem is not None else "Unknown Category"
        
        for placemark in folder.findall(f".//{ns}Placemark"):
            name_elem = placemark.find(f"{ns}name")
            name = name_elem.text if name_elem is not None else "Unnamed"
            
            desc_elem = placemark.find(f"{ns}description")
            description = desc_elem.text if desc_elem is not None else ""
            
            # Sometimes descriptions are in ExtendedData
            if not description:
                ext_data = placemark.find(f"{ns}ExtendedData")
                if ext_data is not None:
                    for data_elem in ext_data.findall(f"{ns}Data"):
                        if data_elem.get('name') == 'description':
                            val_elem = data_elem.find(f"{ns}value")
                            if val_elem is not None and val_elem.text:
                                description = val_elem.text
            
            point = placemark.find(f".//{ns}Point")
            coordinates = None
            if point is not None:
                coord_elem = point.find(f"{ns}coordinates")
                if coord_elem is not None and coord_elem.text:
                    # KML coords are: longitude,latitude,altitude
                    parts = coord_elem.text.strip().split(',')
                    if len(parts) >= 2:
                        coordinates = {
                            "lng": float(parts[0]),
                            "lat": float(parts[1])
                        }
            
            if coordinates:
                data.append({
                    "folder": folder_name,
                    "name": name.strip(),
                    "description": description.strip() if description else "",
                    "coordinates": coordinates
                })
                
    return data

if __name__ == "__main__":
    parsed_data = parse_kml(kml_file)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(parsed_data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully parsed {len(parsed_data)} locations and saved to {output_file}.")
    
    # Print a quick summary of folders
    folders = {}
    for item in parsed_data:
        folders[item['folder']] = folders.get(item['folder'], 0) + 1
        
    print("\nSummary by category:")
    for folder, count in folders.items():
        print(f" - {folder}: {count} locations")
