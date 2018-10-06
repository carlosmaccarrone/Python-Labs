# Este programa determina si un servidor ofrece
# inicios de sesión anónimos

import ftplib
def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous', 'me@your.com')
		print '\n[*] ' + str(hostname) +\
			' FTP Anonymous Logon Succeeded.'
		ftp.quit()
		return True
	except Exception, e:
		print '\n[-] ' + str(hostname) +\
			' FTP Anonymous Logon Failed.'
		return False

host = 'host231.181-105-85.telecom.net.ar'

anonLogin(host)
