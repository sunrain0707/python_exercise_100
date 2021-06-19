#9.暂停一秒输出。

import time
mydic = {1:'a',2:'b'}
for key,value in mydic.items():
    print(key,value)
    time.sleep(1)