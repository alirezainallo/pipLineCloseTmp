from time import sleep
import os

def runCmd(cmd:str):
    # print('[runCmd] start runCmd:', cmd)
    print('[runCmd] start runCmd')
    while True:
        pid = os.getpid()
        # print("The PID of your program is:", pid)
        print('[runCmd]',pid,os.getlogin())
        sleep(0.2)
    print('[runCmd] after while')

# cmd = input()
# runCmd(cmd)
runCmd('')
