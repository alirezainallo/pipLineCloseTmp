import multiprocessing
from time import sleep
import subprocess
import signal
import shlex
import os


# os.system("python3 myTask.py")
# sleep(5)
# print('[main] before terminate')
# os.kill(os.getpid(), signal.SIGINT)
# print('[main] after terminate')
# while True:
#     print('[main]')
#     sleep(5)
#-----------------------------------------------------------------
pid = os.getpid()
print("The PID of your program is:", pid)

proc = subprocess.Popen('python myTask.py', shell=True, stdin=subprocess.PIPE, universal_newlines=True, close_fds=True, restore_signals=True)#shell=True, #, universal_newlines=True)#, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
sleep(5)
proc.terminate()
print('proc.terminate()')
os.kill(proc.pid, signal.CTRL_C_EVENT)
print('os.kill(proc.pid, signal.CTRL_C_EVENT)')
# os.kill(proc.pid, signal.CTRL_BREAK_EVENT)
# print('os.kill(proc.pid, signal.CTRL_BREAK_EVENT)')
#=================================================================
# try:
#     proc = subprocess.Popen('python myTask.py', shell=True, stdin=subprocess.PIPE, universal_newlines=True, close_fds=True, restore_signals=True)#shell=True, #, universal_newlines=True)#, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     proc.send_signal()
#     print('proc.pid:',proc.pid)
#     sleep(5)
# except Exception as e:
#     print(f"Error: {e}")

# finally:
#     # Terminate the process using taskkill
#     try:
#         subprocess.run(shlex.split(f'taskkill /F /PID {proc.pid}'), check=True)
#         print("Process terminated")
#     except subprocess.CalledProcessError as e:
#         print(f"Error terminating process: {e}")
#=================================================================

# proc.stdin.write('my function argument ...\n')
# proc.stdin.flush()

# print('[main] before terminate')
# # proc.terminate()
# # proc.kill()
# # proc.stdin.write(b'^c')
# # proc.stdin.flush()
# # proc.wait()

# # اولین تلاش: استفاده از terminate()
# proc.terminate()
# proc.terminate()
# print('[main] after proc.terminate')

# # انتظار کوتاه برای اطمینان از اتمام پردازه
# sleep(1)

# # دومین تلاش: استفاده از kill()
# proc.kill()
# proc.kill()
# print('[main] after proc.kill')

# # انتظار کوتاه برای اطمینان از اتمام پردازه
# sleep(1)

# # سومین تلاش: استفاده از os.kill() برای ارسال سیگنال SIGKILL
# try:
#     os.kill(proc.pid, signal.SIGKILL)
#     os.kill(proc.pid, signal.SIGKILL)
# except Exception as e:
#     print("Error occurred while trying to force close the process:", e)

# print('[main] after os.kill')

while True:
    print('[main]')
    sleep(5)
#-----------------------------------------------------------------
# def runCmd(cmd:str):
#     print('[runCmd] start runCmd:', cmd)
#     while True:
#         print('[runCmd]')
#         sleep(0.2)
#     print('[runCmd] after while')
# RecorderThread = multiprocessing.Process(target=runCmd, args=('my function argument ...', ))
# RecorderThread.start()
# sleep(5)
# print('[main] after terminate')
# RecorderThread.terminate()
# print('[main] before terminate')
# while True:
#     print('[main]')
#     sleep(5)