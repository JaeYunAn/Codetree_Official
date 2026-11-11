text_1 = input()
text_2 = input()
text_3 = input()

max_len = max(len(text_1), len(text_2), len(text_3))
min_len = min(len(text_1), len(text_2), len(text_3))

print(max_len - min_len)