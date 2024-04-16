birthyear=int(input("birthyear="))
def Favourite(birthyear):
    adolocent=birthyear+18
    if adolocent in range(1973,1987):
        return("Roger Moore")
    elif adolocent in range(1987,1995):
        return("Timothy Dalton")
    elif adolocent in range(1995,2006):
        return("Pierce Brosnan")
    elif adolocent in range(2006,2022):
        return("Daniel Craig")
    else:
        return("404 Not found")
print(Favourite(birthyear))