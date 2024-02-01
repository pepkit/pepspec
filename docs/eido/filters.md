**Filters are an experimental feature and may change in future versions of `eido`.**

# Using eido filters

Eido provides a CLI to convert a PEP into different output formats. These include some built-in formats, like _csv_ (which produces a processed csv file, with project/sample already modified), _yaml_, and a few others. It also provides a plugin system so that you can write your own Python functions to provide custom output formats. You access filters through the `eido convert` command.

## View available filters

To list available filters:

```console
eido convert --list
```

You'll see some output like this. There are a few built-in filters available:


```console
Available filters:
 - basic
 - csv
 - yaml
 - yaml-samples
```

You can add to this list by [writing a custom filter](writing-a-filter.md), which will write your PEP into whatever format you need.

## Convert a PEP into an alternative format with a filter

To convert a PEP into an output format, do this:

```console
eido convert config.yaml -f basic
running plugin pep
Project 'pepconvert' (/home/nsheff/code/pepconvert/config.yaml)
5 samples: WT_REP1, WT_REP2, RAP1_UNINDUCED_REP1, RAP1_UNINDUCED_REP2, RAP1_IAA_30M_REP1
Sections: pep_version, sample_table, subsample_table
...
```

This *basic* format just lists the config file, the number of samples and their names, and identifies the sections in the project config file. Another format is `-f yaml`,

```console
eido convert config.yaml -f yaml
```

This will output your samples in yaml format.

### Parametrizing filters

Filter functions are parameterizable. Some filters may request or require parameters. To learn more about a filter's parameters, use `-d` or `--describe`: `eido convert -f <filter_name> -d`, which displays the plugin documentation. For example:

```console
eido convert -f yaml-samples -d

    YAML samples PEP filter, that returns only Sample object representations.

    This filter can save the YAML to file, if kwargs include `path`.

    :param peppy.Project p: a Project to run filter on
```

In this case, the argument `path` can be provided as an output file. Like this: 

```console
eido convert config.yaml -f yaml-samples -a path=output.yaml
```

More generally, the form to provide parameters is like this

```console
eido convert config.yaml -f <filter_name> -a argument1=value1 argument2=value2
```


