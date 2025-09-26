# Terminology

Key concepts when using pipestat:

### Samples/Records:

- *record identifier*. An identifier for a particular pipeline run, such as a sample name. If you are using pipestat in tandem with looper, record_identifier = sample_name.

### Results:

- *result identifier*. The name of a result, such as `aligned_read_count` or `duplication_rate`.
- *result*: An element produced by a pipeline. Results have defined data types, described herein.
- *value*. The actual data for an output result for a given record.


### Misc:

- *namespace*: A way to group results that belong together. In the api, this is referenced via `pipeline_name`. This is typically an identifier for a particular pipeline, like `rnaseq-pipeline`. All results from this pipeline will share this namespace.
- *pipestat specification*: the way to structure a set of results stored from one or more pipeline runs.
- *backend*. The technology underlying the result storage, which can be either a simple file or a database.
