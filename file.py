import json
def read_file(path):
     with open(path, "r") as json_file:
          properties = json.load(json_file)
          return properties
def write_file(path, data):
     with open(path, "w") as json_file:
          json.dump(data, json_file, indent=4)
def read_ids_from_json(file_path):
     ids = []
     with open(file_path, 'r') as file:
          data = json.load(file)
          for item in data:
               ids.append(item['id'])
     return ids

