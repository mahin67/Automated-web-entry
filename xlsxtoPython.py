import pandas as pd

pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 300)
pd.set_option('display.max_columns', 300)


data = pd.read_excel(r'F:\IPDC_Internship\Main target project\mysite\media\Datasheet.xlsx',sheet_name="Sheet1")


def readDataFromExcel(i):

    name= data['Name'][i]
    dob = str(data['DOB'][i])
    fname = data['Fname'][i]
    mname = data['MName'][i]
    gen = data['Gender'][i]
    add = data['Address'][i]
    cty = data['Cty'][i]
    pin = int(data['Pin'][i])
    cnty = data['Cntry'][i]

    print(name,dob,fname,mname,gen,add,cty,pin,cnty)
    return  name,dob,fname,mname,gen,add,cty,pin,cnty

