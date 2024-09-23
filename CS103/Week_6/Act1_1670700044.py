sentence = input("Enter a sentence : ")
vowel = 0 #สระ
digit = 0 #ตัวเลข
consonant = 0 #พยัญชนะ
vlist = ['A','E','I','O','U']
for i in sentence :
    if i.upper() in vlist :
        vowel = vowel + 1
    elif i >= '0' and i <= '9' :
        digit = digit + 1
    elif i.upper() >='A' and i.upper() <="Z" :
        consonant = consonant + 1 # consonant += 1 
print("Character = " , len(sentence))
print(f"Vowel = {vowel}")
print("Digit = ",digit)
print("Consonant = ",consonant)