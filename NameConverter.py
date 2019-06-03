import re 

class NameConverter:
    def convertGetterName(self,getName):
        if(getName[0:3] == "get"):
            words = re.findall(r'[A-Z](?:[a-z,0-9]+|[A-Z]*(?=[A-Z,0-9]|$))', getName[3:])
        else:
            words = re.findall(r'[A-Z](?:[a-z,0-9]+|[A-Z]*(?=[A-Z,0-9]|$))', getName)

        varName = ""
        for x in words:
            varName = varName + x + '_'
        
        return (varName[:-1])

if __name__ == "__main__":
    name1 = NameConverter()
    print (name1.convertGetterName("getEmpName"))