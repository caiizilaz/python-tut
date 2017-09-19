def planet_mass(gravity, radius):
    mass = (gravity * radius**2) / (6.67 * 10**-11)
    return mass
