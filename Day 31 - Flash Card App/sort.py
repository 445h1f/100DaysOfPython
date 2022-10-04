with open('fr_50k.txt', 'r') as r:
    data = r.readlines()
    words = []
    for i in data:
        words.append(i.split(' ')[0])

    with open("fr_50k_words.txt", 'w') as w:
        w.write('\n'.join(words))