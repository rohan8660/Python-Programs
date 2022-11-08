def createAnagramKey(string):
    key = ''
    for ch in sorted(string):
        key += ch
    return str(key)
 
 
def groupAnagramWords(data):
    group = dict()
    for ele in data:
        if group.get(createAnagramKey(ele)) == None:
            group[createAnagramKey(ele)] = [ele]
        else:
            group[createAnagramKey(ele)].append(ele)
    return group
 

data=words
anagram_grouped = groupAnagramWords(data)
 
anagram_grouped_list = list()
 
for k, v in anagram_grouped.items():
    anagram_grouped_list.append(v)
print(len(anagram_grouped_list))