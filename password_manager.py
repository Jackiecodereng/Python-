# to organize and store your passwords
#pass command does nothing but prevents indetation errors
# with automatically closes the file for us after use
# w means create a new file,r mean just reads the file no edit, a means u  can add anything belowto existing file and create a new file
from os import write

from cryptography.fernet import Fernet
master_pwd = input('what is the master password?')
#key +password+text to encrypt =random text
#random text +key+password =text to encrypt
# use it only once
# def write_key():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as key_file:
#         key_file.write(key)

# write_key()

def view():
    with open('passwords.txt', 'r') as f:
      for line in f.readlines():
          data = line.rstrip()
          user, passw = data.split('|')
          print('user:',user,',Password:',passw)

          # print(line.rstrip()) # rstrip removes the carriage trip/n
def add():
    name = input('Account name')
    pwd = input('Password')

    with open('passwords.txt','a') as f:
          f.write(name +'|'+pwd + '\n')

while True:
   mode= input('would you like to add a new passsword or view existing ones(view/add),press q to quit:')
   if mode == 'q':
       break
   if mode == 'view':
       view()
   elif mode == 'add':
       add()
   else:
       print('invalid mode')
       continue

print('wishing you a merry xmas')

# to encrypt passwords in termina
#pip install cryptography