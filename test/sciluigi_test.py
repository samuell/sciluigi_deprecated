import sciluigi
from nose.tools import with_setup

# Make these variables global
#shell_task = None

def setup():
    global shell_task
    shell_task = sciluigi.shell("cat <i:input> > <o:output:out.txt>")
    return shell_task

def teardown():
    global shell_task
    shell_task = None

@with_setup(setup, teardown)
def test_inports_nonempty():
    assert len(shell_task.inports) == 1

@with_setup(setup, teardown)
def test_outports_nonempty():
    assert len(shell_task.outports) == 1
