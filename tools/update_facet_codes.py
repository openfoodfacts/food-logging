import os
import urllib.request, json

with urllib.request.urlopen(
    "https://static.openfoodfacts.org/data/taxonomies/nutrients.json"
) as url:
    nutrients = json.load(url)
    facet_enum = [
                        nutrient[0].split(":")[1]
                        for nutrient in sorted(nutrients.items())
                        if nutrient[1].get("automatically_computed", {}).get("en")
                        != "yes"
                        and nutrient[1].get("unit", {}).get("en") != "%"
                    ]

    filename = os.path.join(os.path.dirname(__file__), "../schemas/openapi.json")
    with open(filename, "r", encoding="utf-8") as f:
        schema = json.load(f)
        
    schema['components']['schemas']['facetCode']['enum'] = facet_enum
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(schema, ensure_ascii=False, indent=2))
