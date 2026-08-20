# DICTIONARY Basic Exercises
# Word Count — Given a sentence, count how many times each word appears.
def word_count(sentences):
    words=sentences.lower().split()
    count={}
    for word in words:
        count[word]=count.get(word,0)+1
    return count
sentence="Hello how are you.I am fine and you "
print(word_count(sentence))

# Dictionary Reversal — Given {"a": 1, "b": 2}, create a new dict with keys and values swapped.

def dictionary_reversal(d):
    return {value: key for key,value in d.items() }
d={"Hello":1,"are":3,"you":4}
print(dictionary_reversal(d))

# Merge Two Dictionaries — Merge d1 and d2; if a key exists in both, sum the values.

merged={}
def merge_dict(d1,d2):
    for key,value in d1.items():
        merged[key]=value

    for key,value in d2.items():
        if key in merged:
           merged[key]=merged[key]+value
        else:
            merged[key]=value


d1={"hello":2,"b":4,"h":6}
d2={"l":3,"j":4,"r":7}
merge_dict(d1,d2)
print(merged)
        


# Find Max Value's Key — Given a dict of {name: score}, find the name with the highest score.
score_dict={"Ali":100,
            "Hamza":129,
            "ubaid":20
            }
maximum=max(score_dict.items(),key=lambda item:item[1])
print(maximum)

# Filter Dictionary — Given a dict of {item: price}, return only items priced above 50.
filter_dict={
    "bag":60,
    "hand karchief":100,
    "air pods":20,
    "napkin":70
}
filtered=dict(filter(lambda item:item[1]>50,filter_dict.items()))
print(filtered)

ddict={}
def filt(dict):
    for key,value in dict.items():
        if value >50:
            ddict[key]=value
        else:
            print("it is less then")

di={
    "bag":10,
    "car":60,
    "bike":100,
    "cycle":23
}
filt(di)
print(ddict)

# Dictionary from Two Lists — Given keys = ["a","b","c"] and values = [1,2,3], build a dictionary.
keys=["a","b","c"]
values=[1,2,3]
output_dict={}
for i in range(len(keys)):
    output_dict[keys[i]]=values[i]

print(output_dict)


# Character Frequency — Count frequency of each character in a string (ignore spaces).


count={}

def frequency(string):
    words=string.lower().split()
    for char in string:
        if string == "":
            continue
        count[char]=count.get(char,0)+1

string1="HELLO how are you is every thing is fine"
frequency(string1)
print(count)
        



    