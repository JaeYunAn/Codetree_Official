text = input()

if 'ee' in text and 'ab' in text:
    print('Yes Yes')
elif 'ee' not in text and 'ab' in text:
    print('No Yes')
elif 'ee' in text and 'ab' not in text:
    print('Yes No')
elif 'ee' not in text and 'ab' not in text:
    print('No No')