Te re-generate the Python model from the schema use:

```
datamodel-codegen  --input schemas/metadata.json --input-file-type jsonschema --output-model-type pydantic_v2.BaseModel --field-constraints --class-name Metadata --output service/model.py
```

To generate the Meal model use:

```
datamodel-codegen  --input schemas/meal.json --input-file-type jsonschema --output-model-type pydantic_v2.BaseModel --field-constraints --class-name Meal --output service/meal.py
```

Note that currently datamodel-code-generator doesn't handle `unevaluatedProperties`