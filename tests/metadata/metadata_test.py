import json
import os
import unittest
from jsonschema import Draft202012Validator, ValidationError, validate
from referencing import Registry, Resource

script_dir = os.path.dirname(__file__)

def relative_path(file_name):
    return os.path.join(script_dir,file_name)

def load_json(file_name):
    with open(relative_path(file_name)) as f:
        json_data = json.load(f)
    return json_data
    
class MetadataTests(unittest.TestCase):
    def test_metadata(self):
        registry = Registry()
        registry = Resource.from_contents(load_json('../../schemas/facets.json')) @ registry

        schema = load_json('../../schemas/metadata.json')
        validator = Draft202012Validator(schema, registry=registry)

        for invalid_file in sorted(os.listdir(relative_path('invalid'))):
            invalid_json = load_json(os.path.join('invalid', invalid_file))
            with self.assertRaises(ValidationError, msg=invalid_file):
                validator.validate(invalid_json)

        for valid_file in sorted(os.listdir(relative_path('valid'))):
            valid_json = load_json(os.path.join('valid', valid_file))
            try:
                validator.validate(valid_json)
            except ValidationError as e:
                self.fail(f"Valid file: {valid_file} raised {e.message}")
