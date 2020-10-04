def name_in_str(str, name):
    word, j = "", 0
    for i in range(len(str)):
        if j<=len(name)-1 and str[i].lower()==name[j].lower():
            word+=str[i]
            j+=1
    return word.lower()==name.lower()
