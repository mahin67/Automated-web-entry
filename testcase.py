from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import  xlsxtoPython


#global declaration
driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8000/")

def action():

    z=len(xlsxtoPython.data)
    print(z)
    for i in range(0,z):
        name, dob, fname, mname, gen, add, cty, pin, cnty=xlsxtoPython.readDataFromExcel(i)
        print()
        webNameEntry(name)
        webDobEntry(dob)
        webFnameEntry(fname)
        webMnameEntry(mname)
        webGenEntry(gen)
        webAddEntry(add)
        webCtyEntry(cty)
        webPinEntry(pin)
        webCntyEntry(cnty)
        webSbtnClick()








def webNameEntry(a):
    time.sleep(2)
    name = driver.find_element_by_xpath(
        "/html/body/table/tbody/tr[1]/td[2]/input")
    name.send_keys(a)


def webDobEntry(a):
    time.sleep(2)
    name = driver.find_element_by_xpath(
        "/html/body/table/tbody/tr[2]/td[2]/input")
    name.send_keys(a)

def webFnameEntry(a):
    time.sleep(2)
    name = driver.find_element_by_xpath(
        "/html/body/table/tbody/tr[3]/td[2]/input")
    name.send_keys(a)

def webMnameEntry(a):
    time.sleep(2)
    name = driver.find_element_by_xpath(
        "/html/body/table/tbody/tr[4]/td[2]/input")
    name.send_keys(a)

def webGenEntry(x):
    time.sleep(2)
    if x == 'M':
        name = driver.find_element_by_xpath(
        "/html/body/table/tbody/tr[5]/td[2]/input[1]")
        name.click()
    elif x == 'F':
        name = driver.find_element_by_xpath(
        "/html/body/table/tbody/tr[5]/td[2]/input[2]")
        name.click()

def webAddEntry(a):
    time.sleep(2)
    name = driver.find_element_by_xpath(
        "/html/body/table/tbody/tr[6]/td[2]/textarea")
    name.send_keys(a)


def webCtyEntry(a):
    time.sleep(2)
    name = driver.find_element_by_xpath(
        "/html/body/table/tbody/tr[7]/td[2]/input")
    name.send_keys(a)

def webPinEntry(a):
    time.sleep(2)
    name = driver.find_element_by_xpath(
        "/html/body/table/tbody/tr[8]/td[2]/input")
    name.send_keys(a)

def webCntyEntry(a):
    time.sleep(2)
    name = driver.find_element_by_xpath(
        "/html/body/table/tbody/tr[9]/td[2]/input")
    name.send_keys(a)

def webSbtnClick():
    time.sleep(2)
    name = driver.find_element_by_xpath(
        "/html/body/table/tbody/tr[10]/td/input[1]")
    name.click()
