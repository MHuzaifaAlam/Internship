# Basic Exercises
# Word Count — Given a sentence, count how many times each word appears.
def word_count(sentence):
    words=sentence.lower().split()
    count={}
    for word in words:
        count[word]=count.get(word,0)+1
    return count

sentence="there is an man who love his wife"
print(word_count(sentence))

# Dictionary Reversal — Given {"a": 1, "b": 2}, create a new dict with keys and values swapped.
# Merge Two Dictionaries — Merge d1 and d2; if a key exists in both, sum the values.
# Find Max Value's Key — Given a dict of {name: score}, find the name with the highest score.
# Filter Dictionary — Given a dict of {item: price}, return only items priced above 50.
# Dictionary from Two Lists — Given keys = ["a","b","c"] and values = [1,2,3], build a dictionary.
# Character Frequency — Count frequency of each character in a string (ignore spaces).

