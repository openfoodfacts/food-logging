# Food Logging Data Exchange Standard

## Objective

The reason for developing a standard for food logging data exchange is to ensure that people are not locked in to a single application once they start logging food data. For example, they might want to switch to a different application for logging, use another application to analyze their food logging history or supply data to a third party, such as researchers or medical practitioners.

The next section describes the proposed standard with following sections providing background context and documentation of the design process.

## Standard

### Glossary

| Entity | Description | Examples | Also known as |
|---|---|---|---|
| Consumer | The individual that this food log relates to. Note could possibly be an animal in the case of a pet food diary | Me, John Smith | User, Person
| Food | Something that can be ingested in the form that it was purchase by the Consumer | Apple, Lasagne, Soda | Product, fruit, vegetable |
| Source | Where data about a Food or Food Facet came from | Producer, Label, CIQUAL | Provenance |
| Facet | Any kind of information about food that can be aggregated to give insights into nutrition, health, the environment, etc. | 234 kJ per 100g, 68g CO2 per 100ml | Nutrients, Environmental Footprint |
| Facet Type | Description of the facet and its unit of measure per 100 g / ml of the food | kJ, Carbohydrates, CO2, Land usage | Attribute
| Recipe | A collection of Foods that are combined to form the component of a Meal | (for a cake) 100g flour, 50g sugar, 50g butter | Course, Plate, Dish, Ingredients |
| Preparation | The way that the Food is processed before eating | Baked, Fried, Re-heated | Processing |
| Meal | An occasion when Food was consumed | This morning's breakfast | Snack |
| Meal Type | Classification of the nature and timing of the meal | Breakfast, Lunch, Snack | 

### Export Packaging

Exports will be packaged in a zip file with an arbitrary name (determined by the user). Each zip file will contain the following:

* meals.csv
* meals_metadata.json

### Meals

This is a CSV file to make it as simple as possible for moderately technical Consumers or delegated third-parties to analyze their own data in a spreadsheet or database. All columns names should be human readable in the user's chosen language. A Metadata file will cross-reference the column names against pre-defined properties, like meal time, Meal Type, Food and nutrients.

Foods will include the human readable name, e.g. "Heinz Baked Beans" that was presented to the user when they selected the Food.

Date / times will be recorded in the user's local format and timezone, which would be identified in the metadata. Items consumed as part of the same meal should have exactly the same date / time to allow grouping of meals if needed.

Facets, like Nutrients, would have a single column name with a consistent unit of measure (identified in the metadata). The exporter could choose to include the unit in the column name if they feel this would be helpful. All Facets that were retrieved from the source of the Food information that were either presented to the user or used in calculations should be included in the export.

It is suggested that more system oriented fields, such as the Source, Global Trade Item Number (GTIN) and Image URLs are included at the "end" of the export line (this might be the leftmost columns in a right to left language).

An example might look like this (formatted as a table):

| Time | Meal | Recipe | Food | Amount | Measure | Quantity | Unit | Protein | Carbohydrate | Fat | Source | Code | Image |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1-May-2025 6:00am | Breakfast |  | Kelloggs Corn Flakes | 1 | serving | 30 | g | 0.3 | 24 | 1 | GTIN | 5059319030487 | https://images.openfoodfacts.org/images/products/505/931/903/0487/front_en.3.400.jpg |
| 1-May-2025 6:00am | Breakfast |  | Full Fat Milk | 0.5 | pint | 284 | ml | 3.1 | 10.2 | 4.3 | GTIN | 5060066960071 | https://images.openfoodfacts.org/images/products/506/006/696/0071/front_en.3.400.jpg |
| 1-May-2025 9:00am | Snack | White Coffee | Instant Coffee Powder | 1 | teaspoon | 4 | g | 0 | 0.1 | 0 | GTIN | 4056489440628 | https://images.openfoodfacts.net/images/products/405/648/944/0628/front_en.26.400.jpg |
| 1-May-2025 9:00am | Snack | White Coffee | Full Fat Milk | 20 | ml | 20 | ml | 1.3 | 1.2 | 1.2 | GTIN | 5060066960071 | https://images.openfoodfacts.org/images/products/506/006/696/0071/front_en.3.400.jpg |

### Metadata

The Metadata in an export provides a translation between the human readable column names and enumerations used in the Meals file and standardized representations of these. Applications with limited user-customization could potentially hard-code this Metadata file (per user language supported) if their exports always include the same standard column names.

The main component of the Metadata file is the "columns" property which is a single object with a key for each column name mentioned in the Meals CSV file. The value associated with each column is an object whose "type" column will determine the standardized property the column represents. Additional attributes, specific to the type, will identify other data relevant to that property, e.g. the standard nutrient code and unit for a "facet" column.

The full list of properties on the root Metadata object are as follows:

| Property | Description | Example |
|---|---|---|
| columns | Object with a key for each column name used in the Meals CSV file | <pre>"columns":{<br/>  "Food": {"type": "food"}<br/>}</pre> |
| locale | Combination of the user's [ISO 639 2-letter language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) and [ISO 3166 2-letter country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) separated with a hyphen | <pre>"locale": "en-US"</pre> |
| timezone | A standard [IANA TZ identifier](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) | <pre>"timezone": "Europe/London"</pre> |
| {additional properties} | Applications may add their own global properties. It is suggested that each application just adds one root property using a URI owned by that application as the key name. This URI would ideally point to a JSON Schema document describing the structure of the custom properties, but this is not essential. | <pre>"https://openfoodfacts.org/metadata.json": {<br/>  ...</br>}</pre> |

All dates / times in the Meals CSV file will be formatted according to the default format associated with their locale as would be generated by the [JavaScript Intl.DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat) object or equivalent.

However, numbers in both the Meals CSV and Metadata files should follow the [JSON number standard](https://www.rfc-editor.org/rfc/rfc8259#page-7) to avoid the need for unnecessary CSV escaping in regions that normally use a comma as the decimal separator.

The following table lists the different column types and additional attributes to be specified:

<table>
    <thead>
        <tr>
            <th>Type</th>
            <th>Additional Attributes</th>
            <th>Description</th>
            <th>Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>time</td>
            <td>[None]</td>
            <td>The time that the meal was consumed</td>
            <td><pre>"Time": {"type": "time"}</pre></td>
        </tr>
        <tr>
            <td>meal</td>
            <td>values</td>
            <td>The different meal type names used, keyed with the value used in the CSV file. The value will be one of the following (derived from <a href="https://en.wikipedia.org/wiki/Outline_of_meals">here</a>):<ul><li>breakfast</li><li>second-breakfast</li><li>brunch</li><li>elevenses</li><li>lunch</li><li>tea</li><li>dinner</li><li>supper</li><li>high-tea</li><li>siu-yeh</li><li>snack</li><li>daily</li></ul>Note the "daily" item refers to entries where the user has just recorded overall consumption throughout the day, e.g. 6 cups of coffee</td>
            <td><pre>"Meal": {<br/>  "type": "meal",<br/>  "values": {<br/>    "Breakfast": "breakfast",<br/>    "Mail Meal": "dinner",<br/>    "Daily Allowance": "daily"<br/>  }<br/>}</pre></td>
        </tr>
        <tr>
            <td>recipe</td>
            <td>[None]</td>
            <td>The name of a Recipe used that links multiple related foods in the meal</td>
            <td><pre>"Recipe": {"type": "recipe"}</pre></td>
        </tr>
        <tr>
            <td>food</td>
            <td>[None]</td>
            <td>The name of the Food as it was presented to the user when they selected it from the source</td>
            <td><pre>"Food": {"type": "food"}</pre></td>
        </tr>
        <tr>
            <td>entered_quantity</td>
            <td>[None]</td>
            <td>The amount of the food that the user recorded in the specified "entered_unit". Formatted as a <a href="https://www.rfc-editor.org/rfc/rfc8259#page-7">JSON number</a></td>
            <td><pre>"Amount": {"type": "entered_quantity"}</pre></td>
        </tr>
        <tr>
            <td>entered_unit</td>
            <td>[None]</td>
            <td>The unit used when recording the quantity of food. This is a free format string in the end-user's language</td>
            <td><pre>"Measure": {"type": "entered_unit"}</pre></td>
        </tr>
        <tr>
            <td>quantity</td>
            <td>[None]</td>
            <td>The amount of the food in normalized units (g for weight, ml for volume). Formatted as a <a href="https://www.rfc-editor.org/rfc/rfc8259#page-7">JSON number</a></td>
            <td><pre>"Quantity": {"type": "quantity"}</pre></td>
        </tr>
        <tr>
            <td>unit</td>
            <td>[None]</td>
            <td>The normalized unit type. "g" for weight or "ml" for volume. Not localized. This should match the unit used in the source, see the note on Units below.</td>
            <td><pre>"Unit": {"type": "unit"}</pre></td>
        </tr>
        <tr>
            <td rowspan="2">facet</td>
            <td>code</td>
            <td>The facet type as defined in this standard (TBA). e.g. "protein", "carbohydrates-total", "vitamin-b12", "energy-kj"</td>
            <td rowspan="2"><pre>"Protein": {<br/>  "type": "facet",<br/>  "code": "protein"<br/>},<br/>"Iron (g)": {<br/>  "type": "facet",<br/>  "code": "iron"<br/>},<br/>"Vitamin B12 (µg)": {<br/>  "type": "facet",<br/>  "code": "vitamin-b12",<br/>  "factor": 1000000<br/>}</pre></td>
        </tr>
        <tr>
            <td>factor</td>
            <td>Value that the quantity of the facet in the Meals CSV file must be divided by in order to convert it to the unit defined for the facet type. Note that most nutrients will have a units of "g" but energy will be in "kJ" or "kcal" e.g. 1000 if the values in the Meals CSV are expressed in mg. Defaults to 1 if omitted.</td>
        </tr>
        <tr>
            <td>source</td>
            <td>values</td>
            <td>The type of Food identifier used, keyed by the value used in the Meals CSV.
The value has a source, which can be "gtin" or "plu" and a location code, e.g. for GTIN this would be the <a href="https://navigator.gs1.org/gdsn/class-details?name=GLN&version=12">Global Location Number</a></td>
            <td><pre>"Source": {<br/>  "type": "source",<br/>  "values": {<br/>    "Bar code": {<br/>      "source": "gtin",<br/>      "location": "3014517900101"<br/>    },<br/>    "Food code": {<br/>      "source": "plu"<br/>    }<br/>  }<br/>}</pre></td>
        </tr>
        <tr>
            <td>code</td>
            <td>[None]</td>
            <td>The identifier for the Food in the specified source</td>
            <td><pre>"Code": {"type": "code"}</pre></td>
        </tr>
        <tr>
            <td>image</td>
            <td>[None]</td>
            <td>URL to an image that was presented to the user when they selected the food from the source</td>
            <td><pre>"Image": {"type": "image"}</pre></td>
        </tr>
        <tr>
            <td>{additional properties}</td>
            <td>[Any]</td>
            <td>Application properties that are specific to the individual meal. It is suggested that each application adds type for each custom column using a URI owned by that application as the key name. This URI would ideally point to a JSON Schema document describing the structure of the custom type, but this is not essential.</td>
            <td><pre>"Green Score": {<br/>&nbsp;&nbsp;"type":"https://openfoodfacts.org/green.json",<br/>&nbsp;&nbsp;...<br/>}</pre></td>
        </tr>
    </tbody>
</table>

A full example of a Meal Metadata file follows:

```json
{
  "columns": {
    "Heure": {
      "type": "time"
    },
    "Repas": {
      "type": "meal",
      "values": {
        "Petit-déjeuner": "breakfast",
        "Dîner": "dinner"
      }
    },
    "Recette": {
      "type": "recipe"
    },
    "Nourriture": {
      "type": "food"
    },
    "Nombre": {
      "type": "entered_quantity"
    },
    "Mesure": {
      "type": "entered_unit"
    },
    "Quantité": {
      "type": "quantity"
    },
    "Unité": {
      "type": "unit"
    },
    "Protéines": {
      "type": "facet",
      "code": "protein"
    },
    "Fer (g)": {
      "type": "facet",
      "code": "iron"
    },
    "Vitamine B12 (µg)": {
      "type": "facet",
      "code": "vitamin-b12",
      "factor": 1000000
    }
  },
  "locale": "fr-FR",
  "timezone": "Europe/Paris"
}
```

### API Packaging

Storing and retrieving data via an API would be performed by an application rather than a user, so there is no requirement to support localization of fields or units. However, it is still important to store the data that was presented to the user, such as the Food name, as it may not be possible to re-create this from the source.

#### Authentication

APIs should be secured using OAuth using Beater tokens supplied in the [HTTP Authorization Request Header](https://datatracker.ietf.org/doc/html/rfc6750#section-2.1). The method of authentication and obtaining and renewing access tokens is beyond the scope of this specification.

#### Metadata

The metadata format is already in a suitable form for use in a REST API. API backends should support PUT and GET methods for this (automatically qualified by the Consumer based on the authorization header).

#### Meals

Meals should be structured as an array of JSON objects with the following schema:

<table>
    <thead>
        <tr>
            <th>property</th>
            <th>Description</th>
            <th>Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>id</td>
            <td>A UUID string formatted according to <a href="https://datatracker.ietf.org/doc/html/rfc9562#name-uuid-format">RFC 9562</a>. Optional on new entries (will be generated by the receiving service)</td>
            <td><pre>"id": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6"</pre></td>
        </tr>
        <tr>
            <td>time</td>
            <td>The time that the meal was consumed in UTC following the <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8061</a> format</td>
            <td><pre>"time": "2025-07-30T15:56:32Z"</pre></td>
        </tr>
        <tr>
            <td>meal</td>
            <td>The meal type. The value will be one of the following (derived from <a href="https://en.wikipedia.org/wiki/Outline_of_meals">here</a>):<ul><li>breakfast</li><li>second-breakfast</li><li>brunch</li><li>elevenses</li><li>lunch</li><li>tea</li><li>dinner</li><li>supper</li><li>high-tea</li><li>siu-yeh</li><li>snack</li><li>daily</li></ul>Note the "daily" item refers to entries where the user has just recorded overall consumption throughout the day, e.g. 6 cups of coffee</td>
            <td><pre>"meal": "breakfast"</pre></td>
        </tr>
        <tr>
            <td>recipe [optional]</td>
            <td>The name of a Recipe used that links multiple related foods in the meal</td>
            <td><pre>"recipe": "White coffee"</pre></td>
        </tr>
        <tr>
            <td>food</td>
            <td>The name of the Food as it was presented to the user when they selected it from the source</td>
            <td><pre>"food": "Instant Coffee Powder"</pre></td>
        </tr>
        <tr>
            <td>entered_quantity</td>
            <td>The amount of the food that the user recorded in the specified "entered_unit". Formatted according to the <a href="https://www.rfc-editor.org/rfc/rfc8259#page-7">JSON number standard</a></td>
            <td><pre>"entered_quantity": 1</pre></td>
        </tr>
        <tr>
            <td>entered_unit</td>
            <td>The unit used when recording the quantity of food. This is a free format string in the end-user's language</td>
            <td><pre>"entered_unit": "tsp"</pre></td>
        </tr>
        <tr>
            <td>quantity</td>
            <td>The amount of the food in normalized units (g for weight, ml for volume). Formatted according to the <a href="https://www.rfc-editor.org/rfc/rfc8259#page-7">JSON number standard</a></td>
            <td><pre>"quantity": 15</pre></td>
        </tr>
        <tr>
            <td>unit</td>
            <td>The normalized unit type. "g" for weight or "ml" for volume. This should match the unit used in the source, see the note on Units below.</td>
            <td><pre>"unit": "ml"</pre></td>
        </tr>
        <tr>
            <td>{facet}</td>
            <td>The property name will be a facet type as defined in this standard (TBA). e.g. "protein", "carbohydrates-total", "vitamin-b12", "energy-kj". The value will in "g" in most cases but energy will be in "kJ" or "kcal"</td>
            <td><pre>"protein": 0,<br/>"iron": 0.02,<br/>"vitamin-b12": 1.2e-6</pre></td>
        </tr>
        <tr>
            <td>source</td>
            <td>The type of Food identifier used, which can be "gtin" or "plu"</td>
            <td><pre>"source": "gtin"</pre></td>
        </tr>
        <tr>
            <td>location [optional]</td>
            <td>The location code for the source, e.g. for GTIN this would be the <a href="https://navigator.gs1.org/gdsn/class-details?name=GLN&version=12">Global Location Number</a></td>
            <td><pre>"location": "3014517900101"</pre></td>
        </tr>
        <tr>
            <td>code</td>
            <td>The identifier for the Food in the specified source</td>
            <td><pre>"code": "4056489440628"</pre></td>
        </tr>
        <tr>
            <td>image</td>
            <td>URL to an image that was presented to the user when they selected the food from the source</td>
            <td><pre>"image": "https://images.openfoodfacts.net/images/products/405/648/944/0628/front_en.26.400.jpg"</pre></td>
        </tr>
        <tr>
            <td>{additional properties}</td>
            <td>Application properties that are specific to the individual meal. This should match the type specified in the metadata</td>
            <td><pre>"https://openfoodfacts.org/green.json": 34</pre></td>
        </tr>
    </tbody>
</table>

The following shows the data from the above CSV example in JSON format, with the addition of a custom property:

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
        "protein": 0.3,
        "carbohydrate": 24,
        "fat": 1,
        "source": "gtin",
        "location": "3014517900101",
        "code": "5059319030487",
        "image": "https://images.openfoodfacts.org/images/products/505/931/903/0487/front_en.3.400.jpg",
        "https://openfoodfacts.org/green.json": 53
    },
    {
        "time": "2025-05-01T05:00:00Z",
        "meal": "breakfast",
        "food": "Full Fat Milk",
        "entered_quantity": 0.5,
        "entered_unit": "pint",
        "quantity": 284,
        "unit": "ml",
        "protein": 3.1,
        "carbohydrate": 10.2,
        "fat": 4.3,
        "source": "gtin",
        "location": "3014517900101",
        "code": "5060066960071",
        "image": "https://images.openfoodfacts.org/images/products/506/006/696/0071/front_en.3.400.jpg",
        "https://openfoodfacts.org/green.json": 31
    },
    {
        "time": "2025-05-01T08:00:00Z",
        "meal": "snack",
        "recipe": "White Coffee",
        "food": "Instant Coffee Powder",
        "entered_quantity": 1,
        "entered_unit": "teaspoon",
        "quantity": 4,
        "unit": "g",
        "protein": 0,
        "carbohydrate": 0.1,
        "fat": 0,
        "source": "gtin",
        "location": "3014517900101",
        "code": "4056489440628",
        "image": "https://images.openfoodfacts.net/images/products/405/648/944/0628/front_en.26.400.jpg",
        "https://openfoodfacts.org/green.json": 45
    },
    {
        "time": "2025-05-01T08:00:00Z",
        "meal": "snack",
        "recipe": "White Coffee",
        "food": "Full Fat Milk",
        "entered_quantity": 20,
        "entered_unit": "ml",
        "quantity": 20,
        "unit": "ml",
        "protein": 1.3,
        "carbohydrate": 1.2,
        "fat": 1.2,
        "source": "gtin",
        "location": "3014517900101",
        "code": "5060066960071",
        "image": "https://images.openfoodfacts.org/images/products/506/006/696/0071/front_en.3.400.jpg",
        "https://openfoodfacts.org/green.json": 31
    }
]
```

A meals API should support the following methods (only accessing data for the authenticated Consumer):

* POST: Creates meals from the supplied array in the HTTP request body using the application/json content type
* GET: Returns an array of meals in the response body that were logged between mandatory "from_time" and "to_time" query parameters, each specified in [ISO 8061](https://en.wikipedia.org/wiki/ISO_8601) format
* DELETE: Deletes a meal item. The meal "id" is supplied in the path
