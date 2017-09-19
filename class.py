from space.planet import Planet
from space.calc import planet_mass

naboo = Planet('Naboo', 7000, 5.5, 'Naboo System')
print(f'naboo is: {naboo.name}')
print(naboo.orbit())

naboo_mass = planet_mass(naboo.gravity,naboo.radius)
print(naboo_mass)
