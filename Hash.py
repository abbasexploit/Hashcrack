
import hashlib
import Banner
import pyfiglet
def banner():
    abbas = pyfiglet.figlet_format('@abbas.exploit', font= 'big')
    print (abbas)
    print("-----------------------------------------------------------------------------------------------")
banner()
hashvalue = input ("Enter is name : ")
hashob1 = hashlib.md5()
hashob1.update(hashvalue.encode())
print (hashob1.hexdigest())
