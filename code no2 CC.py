import random                       

def password(length):  
  
    
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"  
  
     
    selected_char = random.sample(list_of_chars, length)  

    pass_r= "".join(selected_char)  
      
    return pass_r
  

if __name__ == "__main__":  
    
    length = int(input("Enter the length of the Password: "))  
  
    pass_r=password(length)  
  
    print("Your Randomly Generated Password is:", pass_r)  
    