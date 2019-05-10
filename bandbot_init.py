from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

import param

def loginRefresh(doSilent):
	chromeOptions = {"debuggerAddress":"127.0.0.1:"+param.ChromeDevPort}
	capabilities = {"chromeOptions":chromeOptions}
	print("Driver initializing...")
	driver = webdriver.Remote("http://127.0.0.1:"+param.WebdriverPort, capabilities)
	print("Driver initialized.")
	driver.get(param.chatURL)
	print("Driver get completed.")
	print("Commencing Sleep.....")
	sleep(1)
	print("Commencing Sleep....")
	sleep(1)
	print("Commencing Sleep...")
	sleep(1)
	print("Commencing Sleep..")
	sleep(1)
	print("Commencing Sleep.")
	sleep(1)
	print("[" + param.NAME + "] " + param.version + " boot success")
	msgWrite = driver.find_element_by_class_name("commentWrite")
	if not doSilent:
		msgWrite.send_keys("[" + param.NAME + "] " + param.version + " login success")
		msgWrite.send_keys(Keys.ENTER)
	return driver, msgWrite

if __name__ == "__main__":
	chromeOptions = {"debuggerAddress":"127.0.0.1:9222"}
	capabilities = {"chromeOptions":chromeOptions}
	print("Driver initializing...")
	driver = webdriver.Remote("http://127.0.0.1:33333", capabilities)
	print("Driver initialized.")

	driver.get(chatURL)
	print("Get login page completed.")
	driver.find_element_by_css_selector(".uBtn.-icoType.-phone").click()
	print("Get PhonenumberPage completed.")
	Phonenumber = input("전화번호 입력 :")
	driver.find_element_by_id("input_local_phone_number").send_keys(Phonenumber)
	driver.find_element_by_css_selector(".uBtn.-tcType.-confirm").click()
	print("Get PasswordPage completed.")
	Password = input("비밀번호 입력 :")
	driver.find_element_by_id("pw").send_keys(Password)
	driver.find_element_by_css_selector(".uBtn.-tcType.-confirm").click()
	print("Get SMSPage completed.")
	driver.find_element_by_css_selector(".uBtn.-tcType.-confirm.gMat28").click()
	print("Get SMSWaitPage completed.")
	pw_band=input("인증번호: ")
	driver.find_element_by_id("code").send_keys(str(pw_band))
	driver.find_element_by_css_selector(".uBtn.-tcType.-confirm").click();
	print("Driver get completed.")
	print("Commencing Sleep.....")
	sleep(1)
	print("Commencing Sleep....")
	sleep(1)
	print("Commencing Sleep...")
	sleep(1)
	print("Commencing Sleep..")
	sleep(1)
	print("Commencing Sleep.")
	sleep(1)
	print("[" + param.NAME + "] " + param.version + " boot success")
	msgWrite = driver.find_element_by_class_name("commentWrite")