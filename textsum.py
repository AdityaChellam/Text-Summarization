import re
import string

frequency = {}
file1=open("textpara.txt","r+");
text_string = file1.read().lower()
match_pattern = re.findall(r'\b[a-z]{4,25}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    print(words, frequency[words])

sentence = file1.read().lower()



