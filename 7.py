def revi(szoveg):
	return szoveg[::-1]

def nospace(szoveg):
	for i in range(len(szoveg)):
		if szoveg.__contains__(" "):
			szoveg=szoveg.replace(" ","")
	return szoveg
def palindromic(X):
	maxi=""
	for a in range(len(X)):
		for b in range(len(X),-1,-1):
			if nospace(X[a:b])==nospace(revi(X[a:b])) and len(X[a:b])>len(maxi):
				maxi=X[a:b]
	return maxi

X="Indul a gorog aludni" #Nagybetűt nem veszi külön de egy lower gondolom mindent megold
print(palindromic(X))
