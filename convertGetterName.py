import re 
def convertGetterName(getName):
    if(getName[0:3] == "get"):
        words = re.findall(r'[A-Z](?:[a-z,0-9]+|[A-Z]*(?=[A-Z,0-9]|$))', getName[3:])
    else:
        words = re.findall(r'[A-Z](?:[a-z,0-9]+|[A-Z]*(?=[A-Z,0-9]|$))', getName)

    varName = ""
    for x in words:
        varName = varName + x + '_'
    
    return (varName[:-1])
#print("Enter getter function name -")
#fname = input()

#Test1
fname = "getEmp1Sal2019"
print("function Name:" + fname + '|' + "Variable Name:" + convertGetterName(fname))

#Test2
fname = "getEmpDeptName"
print("function Name:" + fname + '|' + "Variable Name:" + convertGetterName(fname))

#Test3
fname = "EmpDeptName"
print("function Name:" + fname + '|' + "Variable Name:" + convertGetterName(fname))

