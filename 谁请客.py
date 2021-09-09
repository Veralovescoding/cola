print('今天谁负责买单？？')
import random
import time
EBC_web=['Vera','栖铭','朱丽丝','范范','Huahua']
print('Loading.......')
time.sleep(1)
for x in range(len(EBC_web)-1):
    cola = random.randint(0, (len(EBC_web))-1)
    print('It is not '+EBC_web[cola]+'.....')
    del EBC_web[cola]
    time.sleep(1)
print('It is '+EBC_web[0])
