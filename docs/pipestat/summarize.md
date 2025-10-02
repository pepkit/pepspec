# Sharing reported results

Pipestat currently has the ability to create HTML reports of reported pipeline results.


```python

from pipestat import PipestatManager

psm = PipestatManager(schema_path="sample_output_schema.yaml", results_file_path="my_results.yaml")

psm.summarize(output_dir="/home/output_dir")

# You can also create a portable version to share via email etc
psm.summarize(output_dir="/home/output_dir",portable= True )

```


Similarly this can be accomplished via the CLI:

```shell

pipestat summarize --results-file my_results.yaml --schema output_schema.yaml --portable

```