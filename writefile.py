with open('files/write.txt', 'w') as write_file:
    write_file.write('zz')


with open('files/write.txt', 'a') as write_file:
    write_file.write('\naa')

quotes = [
    '\naa',
    '\nbb',
    '\ncc',
]

with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)
