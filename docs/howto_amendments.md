---
title: Store many projects in one file
---

# How to store many projects in one file

The `amendments` section of the config file allows you to include multiple variations of a project within one file. When a PEP is parsed, you may specify one or more included amendments, which will amend the values in the processed PEP. This is a powerful function that can be used for many purposes, such as *on the fly* tweaks or embedding multiple subprojects within a parent project.

## Example

```yaml
sample_table: annotation.csv
project_modifiers:
  amend:
    my_project2:
      sample_table: annotation2.csv
    my_project3:
      sample_table: annotation3.csv
...
```

If you load this configuration file, it will by default use the `annotation.csv` file specified in the `sample_table` attribute, as you would expect. If you don't activate any amendments, they are ignored. But if you choose, you may activate one of the two amendments, which are called `my_project2` and `my_project3`. If you activate `my_project2`, by passing `amendments=my_project2` when parsing the PEP, the resulting object will use the `annotation2.csv` sample_table instead of the default `annotation.csv`. All other project settings will be the same as if no amendment was activated because there are no other values specifed in the `my_project2` amendment.

Practically what happens under the scenes is that the primary project is first loaded, and then, if an amendment is activated, it overrides any attributes with those specified in the amendment.

## Rationale

At times you will want to create two projects that are very similar, but differ just in one or two attributes. For example, you may define a project with one set of samples, and then want an identical project but using a different sample annotation sheet. Or, you may define a project to run on a particular reference genome, and want to define a second project that is identical, but uses a different reference genome.

You could simply define 2 complete PEPs, but this would duplicate information and make it harder to maintain. Instead, you can use *amendments*, which allow you to encode additional similar projects all within the original `project_config.yaml` file. Amendments are like mini embedded `project_config.yaml` files that can be *activated* by software. 

## How do you activate an amendment?

Activating an amendment depends on what software you're using to load your PEP. A PEP-compliant implementation must define some way to activate amendments. For example, you can activate amendments in `peppy` or `pepr` by passing an argument, `amendments=my_project2`, when you construct the `Project` object.

## Can you activate multiple amendments?

Yes! Amendments are passed and parsed as a priority list; so the first amendment is processed, and then the next one, and so on. So, the final amendment in the list has the highest priority.
