import json
import csv


INPUT_FILE = "input.csv"

li=[]

with open(INPUT_FILE, 'w', newline='\n') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    for row in rows:
        print(row)


#def csv_to_list_dict(input_file2) -> list[dict]:
    #...  # TODO реализовать конвертер из csv в json
'''
    with open(INPUT_FILE, 'w', newline='\n') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:
            print(row)
        
        li.append({
            "filename": row['Picture'],
            "region": {
                "shape_attributes": {
                    "name": "polygon",
                    "Coordinates": row['Coordinates'],
                    "region_attribute": {
                        "name": row['Class']}}}})
    with open("file.json", "w") as f:
        json.dump(li, f, indent=4)
        '''

#print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
