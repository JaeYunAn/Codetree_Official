char = input()

if char == 'a':
    print('z')
else:
    char = ord(char) - 1
    print(chr(char))