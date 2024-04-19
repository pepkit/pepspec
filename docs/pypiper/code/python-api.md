<script>
document.addEventListener('DOMContentLoaded', (event) => {
  document.querySelectorAll('h3 code').forEach((block) => {
    hljs.highlightBlock(block);
  });
});
</script>

<style>
h3 .content { 
    padding-left: 22px;
    text-indent: -15px;
 }
h3 .hljs .content {
    padding-left: 20px;
    margin-left: 0px;
    text-indent: -15px;
    martin-bottom: 0px;
}
h4 .content, table .content, p .content, li .content { margin-left: 30px; }
h4 .content { 
    font-style: italic;
    font-size: 1em;
    margin-bottom: 0px;
}

</style>


# Package `pypiper` Documentation

## <a name="PipelineManager"></a> Class `PipelineManager`
Base class for instantiating a PipelineManager object, the main class of Pypiper.

#### Parameters:

- `name` (`str`):  Choose a name for your pipeline;it's used to name the output files, flags, etc.
- `outfolder` (`str`):  Folder in which to store the results.
- `args` (`argparse.Namespace`):  Optional args object from ArgumentParser;Pypiper will simply record these arguments from your script
- `multi` (`bool`):  Enables running multiple pipelines in one scriptor for interactive use. It simply disables the tee of the output, so you won't get output logged to a file.
- `dirty` (`bool`):  Overrides the pipeline's clean_add()manual parameters, to *never* clean up intermediate files automatically. Useful for debugging; all cleanup files are added to manual cleanup script.
- `recover` (`bool`):  Specify recover mode, to overwrite lock files.If pypiper encounters a locked target, it will ignore the lock and recompute this step. Useful to restart a failed pipeline.
- `new_start` (`bool`):  start over and run every command even if output exists
- `force_follow` (`bool`):  Force run all follow functionseven if  the preceding command is not run. By default, following functions  are only run if the preceding command is run.
- `cores` (`int`):  number of processors to use, default 1
- `mem` (`str`):  amount of memory to use. Default units are megabytes unlessspecified using the suffix [K|M|G|T]."
- `config_file` (`str`):  path to pipeline configuration file, optional
- `output_parent` (`str`):  path to folder in which output folder will live
- `overwrite_checkpoints` (`bool`):  Whether to override the stage-skippinglogic provided by the checkpointing system. This is useful if the calls to this manager's run() method will be coming from a class that implements pypiper.Pipeline, as such a class will handle checkpointing logic automatically, and will set this to True to protect from a case in which a restart begins upstream of a stage for which a checkpoint file already exists, but that depends on the upstream stage and thus should be rerun if it's "parent" is rerun.
- `pipestat_record_identifier` (`str`):  record_identifier to report results via pipestat
- `pipestat_schema` (`str`):  output schema used by pipestat to report results
- `pipestat_results_file` (`str`):  path to file backend for reporting results
- `pipestat_config_file` (`str`):  path to pipestat configuration file
- `pipestat_pipeline_type` (`str`):  Sample or Project level pipeline
- `pipestat_result_formatter` (``):  function used to style reported results, defaults to result_formatter_markdown


#### Raises:

- `TypeError`:  if start or stop point(s) are provided both directly andvia args namespace, or if both stopping types (exclusive/prospective and inclusive/retrospective) are provided.


```python
def __init__(self, name, outfolder, version=None, args=None, multi=False, dirty=False, recover=False, new_start=False, force_follow=False, cores=1, mem='1000M', config_file=None, output_parent=None, overwrite_checkpoints=False, logger_kwargs=None, pipestat_record_identifier=None, pipestat_schema=None, pipestat_results_file=None, pipestat_config=None, pipestat_pipeline_type=None, pipestat_result_formatter=None, **kwargs)
```

Initialize self.  See help(type(self)) for accurate signature.



```python
def callprint(self, cmd, shell=None, lock_file=None, nofail=False, container=None)
```

Prints the command, and then executes it, then prints the memory use and return code of the command.

Uses python's subprocess.Popen() to execute the given command. The shell argument is simply
passed along to Popen(). You should use shell=False (default) where possible, because this enables memory
profiling. You should use shell=True if you require shell functions like redirects (>) or stars (*), but this
will prevent the script from monitoring memory use. The pipes (|) will be used to split the command into
subprocesses run within python, so the memory profiling is possible.
cmd can also be a series (a dict object) of multiple commands, which will be run in succession.
#### Parameters:

- `cmd` (`str | Iterable[str]`):  Bash command(s) to be run.
- `lock_file` (`str`):  a lock file name
- `nofail` (`bool`):  FalseNofail can be used to implement non-essential parts of the pipeline; if these processes fail, they will not cause the pipeline to bail out.
- `shell` (`bool`):  None (will tryto determine based on the command)
- `container` (``):  Named Docker container in which to execute.
- `container` (``):  str




```python
def checkprint(self, cmd, shell=None, nofail=False)
```

Just like callprint, but checks output -- so you can get a variable in python corresponding to the return value of the command you call. This is equivalent to running subprocess.check_output() instead of subprocess.call().
#### Parameters:

- `cmd` (`str | Iterable[str]`):  Bash command(s) to be run.
- `shell` (`bool | str`):  If command requires should be run in its own shell. Optional.Default: "guess" -- `run()` will try to guess if the command should be run in a shell (based on the presence of a pipe (|) or redirect (>), To force a process to run as a direct subprocess, set `shell` to False; to force a shell, set True.
- `nofail` (`bool`):  FalseNofail can be used to implement non-essential parts of the pipeline; if these processes fail, they will not cause the pipeline to bail out.


#### Returns:

- `str`:  text output by the executed subprocess (check_output)




```python
def clean_add(self, regex, conditional=False, manual=False)
```

Add files (or regexs) to a cleanup list, to delete when this pipeline completes successfully. When making a call with run that produces intermediate files that should be deleted after the pipeline completes, you flag these files for deletion with this command. Files added with clean_add will only be deleted upon success of the pipeline.
#### Parameters:

- `regex` (`str`):   A unix-style regular expression that matches files to delete(can also be a file name).
- `conditional` (`bool`):  True means the files will only be deleted if no otherpipelines are currently running; otherwise they are added to a manual cleanup script called {pipeline_name}_cleanup.sh
- `manual` (`bool`):  True means the files will just be added to a manual cleanup script.




```python
def complete(self)
```

Stop a completely finished pipeline.



```python
def critical(self, msg, *args, **kwargs)
```



```python
def debug(self, msg, *args, **kwargs)
```



```python
def error(self, msg, *args, **kwargs)
```



```python
def fail_pipeline(self, exc: Exception, dynamic_recover: bool=False)
```

If the pipeline does not complete, this function will stop the pipeline gracefully. It sets the status flag to failed and skips the normal success completion procedure.
#### Parameters:

- `exc` (`Exception`):  Exception to raise.
- `dynamic_recover` (`bool`):  Whether to recover e.g. for job termination.




```python
def fatal(self, msg, *args, **kwargs)
```



```python
def get_container(self, image, mounts)
```



```python
def get_elapsed_time(self)
```

Parse the pipeline profile file, collect the unique and last duplicated runtimes and sum them up. In case the profile is not found, an estimate is calculated (which is correct only in case the pipeline was not rerun)
#### Returns:

- `int`:  sum of runtimes in seconds




```python
def get_stat(self, key)
```

Returns a stat that was previously reported. This is necessary for reporting new stats that are derived from two stats, one of which may have been reported by an earlier run. For example, if you first use report_result to report (number of trimmed reads), and then in a later stage want to report alignment rate, then this second stat (alignment rate) will require knowing the first stat (number of trimmed reads); however, that may not have been calculated in the current pipeline run, so we must retrieve it from the stats.yaml output file. This command will retrieve such previously reported stats if they were not already calculated in the current pipeline run.
#### Parameters:

- `key` (``):  key of stat to retrieve




```python
def halt(self, checkpoint=None, finished=False, raise_error=True)
```

Stop the pipeline before completion point.
#### Parameters:

- `checkpoint` (`str`):  Name of stage just reached or just completed.
- `finished` (`bool`):  Whether the indicated stage was just finished(True), or just reached (False)
- `raise_error` (`bool`):  Whether to raise an exception to trulyhalt execution.




```python
def halted(self)
```

Is the managed pipeline in a paused/halted state?
#### Returns:

- `bool`:  Whether the managed pipeline is in a paused/halted state.




```python
def info(self, msg, *args, **kwargs)
```



```python
def make_sure_path_exists(path)
```

Creates all directories in a path if it does not exist.
#### Parameters:

- `path` (`str`):  Path to create.


#### Raises:

- `Exception`:  if the path creation attempt hits an error with code indicating a cause other than pre-existence.




```python
def pipestat(self)
```

`pipestat.PipestatManager` object to use for pipeline results reporting and status management

Depending on the object configuration it can report to
a YAML-formatted file or PostgreSQL database. Please refer to pipestat
documentation for more details: http://pipestat.databio.org/
#### Returns:

- `pipestat.PipestatManager`:  object to use for results reporting




```python
def process_counter(self)
```

Increments process counter with regard to the follow state: if currently executed command is a follow function of another one, the counter is not incremented.
#### Returns:

- `str | int`:  current counter state, a number if the counter has been incremented or a number of the previous process plus "f" otherwise




```python
def remove_container(self, container)
```



```python
def report_object(self, key, filename, anchor_text=None, anchor_image=None, annotation=None, nolog=False, result_formatter=None, force_overwrite=True)
```

Writes a key:value pair to self.pipeline_stats_file. Note: this function will be deprecated. Using report_result is recommended.
#### Parameters:

- `key` (`str`):  name (key) of the object
- `filename` (`str`):  relative path to the file (relative to parentoutput dir)
- `anchor_text` (`str`):  text used as the link anchor test or caption torefer to the object. If not provided, defaults to the key.
- `anchor_image` (`str`):  a path to an HTML-displayable image thumbnail(so, .png or .jpg, for example). If a path, the path should be relative to the parent output dir.
- `annotation` (`str`):  By default, the figures will be annotated withthe pipeline name, so you can tell which pipeline records which figures. If you want, you can change this.
- `nolog` (`bool`):  Turn on this flag to NOT print this result in thelogfile. Use sparingly in case you will be printing the result in a different format.
- `result_formatter` (`str`):  function for formatting via pipestat backend
- `force_overwrite` (`bool`):  overwrite results if they already exist?


#### Returns:

- `str reported_result`:  the reported result is returned as a list of formatted strings.




```python
def report_result(self, key, value, nolog=False, result_formatter=None, force_overwrite=True)
```

Writes a key:value pair to self.pipeline_stats_file.
#### Parameters:

- `key` (`str`):  name (key) of the stat
- `value` (`dict`):  value of the stat to report.
- `nolog` (`bool`):  Turn on this flag to NOT print this result in thelogfile. Use sparingly in case you will be printing the result in a different format.
- `result_formatter` (`str`):  function for formatting via pipestat backend
- `force_overwrite` (`bool`):  overwrite results if they already exist?


#### Returns:

- `str reported_result`:  the reported result is returned as a list of formatted strings.




```python
def run(self, cmd, target=None, lock_name=None, shell=None, nofail=False, clean=False, follow=None, container=None, default_return_code=0)
```

The primary workhorse function of PipelineManager, this runs a command.

This is the command  execution function, which enforces
race-free file-locking, enables restartability, and multiple pipelines
can produce/use the same files. The function will wait for the file
lock if it exists, and not produce new output (by default) if the
target output file already exists. If the output is to be created,
it will first create a lock file to prevent other calls to run
(for example, in parallel pipelines) from touching the file while it
is being created. It also records the memory of the process and
provides some logging output.
#### Parameters:

- `cmd` (`str | list[str]`):  Shell command(s) to be run.
- `target` (`str | Sequence[str]`):  Output file(s) to produce, optional.If all target files exist, the command will not be run. If no target is given, a lock_name must be provided.
- `lock_name` (`str`):  Name of lock file. Optional.
- `shell` (`bool`):  If command requires should be run in its own shell.Optional. Default: None --will try to determine whether the command requires a shell.
- `nofail` (`bool`):  Whether the pipeline proceed past a nonzero return froma process, default False; nofail can be used to implement non-essential parts of the pipeline; if a 'nofail' command fails, the pipeline is free to continue execution.
- `clean` (`bool`):  True means the target file will be automatically addedto an auto cleanup list. Optional.
- `follow` (`callable`):  Function to call after executing (each) command.
- `container` (`str`):  Name for Docker container in which to run commands.
- `default_return_code` (`Any`):  Return code to use, might be used to discriminatebetween runs that did not execute any commands and runs that did.


#### Returns:

- `int`:  Return code of process. If a list of commands is passed,this is the maximum of all return codes for all commands.




```python
def start_pipeline(self, args=None, multi=False)
```

Initialize setup. Do some setup, like tee output, print some diagnostics, create temp files. You provide only the output directory (used for pipeline stats, log, and status flag files).



```python
def stop_pipeline(self, status='completed')
```

Terminate the pipeline.

This is the "healthy" pipeline completion function.
The normal pipeline completion function, to be run by the pipeline
at the end of the script. It sets status flag to completed and records
some time and memory statistics to the log file.



```python
def time_elapsed(time_since)
```

Returns the number of seconds that have elapsed since the time_since parameter.
#### Parameters:

- `time_since` (`float`):  Time as a float given by time.time().




```python
def timestamp(self, message='', checkpoint=None, finished=False, raise_error=True)
```

Print message, time, and time elapsed, perhaps creating checkpoint.

This prints your given message, along with the current time, and time
elapsed since the previous timestamp() call.  If you specify a
HEADING by beginning the message with "###", it surrounds the message
with newlines for easier readability in the log file. If a checkpoint
is designated, an empty file is created corresponding to the name
given. Depending on how this manager's been configured, the value of
the checkpoint, and whether this timestamp indicates initiation or
completion of a group of pipeline steps, this call may stop the
pipeline's execution.
#### Parameters:

- `message` (`str`):  Message to timestamp.
- `checkpoint` (`str`):  Name of checkpoint; this tends to be somethingthat reflects the processing logic about to be or having just been completed. Provision of an argument to this parameter means that a checkpoint file will be created, facilitating arbitrary starting and stopping point for the pipeline as desired.
- `finished` (`bool`):  Whether this call represents the completion of aconceptual unit of a pipeline's processing
- `raise_error` (``):  Whether to raise exception ifcheckpoint or current state indicates that a halt should occur.




```python
def warning(self, msg, *args, **kwargs)
```






*Version Information: `pypiper` v0.14.1, generated by `lucidoc` v0.4.4*