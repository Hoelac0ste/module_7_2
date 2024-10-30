strings_positions = {}

def custom_write(*strings, file_name = 'file1.txt'):
    a = len(strings_positions) + 1
    for i in strings:
        file = open(file_name, 'a', encoding='utf-8')
        strings_positions[f'{a}, {file.tell()}'] = i
        file.write(f'{i}\n')
        file.close()
        a += 1
    print(strings_positions)

custom_write('hey', 'hello', 'hola', 'привет')
custom_write('hey', 'hello', 'hola', 'привет')
