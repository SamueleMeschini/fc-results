import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('data/basic_fc_flow.csv', delimiter=',', names=True)
t = data['times']
m_in = data['m_in']
m_out = 8.99e-7/0.01 # N_dot/TBE
t_infl = t[(m_in>m_out)][0]
fig, ax = plt.subplots()
print(t_infl)
ax.loglog(t, m_in)
ax.hlines(m_out, xmin=0,xmax=t[-1])
(ymin,ymax) = ax.get_ylim()
ax.vlines(t_infl, ymin=ymin, ymax=ymax)
ax.vlines(3*3600*24, ymin=ymin, ymax=ymax)
ax.set_xlim(1e4,1e6)
plt.show()