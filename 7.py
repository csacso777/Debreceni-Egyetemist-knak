def revi(szoveg):
	return szoveg[::-1]

def nospace(szoveg):
    for i in range(len(szoveg)):
        if szoveg.__contains__(" "):
            szoveg=szoveg.replace(" ","")
        if szoveg.__contains__(","):
            szoveg=szoveg.replace(",","")
        if szoveg.__contains__("."):
            szoveg=szoveg.replace(".","")
        if szoveg.__contains__("!"):
            szoveg=szoveg.replace("!","")
        if szoveg.__contains__("?"):
            szoveg=szoveg.replace("?","")
    return szoveg.lower()

def ha(X,a,b):
    if X[a]=="," or X[a]=="." or X[a]=="!" or X[a]=="!" or X[b-1]=="," or X[b-1]=="." or X[b-1]=="!" or X[b-1]=="?":
        return False
    else:
        return True

def palindromic(X):
	maxi=""
	for a in range(len(X)):
		for b in range(len(X),-1,-1):
			if nospace(X[a:b])==nospace(revi(X[a:b])) and len(X[a:b])>len(maxi) and ha(X,a,b):
				maxi=X[a:b]
	return maxi

X="Indul a gorog aludni!!!!!"
print(palindromic(X))
