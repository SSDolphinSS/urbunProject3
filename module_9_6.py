def all_variants(text):
    a = len(text)
    for i in range(1, a + 1):
        for j in range(a - i + 1):
            yield text[j:j + i]


a = all_variants("abc")
for i in a:
    print(i)
