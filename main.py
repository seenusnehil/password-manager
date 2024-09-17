from cryptography.fernet import Fernet

class passwordManager:
    
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}
    
    # fucntion to create a key to encrypt the passwords 
    def createKey(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)
    
    # function to load the key for decrypting the passwords     
    def loadKey(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()
      
    # function to import the password file in the given location  
    # either to create a new password file or to convert the existing 
    # password file in dictionary and store in here    
    def createPasswordFile(self, path, initialValues=None):
        self.password_file = path
        
        if initialValues is not None:
            for key, value in initialValues.items():
                self.addPassword(key, value)
     
     # function to load the password file with its passwords respectively           
    def loadPasswordFile(self, path):
        self.password_file = path
        
        with open(path, 'rb') as f:
            for line in f:
                try:
                    site, encrypted = line.decode('utf-8').strip().split(":")
                    self.password_dict[site.strip()] = Fernet(self.key).decrypt(encrypted.encode()).decode()
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
            
    # fucntion to add a new password to your password file    
    def addPassword(self, site, password):
        self.password_dict[site] = password
        
        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")
    
    # finally a function to get the saved password when you need it       
    def getPassword(self, site):
        return self.password_dict[site]
    
    def listAllPasswords(self):
        print('\n')
        for i in self.password_dict:
            print(f"{i}: {self.password_dict[i]}")
            

masterKey = "uneeslihens"
passKey = input("Enter the master key to process further: ")

if passKey == masterKey: 
    
    print("-------------------- Welcome your password manager --------------------")
    def main():
        
        # sample passwords just to test
        password = {}
        
        pm = passwordManager()
        
        print(""" What do you want to do?
            (1) Create a new key
            (2) Load an existing key
            (3) Create a new password file
            (4) Load an existing password file
            (5) Add a new password
            (6) Get a password
            (7) List all the stored passwords
            (q) Quit
            """)
        
        done = False
        
        while not done:
            
            choice = input("Enter your choice: ")
            if choice == "1":
                path = input("Enter path: ")
                pm.createKey(path)
                
            elif choice == "2":
                path = input("Enter path: ")
                pm.loadKey(path)
            
            elif choice == "3":
                path = input("Enter path: ")
                pm.createPasswordFile(path, password) 
                
            elif choice == "4":
                path = input("Enter path: ")
                pm.loadPasswordFile(path)
                
            elif choice == "5":
                site = input("Enter the site: ")
                password = input("Enter the password: ")
                pm.addPassword(site, password)
                
            elif choice == "6":
                site = input("What site you want password for: ")
                print(f"Password for {site} is: {pm.getPassword(site)}")
                
            elif choice == "7":
                pm.listAllPasswords()
            
            elif choice == "q":
                done = True
                print("Bye")
                
            else:
                print("Invalid choice!!!")
                
                
    if __name__ == "__main__":
        main()
        
else:
    print("Go away intruder!!!")
