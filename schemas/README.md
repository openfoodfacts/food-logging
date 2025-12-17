
<h1 id="food-consumption-logging-data-exchange">Food Consumption Logging Data Exchange v0.0.1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

The reason for developing a standard for food logging data exchange is to ensure that people are not locked in to a single application once they start logging food data. For example, they might want to switch to a different application for logging, use another application to analyze their food logging history or supply data to a third party, such as researchers or medical practitioners.

<h1 id="food-consumption-logging-data-exchange-default">Default</h1>

## get__metadata

`GET /metadata`

> Example responses

> 200 Response

```json
{
  "columns": {
    "columns": {
      "Food": {
        "type": "food"
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

<aside class="success">
This operation does not require authentication
</aside>

## put__metadata

`PUT /metadata`

> Body parameter

```json
{
  "columns": {
    "columns": {
      "Food": {
        "type": "food"
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

<aside class="success">
This operation does not require authentication
</aside>

## post__meals

`POST /meals`

> Body parameter

```json
[
  {
    "id": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
    "time": "2025-07-30T15:56:32Z",
    "meal": "breakfast",
    "recipe": "White coffee",
    "food": "Instant Coffee Powder",
    "entered_quantity": 1,
    "entered_unit": "tsp",
    "quantity": 15,
    "unit": "g",
    "facets": [
      {
        "code": "protein",
        "value": 0
      },
      {
        "code": "iron",
        "value": 0.02
      },
      {
        "code": "vitamin-b12",
        "value": 0.0000012
      }
    ],
    "source": "gtin",
    "location": 3014517900101,
    "code": 4056489440628,
    "image": "https://images.openfoodfacts.net/images/products/405/648/944/0628/front_en.26.400.jpg"
  }
]
```

<h3 id="post__meals-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[meal](#schemameal)|false|none|

<h3 id="post__meals-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_metadata">metadata</h2>

<a id="schemametadata"></a>
<a id="schema_metadata"></a>
<a id="tocSmetadata"></a>
<a id="tocsmetadata"></a>

```json
{
  "columns": {
    "columns": {
      "Food": {
        "type": "food"
      }
    }
  },
  "locale": "fr-FR",
  "timezone": "Europe/France"
}

```

metadata

Metadata provides a translation between the human readable column names and enumerations used in a Meals CSV file and standardized representations of these. Applications with limited user-customization could potentially hard-code their Metadata (per user language supported) if their exports always include the same standard column names.

The main component of the Metadata is the "columns" property which is a single object with a key for each column name mentioned in a Meals CSV file. The value associated with each column is an object whose "type" column will determine the standardized property the column represents. Additional attributes, specific to the type, will identify other data relevant to that property, e.g. the standard nutrient code and unit for a "facet" column.

Applications may add their own global properties. It is suggested that each application adds just one root property using a URI owned by that application as the key name. This URI would ideally point to a JSON Schema document describing the structure of the custom properties, but this is not essential.

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

```json
{
  "type": "time"
}

```

columnDefinition

Maps the standard fields to the specified column name

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

```json
{
  "type": "time"
}

```

timeColumn

The time that the meal was consumed

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

mealColumn

The different meal type names used, keyed with the value used in the CSV file.

Note the "daily" item refers to entries where the user has just recorded overall consumption throughout the day, e.g. 6 cups of coffee

### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"meal"|true|none|
|values|object|true|Object whose key is the value that appears in the CSV file|
|» **additionalProperties**|[mealType](#schemamealtype)|false|Standardized identifier for the kind of meal, derived from [here](https://en.wikipedia.org/wiki/Outline_of_meals)|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_mealType">mealType</h2>

<a id="schemamealtype"></a>
<a id="schema_mealType"></a>
<a id="tocSmealtype"></a>
<a id="tocsmealtype"></a>

```json
"breakfast"

```

mealType

Standardized identifier for the kind of meal, derived from [here](https://en.wikipedia.org/wiki/Outline_of_meals)

### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|mealType|any|false|Standardized identifier for the kind of meal, derived from [here](https://en.wikipedia.org/wiki/Outline_of_meals)|

#### Enumerated Values

|Property|Value|
|---|---|
|mealType|breakfast|
|mealType|second-breakfast|
|mealType|brunch|
|mealType|elevenses|
|mealType|lunch|
|mealType|tea|
|mealType|dinner|
|mealType|supper|
|mealType|high-tea|
|mealType|siu-yeh|
|mealType|snack|
|mealType|daily|

<h2 id="tocS_recipeColumn">recipeColumn</h2>

<a id="schemarecipecolumn"></a>
<a id="schema_recipeColumn"></a>
<a id="tocSrecipecolumn"></a>
<a id="tocsrecipecolumn"></a>

```json
{
  "type": "recipe"
}

```

recipeColumn

The name of a Recipe used that links multiple related Foods in the Meal

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

```json
{
  "type": "food"
}

```

foodColumn

The name of the Food as it was presented to the user when they selected it from the Source

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

```json
{
  "type": "entered_quantity"
}

```

enteredQuantityColumn

The amount of the Food that the user recorded in the specified "entered_unit". Formatted as a [JSON number](https://www.rfc-editor.org/rfc/rfc8259#page-7)

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

```json
{
  "type": "unit"
}

```

enteredUnitColumn

The unit used when recording the quantity of Food. This is a free format string in the end-user's language

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

```json
{
  "type": "quantity"
}

```

quantityColumn

The amount of the Food in normalized units (grams for weight, milliliters for volume). Formatted as a [JSON number](https://www.rfc-editor.org/rfc/rfc8259#page-7)

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

```json
{
  "type": "unit"
}

```

unitColumn

The normalized unit type. "g" for weight or "ml" for volume. Not localized. This should match the unit used in the Source.

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

```json
{
  "type": "facet",
  "code": "protein"
}

```

facetColumn

A particular facet of the food, typically a nutrient

### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|type|"facet"|true|none|
|code|[facetCode](#schemafacetcode)|true|Standard identifier for the facet, typically a nutrient|
|factor|integer|false|Value that the quantity of the Facet in the Meals CSV file must be divided by in order to convert it to the unit defined for the Facet type. Note that most nutrients will have a units of "g" but energy will be in "kJ" or "kcal". For example, a factor of 1000 would be specified if the values in the Meals CSV are expressed in mg. Defaults to 1 if omitted.|
|sequence|[sequence](#schemasequence)|false|The column number when exporting as CSV|

<h2 id="tocS_facetCode">facetCode</h2>

<a id="schemafacetcode"></a>
<a id="schema_facetCode"></a>
<a id="tocSfacetcode"></a>
<a id="tocsfacetcode"></a>

```json
"acidity"

```

facetCode

Standard identifier for the facet, typically a nutrient

### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|facetCode|any|false|Standard identifier for the facet, typically a nutrient|

#### Enumerated Values

|Property|Value|
|---|---|
|facetCode|acidity|
|facetCode|added-salt|
|facetCode|added-sugars|
|facetCode|alcohol|
|facetCode|alpha-linolenic-acid|
|facetCode|ammonium-chloride|
|facetCode|arachidic-acid|
|facetCode|arachidonic-acid|
|facetCode|bcaa|
|facetCode|behenic-acid|
|facetCode|beta-alanine|
|facetCode|beta-carotene|
|facetCode|beta-glucan|
|facetCode|bicarbonate|
|facetCode|biotin|
|facetCode|butyric-acid|
|facetCode|caffeine|
|facetCode|calcium|
|facetCode|calcium-iodate-anhydrous|
|facetCode|capric-acid|
|facetCode|caproic-acid|
|facetCode|caprylic-acid|
|facetCode|carbohydrates|
|facetCode|carbohydrates-total|
|facetCode|carbon-footprint|
|facetCode|carnitine|
|facetCode|casein|
|facetCode|cassia-gum|
|facetCode|cerotic-acid|
|facetCode|chloride|
|facetCode|chlorophyl|
|facetCode|cholesterol|
|facetCode|choline|
|facetCode|choline-chloride|
|facetCode|chromium|
|facetCode|copper|
|facetCode|copper-ii-sulphate-pentahydrate|
|facetCode|creatine|
|facetCode|dihomo-gamma-linolenic-acid|
|facetCode|docosahexaenoic-acid|
|facetCode|dry-residue|
|facetCode|eicosapentaenoic-acid|
|facetCode|elaidic-acid|
|facetCode|energy|
|facetCode|energy-from-fat|
|facetCode|energy-kcal|
|facetCode|energy-kj|
|facetCode|erucic-acid|
|facetCode|erythritol|
|facetCode|fat|
|facetCode|fiber|
|facetCode|fluoride|
|facetCode|folates|
|facetCode|fructose|
|facetCode|galactose|
|facetCode|gamma-linolenic-acid|
|facetCode|gamma-oryzanol|
|facetCode|glucose|
|facetCode|glycemic-index|
|facetCode|gondoic-acid|
|facetCode|hydrogencarbonate|
|facetCode|inositol|
|facetCode|insoluble-fiber|
|facetCode|iodine|
|facetCode|iron|
|facetCode|iron-ii-sulphate-monohydrate|
|facetCode|isomalt|
|facetCode|l-arginine|
|facetCode|l-citrulline|
|facetCode|l-cysteine|
|facetCode|l-glutamine|
|facetCode|l-glutathione|
|facetCode|l-isoleucine|
|facetCode|l-leucine|
|facetCode|l-valine|
|facetCode|lactose|
|facetCode|lauric-acid|
|facetCode|lignoceric-acid|
|facetCode|linoleic-acid|
|facetCode|magnesium|
|facetCode|maltitol|
|facetCode|maltodextrins|
|facetCode|maltose|
|facetCode|manganese|
|facetCode|manganous-sulphate-monohydrate|
|facetCode|mead-acid|
|facetCode|melatonin|
|facetCode|melissic-acid|
|facetCode|methylsulfonylmethane|
|facetCode|molybdenum|
|facetCode|monounsaturated-fat|
|facetCode|montanic-acid|
|facetCode|myristic-acid|
|facetCode|nervonic-acid|
|facetCode|nitrate|
|facetCode|nitrite|
|facetCode|nucleotides|
|facetCode|oleic-acid|
|facetCode|oligosaccharide|
|facetCode|omega-3-fat|
|facetCode|omega-6-fat|
|facetCode|omega-9-fat|
|facetCode|palmitic-acid|
|facetCode|pantothenic-acid|
|facetCode|ph|
|facetCode|phosphorus|
|facetCode|phylloquinone|
|facetCode|polydextrose|
|facetCode|polyols|
|facetCode|polyunsaturated-fat|
|facetCode|potassium|
|facetCode|potassium-iodide|
|facetCode|protein-value|
|facetCode|proteins|
|facetCode|psicose|
|facetCode|salt|
|facetCode|saturated-fat|
|facetCode|selenium|
|facetCode|serum-proteins|
|facetCode|silica|
|facetCode|sodium|
|facetCode|sodium-selenite|
|facetCode|soluble-fiber|
|facetCode|sorbitol|
|facetCode|spermidine|
|facetCode|starch|
|facetCode|stearic-acid|
|facetCode|sucrose|
|facetCode|sugars|
|facetCode|sulphate|
|facetCode|taurine|
|facetCode|trans-fat|
|facetCode|unsaturated-fat|
|facetCode|vitamin-a|
|facetCode|vitamin-b1|
|facetCode|vitamin-b12|
|facetCode|vitamin-b2|
|facetCode|vitamin-b6|
|facetCode|vitamin-b9|
|facetCode|vitamin-c|
|facetCode|vitamin-d|
|facetCode|vitamin-e|
|facetCode|vitamin-k|
|facetCode|vitamin-pp|
|facetCode|water|
|facetCode|water-hardness|
|facetCode|zinc|
|facetCode|zinc-sulphate-monohydrate|

<h2 id="tocS_sourceColumn">sourceColumn</h2>

<a id="schemasourcecolumn"></a>
<a id="schema_sourceColumn"></a>
<a id="tocSsourcecolumn"></a>
<a id="tocssourcecolumn"></a>

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

sourceColumn

The type of Food identifier used, keyed by the value used in the Meals CSV.

The value has a source and a location code, e.g. for GTIN the location code would be the [Global Location Number](https://navigator.gs1.org/gdsn/class-details?name=GLN&version=12)

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

```json
{
  "source": "gtin",
  "location": "string"
}

```

sourceValue

Describes where the food code came from.

### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|source|[sourceType](#schemasourcetype)|true|The type of Food identifier used|
|location|string|false|none|

<h2 id="tocS_sourceType">sourceType</h2>

<a id="schemasourcetype"></a>
<a id="schema_sourceType"></a>
<a id="tocSsourcetype"></a>
<a id="tocssourcetype"></a>

```json
"gtin"

```

sourceType

The type of Food identifier used

### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|sourceType|any|false|The type of Food identifier used|

#### Enumerated Values

|Property|Value|
|---|---|
|sourceType|gtin|
|sourceType|plu|

<h2 id="tocS_codeColumn">codeColumn</h2>

<a id="schemacodecolumn"></a>
<a id="schema_codeColumn"></a>
<a id="tocScodecolumn"></a>
<a id="tocscodecolumn"></a>

```json
{
  "type": "food"
}

```

codeColumn

The identifier for the Food in the specified Source

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

```json
{
  "type": "image"
}

```

imageColumn

URL to an image that was presented to the user when they selected the Food from the Source

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

```json
{
  "type": "custom",
  "code": "https://openfoodfacts.org/green.json"
}

```

customColumn

Application properties that are specific to the individual meal. It is suggested that each application adds one code for each custom column using a URI owned by that application. This URI would ideally point to a JSON Schema document describing the structure of the custom type, but this is not essential.

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

```json
0

```

Column sequence

The column number when exporting as CSV

### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|Column sequence|integer|false|The column number when exporting as CSV|

<h2 id="tocS_meal">meal</h2>

<a id="schemameal"></a>
<a id="schema_meal"></a>
<a id="tocSmeal"></a>
<a id="tocsmeal"></a>

```json
{
  "id": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "time": "2025-07-30T15:56:32Z",
  "meal": "breakfast",
  "recipe": "White coffee",
  "food": "Instant Coffee Powder",
  "entered_quantity": 1,
  "entered_unit": "tsp",
  "quantity": 15,
  "unit": "g",
  "facets": [
    {
      "code": "protein",
      "value": 0
    },
    {
      "code": "iron",
      "value": 0.02
    },
    {
      "code": "vitamin-b12",
      "value": 0.0000012
    }
  ],
  "source": "gtin",
  "location": 3014517900101,
  "code": 4056489440628,
  "image": "https://images.openfoodfacts.net/images/products/405/648/944/0628/front_en.26.400.jpg"
}

```

meal

A specific instance of a food that has been consumed.

Applications may add their own custom properties that are specific to the individual meal. It is suggested that each application adds one type for each custom column using a URI owned by that application as the key name. This URI would ideally point to a JSON Schema document describing the structure of the custom type, but this is not essential.

### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|id|string(uuid)|false|A UUID string formatted according to [RFC 9562](https://datatracker.ietf.org/doc/html/rfc9562#name-uuid-format). Optional on new entries (will be generated by the receiving service)|
|time|string(date-time)|false|The time that the Meal was consumed in UTC following the [ISO 8061](https://en.wikipedia.org/wiki/ISO_8601) format|
|meal|[mealType](#schemamealtype)|false|Standardized identifier for the kind of meal, derived from [here](https://en.wikipedia.org/wiki/Outline_of_meals)|
|recipe|string|false|The name of a Recipe used that links multiple related Foods in the meal|
|food|string|false|The name of the Food as it was presented to the user when they selected it from the Source|
|entered_quantity|number|false|The amount of the Food that the user recorded in the specified "entered_unit". Formatted according to the [JSON number standard](https://www.rfc-editor.org/rfc/rfc8259#page-7)|
|entered_unit|string|false|The unit used when recording the quantity of Food. This is a free format string in the end-user's language|
|quantity|number|false|The amount of the Food in normalized units (grams for weight, milliliters for volume). Formatted according to the [JSON number standard](https://www.rfc-editor.org/rfc/rfc8259#page-7)|
|unit|[unit](#schemaunit)|false|The normalized unit type. "g" for weight or "ml" for volume. This should match the unit used in the source.|
|facets|[object]|false|An array of objects where the `code` property will be a facet code as defined in this schema. e.g. "proteins", "carbohydrates-total", "vitamin-b12", "energy-kj" and the `value` property gives the quantity of the facet|
|» code|[facetCode](#schemafacetcode)|true|Standard identifier for the facet, typically a nutrient|
|» value|number|true|The quantity of the facet in the specific meal which will be in grams in most cases but energy will be in kJ or kcal|
|source|[sourceType](#schemasourcetype)|false|The type of Food identifier used|
|location|string|false|The location code for the Source, e.g. for GTIN this would be the [Global Location Number](https://navigator.gs1.org/gdsn/class-details?name=GLN&version=12)|
|code|string|false|The identifier for the Food in the specified Source|
|image|string|false|URL to an image that was presented to the user when they selected the Food from the Source|

<h2 id="tocS_unit">unit</h2>

<a id="schemaunit"></a>
<a id="schema_unit"></a>
<a id="tocSunit"></a>
<a id="tocsunit"></a>

```json
"g"

```

unit

The normalized unit type. "g" for weight or "ml" for volume. This should match the unit used in the source.

### Properties

|Name|Type|Required|Description|
|---|---|---|---|
|unit|any|false|The normalized unit type. "g" for weight or "ml" for volume. This should match the unit used in the source.|

#### Enumerated Values

|Property|Value|
|---|---|
|unit|g|
|unit|ml|

undefined

