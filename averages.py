import numpy as np

size = 10

mean_x = 1.78
std_x = 0.1
dist_x = np.random.normal(loc=mean_x, scale=std_x, size=size)

mean_y = 1.66
std_y = 0.1
dist_y = np.random.normal(loc=mean_x, scale=std_x, size=size)

xbar = np.sum(dist_x) / size
ybar = np.sum(dist_y) / size

xvar = np.sum([(x-xbar)**2 for x in dist_x]) / (size - 1)
xstd = xvar ** 0.5

xycov = np.sum([(x - xbar)*(y - ybar) for x, y in zip(dist_x, dist_y)]) / (size - 1)


assert xbar == np.mean(dist_x)
assert xvar == np.var(dist_x, ddof=1)
assert xycov == np.cov(dist_x, dist_y)[1][0]