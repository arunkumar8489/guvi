jk=input()
if((jk>='a' and jk<='z')or(jk>='A' and jk<='Z')):
    if(jk=='a' or jk=='A' or jk=='e' or jk=='E' or jk=='i' or jk=='I' or jk=='o' or jk=='O' or jk=='u' or jk=='U'):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")        
        
