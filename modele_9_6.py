def all_variants(text):
    for i in range(len(text)):
        for l in range(i, len(text)):
            yield text[i:l+1]
a = all_variants("abc")
for i in a:
     print(i)