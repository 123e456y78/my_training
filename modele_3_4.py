def single_root_words (root_words,*other_words):
    same_words=[]
    words = list(other_words)
    for i in range(len(words)):
        if root_words.lower() in words[i].lower() or words[i].lower() in root_words.lower():
            same_words.append(words[i])
    return (same_words)
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)