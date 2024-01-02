import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
from math import *
from scipy.optimize import curve_fit



def Maxdev(l,il):
    """
    
    """
    for i in l:
        dev=abs(np.average(l)-i)
        if dev>il:
                il=dev
    return np.average(l),dev
    
    
def F(x,m):
    """_summary_

    Args:
        x (_type_): _description_
        m (_type_): _description_
        b (_type_): _description_
    """
    return m*x
def ajuste(x,y,title="",xlabel="B",ylabel=r"$\varepsilon (mV)$"):
    """_summary_

    Args:
        f (_type_): _description_
        x (_type_): _description_
        y (_type_): _description_
    """
    m,im=curve_fit(F,x,y)
    xmax=x[-1]
    plt.plot(np.linspace(0,xmax+xmax/10,20000),F(np.linspace(0,xmax+xmax/10,20000),m),label="Ajuste linear $y=mx+b$")
    plt.scatter(x,y,label="Data")
    plt.legend(loc="best",frameon=False)
    plt.ticklabel_format(axis='y',scilimits=(0,0),useMathText=True,style='sci')
    plt.xlim(0)
    plt.ylim(0)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    
    return [m,np.sqrt(im)]



##Parte 1
ca=4186
mconjunto=21.91*10**(-3)

mh2oe=175.33*10**(-3)

mesfera=229.98*10**(-3)

Tie=372.55
Tia=295
Tf=297.8

ce=-(Tf-Tia)*ca*mh2oe/((Tf-Tie)*mesfera)

print("c esfera=",ce)

mh2oc1=246.16*10**(-3)-mconjunto



mcilindro1=200.92*10**(-3)


Tic1=372.75
Tia=295.5
Tf=306.7

cc1=-(Tf-Tia)*ca*mh2oc1/((Tf-Tic1)*mcilindro1)

print("c c1=",cc1)


mh2oc2=204.26*10**(-3)-mconjunto
mcilindro2=193.54*10**(-3)
Tic2=373.15
Tia=295.8
Tf=302.4
cc2=-(Tf-Tia)*ca*mh2oc2/((Tf-Tic2)*mcilindro2)

print("c c2=",cc2)

mh2oi=171.57*10**(-3)-mconjunto
mh2oq=233.34*10**(-3)-mconjunto-mh2oi
Tia=296
Tiq=364.85
Tf=315.5
meq=-(mh2oq*(Tf-Tiq)+mh2oi*(Tf-Tia))/(Tf-Tia)

print("Meq=",meq*10**3,"g")


print("Com correção:")
ca=4186
mconjunto=21.91*10**(-3)

mh2oe=175.33*10**(-3)

mesfera=229.98*10**(-3)

Tie=372.55
Tia=295
Tf=297.8

ce=-(Tf-Tia)*ca*(mh2oe+meq)/((Tf-Tie)*mesfera)

print("c esfera=",ce)

mh2oc1=246.16*10**(-3)-mconjunto



mcilindro1=200.92*10**(-3)


Tic1=372.75
Tia=295.5
Tf=306.7

cc1=-(Tf-Tia)*ca*(mh2oc1+meq)/((Tf-Tic1)*mcilindro1)

print("c c1=",cc1)


mh2oc2=204.26*10**(-3)-mconjunto
mcilindro2=193.54*10**(-3)
Tic2=373.15
Tia=295.8
Tf=302.4
cc2=-(Tf-Tia)*ca*(mh2oc2+meq)/((Tf-Tic2)*mcilindro2)

print("c c2=",cc2)



####Ex 2


mh2oi=252.26*10**(-3)-mconjunto


Tih2o=321.8
Tfh2o=304.4

mh2of=288.34*10**(-3)-mconjunto

mgelo=mh2of-mh2oi

print("Mgelo=",mgelo*10**3,"g")


Lfusao=-((meq+mh2oi)*4186*(Tfh2o-Tih2o)+mgelo*4186*(Tfh2o-273.15))/mgelo
print("Lfusao=",Lfusao)
print("erro",(Lfusao-334*10**3)/(334*10**3)*100)