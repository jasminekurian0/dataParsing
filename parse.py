import csv
import json
import xml.etree.ElementTree as ET

def read_tab_delimited_file(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        return [row for row in csv.reader(file, delimiter='\t')]

def write_csv(data, output_filename):
    with open(output_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def write_json(data, output_filename):
    keys = data[0]
    json_data = [dict(zip(keys, row)) for row in data[1:]]
    with open(output_filename, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4)

def write_xml(data, output_filename):
    root = ET.Element("Root")
    keys = data[0]
    for row in data[1:]:
        item = ET.SubElement(root, "Record")
        for key, value in zip(keys, row):
            child = ET.SubElement(item, key)
            child.text = value
    tree = ET.ElementTree(root)
    tree.write(output_filename, encoding='utf-8', xml_declaration=True)

def main():
    filename = input("Enter the filename: ")
    format_option = input("Enter the format (-c for CSV, -j for JSON, -x for XML): ")
    
    try:
        data = read_tab_delimited_file(filename)
        if not data:
            print("Error: File is empty or unreadable.")
            return
        
        output_filename = filename.rsplit('.', 1)[0]
        
        if format_option == '-c':
            output_filename += '.csv'
            write_csv(data, output_filename)
        elif format_option == '-j':
            output_filename += '.json'
            write_json(data, output_filename)
        elif format_option == '-x':
            output_filename += '.xml'
            write_xml(data, output_filename)
        else:
            print("Error: Unsupported format option. Use -c for CSV, -j for JSON, -x for XML.")
            return
        
        print(f"File successfully converted and saved as {output_filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
