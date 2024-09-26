def find_anagrams(word, candidates):
    word = word.lower()
    candidate_list = []
    for c in candidates:
        c = c.lower()
        check = 0
        if len(word) != len(c):
            check += 1
        for letter in word:
            if letter not in c:
                check += 1
        if check == 0:
            candidate_list.append(c)
    return candidate_list