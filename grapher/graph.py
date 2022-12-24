import numpy as np, math, random
from io import BytesIO
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def compute(size, end, num, drift, diffusion_coefficient):
    sigma=math.sqrt(diffusion_coefficient)
    def boxmuller():
        arr=[]
        while len(arr) < size-1 :
            R=math.sqrt(-2*math.log(random.random()))
            theta=2*math.pi*(random.random())
            arr.append(R*math.cos(theta))
        return arr

    t=np.linspace(0, end, size)

    def brownian():
        X=[]
        X.append(0)
        Z=boxmuller()
        for i in range(size-1):
            X.append(X[i]+drift*(t[i+1]-t[i])+sigma*math.sqrt(t[i+1]-t[i])*Z[i])
        return X

    plt.xlabel('t')
    plt.ylabel('X(t)')  
    for _ in range(num):
        plt.plot(t, brownian())
    plt.show()
    image=BytesIO()
    plt.savefig(image, format='png')
    plt.clf()
    return base64.b64encode(image.getvalue())