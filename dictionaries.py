def belt_count(dic):
  belts = list(dic.values())
  for belt in set(belts):
    num = belts.count(belt)
    print(f'There are {num} {belt} belts')

# def ninja_intro(dic):
#   for key, val in dic.items():
#      print(f'I am {key} and I am a {val} belt')

ninja_belts = {}

# ninja_belts = dict()

while True:
  ninja_name = input('enter a ninja name: ')
  ninja_belt = input('enter belt color: ')
  ninja_belts[ninja_name] = ninja_belt

  another = input('add another ? (y/n): ')
  if another == 'y':
    continue
  else:
    break

# ninja_intro(ninja_belts)

belt_count(ninja_belts)

