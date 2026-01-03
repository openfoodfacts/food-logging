
<h1 id="food-consumption-logging-data-exchange">Food Consumption Logging Data Exchange v0.0.1</h1>

The reason for developing a standard for food logging data exchange is to ensure that people are not locked in to a single application once they start logging food data. For example, they might want to switch to a different application for logging, use another application to analyze their food logging history or supply data to a third party, such as researchers or medical practitioners.

This document defines the specification for a web service API for storing food logging data and metadata. The metadata is also used to describe the structure of a Meals CSV file used for interactive import / export operations.

Exports will be packaged in a zip file with an arbitrary name (determined by the user). Each zip file will contain the following:

* meals.csv
* meals_metadata.json

### meals.csv

This is a CSV file to make it as simple as possible for moderately technical Consumers or delegated third-parties to analyze their own data in a spreadsheet or database. All column names should be human readable in the user's chosen language. The Metadata file will cross-reference the column names against pre-defined properties, like Meal time, Meal Type, Food and Nutrients.

Foods will include the human readable name, e.g. "Baked Beans", that was presented to the user when they selected the Food.

Date times will be recorded in the user's local format and timezone, as identified in the metadata. Items consumed as part of the same meal should have exactly the same date time to allow grouping of Meals for display or analysis purposes.

Facets, like Nutrients, will have a single column name with a consistent unit of measure (identified in the metadata). The exporter could choose to include the unit in the column name if they feel this would be helpful. All Facets that were retrieved from the Source of the Food information that were either presented to the user or used in calculations should be included in the export.

It is suggested that fields of less interest to the Consumer, such as the Source, Global Trade Item Number (GTIN) and Image URLs are included at the "end" of the export line (this might be the leftmost columns in a right to left language).

### meals_metadata.json

This is a JSON representation of the [metadata](#schemametadata) that describes the structure of the Meals CSV file.

# Authentication

- HTTP Authentication, scheme: bearer<br/>APIs should be secured using OAuth using Bearer tokens supplied in the [HTTP Authorization Request Header](https://datatracker.ietf.org/doc/html/rfc6750#section-2.1).
The method of authentication and obtaining and renewing access tokens is beyond the scope of this specification.

<h1 id="food-consumption-logging-data-exchange-default">Methods</h1>

## GET /metadata

Get the metadata for the Consumer identified in the authorization header

> Example responses

> 200 Response

```json
{
  "columns": {
    "Food": {
      "type": "food"
    },
    "Code": {
      "type": "code"
    },
    "Protein": {
      "type": "facet",
      "code": "protein"
    },
    "Source": {
      "type": "source",
      "values": {
        "Bar Code": {
          "source": "gtin",
          "location": 3014517900101
        }
      }
    }
  },
  "locale": "fr-FR",
  "timezone": "Europe/France"
}
```

<h3 id="get__metadata-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[metadata](#schemametadata)|

<aside class="warning">
To perform this operation, you must be authenticated with a Bearer Token
</aside>

## PUT /metadata

Store the metadata for the Consumer identified in the authorization header

> Body parameter

```json
{
  "columns": {
    "Food": {
      "type": "food"
    },
    "Code": {
      "type": "code"
    },
    "Protein": {
      "type": "facet",
      "code": "protein"
    },
    "Source": {
      "type": "source",
      "values": {
        "Bar Code": {
          "source": "gtin",
          "location": 3014517900101
        }
      }
    }
  },
  "locale": "fr-FR",
  "timezone": "Europe/France"
}
```

<h3 id="put__metadata-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[metadata](#schemametadata)|false|none|

<h3 id="put__metadata-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|

<aside class="warning">
To perform this operation, you must be authenticated with a Bearer Token
</aside>

## POST /meals

Creates meals from the supplied array in the HTTP request body

> Body parameter

```json
[
  {
    "time": "2025-05-01T05:00:00Z",
    "meal": "breakfast",
    "food": "Kelloggs Corn Flakes",
    "entered_quantity": 1,
    "entered_unit": "serving",
    "quantity": 30,
    "unit": "g",
    "facets": [
      {
        "code": "proteins",
        "value": 0.3
      },
      {
        "code": "carbohydrate",
        "value": 24
      },
      {
        "code": "fat",
        "value": 1
      }
    ],
    "source": "gtin",
    "location": "3014517900101",
    "code": "5059319030487",
    "image": "https://images.openfoodfacts.org/images/products/505/931/903/0487/front_en.3.400.jpg",
    "https://openfoodfacts.org/green.json": 53
  }
]
```

<h3 id="post__meals-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[meals](#schemameals)|false|none|

<h3 id="post__meals-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|

<aside class="warning">
To perform this operation, you must be authenticated with a Bearer Token
</aside>

## GET /meals

Returns an array of meals in the response body that were logged between mandatory "from_time" and "to_time" query parameters,
each specified in [ISO 8061](https://en.wikipedia.org/wiki/ISO_8601) format

<h3 id="get__meals-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|from_time|query|string(date-time)|true|The earliest dated meal to return, specified in [ISO 8061](https://en.wikipedia.org/wiki/ISO_8601) format|
|to_time|query|string(date-time)|true|The latest dated meal to return, specified in [ISO 8061](https://en.wikipedia.org/wiki/ISO_8601) format|

> Example responses

> 200 Response

```json
[
  {
    "time": "2025-05-01T05:00:00Z",
    "meal": "breakfast",
    "food": "Kelloggs Corn Flakes",
    "entered_quantity": 1,
    "entered_unit": "serving",
    "quantity": 30,
    "unit": "g",
    "facets": [
      {
        "code": "proteins",
        "value": 0.3
      },
      {
        "code": "carbohydrate",
        "value": 24
      },
      {
        "code": "fat",
        "value": 1
      }
    ],
    "source": "gtin",
    "location": "3014517900101",
    "code": "5059319030487",
    "image": "https://images.openfoodfacts.org/images/products/505/931/903/0487/front_en.3.400.jpg",
    "https://openfoodfacts.org/green.json": 53
  }
]
```

<h3 id="get__meals-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[meals](#schemameals)|

<aside class="warning">
To perform this operation, you must be authenticated with a Bearer Token
</aside>

## DELETE /meals

Deletes a meal item. The meal "id" is supplied in the path

<h3 id="delete__meals-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string(uuid)|true|The id of the meal to be deleted|

<h3 id="delete__meals-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|

<aside class="warning">
To perform this operation, you must be authenticated with a Bearer Token
</aside>

# Schemas

<h2 id="tocS_metadata">metadata</h2>

<a id="schemametadata"></a>
<a id="schema_metadata"></a>
<a id="tocSmetadata"></a>
<a id="tocsmetadata"></a>

Metadata provides a translation between the human readable column names and enumerations used in a Meals CSV file and standardized representations of these. Applications with limited user-customization could potentially hard-code their Metadata (per user language supported) if their exports always include the same standard column names.

The main component of the Metadata is the "columns" property which is a single object with a key for each column name mentioned in a Meals CSV file. The value associated with each column is an object whose "type" column will determine the standardized property the column represents. Additional attributes, specific to the type, will identify other data relevant to that property, e.g. the standard nutrient code and unit for a "facet" column.

Applications may add their own global properties. It is suggested that each application adds just one root property using a URI owned by that application as the key name. This URI would ideally point to a JSON Schema document describing the structure of the custom properties, but this is not essential.

```json
{
  "columns": {
    "Food": {
      "type": "food"
    },
    "Code": {
      "type": "code"
    },
    "Protein": {
      "type": "facet",
      "code": "protein"
    },
    "Source": {
      "type": "source",
      "values": {
        "Bar Code": {
          "source": "gtin",
          "location": 3014517900101
        }
      }
    }
  },
  "locale": "fr-FR",
  "timezone": "Europe/France"
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|columns|object|true|Object with a key for each column name used in the Meals CSV file|
|» **additionalProperties**|[columnDefinition](#schemacolumndefinition)|false|Maps the standard fields to the specified column name|
|locale|string|true|Combination of the user's [ISO 639 2-letter language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) and [ISO 3166 2-letter country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) separated with a hyphen|
|timezone|string|false|A standard [IANA TZ identifier](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)|

<h2 id="tocS_columnDefinition">columnDefinition</h2>

<a id="schemacolumndefinition"></a>
<a id="schema_columnDefinition"></a>
<a id="tocScolumndefinition"></a>
<a id="tocscolumndefinition"></a>

Maps the standard fields to the specified column name

```json
{
  "type": "time"
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|columnDefinition|any|false|Maps the standard fields to the specified column name|

oneOf

|Name|Type|Required|Description|
|---|---|---|---|
|*anonymous*|[timeColumn](#schematimecolumn)|false|The time that the meal was consumed|

xor

|Name|Type|Required|Description|
|---|---|---|---|
|*anonymous*|[mealColumn](#schemamealcolumn)|false|The different meal type names used, keyed with the value used in the CSV file.<br><br>Note the "daily" item refers to entries where the user has just recorded overall consumption throughout the day, e.g. 6 cups of coffee|

xor

|Name|Type|Required|Description|
|---|---|---|---|
|*anonymous*|[recipeColumn](#schemarecipecolumn)|false|The name of a Recipe used that links multiple related Foods in the Meal|

xor

|Name|Type|Required|Description|
|---|---|---|---|
|*anonymous*|[foodColumn](#schemafoodcolumn)|false|The name of the Food as it was presented to the user when they selected it from the Source|

xor

|Name|Type|Required|Description|
|---|---|---|---|
|*anonymous*|[enteredQuantityColumn](#schemaenteredquantitycolumn)|false|The amount of the Food that the user recorded in the specified "entered_unit". Formatted as a [JSON number](https://www.rfc-editor.org/rfc/rfc8259#page-7)|

xor

|Name|Type|Required|Description|
|---|---|---|---|
|*anonymous*|[enteredUnitColumn](#schemaenteredunitcolumn)|false|The unit used when recording the quantity of Food. This is a free format string in the end-user's language|

xor

|Name|Type|Required|Description|
|---|---|---|---|
|*anonymous*|[quantityColumn](#schemaquantitycolumn)|false|The amount of the Food in normalized units (grams for weight, milliliters for volume). Formatted as a [JSON number](https://www.rfc-editor.org/rfc/rfc8259#page-7)|

xor

|Name|Type|Required|Description|
|---|---|---|---|
|*anonymous*|[unitColumn](#schemaunitcolumn)|false|The normalized unit type. "g" for weight or "ml" for volume. Not localized. This should match the unit used in the Source.|

xor

|Name|Type|Required|Description|
|---|---|---|---|
|*anonymous*|[facetColumn](#schemafacetcolumn)|false|A particular facet of the food, typically a nutrient|

xor

|Name|Type|Required|Description|
|---|---|---|---|
|*anonymous*|[sourceColumn](#schemasourcecolumn)|false|The type of Food identifier used, keyed by the value used in the Meals CSV.<br><br>The value has a source and a location code, e.g. for GTIN the location code would be the [Global Location Number](https://navigator.gs1.org/gdsn/class-details?name=GLN&version=12)|

xor

|Name|Type|Required|Description|
|---|---|---|---|
|*anonymous*|[codeColumn](#schemacodecolumn)|false|The identifier for the Food in the specified Source|

xor

|Name|Type|Required|Description|
|---|---|---|---|
|*anonymous*|[imageColumn](#schemaimagecolumn)|false|URL to an image that was presented to the user when they selected the Food from the Source|

xor

|Name|Type|Required|Description|
|---|---|---|---|
|*anonymous*|[customColumn](#schemacustomcolumn)|false|Application properties that are specific to the individual meal. It is suggested that each application adds one code for each custom column using a URI owned by that application. This URI would ideally point to a JSON Schema document describing the structure of the custom type, but this is not essential.|

<h2 id="tocS_timeColumn">timeColumn</h2>

<a id="schematimecolumn"></a>
<a id="schema_timeColumn"></a>
<a id="tocStimecolumn"></a>
<a id="tocstimecolumn"></a>

The time that the meal was consumed

```json
{
  "type": "time"
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"time"|true|none|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_mealColumn">mealColumn</h2>

<a id="schemamealcolumn"></a>
<a id="schema_mealColumn"></a>
<a id="tocSmealcolumn"></a>
<a id="tocsmealcolumn"></a>

The different meal type names used, keyed with the value used in the CSV file.

Note the "daily" item refers to entries where the user has just recorded overall consumption throughout the day, e.g. 6 cups of coffee

```json
{
  "type": "meal",
  "values": {
    "Breakfast": "breakfast",
    "Mail Meal": "dinner",
    "Daily Allowance": "daily"
  }
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"meal"|true|none|
|values|object|true|Object whose key is the value that appears in the CSV file|
|» **additionalProperties**|[mealType](#schemamealtype)|false|Standardized identifier for the kind of meal. This is not an exhaustive cultural meal taxonomy,<br>but a practical subset for common use cases, derived from [here](https://en.wikipedia.org/wiki/Outline_of_meals)|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_mealType">mealType</h2>

<a id="schemamealtype"></a>
<a id="schema_mealType"></a>
<a id="tocSmealtype"></a>
<a id="tocsmealtype"></a>

Standardized identifier for the kind of meal. This is not an exhaustive cultural meal taxonomy,
but a practical subset for common use cases, derived from [here](https://en.wikipedia.org/wiki/Outline_of_meals)

### Enumerated Values

* breakfast
* second-breakfast
* brunch
* elevenses
* lunch
* tea
* dinner
* supper
* high-tea
* siu-yeh
* snack
* daily

<h2 id="tocS_recipeColumn">recipeColumn</h2>

<a id="schemarecipecolumn"></a>
<a id="schema_recipeColumn"></a>
<a id="tocSrecipecolumn"></a>
<a id="tocsrecipecolumn"></a>

The name of a Recipe used that links multiple related Foods in the Meal

```json
{
  "type": "recipe"
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"recipe"|true|none|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_foodColumn">foodColumn</h2>

<a id="schemafoodcolumn"></a>
<a id="schema_foodColumn"></a>
<a id="tocSfoodcolumn"></a>
<a id="tocsfoodcolumn"></a>

The name of the Food as it was presented to the user when they selected it from the Source

```json
{
  "type": "food"
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"food"|true|none|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_enteredQuantityColumn">enteredQuantityColumn</h2>

<a id="schemaenteredquantitycolumn"></a>
<a id="schema_enteredQuantityColumn"></a>
<a id="tocSenteredquantitycolumn"></a>
<a id="tocsenteredquantitycolumn"></a>

The amount of the Food that the user recorded in the specified "entered_unit". Formatted as a [JSON number](https://www.rfc-editor.org/rfc/rfc8259#page-7)

```json
{
  "type": "entered_quantity"
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"entered_quantity"|true|none|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_enteredUnitColumn">enteredUnitColumn</h2>

<a id="schemaenteredunitcolumn"></a>
<a id="schema_enteredUnitColumn"></a>
<a id="tocSenteredunitcolumn"></a>
<a id="tocsenteredunitcolumn"></a>

The unit used when recording the quantity of Food. This is a free format string in the end-user's language

```json
{
  "type": "unit"
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"entered_unit"|true|none|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_quantityColumn">quantityColumn</h2>

<a id="schemaquantitycolumn"></a>
<a id="schema_quantityColumn"></a>
<a id="tocSquantitycolumn"></a>
<a id="tocsquantitycolumn"></a>

The amount of the Food in normalized units (grams for weight, milliliters for volume). Formatted as a [JSON number](https://www.rfc-editor.org/rfc/rfc8259#page-7)

```json
{
  "type": "quantity"
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"quantity"|true|none|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_unitColumn">unitColumn</h2>

<a id="schemaunitcolumn"></a>
<a id="schema_unitColumn"></a>
<a id="tocSunitcolumn"></a>
<a id="tocsunitcolumn"></a>

The normalized unit type. "g" for weight or "ml" for volume. Not localized. This should match the unit used in the Source.

```json
{
  "type": "unit"
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"unit"|true|none|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_facetColumn">facetColumn</h2>

<a id="schemafacetcolumn"></a>
<a id="schema_facetColumn"></a>
<a id="tocSfacetcolumn"></a>
<a id="tocsfacetcolumn"></a>

A particular facet of the food, typically a nutrient

```json
{
  "type": "facet",
  "code": "protein"
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"facet"|true|none|
|code|[facetCode](#schemafacetcode)|true|Standard identifier for the facet, typically a nutrient. This list is derived from the Open Food Facts<br>[Nutrients](https://static.openfoodfacts.org/data/taxonomies/nutrients.json) taxonomy.|
|factor|integer|false|Value that the quantity of the Facet in the Meals CSV file must be divided by in order to convert it to the unit defined for the Facet type. Note that most nutrients will have a units of "g" but energy will be in "kJ" or "kcal". For example, a factor of 1000 would be specified if the values in the Meals CSV are expressed in mg. Defaults to 1 if omitted.|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_facetCode">facetCode</h2>

<a id="schemafacetcode"></a>
<a id="schema_facetCode"></a>
<a id="tocSfacetcode"></a>
<a id="tocsfacetcode"></a>

Standard identifier for the facet, typically a nutrient. This list is derived from the Open Food Facts
[Nutrients](https://static.openfoodfacts.org/data/taxonomies/nutrients.json) taxonomy.

### Enumerated Values

* acidity
* added-salt
* added-sugars
* alcohol
* alpha-linolenic-acid
* ammonium-chloride
* arachidic-acid
* arachidonic-acid
* bcaa
* behenic-acid
* beta-alanine
* beta-carotene
* beta-glucan
* bicarbonate
* biotin
* butyric-acid
* caffeine
* calcium
* calcium-iodate-anhydrous
* capric-acid
* caproic-acid
* caprylic-acid
* carbohydrates
* carbohydrates-total
* carbon-footprint
* carnitine
* casein
* cassia-gum
* cerotic-acid
* chloride
* chlorophyl
* cholesterol
* choline
* choline-chloride
* chromium
* copper
* copper-ii-sulphate-pentahydrate
* creatine
* dihomo-gamma-linolenic-acid
* docosahexaenoic-acid
* dry-residue
* eicosapentaenoic-acid
* elaidic-acid
* energy
* energy-from-fat
* energy-kcal
* energy-kj
* erucic-acid
* erythritol
* fat
* fiber
* fluoride
* folates
* fructose
* galactose
* gamma-linolenic-acid
* gamma-oryzanol
* glucose
* glycemic-index
* gondoic-acid
* hydrogencarbonate
* inositol
* insoluble-fiber
* iodine
* iron
* iron-ii-sulphate-monohydrate
* isomalt
* l-arginine
* l-citrulline
* l-cysteine
* l-glutamine
* l-glutathione
* l-isoleucine
* l-leucine
* l-valine
* lactose
* lauric-acid
* lignoceric-acid
* linoleic-acid
* magnesium
* maltitol
* maltodextrins
* maltose
* manganese
* manganous-sulphate-monohydrate
* mead-acid
* melatonin
* melissic-acid
* methylsulfonylmethane
* molybdenum
* monounsaturated-fat
* montanic-acid
* myristic-acid
* nervonic-acid
* nitrate
* nitrite
* nucleotides
* oleic-acid
* oligosaccharide
* omega-3-fat
* omega-6-fat
* omega-9-fat
* palmitic-acid
* pantothenic-acid
* ph
* phosphorus
* phylloquinone
* polydextrose
* polyols
* polyunsaturated-fat
* potassium
* potassium-iodide
* protein-value
* proteins
* psicose
* salt
* saturated-fat
* selenium
* serum-proteins
* silica
* sodium
* sodium-selenite
* soluble-fiber
* sorbitol
* spermidine
* starch
* stearic-acid
* sucrose
* sugars
* sulphate
* taurine
* trans-fat
* unsaturated-fat
* vitamin-a
* vitamin-b1
* vitamin-b12
* vitamin-b2
* vitamin-b6
* vitamin-b9
* vitamin-c
* vitamin-d
* vitamin-e
* vitamin-k
* vitamin-pp
* water
* water-hardness
* zinc
* zinc-sulphate-monohydrate

<h2 id="tocS_sourceColumn">sourceColumn</h2>

<a id="schemasourcecolumn"></a>
<a id="schema_sourceColumn"></a>
<a id="tocSsourcecolumn"></a>
<a id="tocssourcecolumn"></a>

The type of Food identifier used, keyed by the value used in the Meals CSV.

The value has a source and a location code, e.g. for GTIN the location code would be the [Global Location Number](https://navigator.gs1.org/gdsn/class-details?name=GLN&version=12)

```json
{
  "type": "source",
  "values": {
    "Bar code": {
      "source": "gtin",
      "location": 3014517900101
    },
    "Food code": {
      "source": "plu"
    }
  }
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"source"|true|none|
|values|object|true|Object whose key is the value that appears in the CSV file|
|» **additionalProperties**|[sourceValue](#schemasourcevalue)|false|Describes where the food code came from.|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_sourceValue">sourceValue</h2>

<a id="schemasourcevalue"></a>
<a id="schema_sourceValue"></a>
<a id="tocSsourcevalue"></a>
<a id="tocssourcevalue"></a>

Describes where the food code came from.

```json
{
  "source": "gtin",
  "location": "string"
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|source|[sourceType](#schemasourcetype)|true|The type of Food identifier used.<br>  * gtin: A GS1 [Global Trade Item Number](https://www.gs1.org/standards/id-keys/gtin), i.e. a product bar code.<br>  * plu: International Federation for Produce Standards [Price Look Up code](https://www.ifpsglobal.com/plu-codes-search)<br><br>Further source types, such as [USDA Foundation Foods](https://fdc.nal.usda.gov/food-search?type=Foundation), may be added in the future as the standard develops.|
|location|string|false|none|

<h2 id="tocS_sourceType">sourceType</h2>

<a id="schemasourcetype"></a>
<a id="schema_sourceType"></a>
<a id="tocSsourcetype"></a>
<a id="tocssourcetype"></a>

The type of Food identifier used.
  * gtin: A GS1 [Global Trade Item Number](https://www.gs1.org/standards/id-keys/gtin), i.e. a product bar code.
  * plu: International Federation for Produce Standards [Price Look Up code](https://www.ifpsglobal.com/plu-codes-search)

Further source types, such as [USDA Foundation Foods](https://fdc.nal.usda.gov/food-search?type=Foundation), may be added in the future as the standard develops.

### Enumerated Values

* gtin
* plu

<h2 id="tocS_codeColumn">codeColumn</h2>

<a id="schemacodecolumn"></a>
<a id="schema_codeColumn"></a>
<a id="tocScodecolumn"></a>
<a id="tocscodecolumn"></a>

The identifier for the Food in the specified Source

```json
{
  "type": "food"
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"code"|true|none|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_imageColumn">imageColumn</h2>

<a id="schemaimagecolumn"></a>
<a id="schema_imageColumn"></a>
<a id="tocSimagecolumn"></a>
<a id="tocsimagecolumn"></a>

URL to an image that was presented to the user when they selected the Food from the Source

```json
{
  "type": "image"
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"image"|true|none|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_customColumn">customColumn</h2>

<a id="schemacustomcolumn"></a>
<a id="schema_customColumn"></a>
<a id="tocScustomcolumn"></a>
<a id="tocscustomcolumn"></a>

Application properties that are specific to the individual meal. It is suggested that each application adds one code for each custom column using a URI owned by that application. This URI would ideally point to a JSON Schema document describing the structure of the custom type, but this is not essential.

```json
{
  "type": "custom",
  "code": "https://openfoodfacts.org/green.json"
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"custom"|true|none|
|code|string|true|The application specific identifier for the custom column. Ideally a URI owned by the application.|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_sequence">sequence</h2>

<a id="schemasequence"></a>
<a id="schema_sequence"></a>
<a id="tocSsequence"></a>
<a id="tocssequence"></a>

Column sequence

The column number when exporting as CSV

```json
0

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|Column sequence|integer|false|The column number when exporting as CSV|

<h2 id="tocS_meals">meals</h2>

<a id="schemameals"></a>
<a id="schema_meals"></a>
<a id="tocSmeals"></a>
<a id="tocsmeals"></a>

An array of meals.

```json
[
  {
    "time": "2025-05-01T05:00:00Z",
    "meal": "breakfast",
    "food": "Kelloggs Corn Flakes",
    "entered_quantity": 1,
    "entered_unit": "serving",
    "quantity": 30,
    "unit": "g",
    "facets": [
      {
        "code": "proteins",
        "value": 0.3
      },
      {
        "code": "carbohydrate",
        "value": 24
      },
      {
        "code": "fat",
        "value": 1
      }
    ],
    "source": "gtin",
    "location": "3014517900101",
    "code": "5059319030487",
    "image": "https://images.openfoodfacts.org/images/products/505/931/903/0487/front_en.3.400.jpg",
    "https://openfoodfacts.org/green.json": 53
  }
]

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|meals|[[meal](#schemameal)]|false|An array of meals.|

<h2 id="tocS_meal">meal</h2>

<a id="schemameal"></a>
<a id="schema_meal"></a>
<a id="tocSmeal"></a>
<a id="tocsmeal"></a>

A specific instance of a food that has been consumed.

Applications may add their own custom properties that are specific to the individual meal. It is suggested that each application adds one type for each custom column using a URI owned by that application as the key name. This URI would ideally point to a JSON Schema document describing the structure of the custom type, but this is not essential.

```json
{
  "time": "2025-05-01T05:00:00Z",
  "meal": "breakfast",
  "food": "Kelloggs Corn Flakes",
  "entered_quantity": 1,
  "entered_unit": "serving",
  "quantity": 30,
  "unit": "g",
  "facets": [
    {
      "code": "proteins",
      "value": 0.3
    },
    {
      "code": "carbohydrate",
      "value": 24
    },
    {
      "code": "fat",
      "value": 1
    }
  ],
  "source": "gtin",
  "location": "3014517900101",
  "code": "5059319030487",
  "image": "https://images.openfoodfacts.org/images/products/505/931/903/0487/front_en.3.400.jpg",
  "https://openfoodfacts.org/green.json": 53
}

```
### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|id|string(uuid)|false|A UUID string formatted according to [RFC 9562](https://datatracker.ietf.org/doc/html/rfc9562#name-uuid-format). Optional on new entries (will be generated by the receiving service)|
|time|string(date-time)|false|The time that the Meal was consumed in UTC following the [ISO 8061](https://en.wikipedia.org/wiki/ISO_8601) format|
|meal|[mealType](#schemamealtype)|false|Standardized identifier for the kind of meal. This is not an exhaustive cultural meal taxonomy,<br>but a practical subset for common use cases, derived from [here](https://en.wikipedia.org/wiki/Outline_of_meals)|
|recipe|string|false|The name of a Recipe used that links multiple related Foods in the meal|
|food|string|false|The name of the Food as it was presented to the user when they selected it from the Source|
|entered_quantity|number|false|The amount of the Food that the user recorded in the specified "entered_unit". Formatted according to the [JSON number standard](https://www.rfc-editor.org/rfc/rfc8259#page-7)|
|entered_unit|string|false|The unit used when recording the quantity of Food. This is a free format string in the end-user's language|
|quantity|number|false|The amount of the Food in normalized units (grams for weight, milliliters for volume). Formatted according to the [JSON number standard](https://www.rfc-editor.org/rfc/rfc8259#page-7)|
|unit|[unit](#schemaunit)|false|The normalized unit type. "g" for weight or "ml" for volume. This should match the unit used in the source.|
|facets|[object]|false|An array of objects where the `code` property will be a facet code as defined in this schema. e.g. "proteins", "carbohydrates-total", "vitamin-b12", "energy-kj" and the `value` property gives the quantity of the facet|
|» code|[facetCode](#schemafacetcode)|true|Standard identifier for the facet, typically a nutrient. This list is derived from the Open Food Facts<br>[Nutrients](https://static.openfoodfacts.org/data/taxonomies/nutrients.json) taxonomy.|
|» value|number|true|The quantity of the facet in the specific meal which will be in grams in most cases but energy will be in kJ or kcal|
|source|[sourceType](#schemasourcetype)|false|The type of Food identifier used.<br>  * gtin: A GS1 [Global Trade Item Number](https://www.gs1.org/standards/id-keys/gtin), i.e. a product bar code.<br>  * plu: International Federation for Produce Standards [Price Look Up code](https://www.ifpsglobal.com/plu-codes-search)<br><br>Further source types, such as [USDA Foundation Foods](https://fdc.nal.usda.gov/food-search?type=Foundation), may be added in the future as the standard develops.|
|location|string|false|The location code for the Source, e.g. for GTIN this would be the [Global Location Number](https://navigator.gs1.org/gdsn/class-details?name=GLN&version=12)|
|code|string|false|The identifier for the Food in the specified Source|
|image|string|false|URL to an image that was presented to the user when they selected the Food from the Source|

<h2 id="tocS_unit">unit</h2>

<a id="schemaunit"></a>
<a id="schema_unit"></a>
<a id="tocSunit"></a>
<a id="tocsunit"></a>

The normalized unit type. "g" for weight or "ml" for volume. This should match the unit used in the source.

### Enumerated Values

* g
* ml

