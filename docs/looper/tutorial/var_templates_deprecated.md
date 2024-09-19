This is old, outdated docs. Really you should only use var_templates to pass template-rendered variables to presubmission functions.


var templates

The value of the var_templates section is that it's the only way to pass a derived parameter to a python presubmission function.



### Variable templates via `var_templates`

Let us circle back to the `var_templates` key. You can use `var_templates` to render re-usable variables for use in the command template.

```yaml title="pipeline_interface.yaml" hl_lines="3 4"
pipeline_name: count_lines
output_schema: output_schema.yaml
var_templates:
  pipeline: '{looper.piface_dir}/count_lines.sh'
sample_interface:
  command_template: {pipeline.var_templates.pipeline} {sample.file} --output-parent {looper.sample_output_folder}
```

You can add anything to the var_templates that you need to later access in the command templates:
```yaml title="pipeline_interface.yaml"
pipeline_name: count_lines
var_templates:  
  pipeline: '{looper.piface_dir}/count_lines.sh' 
  refgenie_config: "$REFGENIE"
sample_interface:
  command_template: >
    {pipeline.var_templates.pipeline} --config {pipeline.var_templates.refgenie_config} {sample.file_path} --output-parent {looper.sample_output_folder}
```




There are two primary uses for `var_templates`:

### Syntactic sugar for repeated use of variables

The `var_templates` allows you to define templates that will be populated, which can then be used as variables in other templates in the pipeline interface, such as the `command_template`.

For example, we can define 

``` yaml title="var_templates"
var_templates:  
  pipeline_path: "{looper.piface_dir}/pipelines/pipeline1.py"  
```

Then, we can use this in our command template, under `{pipeline.var_templates.pipeline_path}`.

``` yaml title="command_template"
command_template: >  
  {pipeline.var_templates.pipeline_path} {sample.file_path}
```

How is this useful? Well, we might want to re-use this variable in a pre-submission script.
Say our pipeline also has a function that runs some preparation. We could do this:

``` yaml title="command_template"
var_templates:  
  pipeline_path: "{looper.piface_dir}/pipelines/pipeline1.py"  
command_template: >  
  {pipeline.var_templates.pipeline_path} {sample.file_path}
pre_submit:
  command_templates:
    - "{pipeline.var_templates.pipeline_path} --pre {sample.sample_name}"
```

This just makes the pipeline interface a little cleaner, since we only specify the relative path to the pipeline once.

## Parameterizing plugins with variable templates

Pre-submission hooks can run either CLI commands or they can run Python functions.
When they run python functions, they 

Sometimes plugins require a parameter, that benefits from having access to the looper variable namespaces.

For example, the `write_sample_yaml` plugin will write a sample yaml file for each sample. 
Where should this file be saved? We can just spit it out somewhere, but it would be nice to have a parameter.
So, we have a parameter.
Now, we could just pass that parameter in any of the templates

like `{pipeline.my_param}`. 

Great. But wait, what if we want to use another looper variable in there? The problem is, this isn't a template, so we can't

That's what `var_templates` are. they are populated first through the template system, so they are rendered, then, they are provided.




Example using var_templates:
```yaml
pipeline_name: example_pipeline  
output_schema: output_schema.yaml  
var_templates:  
  pipeline_path: "{looper.piface_dir}/pipelines/pipeline1.py"  
command_template: >  
  {pipeline.var_templates.pipeline_path} --sample-name {sample.sample_name} --req-attr {sample.attr} 
```
