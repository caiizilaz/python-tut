gmy_name = 'ryu'
my_lastname = 'xxx'


def print_name():
  global gmy_name
  gmy_name = 'yoshi'
  my_lastname = 'yyy'
  print(f'name: {gmy_name}, lastname: {my_lastname}')

print_name()

print(f'name: {gmy_name}, lastname: {my_lastname}')