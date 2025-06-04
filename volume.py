from scipy import integrate

func = lambda y, x: x**2 + y**2
volume, error = integrate.dblquad(func, 0, 1, lambda x: 0, lambda x: 1)

print("Volume =", volume)