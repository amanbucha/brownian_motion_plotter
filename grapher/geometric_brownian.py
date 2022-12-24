import numpy as np, math, random
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def compute(size, start, end, num, mean, volatility):
    sigma=math.sqrt(volatility)
    def boxmuller():
        arr=[]
        while len(arr) < size-1 :
            R=math.sqrt(-2*math.log(random.random()))
            theta=2*math.pi*(random.random())
            arr.append(R*math.cos(theta))
        return arr

    t=np.linspace(0, end, size)

    def geom_brownian():
        X=[]
        X.append(start)
        Z=boxmuller()
        for i in range(size-1):
            X.append(X[i]*math.exp((mean-sigma*sigma/2)*(t[i+1]-t[i])+sigma*math.sqrt(t[i+1]-t[i])*Z[i]))
        return X

    plt.xlabel('t')
    plt.ylabel('X(t)')  
    for _ in range(num):
        plt.plot(t, geom_brownian())
    plt.show()
    image=BytesIO()
    plt.savefig(image, format='png')
    plt.clf()
    return base64.b64encode(image.getvalue())