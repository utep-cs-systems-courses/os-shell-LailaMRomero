import os
from myRedirect import redirect
from Lab1 import executeCommands
import pipe
def pipeInput(args):#the pipes method that take output of one method as input of another. eg output | input
    left=args[0:args.index("|")]# gets data of left side of pipe
    right=args[len(left)+1:]#gets the data of right side of pipe
    pRead, pWrite = os.pipe()#making the read and write 
    rc=os.fork()##creates a child process
    if rc<0:# if the returns a 0 the for failed
        os.write(2, ("Fork has failed returning now %d\n" %rc).encode())#
        sys.exit(1)# used to exit
    elif rc==0:#if return value is 0 do the following
        os.close(1)#close file descriptor 1
        os.dup(pWrite)#copies the file descriptors of the child and put into pipeWrite
        os.set_inheritable(1,True)#
        for fd in (pRead,pWrite):
            os.close(fd)#closes all the file descriptors
        executeCommands(left)#inputs the left argument into executeCommands
    else:
        os.close(0)#closes file descriptor 0
        os.dup(pRead)#copies the files descriptor of the parent and puts it into pRead
        os.set_inheritable(0,True)#
        for fd in (pWrite, pRead):
            os.close(fd)#closes file descriptors in both pRead,pWrite
        if "|" in right:#if it finds '|' on the right side of argument then it pipes right vars
            pipe(right)#goes into pipe 
        executeCommands(right)#inputs the right argument executeCommands
