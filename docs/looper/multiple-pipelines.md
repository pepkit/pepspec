# A project with multiple pipelines

In earlier versions of looper (v < 1.0), we used a `protocol_mappings` section to map samples with different `protocol` attributes to different pipelines. In the current pipeline interface (looper v > 1.0), we eliminated the `protocol_mappings`, because this can now be handled using sample modifiers, simplifying the pipeline interface. 
Now, each pipeline has exactly 1 pipeline interface.

The preferred method is to specify pipeline interfaces in the looper config file:

```yaml
pep_config: pephub::databio/looper:default
output_dir: "$HOME/hello_looper-master/output"
pipeline_interfaces:
  sample: "$HOME/hello_looper-master/pipeline/pipeline_interface"
  project: "$HOME/hello_looper-master/project/pipeline"
```

However, you can also link to the pipeline interface with a sample attribute. If you want the same pipeline to run on all samples, it's as easy as using an `append` modifier like this:

```
sample_modifiers:
  append:
    pipeline_interfaces: "test.yaml"
```

But if you want to submit different samples to different pipelines, depending on a sample attribute, like `protocol`, you can use an implied attribute:

```
sample_modifiers:
  imply:
    - if:
        protocol: [PRO-seq, pro-seq, GRO-seq, gro-seq] # OR
      then:
        pipeline_interfaces: ["peppro.yaml"]
```

This approach uses only functionality of PEPs to handle the connection to pipelines as sample attributes, which provides full control and power using the familiar sample modifiers. It completely eliminates the need for re-inventing this complexity within looper, which eliminated the protocol mapping section to simplify the looper pipeline interface files. You can read more about the rationale of this change in [issue 244](https://github.com/pepkit/looper/issues/244#issuecomment-611154594).
