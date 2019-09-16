'''
正则表达式中，如果直接给出字符，就是精确匹配，个数要一致。
用\d匹配一个数字，\w匹配一个字母或数字，.可以匹配任意字符，\s可以匹配一个空格（也包括Tab等空白符）

匹配变长的字符：
用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，
用{n}表示n个字符，用{n,m}表示n-m个字符，可以用[]表示范围
^表示行的开头，^\d表示必须以数字开头。
$表示行的结束，\d$表示必须以数字结束。
'py'也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了
'''
import re
test='abcd'
if re.match(r'bc\w',test):      #建议使用r反转义符
    print('ok')
else:
    print('failed')

print(re.match(r'^\d{3}[\-\s]+\d{3,8}$', '010 -12345'))

print('========可以用re来进行切片，可以识别连续且不同的分隔符')
print('a b   c'.split(' '),
      re.split(r'\s+','a b    c'),
      re.split(r'[\s\,\-]+','a b,c-,d -, e'))

print('========re提取子串:用()表示的就是要提取的分组,用group()取出')
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0),m.group(1),m.group(2),m.groups())
#注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串,超出个数报错
#groups()可以获取所有子串

print('========正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符，加个?可以实现经可能少匹配')
print(re.match(r'^(\d+)(0*)$','122012000').groups())
print(re.match(r'^(\d+?)(0*)$','122012000').groups())

print('========上诉正则表达式每次都会编译，可以预编译实现一次编译多次使用')
ret=re.compile(r'^(\d{3})-(\d{3,8})$')
print(ret.match('010-12345').groups())
print(ret.match('015-65425').groups())

print('========匹配二进制数据')
b=b'abcde'
print(re.match(b'a(b|c)*.*',b).groups())