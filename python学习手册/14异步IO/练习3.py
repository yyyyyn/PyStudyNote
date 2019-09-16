import threading
import asyncio

hello_num = 0
@asyncio.coroutine
def hello():
    global hello_num
    hello_num += 1
    num = hello_num
    print('Hello world! (%s),begin time is %d' % (threading.currentThread(), num))
    yield from asyncio.sleep(4)
    print('Hello again! (%s),begin time is %s' % (threading.currentThread(), num))

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

