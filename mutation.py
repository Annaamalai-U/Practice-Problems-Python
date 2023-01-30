def mutate_string(string,pos,char):
    l=list(string)
    l[pos]=char
    string=''.join(l)
    return string
string=input()
inpt=input()
inpt=inpt.split(" ")
result=mutate_string(string,int(inpt[0]),inpt[1])
print(result)
