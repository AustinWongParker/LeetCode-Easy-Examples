class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]", 4)      
        
        # Code is much simpler than I initially thought, all you have to do is use .relace - no need for for loops
        
        
        
        '''
        dot = "."
        defang_addr = ""
        for x in address:
            if dot in x:
                index(dot)
                address[:dot] + "[" + address[dot:] + "]"
        print(address)
                
        '''