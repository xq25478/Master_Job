import os
import numpy as np
import shutil

imgs = os.listdir('./concat')
for i in range(10):
    if not os.path.exists(str(i)):
        os.mkdir(str(i))
cnt = [0]*10
for img in imgs:
    score = float(img.split('_')[0])
    for i in range(10):
        if i*0.1 <= score <= (i+1)*0.1:
            cnt[i] += 1
            shutil.copy('./concat/'+img,'./'+str(i)+'/'+img)
    print(score)
print(cnt,sum(cnt))