import sys
import re

stem_word = ["the","a","an","was","is","are","of"]
weight={}
max_heap=[tuple()]
heap_size = 0
def insert(weight_set):
    max_heap.append(weight_set)
    swim()
def swim():
    index = len(max_heap)-1
    while (index > 1 and max_heap[(index)//2][0]< max_heap[index][0]):
        swap((index)//2,index)
        index = (index)//2
    return
def sink(n):
    right_index = 2*n+1
    left_index = 2*n
    source = n
    if (right_index<(len(max_heap)-1) and max_heap[right_index][0]>max_heap[source][0]):
        source = right_index
    if (right_index<(len(max_heap)-1) and max_heap[left_index][0]>max_heap[source][0]):
        source = left_index
    if (source != n):
        swap(n,source)
        sink(source)
    return
def swap(a,b):
    max_heap[a],max_heap[b]=max_heap[b],max_heap[a]
def pop():
    index = len(max_heap)-1
    val = max_heap[1]
    max_heap[1] = max_heap[index]
    del max_heap[index]
    sink(1)
    return val

min_heap=[tuple()]
def insert1(weight_set):
    min_heap.append(weight_set)
    swim1()
def swim1():
    index = len(min_heap)-1
    while (index > 1 and min_heap[(index)//2][0]> min_heap[index][0]):
        swap1((index)//2,index)
        index = (index)//2
    return
def sink1(n):
    right_index = 2*n+1
    left_index = 2*n
    source = n
    if (right_index<(len(min_heap)-1) and min_heap[right_index][0]<min_heap[source][0]):
        source = right_index
    if (right_index<(len(min_heap)-1) and min_heap[left_index][0]<min_heap[source][0]):
        source = left_index
    if (source != n):
        swap1(n,source)
        sink1(source)
    return
def swap1(a,b):
    min_heap[a],min_heap[b]=min_heap[b],min_heap[a]
def pop1():
    index = len(min_heap)-1
    val = min_heap[1]
    min_heap[1] = min_heap[index]
    del min_heap[index]
    sink1(1)
    return val

if __name__=='__main__':
    file1=open("textpara.txt","r+");
    text_string = file1.read().lower()
    match_pattern = re.findall(r'\b[a-z]{3,25}\b', text_string)

for word in match_pattern:
        count = weight.get(word,0)
        weight[word] = count + 1
    frequency_list = weight.keys()
    for words in frequency_list:
        print(words, weight[words]/sum(weight.values()))
    file1.close()

print("\n\nPART 2")
    file1=open("textpara.txt","r+");
    sentence = file1.read().lower().split()
    for word in sentence:
        if word[-1]==".":
            print(word)
    file1.close()

local_sentence= []
    weight_sentence=0
    for word in sentence:
        if word[-1]==".":
            if (word in stem_word):
                pass
            else:
                weight_sentence+=weight[word[0:-1]]
            local_sentence.append(word)
            insert(tuple((weight_sentence," ".join(local_sentence))))
            weight_sentence=0
            local_sentence = []
        else:
            if (word in stem_word):
                pass
            else:
                count+=weight.get(word,0)
                weight_sentence+=count
                weight[word]=count
            local_sentence.append(word)
    print(max_heap)

for _ in range(len(max_heap//3)):
        insert1(pop())

for i in range(len(min_heap)-1):
        print(pop1()[1].capitalize()," ")
