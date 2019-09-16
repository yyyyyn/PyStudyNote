'''
subprocess通过子进程来执行外部指令，并通过input/output/error管道，获取子进程的执行的返回信息。
'''
import subprocess

print('你好')
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
