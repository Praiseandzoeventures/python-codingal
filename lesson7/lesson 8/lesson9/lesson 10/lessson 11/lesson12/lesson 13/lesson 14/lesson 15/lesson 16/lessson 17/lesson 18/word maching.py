def match_words(words):
    ctr=0
    Ist=[]
    
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr =ctr+1
            Ist.append(word)
            print("the list of words who have length greater than 1 and whose first and last element is same",Ist)
            return ctr 
        count=match_words(["abc","cfc","xyz","1221"])
        print("number of words having Ist and  last  character same:",count)