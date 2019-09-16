import sys
print('------平台与版本---------')
print(sys.__dict__['platform'] if 'platform' in sys.__dict__ else 'unknow')
print(sys.platform,sys.maxsize,sys.version)
if sys.platform[:3]=='win':
    print('hello windows')

print('------模块搜索路径---------')
print(type(sys.path))
for l in sys.path:
    print(l)

print('-----已加载模块表---------')
print(sys)
print(type(sys.modules))
print(sys.modules['sys'])
print(list(sys.modules.keys()))
print('内置模块:',sys.builtin_module_names)

print('------异常的详细信息-----------')
"sys.exc_info函数会返回一个元祖，其中包好最近异常的类型，值和跟踪对象"
try:
    raise IndexError('abc')
except:
    print(sys.exc_info())

print('------sys模块导出的其它工具-----------')
"sys.argv:显示文件位置"
"标准流，包括sys.stdin, sys.stdout, sys.stderr"
"sys.exit强制退出程序"
print('sys.argv',type(sys.argv),sys.argv)
print('sys.stdin',type(sys.stdin),sys.stdin)
sys.exit()
print('aaa')