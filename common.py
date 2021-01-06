import json


def convert_json_to_dict(json_data):
    parsed_params = json.loads(json_data)
    return parsed_params
