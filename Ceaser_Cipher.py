Alpha="abcdefghijklmnopqrstuvwxyz"
def ceaser_encrypt(s,key):
    n=len(s)
    s=s.lower()
    cipher=""
    for i in range(n):
        intval=0
        keyval=0
        if s[i] in Alpha:
            intval=Alpha.find(s[i])
            keyval=(intval+key)%26
            cipher=cipher+Alpha[keyval]
        else:
            cipher=cipher+s[i]
    return cipher
def ceaser_decrypt(s,key):
    n=len(s)
    s=s.lower()
    plain=""
    for i in range(n):
        intval=0
        keyval=0
        if s[i] in Alpha:
            intval=Alpha.find(s[i])
            keyval=(intval-key)%26
            plain=plain+Alpha[keyval]
        else:
            plain= plain+s[i]
    return  plain
def brute_force(s):
    res=[]
    for i in range(1,26):
        op_str=ceaser_encrypt(s,i)
        res.append(op_str)
    return res
def freq_analysis(s,letter,replace):
    if letter in s and replace in Alpha:
        st_val=Alpha.find(letter)
        ed_val=Alpha.find(replace)
        keyval=st_val-ed_val
        result=ceaser_decrypt(s,keyval)
        return result
    else:
        if letter not in s:
            return "Character NOT IN the Cipher"
        else:
            return "Enter the CORRECT ALPHABET"
print("CEASER-CIPHER ALGORITHM....")
print("Enter 1 for ENCIPHERMENT")
print("Enter 2 for DECIPHERMENT")
print("Enter 3 for BRUTE-FORCE ANALYSIS")
print("Enter 4 for FREQUENCY-ANALYSIS ATTACK")
while(True):
    opt=int(input("Enter your OPTION:"))
    if opt==1:
        plain=input("Enter the Plain-Text:")
        key=int(input("Enter the Key Value:"))
        if key>0 and key<26:
            result=ceaser_encrypt(plain,key)
            print("Encrypted Message:",result)
        else:
            print("Key should be between 1 and 25")
    elif opt==2:
        cipher=input("Enter the Cipher-Text:")
        key=int(input("Enter the Key Value:"))
        if key>0 and key<26:
            result=ceaser_decrypt(cipher,key)
            print("Decrypted Message:",result)
        else:
            print("Key should be between 1 and 25")
    elif opt==3:
        cipher=input("Enter the Cipher-Text:")
        res=brute_force(cipher)
        print(res)
    elif opt==4:
        cipher=input("Enter the Cipher-Text:")
        letter=input("Letter to be REPLACED:")
        replace=input("REPLACING Letter:")
        result=freq_analysis(cipher,letter,replace)
        print(result)
    else:
        print("Enter a Vaild Option!!!")
    print("Enter 0 to CONTINUE")
    print("Enter any to BREAK")
    choice=(input("Enter your choice:"))
    print("------------------")
    if(int(choice)==0):
        pass
    else:
        break