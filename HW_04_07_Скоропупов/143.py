def anagram(word1, word2):
    letters1 = list(word1.lower())
    letters1.sort()
    letters2 = list(word2.lower())
    letters2.sort()
    return letters1 == letters2

print(anagram('Live', 'evil'))

# True
