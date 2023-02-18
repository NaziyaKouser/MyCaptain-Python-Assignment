# Finding a frequency of a string 

def most_frequent(str):
    d={ }
    for i in str:
        if i not in d and i.isalpha():
            d[i]=0
        if i in d and i.isalpha():
            d[i]+=1
    D=dict(sorted(d.items(),key=lambda x:x[1], reverse=True))
    for i in D.items():
        print(i)
    
most_frequent('Mississippi')
