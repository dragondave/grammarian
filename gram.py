from Levenshtein import distance
with open("/usr/share/dict/british-english") as f:
    words = set([x.strip().lower() for x in f.readlines() if x.strip()])

with open("spells.txt") as f:
    spells = [x.strip() for x in f.readlines() if x.strip()]

def skip(spellword, word):
    if len(word) < 3: return True
    if word + "s" == spellword: return True
    if spellword + "s" == word: return True
    return False

def disp(spellwords, word, pos):
    x = []
    for i in range(len(spellwords)):
        if i==pos:
            x.append(word)
        else:
            x.append(spellwords[i])
    return ' '.join(x)

for spell in spells:
    print(spell)
    spellwords = spell.lower().split(" ")
    for i, spellword in enumerate(spellwords):
        for word in words:
            if distance(spellword, word) == 1 and not skip(spellword, word):
                print ("> ", disp(spellwords, word, i))
    print()
