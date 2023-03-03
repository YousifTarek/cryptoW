import Crypto
from cryptography.fernet import Fernet

choice = input("here are the choices:\n 1.encrypt a file \n 2.decrypt a file \n")

if int(choice) == 1:

     file = input('name of the target file: ')
     file_key = input('the name of the key file:')
     key = Fernet.generate_key()

     with open(file_key,'wb'): #create the file if it doesn't exist
          pass

     with open(file,'rb') as File: #gets the text to encrypt
          text = File.read()


     with open(file_key,'wb') as key_file: #save the key
          key_file.write(key)
     
     with open(file_key,'rb') as key_file: #gets the saved key
          key = key_file.read()



     f = Fernet(key)

     encrypted = f.encrypt(text)

     with open(file,'wb') as encr: #encrypt the file
          encr.write(encrypted)

else:

     file = input('name of the target file:')
     key = input('name of the key file:')
     with open(key,"rb") as Key:
        key = Key.read()
     f = Fernet(key)

     with open(file,'rb') as encrypted:
        decrypted =  f.decrypt(encrypted.read())
     with open(file,"wb") as final:
          final.write(decrypted)

# made by Yousif Tarek 
