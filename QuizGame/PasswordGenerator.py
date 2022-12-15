from cryptography.fernet import Fernet

print('welcome to the password generator!')

def generateEncryptKey(password):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    
    encodeString = fernet.encrypt(password.encode())

    return encodeString


def decruptKey(key1):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    
    decruptString = fernet.decrypt(key1).decode()
    
    return decruptString


while True:

    try:
        userinput=  input('Do you want to generate user and password or view your own password \n press new for the new user and old for existing user')
    except:
        print('invalid userInput!')
        continue
    else:
        if userinput.lower() == 'new':
            
            username = input('Enter the username \n')
            password = input('Enter password \n')

            with open('password.txt','a') as file:
                file.write(f'username: {username} | password: {password}')
            with open('encryptfile.txt','a') as file:
                file.write(f'username: {username} | password: {generateEncryptKey(password)}')
            break
        if userinput.lower() == 'old':

            with open('encryptfile.txt','r') as file:
                for i in file.readlines():
                    print(i)
                    '''data = i.strip()
                    print(data)
                    user,password = data.split('|')
                    passw = (password.split(':')[1].strip())
                    print(passw)
                    res = passw.replace('b','')
                    res = res.replace("'","")
                    res = bytes(res,'UTF-8')
                    print(res)
                    print(type(res))
                    print(f'username: {user} | password: {decruptKey(res)} ')
                    '''
            break

