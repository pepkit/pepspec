## Create a folder of linked similar objects (symlinks)

Looper has the ability to create a folder containing symlinks to similar objects (e.g. images). This is helpful if your pipeline reports many objects, and you would like to see them in one place.

You must configure [pipestat](../tutorial/pipestat.md) to use this feature. 

Once your pipeline has finished running, you can run the command:

```shell
looper link
```

This command will create symlinks of all objects of the same type and place them in the results folder for convenient browsing.


