'''Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line.'''

def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2))  # Union of both words

def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))  # Intersection of both words

def letters_in_either_but_not_both(word1, word2):
    return sorted(set(word1) ^ set(word2))  # Symmetric difference between both words

word1 = "cheese"
word2 = "seesaw"

print(f"Letters in either word: {letters_in_either(word1, word2)}")
print(f"Letters in both words: {letters_in_both(word1, word2)}")
print(f"Letters in either but not both: {letters_in_either_but_not_both(word1, word2)}")
