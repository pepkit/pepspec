# How to run jobs in containers

Because `looper` uses `divvy` for computing configuration, running jobs in containers is easy! `Divvy` can use the same template system to do either cluster computing or to run jobs in linux containers (for example, using `docker` or `singularity`). The way to do this is similar to how you would run jobs on a cluster, but you use templates that run jobs in containers. You can even run jobs in a container *on a cluster*.


!!! note "What you'll accomplish"
    Configure looper to run pipeline jobs inside Docker or Singularity containers.



## 1. Get your container image.

This could be a docker image (hosted on dockerhub), which you would download via `docker pull`, or it could be a `singularity` image you have saved in a local folder. This is pipeline-specific, and you'll need to download the image recommended by the authors of the pipeline or pipelines you want to run.


## 2. Specify the image in your `pipeline_interface`

The `pipeline_interface.yaml` file will need a `compute` section for each pipeline that can be run in a container, specifying the image. For example:


```yaml title="pipeline_interface.yaml"
compute:
  singularity_image: ${SIMAGES}myimage
  docker_image: databio/myimage
```

For singularity images, you just need to make sure that the images indicated in the `pipeline_interface` are available in those locations on your system. For docker, make sure you have the docker images pulled.


## 3. Add a new compute package for containerized jobs

You will just need to add a new compute package that uses. Here's an example of how to add one for using singularity in a SLURM environment:

```yaml hl_lines="5 6 7 8"
compute_packages:
  default:
    submission_template: divvy_templates/local_template.sub
    submission_command: sh
  singularity_slurm:
    submission_template: templates/slurm_singularity_template.sub
    submission_command: sbatch
    singularity_args: -B /sfs/lustre:/sfs/lustre,/nm/t1:/nm/t1
```

In `singularity_args` you'll need to pass any mounts or other settings to be passed to singularity. The actual `slurm_singularity_template.sub` file looks something like this:

```bash title="slurm_singularity_template.sub"
#!/bin/bash
#SBATCH --job-name='{JOBNAME}'
#SBATCH --output='{LOGFILE}'
#SBATCH --mem='{MEM}'
#SBATCH --cpus-per-task='{CORES}'
#SBATCH --time='{TIME}'
#SBATCH --partition='{PARTITION}'
#SBATCH -m block
#SBATCH --ntasks=1

echo 'Compute node:' `hostname`
echo 'Start time:' `date +'%Y-%m-%d %T'`

singularity instance.start {SINGULARITY_ARGS} {SINGULARITY_IMAGE} {JOBNAME}_image
srun singularity exec instance://{JOBNAME}_image {CODE}

singularity instance.stop {JOBNAME}_image
```

Notice how these values will be used to populate a template that will run the pipeline in a container. Now, submit a job that will use singularity, you activate this compute package with `looper run --package singularity_slurm`.


Here's another example divvy config file that adds a compute package to run jobs in docker on a local computer:

```yaml title="divvy_config.yaml"
compute:
  default:
    submission_template: templates/localhost_template.sub
    submission_command: sh
  singularity:
    submission_template: templates/localhost_singularity_template.sub
    submission_command: sh
    singularity_args: --bind /ext:/ext
  docker:
    submission_template: templates/localhost_docker_template.sub
    submission_command: sh
    docker_args: |
      --user=$(id -u) \
      --env="DISPLAY" \
      --volume ${HOME}:${HOME} \
      --volume="/etc/group:/etc/group:ro" \
      --volume="/etc/passwd:/etc/passwd:ro" \
      --volume="/etc/shadow:/etc/shadow:ro"  \
      --volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
      --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
      --workdir="`pwd`" \
```

Notice the `--volume` arguments, which mount disk volumes from the host into the container. This should work out of the box for most docker users.


!!! note "Looper and bulker"
    Many other pipeline frameworks wrap containers into the pipeline. Looper avoids this approach because it tightly couples the computing environment to the pipeline. Instead, Looper's approach is to level these things separated. Specifying a container in a submission template, as described here, works well for pipelines that use *monolithic* containers -- that is, there is one giant container, and the whole pipeline runs in that container. An alternative approach is to have a pipeline submit container jobs for each individual task. This approach allows you to use smaller, lightweight containers with only one tool, which makes them more reusable. If you want to use this modular approach, you might be interested in [bulker](https://bulker.io), the computing environment manager in PEPkit. 




!!! tip "Summary"
    - To looper, containers are just another computing environment setting. You can use the submission template to wrap the command in whatever boilerplate you want, which can be used either for cluster submission or for containers.
