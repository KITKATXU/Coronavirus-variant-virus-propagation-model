import numpy as np
t=5
while 1:
  up=40410659
  down=pow((np.exp(-0.05*t)*134933+1),2)*np.exp(0.05*t)
  res=up/down
  print(res,t)
  t=t+1
  if  res<10:
      break