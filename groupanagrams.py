words=["cat", "silent", "listen", "kitten", "salient"]


lettermap=[[0*26]*len(words)]
for i in range(len(words)):
    for j in words[i]:
        lettermap[i][ord(j)-97]=1;
        
