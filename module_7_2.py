
def custom_write(*strings, file_name = 'file_name.txt'):
    strings_positions = {}
    a = 1
    for i in strings:
        file = open(file_name, 'a')
        strings_positions[f'{a}, {file.tell()}'] = i
        file.write(f'{i}\n')
        file.close()
    print(strings_positions)

custom_write('hey', 'hello', 'hola')