# How to write a pipestat schema

## Introduction
Pipestat requires a schema, in which all the results that the pipeline can report are specified. 

It is written in [JSON schema](https://cswr.github.io/JsonSchema/spec/basic_types/) which defines specific data types:

### Data types

Each *result* reported by a pipeline must have a specified data type. The supported basic types include:

- string
- number
- integer
- boolean
- null

Pipestat also extends the json schema vocabulary by adding two _additional_ types, which are common results of a pipeline: `image` and `file`. These types require reporting objects with the following attributes:

- `file`:
    - `path`: path to the reported file
    - `title`: human readable description of the file
- `image`:
    - `path`: path to the reported image, usually PDF
    - `thumbnail_path` (optional): path to the reported thumbnail, usually PNG or JPEG. If not provided, falls back to `path`.
    - `title`: human readable description of the image


### Complex objects
Pipestat also supports reporting more [complex objects](./code/reporting-objects.md)

### Unsupported data types

`tuples` are currently unsupported for reporting and retrieving.

## A simple example

The pipestat output schema is a YAML-formatted file. The top level keys are the unique result identifiers. The associated values are jsonschema types. The `type` attribute is required. This is an example of a minimal component, specifying only an identifier, and its type:

```yaml
result_identifier:
  type: <type>
```

Here, `result_identifier` can be whatever name you want to use to identify this result. Here's a simple schema example that showcases most of the supported types:

```yaml
title: Example Pipestat Output Schema
description: A pipeline that uses pipestat to report sample level results.
type: object
properties:
  pipeline_name: "default_pipeline_name"
  samples:
    type: array
    properties: # result identifiers are properties of the samples object
      number_of_things:
        type: integer
        description: "Number of things"
      percentage_of_things:
        type: number
        description: "Percentage of things"
      name_of_something:
        type: string
        description: "Name of something"
      switch_value:
        type: boolean
        description: "Is the switch on or off"
```

The top level schema is of `type` `object`. It contains properties that define `samples`. Here, the `samples`'s properties are the results. So in the above example, the results that can be reported are: `number_of_things`,`percentage_of_things`,`name_of_something`, and `switch_value`.

## A more complex example
Here's a more complex schema example that showcases some of the more advanced jsonschema features:

```yaml
title: An example Pipestat output schema
description: A pipeline that uses pipestat to report sample and project level results.
type: object
properties:
  pipeline_name: "default_pipeline_name"
  samples:
    type: array
    items:
      type: object
      properties:
        number_of_things:
          type: integer
          description: "Number of things"
        percentage_of_things:
          type: number
          description: "Percentage of things"
        name_of_something:
          type: string
          description: "Name of something"
        switch_value:
          type: boolean
          description: "Is the switch on or off"
        md5sum:
          type: string
          description: "MD5SUM of an object"
          highlight: true
        collection_of_images:
          description: "This store collection of values or objects"
          type: array
          items:
            properties:
                prop1:
                  description: "This is an example file"
                  $ref: "#/$defs/file"
        output_file_in_object:
          type: object
          properties:
            prop1:
              description: "This is an example file"
              $ref: "#/$defs/file"
            prop2:
              description: "This is an example image"
              $ref: "#/$defs/image"
          description: "Object output"
        output_file_in_object_nested:
          type: object
          description: First Level
          properties:
            prop1:
              type: object
              description: Second Level
              properties:
                prop2:
                  type: integer
                  description: Third Level
        output_file:
          $ref: "#/$defs/file"
          description: "This a path to the output file"
        output_image:
          $ref: "#/$defs/image"
          description: "This a path to the output image"
$defs:
  image:
    type: object
    object_type: image
    properties:
      path:
        type: string
      thumbnail_path:
        type: string
      title:
        type: string
    required:
      - path
      - title
  file:
    type: object
    object_type: file
    properties:
      path:
        type: string
      title:
        type: string
    required:
      - path
      - title

```

In this example, we define reusable type definitions in `image` and `file`.

For more details, see [pipestat specification](pipestat-specification.md).