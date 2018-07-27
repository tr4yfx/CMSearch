import requests
import time
import os,sys
import vulners



def main():
	os.system("clear")
	print("""
 _____ ___  ___ _____                           _    
/  __ \|  \/  |/  ___|                         | |    
| /  \/| .  . |\ `--.   ___   __ _  _ __   ___ | |__  
| |    | |\/| | `--. \ / _ \ / _` || '__| / __|| '_ \ 
| \__/\| |  | |/\__/ /|  __/| (_| || |   | (__ | | | |
 \____/\_|  |_/\____/  \___| \__,_||_|    \___||_| |_|
                                                                                                        
Criado por Tr4yfx

EXEMPLO:

==> python3 cmsearch.py http://www.site.com
		""")
main()
if len(sys.argv) <2:
	main()
	sys.exit(0)
def cms(site):
	cmss = {
	"/user/login/":"Drupal!",
	"/administrator/index.php":"Joomla!",
	"/wp-login.php":"WordPress!",
	"/admin/login.php":"OpenCart!"
}

	time.sleep(1)

	try:
	    print("[*] Target: {}".format(site))
	    test = requests.get(site)
	    if(test.status_code==200):
	        print("[*] Status: 200 OK")
	        print("[*] Procurando CMS...")
	        for x in cmss:
	    	    r = requests.get(site+x)
	    	    if(r.status_code==200):
	    		    print("[*] CMS Encontrado!\n[*] CMS: "+cmss[x])
	    		    time.sleep(1)
	    		    api = vulners.Vulners()
	    		    busca = api.search(cmss[x],limit=10)
	    		    for y in busca:
	    			    time.sleep(1)
	    			    print("\n[*] Title: {}".format(y['title']))
	    			    print("[*] ID: {}".format(y['id']))
	    			    print("[*] Href: {}".format(y['href']))
	    
	except:
		print("[*] ERRO! Verifique se o site está correto.")

web = str(sys.argv[1])
cms(web)