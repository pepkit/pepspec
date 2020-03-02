# How to integrate imports and amendments

Imports and amendments can be combined to make really powerful analysis integration. One use case is to keep track of a bunch of pipelines and analyses.

First, make a PEP that specifies your list of pipelines, each as an amendment with a key you choose. Save this as `my_pipelines.yaml`
```
pep_version: 2.0.0
amendments:
  pipeline1:
    looper:
      pipeline_interface: http://piface.databio.org/peppro.yaml
  pipeline2:
    looper:
      pipeline_interface: http://piface.databio.org/pepatac.yaml
```

Now create a PEP that lists a bunch of separate sample collections under amendments. Save this file as `my_data.yaml`:

```
pep_version: 2.0.0
imports: my_pipelines.yaml
amendments:
  data1:
    sample_table: my_samples.csv
  data2:
  	sample_table: samples2.csv
```

Since this second file imports the first, all of the amendments will be available. Now you can mix and match data and analysis with:

```
cmd ... --pep=my_data.yaml --amend=pipeline1,data1
cmd ... --pep=my_data.yaml --amend=pipeline1,data2
cmd ... --pep=my_data.yaml --amend=pipeline2,data1
cmd ... --pep=my_data.yaml --amend=pipeline2,data2
```

You could import the same pipelines file in a different data description file to keep your pipelines consistent across analysis.
