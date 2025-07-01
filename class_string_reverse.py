k = input("Enter your string to reverse: ")

class String_reverse():

    def __init__(self):
        pass
    
    def reverse_String(self, str):
       self.str = str
       reversed_string = str[::-1]
       return reversed_string
    
        
obj = String_reverse()
print(obj.reverse_String(k))
   




