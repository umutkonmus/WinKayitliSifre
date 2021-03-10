import subprocess
import time
 
HedefAg = str(subprocess.check_output(["netsh","wlan","show","profiles"]),"cp437").split("\n")
 
def FindNetwork():
    for i in HedefAg:
        if "All User Profile" in i:
            i = i.split(":")
            yield i[-1].strip()
 
Aglar = list(FindNetwork())
print(Aglar)
 
AgSec = input("Hedef ağın ismini girin :").strip()
if AgSec in Aglar:
    HefefBilgi = str(subprocess.check_output(["netsh","wlan","show","profiles",SelectNetwork,"key=clear"]),"cp437").split("\n")
    for p in HefefBilgi:
        if "Key Content" in p:
            p = p.strip().split(":")
            print("\nPassword :",p[-1].strip())
            break
else:
    print("Böyle bir ağ bulunamadı !")
    time.sleep(3)
