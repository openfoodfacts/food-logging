To re-generate the Python model from the schema use:

```
datamodel-codegen  --input schemas/openapi.yaml --input-file-type openapi --output-model-type pydantic_v2.BaseModel --field-constraints --output service/model.py
```

Note that currently datamodel-code-generator doesn't handle `unevaluatedProperties`

To generate the openapi.md from the API docs use:

```
npx widdershins --code true --omitHeader schemas/openapi.yaml -o schemas/openapi.md
```

