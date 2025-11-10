import os
import urllib.request, json

with urllib.request.urlopen(
    "https://static.openfoodfacts.org/data/taxonomies/nutrients.json"
) as url:
    nutrients = json.load(url)
    schema = {
        "$id": "https://static.openfoodfacts.org/food-logging/facets.json",
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$defs": {
            "code": {
                "enum": [
                    nutrient[0].split(":")[1]
                    for nutrient in sorted(nutrients.items())
                    if nutrient[1].get("automatically_computed", {}).get("en") != "yes" and nutrient[1].get("unit", {}).get("en") != "%"
                ]
            }
        },
    }

    filename = os.path.join(os.path.dirname(__file__), "../schemas/facets.json")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(schema, ensure_ascii=False, sort_keys=True, indent=2))
