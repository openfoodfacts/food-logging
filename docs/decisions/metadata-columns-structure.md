# Metadata Columns Structure

## Context and Problem Statement

The purpose of the `columns` property of the Food Metadata file is to map the column names used in the Food CSV file to standard Meal properties so that the CSV file can be unambiguously interpreted by computer systems.

There are a number of ways to structure this which have various pros and cons regarding implementation.

## Decision Drivers

* Structure should intuitive
* As much validation as possible should be incorporated into the JSON schema
* Schema should translate well to common implementation data models, e.g. FastAPI Pydantic models

## Considered Options

There are two dimensions to this decision. The first concerns how the columns object is structured:

* Dictionary whose key is the CSV column name
* Dictionary whose key is the standardized meal property name
* Array of objects whose type varies depending on the standardized meal property type

The second aspect of the decision is how to model custom types and facets, where there are potentially a large number of types. The considered options here are:

* A type field that uniquely identifies the property
* a simple type field, e.g. "custom", with an additional field to discriminate

## Decision Outcome

Chosen option: "Dictionary whose key is the CSV column name" with "a simple type field", because imports are generally more complex than exports, so having a slightly easier mapping on import will be helpful and simple type fields are easier to enforce in JSON Schema.

### Consequences

Separate validation outside of JSON Schema will be needed to ensure that mandatory properties are mapped to a CSV column.

### Confirmation

Schemas should be accompanied by a comprehensive test suite.

## Pros and Cons of the Options for Overall Column Structure

### Dictionary whose key is the CSV column name

With this approach the columns might look like this when using a unique type property:

```json
"columns": {
    "Time of Meal": {
        "type": "time",
        "sequence": 1
    },
    "Protein": {
        "type": "proteins",
        "sequence": 3
    },
    "Gross Carbohydrates": {
        "type": "carbohydrate-total",
        "sequence": 2
    },
    "Green Score": {
        "type": "https://openfoodfacts.org/greenscore.json",
        "sequence": 4
    }
}
```

or this when using a simple type field:

```json
"columns": {
    "Time of Meal": {
        "type": "time",
        "sequence": 1
    },
    "Protein": {
        "type": "facet",
        "code": "proteins",
        "sequence": 3
    },
    "Gross Carbohydrates": {
        "type": "facet",
        "code": "carbohydrate-total",
        "sequence": 2,
    },
    "Green Score": {
        "type": "custom",
        "code": "https://openfoodfacts.org/greenscore.json",
        "sequence": 4
    }
}
```

* Good: Uniqueness of CSV column names is enforced
* Good: Supports both ways of handling property type
* Good: Easiest structure to use when interpreting an existing CSV file using metadata
* Neutral: An additional field is needed to define the column order
* Bad: Uniqueness of standardized property types is not enforced

### Dictionary whose key is the standardized meal property name

With this approach the columns might look like this when using a unique type property:

```json
"columns": {
    "time": {
        "name": "Time of Meal",
        "sequence": 1
    },
    "proteins": {
        "name": "Protein",
        "sequence": 3
    },
    "carbohydrate-total": {
        "name": "Gross Carbohydrates",
        "sequence": 2
    },
    "https://openfoodfacts.org/greenscore.json": {
        "name": "Green Score",
        "sequence": 4
    }
}
```

A nested approach would be needed to support simple property types, e.g.:

```json
"columns": {
    "time": {
        "name": "Time of Meal",
        "sequence": 1
    },
    "facets": {
        "proteins": {
            "name": "Protein",
            "sequence": 3
        },
        "carbohydrate-total": {
            "name": "Gross Carbohydrates",
            "sequence": 2
        }
    },
    "custom": {
        "https://openfoodfacts.org/greenscore.json": {
            "name": "Green Score",
            "sequence": 4
        }
    }
}
```

* Good: Easier to enforce presence of mandatory properties
* Good: Uniqueness of property types is enforced
* Neutral: An additional field is needed to define the column order
* Bad: Uniqueness of CSV column names is not enforced
* Bad: Root schema would be very verbose when using unique property types

### Array of objects whose type varies depending on the standardized meal property type

With this approach the columns might look like this when using a unique type property:

```json
"columns": [
    {
        "name": "Time of Meal",
        "type": "time"
    },
    {
        "name": "Gross Carbohydrates",
        "type": "carbohydrate-total"
    },
    {
        "name": "Protein",
        "type": "proteins"
    },
    {
        "name": "Green Score",
        "type": "https://openfoodfacts.org/greenscore.json"
    }
]
```

or this when using simplified property types:

```json
"columns": [
    {
        "name": "Time of Meal",
        "type": "time"
    },
    {
        "name": "Gross Carbohydrates",
        "type": "facet",
        "code": "carbohydrate-total"
    },
    {
        "name": "Protein",
        "type": "facet",
        "code": "proteins"
    },
    {
        "name": "Green Score",
        "type": "custom",
        "code": "https://openfoodfacts.org/greenscore.json"
    }
]
```

* Good: An additional field is not needed to define the column order
* Good: Easiest structure to use when generating a CSV from metadata
* Neutral: Uniqueness of standardized property types is not enforced even if unique property types are used
* Bad: Uniqueness of CSV column names is not enforced

## Pros and Cons of the Options for Handling Property Types

### Unique Types

* Good: Less fields
* Bad: Difficult to validate with JSON Schema
* Bad: Root of JSON Schema will be very verbose

### Simple Types with additional Discriminator

* Good: Moves complexity of facets out of the root of the JSON Schema
* Good: Easier to discriminate between the different classes of property in the JSON Schema
* Bad: More fields
