To re-generate the Python model from the schema use:

```
datamodel-codegen  --input schemas/openapi.yaml --input-file-type openapi --output-model-type pydantic_v2.BaseModel --field-constraints --output service/model.py
```

To generate the openapi.md from the API docs use:

```
npx widdershins --code true --omitHeader --user_templates templates schemas/openapi.yaml -o schemas/README.md
```

To refresh the facet list from the OFF taxonomy use:

```
python ./tools/update_facet_codes.py
```