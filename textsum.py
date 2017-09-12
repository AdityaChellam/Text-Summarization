import re
import string

"""to count the words and their frequencies"""
frequency = {}
file1=open("textpara.txt","r+");
text_string = file1.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,25}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()

	
