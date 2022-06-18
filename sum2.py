import os
import random
import numpy as np
import pandas as pd

tsk1 = []
import pandas as pd
import csv
from datetime import datetime,timedelta
st=0
end=150
date_time=datetime(2021,1,31)
res_s=[]
res_w=[]
res_e=[]
res_n=[]
path = 'C:\\Users\\Administrator\\Desktop\\checked.csv'  # 获取文件夹的路径
data = pd.read_csv(path, error_bad_lines=False)

data.index = pd.to_datetime(data['date'])


for t in range(end-st):
        sum_S = 0
        sum_E = 0
        sum_N = 0
        sum_W = 0

        dataframe_1 = data.loc[data.index == date_time, ['region', 'type', 'newCasesBySpecimenDate']]
        for i in range(376):
           if dataframe_1['region'][i][0]=='S' and dataframe_1['type'][i]==1:
               sum_S=sum_S+dataframe_1['newCasesBySpecimenDate'][i]
           if dataframe_1['region'][i][0]=='E' and dataframe_1['type'][i]==1:
               sum_E=sum_E+dataframe_1['newCasesBySpecimenDate'][i]
           if dataframe_1['region'][i][0]=='W' and dataframe_1['type'][i]==1:
               sum_W=sum_W+dataframe_1['newCasesBySpecimenDate'][i]
           if dataframe_1['region'][i][0]=='N' and dataframe_1['type'][i]==1:
               sum_N=sum_N+dataframe_1['newCasesBySpecimenDate'][i]
        date_time=date_time+timedelta(days = 1)
        res_s.append(sum_S)
        res_w.append(sum_W)
        res_e.append(sum_E)
        res_n.append(sum_N)
print('s=',res_s,'w=',res_w,'e=',res_e,'n=',res_n)

res_s_2=[]
res_w_2=[]
res_e_2=[]
res_n_2=[]
date_time=datetime(2021,1,31)
for t in range(end-st):
        sum_S = 0
        sum_E = 0
        sum_N = 0
        sum_W = 0
        dataframe_1 = data.loc[data.index == date_time, ['region', 'type', 'newCasesBySpecimenDate']]
        for i in range(376):
           if dataframe_1['region'][i][0]=='S' and dataframe_1['type'][i]==2:
               sum_S=sum_S+dataframe_1['newCasesBySpecimenDate'][i]
           if dataframe_1['region'][i][0]=='E' and dataframe_1['type'][i]==2:
               sum_E=sum_E+dataframe_1['newCasesBySpecimenDate'][i]
           if dataframe_1['region'][i][0]=='W' and dataframe_1['type'][i]==2:
               sum_W=sum_W+dataframe_1['newCasesBySpecimenDate'][i]
           if dataframe_1['region'][i][0]=='N' and dataframe_1['type'][i]==2:
               sum_N=sum_N+dataframe_1['newCasesBySpecimenDate'][i]
        date_time=date_time+timedelta(days = 1)
        res_s_2.append(sum_S)
        res_w_2.append(sum_W)
        res_e_2.append(sum_E)
        res_n_2.append(sum_N)
print('s2=',res_s_2,'w2=',res_w_2,'e2=',res_e_2,'n2=',res_n_2)

res_s_3=[]
res_w_3=[]
res_e_3=[]
res_n_3=[]
date_time=datetime(2021,1,31)
for t in range(end-st):
        sum_S = 0
        sum_E = 0
        sum_N = 0
        sum_W = 0

        dataframe_1 = data.loc[data.index == date_time, ['region', 'type', 'newCasesBySpecimenDate']]
        for i in range(376):

           if dataframe_1['region'][i][0]=='S' and dataframe_1['type'][i]==3:
               sum_S=sum_S+dataframe_1['newCasesBySpecimenDate'][i]
           if dataframe_1['region'][i][0]=='E' and dataframe_1['type'][i]==3:
               sum_E=sum_E+dataframe_1['newCasesBySpecimenDate'][i]
           if dataframe_1['region'][i][0]=='W' and dataframe_1['type'][i]==3:
               sum_W=sum_W+dataframe_1['newCasesBySpecimenDate'][i]
           if dataframe_1['region'][i][0]=='N' and dataframe_1['type'][i]==3:
               sum_N=sum_N+dataframe_1['newCasesBySpecimenDate'][i]
        date_time=date_time+timedelta(days = 1)
        res_s_3.append(sum_S)
        res_w_3.append(sum_W)
        res_e_3.append(sum_E)
        res_n_3.append(sum_N)
print('s3=',res_s_3,'w3=',res_w_3,'e3=',res_e_3,'n3=',res_n_3)
s_total=[]
w_total=[]
e_total=[]
n_total=[]
for i in range(150):
    s_total.append(res_s[i]+res_s_2[i]+res_s_3[i])
    w_total.append(res_w[i] + res_w_2[i] + res_w_3[i])
    e_total.append(res_e[i] + res_e_2[i] + res_e_3[i])
    n_total.append(res_n[i] + res_n_2[i] + res_n_3[i])
print('st=',s_total,'wt=',w_total,'et=',e_total,'nt=',n_total)

df = pd.DataFrame(res_s)
df.to_csv(os.path.join('C:\\Users\\Administrator\\Desktop\\regions', 'res_s_4' + '.csv'))
df = pd.DataFrame(res_n)
df.to_csv(os.path.join('C:\\Users\\Administrator\\Desktop\\regions', 'res_n_4' + '.csv'))
df = pd.DataFrame(res_e)
df.to_csv(os.path.join('C:\\Users\\Administrator\\Desktop\\regions', 'res_e_4' + '.csv'))
df = pd.DataFrame(res_w)
df.to_csv(os.path.join('C:\\Users\\Administrator\\Desktop\\regions', 'res_w_4' + '.csv'))

df = pd.DataFrame(res_s_2)
df.to_csv(os.path.join('C:\\Users\\Administrator\\Desktop\\regions', 'res_s_5' + '.csv'))
df = pd.DataFrame(res_n_2)
df.to_csv(os.path.join('C:\\Users\\Administrator\\Desktop\\regions', 'res_n_5' + '.csv'))
df = pd.DataFrame(res_e_2)
df.to_csv(os.path.join('C:\\Users\\Administrator\\Desktop\\regions', 'res_e_5' + '.csv'))
df = pd.DataFrame(res_w_2)
df.to_csv(os.path.join('C:\\Users\\Administrator\\Desktop\\regions', 'res_w_5' + '.csv'))

df = pd.DataFrame(res_s_3)
df.to_csv(os.path.join('C:\\Users\\Administrator\\Desktop\\regions', 'res_s_6' + '.csv'))
df = pd.DataFrame(res_n_3)
df.to_csv(os.path.join('C:\\Users\\Administrator\\Desktop\\regions', 'res_n_6' + '.csv'))
df = pd.DataFrame(res_e_3)
df.to_csv(os.path.join('C:\\Users\\Administrator\\Desktop\\regions', 'res_e_6' + '.csv'))
df = pd.DataFrame(res_w_3)
df.to_csv(os.path.join('C:\\Users\\Administrator\\Desktop\\regions', 'res_w_6' + '.csv'))