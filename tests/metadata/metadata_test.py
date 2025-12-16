import os
import unittest
from jsonschema import Draft202012Validator, ValidationError
from referencing import Registry, Resource, jsonschema
import yaml

script_dir = os.path.dirname(__file__)

def relative_path(file_name):
    return os.path.join(script_dir,file_name)

def load_yaml(file_name):
    with open(relative_path(file_name)) as f:
        schema = yaml.safe_load(f)
    return schema
    
def resource_tuple(file_name):
    return (file_name, Resource.from_contents(load_yaml("../../schemas/" + file_name), jsonschema.DRAFT202012))

class MetadataTests(unittest.TestCase):
    def test_metadata(self):
        registry = Registry().with_resources([
            resource_tuple("openapi.yaml"),
        ])

        schema = load_yaml('../../schemas/metadata-file.yaml')
        validator = Draft202012Validator(schema, registry=registry)

        for invalid_file in sorted(os.listdir(relative_path('invalid'))):
            invalid_json = load_yaml(os.path.join('invalid', invalid_file))
            with self.assertRaises(ValidationError, msg=invalid_file):
                validator.validate(invalid_json)

        for valid_file in sorted(os.listdir(relative_path('valid'))):
            valid_json = load_yaml(os.path.join('valid', valid_file))
            try:
                validator.validate(valid_json)
            except ValidationError as e:
                self.fail(f"Valid file: {valid_file} raised {e.message}")
