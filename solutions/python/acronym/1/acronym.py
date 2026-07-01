def abbreviate(words):
    words = words.replace("-", " ").replace("_", " ")
    word_list = words.split()
    acronym = "".join(word[0].upper() for word in word_list)
    return acronym
