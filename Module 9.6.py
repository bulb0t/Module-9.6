def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text)):
            if j+i+1 > len(text):
                continue
            yield text[j:j+i+1]

a = all_variants("abcd")
for m in a:
    print(m)
