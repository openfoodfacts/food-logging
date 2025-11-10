Te re-generate the Python model from the schema use:

```
datamodel-codegen  --input schemas/metadata.json --input-file-type jsonschema --output-model-type pydantic_v2.BaseModel --field-constraints --output service/model.py
```

Note that currently datamodel-code-generator doesn't handle `unevaluatedProperties`