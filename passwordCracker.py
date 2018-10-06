import crypt

def testPass(cryptPass):
	salt = cryptPass[0:2]
	dictFile = open('diccionario.txt','r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word,salt)
		if (cryptWord == cryptPass):
			print "[+] Clave encontrada: "+word+"\n"
			return
	print "[-] Clave no encontrada.\n"
	return


def main():
	passFile = open('/etc/shadow')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print "[*] Clave crackeada para: "+user
			testPass(cryptPass)

if __name__ == "__main__":
	main()
