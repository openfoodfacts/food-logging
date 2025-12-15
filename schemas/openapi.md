<!-- Generator: Widdershins v4.0.1 -->

<h1 id="food-consumption-logging-data-exchange">Food Consumption Logging Data Exchange v0.0.1</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="food-consumption-logging-data-exchange-default">Default</h1>

## get__metadata

`GET /metadata`

> Example responses

> 200 Response

```json
{
  "columns": {
    "ColumnName1": {
      "sequence": 0,
      "type": "time"
    },
    "ColumnName2": {
      "sequence": 0,
      "type": "time"
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
    "ColumnName1": {
      "sequence": 0,
      "type": "time"
    },
    "ColumnName2": {
      "sequence": 0,
      "type": "time"
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
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "time": "2019-08-24T14:15:22Z",
    "meal": "breakfast",
    "recipe": "string",
    "food": "string",
    "entered_quantity": 0,
    "entered_unit": "string",
    "quantity": 0,
    "unit": "g",
    "facets": [
      {
        "code": "acidity",
        "value": 0
      }
    ],
    "source": "gtin",
    "location": "string",
    "code": "string",
    "image": "string"
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
<!-- backwards compatibility -->
<a id="schemametadata"></a>
<a id="schema_metadata"></a>
<a id="tocSmetadata"></a>
<a id="tocsmetadata"></a>

```json
{
  "columns": {
    "ColumnName1": {
      "sequence": 0,
      "type": "time"
    },
    "ColumnName2": {
      "sequence": 0,
      "type": "time"
    }
  },
  "locale": "fr-FR",
  "timezone": "Europe/France"
}

```

metadata

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|columns|object|true|none|Object with a key for each column name used in the Meals CSV file|
|» **additionalProperties**|[column](#schemacolumn)|false|none|none|
|locale|string|true|none|none|
|timezone|string|false|none|none|

<h2 id="tocS_column">column</h2>
<!-- backwards compatibility -->
<a id="schemacolumn"></a>
<a id="schema_column"></a>
<a id="tocScolumn"></a>
<a id="tocscolumn"></a>

```json
{
  "sequence": 0,
  "type": "time"
}

```

### Properties

oneOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[timeColumn](#schematimecolumn)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[mealColumn](#schemamealcolumn)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[recipeColumn](#schemarecipecolumn)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[foodColumn](#schemafoodcolumn)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[enteredQuantityColumn](#schemaenteredquantitycolumn)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[enteredUnitColumn](#schemaenteredunitcolumn)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[quantityColumn](#schemaquantitycolumn)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[unitColumn](#schemaunitcolumn)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[facetColumn](#schemafacetcolumn)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[sourceColumn](#schemasourcecolumn)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[codeColumn](#schemacodecolumn)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[imageColumn](#schemaimagecolumn)|false|none|none|

xor

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[customColumn](#schemacustomcolumn)|false|none|Application properties that are specific to the individual meal. It is suggested that each application adds one code for each custom column using a URI owned by that application. This URI would ideally point to a JSON Schema document describing the structure of the custom type, but this is not essential.|

<h2 id="tocS_baseColumn">baseColumn</h2>
<!-- backwards compatibility -->
<a id="schemabasecolumn"></a>
<a id="schema_baseColumn"></a>
<a id="tocSbasecolumn"></a>
<a id="tocsbasecolumn"></a>

```json
{
  "sequence": 0
}

```

baseColumn

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sequence|integer|false|none|The column number when exporting as CSV|

<h2 id="tocS_timeColumn">timeColumn</h2>
<!-- backwards compatibility -->
<a id="schematimecolumn"></a>
<a id="schema_timeColumn"></a>
<a id="tocStimecolumn"></a>
<a id="tocstimecolumn"></a>

```json
{
  "sequence": 0,
  "type": "time"
}

```

timeColumn

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|timeColumn|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[baseColumn](#schemabasecolumn)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|any|false|none|none|

<h2 id="tocS_mealColumn">mealColumn</h2>
<!-- backwards compatibility -->
<a id="schemamealcolumn"></a>
<a id="schema_mealColumn"></a>
<a id="tocSmealcolumn"></a>
<a id="tocsmealcolumn"></a>

```json
{
  "sequence": 0,
  "type": "meal",
  "values": {
    "property1": "breakfast",
    "property2": "breakfast"
  }
}

```

mealColumn

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mealColumn|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[baseColumn](#schemabasecolumn)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|any|false|none|none|
|» values|object|false|none|none|
|»» **additionalProperties**|[mealType](#schemamealtype)|false|none|none|

<h2 id="tocS_mealType">mealType</h2>
<!-- backwards compatibility -->
<a id="schemamealtype"></a>
<a id="schema_mealType"></a>
<a id="tocSmealtype"></a>
<a id="tocsmealtype"></a>

```json
"breakfast"

```

mealType

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mealType|any|false|none|none|

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
<!-- backwards compatibility -->
<a id="schemarecipecolumn"></a>
<a id="schema_recipeColumn"></a>
<a id="tocSrecipecolumn"></a>
<a id="tocsrecipecolumn"></a>

```json
{
  "sequence": 0,
  "type": "recipe"
}

```

recipeColumn

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|recipeColumn|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[baseColumn](#schemabasecolumn)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|any|false|none|none|

<h2 id="tocS_foodColumn">foodColumn</h2>
<!-- backwards compatibility -->
<a id="schemafoodcolumn"></a>
<a id="schema_foodColumn"></a>
<a id="tocSfoodcolumn"></a>
<a id="tocsfoodcolumn"></a>

```json
{
  "sequence": 0,
  "type": "food"
}

```

foodColumn

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|foodColumn|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[baseColumn](#schemabasecolumn)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|any|false|none|none|

<h2 id="tocS_enteredQuantityColumn">enteredQuantityColumn</h2>
<!-- backwards compatibility -->
<a id="schemaenteredquantitycolumn"></a>
<a id="schema_enteredQuantityColumn"></a>
<a id="tocSenteredquantitycolumn"></a>
<a id="tocsenteredquantitycolumn"></a>

```json
{
  "sequence": 0,
  "type": "entered_quantity"
}

```

enteredQuantityColumn

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|enteredQuantityColumn|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[baseColumn](#schemabasecolumn)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|any|false|none|none|

<h2 id="tocS_enteredUnitColumn">enteredUnitColumn</h2>
<!-- backwards compatibility -->
<a id="schemaenteredunitcolumn"></a>
<a id="schema_enteredUnitColumn"></a>
<a id="tocSenteredunitcolumn"></a>
<a id="tocsenteredunitcolumn"></a>

```json
{
  "sequence": 0,
  "type": "entered_unit"
}

```

enteredUnitColumn

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|enteredUnitColumn|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[baseColumn](#schemabasecolumn)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|any|false|none|none|

<h2 id="tocS_quantityColumn">quantityColumn</h2>
<!-- backwards compatibility -->
<a id="schemaquantitycolumn"></a>
<a id="schema_quantityColumn"></a>
<a id="tocSquantitycolumn"></a>
<a id="tocsquantitycolumn"></a>

```json
{
  "sequence": 0,
  "type": "quantity"
}

```

quantityColumn

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|quantityColumn|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[baseColumn](#schemabasecolumn)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|any|false|none|none|

<h2 id="tocS_unitColumn">unitColumn</h2>
<!-- backwards compatibility -->
<a id="schemaunitcolumn"></a>
<a id="schema_unitColumn"></a>
<a id="tocSunitcolumn"></a>
<a id="tocsunitcolumn"></a>

```json
{
  "sequence": 0,
  "type": "unit"
}

```

unitColumn

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|unitColumn|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[baseColumn](#schemabasecolumn)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|any|false|none|none|

<h2 id="tocS_facetColumn">facetColumn</h2>
<!-- backwards compatibility -->
<a id="schemafacetcolumn"></a>
<a id="schema_facetColumn"></a>
<a id="tocSfacetcolumn"></a>
<a id="tocsfacetcolumn"></a>

```json
{
  "sequence": 0,
  "type": "facet",
  "code": "acidity",
  "factor": 0
}

```

facetColumn

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|facetColumn|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[baseColumn](#schemabasecolumn)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|any|false|none|none|
|» code|[facetCode](#schemafacetcode)|true|none|none|
|» factor|integer|false|none|none|

<h2 id="tocS_facetCode">facetCode</h2>
<!-- backwards compatibility -->
<a id="schemafacetcode"></a>
<a id="schema_facetCode"></a>
<a id="tocSfacetcode"></a>
<a id="tocsfacetcode"></a>

```json
"acidity"

```

facetCode

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|facetCode|any|false|none|none|

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
<!-- backwards compatibility -->
<a id="schemasourcecolumn"></a>
<a id="schema_sourceColumn"></a>
<a id="tocSsourcecolumn"></a>
<a id="tocssourcecolumn"></a>

```json
{
  "sequence": 0,
  "type": "source",
  "values": {
    "property1": {
      "source": "gtin",
      "location": "string"
    },
    "property2": {
      "source": "gtin",
      "location": "string"
    }
  }
}

```

sourceColumn

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sourceColumn|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[baseColumn](#schemabasecolumn)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|any|false|none|none|
|» values|object|true|none|none|
|»» **additionalProperties**|[sourceValue](#schemasourcevalue)|false|none|none|

<h2 id="tocS_sourceValue">sourceValue</h2>
<!-- backwards compatibility -->
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

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|source|[sourceType](#schemasourcetype)|true|none|none|
|location|string|false|none|none|

<h2 id="tocS_sourceType">sourceType</h2>
<!-- backwards compatibility -->
<a id="schemasourcetype"></a>
<a id="schema_sourceType"></a>
<a id="tocSsourcetype"></a>
<a id="tocssourcetype"></a>

```json
"gtin"

```

sourceType

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sourceType|any|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|sourceType|gtin|
|sourceType|plu|

<h2 id="tocS_codeColumn">codeColumn</h2>
<!-- backwards compatibility -->
<a id="schemacodecolumn"></a>
<a id="schema_codeColumn"></a>
<a id="tocScodecolumn"></a>
<a id="tocscodecolumn"></a>

```json
{
  "sequence": 0,
  "type": "code"
}

```

codeColumn

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|codeColumn|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[baseColumn](#schemabasecolumn)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|any|false|none|none|

<h2 id="tocS_imageColumn">imageColumn</h2>
<!-- backwards compatibility -->
<a id="schemaimagecolumn"></a>
<a id="schema_imageColumn"></a>
<a id="tocSimagecolumn"></a>
<a id="tocsimagecolumn"></a>

```json
{
  "sequence": 0,
  "type": "image"
}

```

imageColumn

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|imageColumn|any|false|none|none|

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[baseColumn](#schemabasecolumn)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|any|false|none|none|

<h2 id="tocS_customColumn">customColumn</h2>
<!-- backwards compatibility -->
<a id="schemacustomcolumn"></a>
<a id="schema_customColumn"></a>
<a id="tocScustomcolumn"></a>
<a id="tocscustomcolumn"></a>

```json
{
  "sequence": 0,
  "type": "custom",
  "code": "string"
}

```

customColumn

### Properties

allOf

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[baseColumn](#schemabasecolumn)|false|none|none|

and

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|object|false|none|none|
|» type|any|false|none|none|
|» code|string|true|none|none|

<h2 id="tocS_meal">meal</h2>
<!-- backwards compatibility -->
<a id="schemameal"></a>
<a id="schema_meal"></a>
<a id="tocSmeal"></a>
<a id="tocsmeal"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "time": "2019-08-24T14:15:22Z",
  "meal": "breakfast",
  "recipe": "string",
  "food": "string",
  "entered_quantity": 0,
  "entered_unit": "string",
  "quantity": 0,
  "unit": "g",
  "facets": [
    {
      "code": "acidity",
      "value": 0
    }
  ],
  "source": "gtin",
  "location": "string",
  "code": "string",
  "image": "string"
}

```

meal

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|time|string(date-time)|false|none|none|
|meal|[mealType](#schemamealtype)|false|none|none|
|recipe|string|false|none|none|
|food|string|false|none|none|
|entered_quantity|number|false|none|none|
|entered_unit|string|false|none|none|
|quantity|number|false|none|none|
|unit|any|false|none|none|
|facets|[object]|false|none|none|
|» code|[facetCode](#schemafacetcode)|true|none|none|
|» value|number|true|none|none|
|source|[sourceType](#schemasourcetype)|false|none|none|
|location|string|false|none|none|
|code|string|false|none|none|
|image|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|unit|g|
|unit|ml|

