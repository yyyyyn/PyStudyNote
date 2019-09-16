'''
编写登录接口：
输入用户名密码
认证成功后显示欢迎信息
输错三次后锁定
'''
print('-------欢迎进入登录界面-------')
f=open('homework1.txt','a')
f.close()

def addAccount(s):
    f=open('homework1.txt','a')
    f.write(s+'\n')
    f.close()
    print('you add an account successful!')
times=3
while times:
    user=input('Enter your name:')
    psd=input('Enter your password:')
    userinof=user+'#'+psd

    f=open('homework1.txt')
    users=f.read()
    f.close()
    if userinof in users:
        times=3
        print('welcome to login!')
        while True:
            choices=input('what you want to do(1:sing 2:swing 3:login out)?')
            if choices=='1':
                print('you are singing happly!')
            elif choices=='2':
                print('you are swing happly')
            elif choices=='3':
                print('welcome to login in again!')
                break
            else:
                print('your choice is out of options what we have,please chose again!')
    else:
        times -= 1
        print('your message is wrong!')
        choices=input('Please chose to login in again or create an account(input a or b):')
        if(choices=='b'):
            addAccount(userinof)
        print("Attention:now you just have {0} times to login".format(times))