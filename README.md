# tensorboard-example

Simple example of how to use Tensorboard with Valohai.

## Run the example

> **⚠️ Prerequirements**
> 
> * Clone this repository
> * Install Valohai command-line tools (`pip install --upgrade valohai-cli`)
> * Login to Valohai (`vh login`)

Clone this repository to your local machine and navigate to the local directory.

Run `vh project create` to create a new Valohai project and link your working directory to that project. Make sure you're in the root of this repository.

Run a new Valohai job:
`vh exec run --adhoc train --watch`

You can view the results on Tensorboard after the job completes. 

First, make sure you're running Tensorboard on your local machine (`tensorboard --logdir=./logs`) and then download the logs from your Valohai execution with `vh exec outputs -f events.out.tfevents.* -d ./logs/exec-1 1`

> See the [Valohai Fundamentals tutorial](https://docs.valohai.com/tutorials/learning-paths/fundamentals/) to learn more about Valohai executions and the CLI.

## FAQ

### Can I view currently running executions on Tensorboard?

Yes. First, make sure you're running Tensorboard (`tensorboard --logdir=./logs`)

Then start a new job on Valohai and sync the logs to your local machine:

`vh exec run --adhoc train --sync=./logs/exec-{counter}`

After the job starts you'll start seeing data on your Tensorboard.

If you already started the job without `--sync` you can get the metrics by running `vh exec outputs -f events.out.tfevents.* -d ./logs/exec-1 --sync 1` (where 1 is the number of the execution)

### Can I compare completed Valohai executions on Tensorboard?

Yes. You can download the logs from any execution with:

`vh exec outputs -f events.out.tfevents.* -d ./logs/exec-1 1`
Valohai execution download outputs, filter files that start with `events.out.tfevents.` and download them to a directory `./logs/exec-1` from execution `1`.

You'd do the same for execution 3 with:
`vh exec outputs -f events.out.tfevents.* -d ./logs/exec-3 3`

You should now see all the jobs on your local Tensorboard.

### Can I compare the currently running job and any completed jobs?

Yes. Make sure you've downloaded all the logs from the completed jobs by following the steps above (`vh exec outputs -f ...`)

Then start a new job with `vh exec run --adhoc train --sync=./logs/exec-{counter}` and you'll see both the currently running job and past jobs on your Tensorboard.
