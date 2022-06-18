import os
import random
import numpy as np
import pandas as pd

tsk1 = []
import pandas as pd
import csv
from datetime import datetime,timedelta

path='C:\\Users\\Administrator\\Desktop\\sumup1.csv'  # 获取文件夹的路径
data = pd.read_csv(path,error_bad_lines=False)

path='C:\\Users\\Administrator\\Desktop\\check.csv'  # 获取文件夹的路径
data_check = pd.read_csv(path,error_bad_lines=False)

dataframe_1=pd.DataFrame(data)

print(len(data),len(data_check))
new=[]
dataframe_check=pd.DataFrame(data_check)
for i in range(len(data)):
    ind=0
    for j in range(len(data_check)):
       if dataframe_1['city'][i]==dataframe_check['LAD20NM'][j]:
           ind=j
           break
    new.append(dataframe_check['LAD20CD'][ind])
dataframe_1['region']=new
dataframe_1.to_csv(os.path.join('C:\\Users\\Administrator\\Desktop', 'checked' + '.csv'))
