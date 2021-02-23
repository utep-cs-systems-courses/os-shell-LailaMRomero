import os
from myRedirect import redirect
def pipeInput(Input):
    #global Input
    Input = Input.split('|')
    leftArg = Input[0].split()
    rightArg = Input[1].split()
    pipeRead, pipeWrite = os.pipe()
    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed\n").encode())
        sys.exit(1)
    elif rc == 0: #we will exec left arg here
        if '<' in leftArg:
            redirect("in")         
        if '>' in leftArg:
            redirect("out")
            #FINISH LEFTARG
            
    else: #then exec the right arg here
        if '<' in rightArg:
            redirect("in")
        if '>' in rightArg:
            redirect("out")
            #FINISH RIGHTARG
