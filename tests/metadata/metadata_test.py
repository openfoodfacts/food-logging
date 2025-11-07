import json
import os
import unittest
from jsonschema import ValidationError, validate

script_dir = os.path.dirname(__file__)

def relative_path(file_name):
    return os.path.join(script_dir,file_name)

def load_json(file_name):
    with open(relative_path(file_name)) as f:
        json_data = json.load(f)
    return json_data
    
class MetadataTests(unittest.TestCase):
    def test_metadata(self):
        schema = load_json('../../schemas/metadata.json')

        for invalid_file in sorted(os.listdir(relative_path('invalid'))):
            invalid_json = load_json(os.path.join('invalid', invalid_file))
            with self.assertRaises(ValidationError, msg=invalid_file):
                validate(invalid_json, schema)

        for valid_file in sorted(os.listdir(relative_path('valid'))):
            valid_json = load_json(os.path.join('valid', valid_file))
            try:
                validate(valid_json, schema)
            except ValidationError as e:
                self.fail(f"Valid file: {valid_file} raised {e.message}")
