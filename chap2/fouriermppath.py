import mpmath as mp
import matplotlib.pyplot as plt

PI = mp.pi
I = [-PI, PI]
x = lambda t: abs(t)

ps = mp.fourier(x, I, 3)
psval = lambda t: mp.fourierval(ps, I, t)
mp.plot([x, psval], xlim=I, file='mp.png')
#plt.savefig("fmp.png")