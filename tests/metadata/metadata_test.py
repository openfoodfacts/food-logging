import json
import os
import unittest
from jsonschema import ValidationError, validate

script_dir = os.path.dirname(__file__)

class MetadataTests(unittest.TestCase):
    def test_metadata(self):
        with open(os.path.join(script_dir,'../../schemas/metadata.json')) as f:
            schema = json.load(f)

        with open(os.path.join(script_dir,'invalid/root_array.json')) as f:
            invalid = json.load(f)

        self.assertRaises(ValidationError, validate, invalid, schema)