import json


# Function to read the json file
def read_json_file(path):
    try:
        with open(path, 'r') as f:
            print(f'Started reading the json file {path}')
            return json.load(f)
    except FileNotFoundError:
        print('Error occurred, check if the path exists')
        raise
    except json.decoder.JSONDecodeError:
        print('Error occurred,unable to convert the input file data to json')
        raise


# Function to write the data into file
def write_file(data, path, operation):
    with open(path, operation) as f:
        print(f'Writing to file {path}, data {data}')
        f.writelines(data)
