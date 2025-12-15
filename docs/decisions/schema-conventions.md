# Schema Conventions

Work in progress document covering issues found when designing the schema layout.

## Sub-schema files

Tried creating a file that just contained the sub-schema, but it then does not appear in the Schemas section in the Swagger UI. Needs to be under `components/schemas` to appear in the Swagger UI.

It was found that the Python `datamodel-codegen` tool could not cope with [external references](https://github.com/koxudaxi/datamodel-code-generator/issues/2207) so all schemas are now bundled in one `openapi.json` file.

## Sub-schema folders

The redocly [split](https://idratherbewriting.com/learnapidoc/pubapis_redocly.html#break_openapi) command creates components/schemas sub-folders but this would add a lot of redundancy to the paths, e.g. `components/schemas/facets.json#/components/schemas/facetCode`

For brevity a `lib` folder is used.

Above superseded by decision to bundle all schemas in one file.

## Use of $id and $schema

These were showing up in the Swagger UI when trying to use files that just contained the sub-schema so they were removed. However, they could be restored now that we are always putting schemas under `components/schemas`

## title

When referencing sub-schemas the Swagger UI shows a messy path if there is no title. Hence the title is always used and always matches the schema name.

In the Swagger UI an odd name is still shown on the `Schema` tab under the specific paths if an external ref is used. Adding a `title` doesn't seem to fix this.

To work around this all of the root schemas are defined in the `openapi.json` file.

## description

Markdown formatting is used as per the OpenAPI specification, even though this is not officially supported in JSON Schema.

## Additional Properties

It looks like the Python `datamodel-codegen` tool doesn't recognize additionalProperties when this is an object and not just `true` when specified on a schema that also has other non-custom properties.

To work around this the documentation for additionalProperties is included in the root of the schema.

Also it was found that widdershins coped better if the schema for additionalProperties was included as a reference rather than inline.