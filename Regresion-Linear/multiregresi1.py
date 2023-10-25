import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib as mpl

df = pd.read_csv("data2.csv")
reg = LinearRegression()
reg.fit(df[['x1','x2']].values,df.y)

mpl.rcParams['legend.fontsize'] = 12
fig = plt.figure()
ax = fig.add_subplot(projection ='3d')
ax.scatter(df.x1, df.x2, df.y)
ax.legend()
ax.view_init(45, 0)
plt.show()

a = reg.coef_
b = reg.intercept_

X_baru = np.array([8, 125]).reshape(-1, 2)
prediksi_Y = reg.predict(X_baru)

print('Koefisien regresi = ', a[0],'dan', a[1])
print('Intercept = ', b)
print('Hasil prediksi untuk x1=8 dan x2=125 yaitu', prediksi_Y)