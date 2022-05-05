from string import punctuation

# string = input()

pali1 = 'Herb the sage eats sage, the herb'
pali2 = 'Information school graduate seeks graduate school information'


def cleaner(string):
    string = string.lower()
    for i in punctuation:
        string = string.replace(punctuation, '').strip()
    string = string.split()
    return string


def ispali(string):
    string = cleaner(string)
    return string == string[::-1]


print(ispali(pali2))
# True
