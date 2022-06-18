from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

path = 'C:\\Users\\Administrator\\Desktop\\regions_result\\res_w.csv'
# 使用pandas读入
data = pd.read_csv(path) #读取文件中所有数据
# 按列分离数据
xdata = data[['t']]
print(xdata)
xdata = np.array(xdata).flatten()
ydata = data[['s']]
print(ydata)
ydata = np.array(ydata).flatten()
arr = []
arr2 =[]
ct = 0
for i in range(ydata.size):
        arr.append(xdata[ct])
        arr2.append(ydata[ct])
        ct = ct + 1

xdata = arr
ydata = arr2
print(xdata)
print(ydata)

x = list(np.arange(0,700, 0.01))

# 绘制散点
plt.scatter(xdata[:], ydata[:], 25, "darkgreen")

hyperparameters_r = None
hyperparameters_K = None
def logistic_increase_function(t,P0):
    # logistic生长函数：t:time   P0:initial_value    K:capacity  r:increase_rate
    # 后面将对r和K进行网格优化

    r = hyperparameters_r
    K = hyperparameters_K

    t=np.array(t)
    exp_value = np.exp(r * (t))
    return (K * exp_value * P0) / (K + (exp_value - 1) * P0)

def fitting(logistic_increase_function, x_data, y_data):
    print(x_data,y_data)
    # 传入要拟合的logistic函数以及数据集
    # 返回拟合结果
    popt = None
    mse = float("inf")
    i = 0
    # 网格搜索来优化r和K参数
    r = None
    k = None
    k_range = np.arange(100, 200000, 5000)
    r_range = np.arange(0, 1, 0.01)
    for k_ in k_range:
        global hyperparameters_K
        hyperparameters_K = k_
        for r_ in r_range:
            global hyperparameters_r
            hyperparameters_r = r_
            # 用非线性最小二乘法拟合
            popt_, pcov_ = curve_fit(logistic_increase_function, x_data, y_data, maxfev = 10000)
            # 采用均方误准则选择最优参数
            mse_ = mean_squared_error(y_data, logistic_increase_function(x_data, *popt_))
            if mse_ <= mse:
                mse = mse_
                popt = popt_
                r = r_
                k = k_
            i = i+1
            print('\r当前进度：{0}{1}%'.format('▉'*int(i*10/len(k_range)/len(r_range)),int(i*100/len(k_range)/len(r_range))), end='')
    print('拟合完成')
    hyperparameters_K = k
    hyperparameters_r = r
    popt, pcov = curve_fit(logistic_increase_function, x_data, y_data)
    print("K:capacity  P0:initial_value   r:increase_rate")
    print(hyperparameters_K, popt, hyperparameters_r)
    print(popt)
    y6 = [logistic_increase_function(i, popt) for i in x]
    x0 = 47
    y0 = logistic_increase_function(x0, popt)
    plt.plot([x0, x0], [y0, 0], 'k--', lw=2)
    plt.xlabel('Day')
    plt.ylabel('Number of Patients')
    # method1
    #plt.annotate(r'$y = 2 / K$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points',
     #            fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))
    plt.plot(x, y6, c='grey')
return hyperparameters_K, hyperparameters_r, popt

K, r, popt = fitting(logistic_increase_function, xdata, ydata)
plt.show()
