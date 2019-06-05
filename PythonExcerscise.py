import re 
import logging as log

class NameConverter:
    def convertGetterName(self,getName):
        """
            This functions convert input getterMethod to '_' separated string 
            based on camel case words in input sting.
        """
        try:
            if(getName[0:3] == "get"):
                words = re.findall(r'[A-Z,0-9](?:[a-z,0-9]+|[A-Z,0-9]*(?=[A-Z,0-9]|$))', getName[3:])
            else:
                words = re.findall(r'[A-Z][0-9](?:[a-z,0-9]+|[A-Z]*(?=[A-Z,0-9]|$))', getName)

            varName = ""
            for x in words:
                varName = varName + x + '_' 
            
            #remove last '_'
            return (varName[:-1].lower())
        except:
            raise Exception("Error")
#call main  
if __name__ == "__main__":
    #in case we need to log warnings or debug
    log.warning("inside main...")
    
    #create an object
    nconv = NameConverter()
    
    print ("Input getterMethod name - ",end='')
    name = input()
    print ("Variable Name should be - " + nconv.convertGetterName(name))

