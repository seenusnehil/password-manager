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
        password = {
            'LinkedIn': 'aY.V9&^a)b:.6sQ',
            'The Linux Foundation': '*X58pCPf4LAdUuP',
            'Oracle': 'QcDGw?5K*S-655n',
            'Goldman Sachs': 'Z7mSQyCmNZ_z6!Y',
            'Angel List': 'YN%ySsx-L+fEp3e',
            'Indeed': 'fs%.8i6_9L!.h*X',
            'ICPC': 'd*bPuC9KbY6*+ar',
            'AICTE Internship': 'VcC@nSrBLeT2d3b',
            'BlackHat Usa': '@bbYm.FFq8!ASBm',
            'New email': 'aA@0b74b00174d11f5e6',
            'IBM Job Application': '_Ea-zp82iJ6kfmQ',
            'Amazon University recruiting': '=TRyrEZFK4t-8Qm/ b.5#%cRq72j6@CQ',
            'Amazon Jobs': '_DgwYCP,sdG$7c8',
            'Apple jobs ID': 'cTj6v6D.2JDEvux',
            'HP Jobs': '62afZXnt-j7ZuqE',
            'ThemeSoft Jobs': 'sFTWNzeRfb6kYSX@',
            'Goldman Sachs Job': 'rAh%G-ZSZX2D7sh',
            'Cadence Jobs': 'J7Ec.qxGTUQEAir',
            'IEEE Account': 'h3k+NSt,m&Y3C2M',
            'GSK Jobs Portal': 'jB:-RJF6!NcU8eN',
            'Helwett Packard Enterprise Jobs': 'w:k9Lujf.E4TCwB',
            'DeepLearning.ai': 'pwgQBm7Kc.p8wcq',
            'Salesforce jobs': 'Snehilseenu@2001',
            'Baker Hughes': 'Ap6:uHrZ9RtV83Q',
            'MITACS Globalink': 'gxQ32bW_Ue9mnDf',
            'Samsung Prism R&D': 'b8qBJPUg@R528wF',
            'Outreachy': '2.x2i**wJ!Tw9RR',
            'P&G jobs': 'hw7eT:afbEH3eSP',
            'intel': ':tVatmsdskwZ!H9',
            'Instagram': 'Wanttobethebestcoder@2026',
            'Boston Consulting Group': 'NXZkuXK$A?6Vw9W',
            'IOB Mobile banking app passcode': '741195',
            'IOB mPin (for transactions)': '151263',
            'Adobe Careers': 'UV6A-367rWG.zQu',
            'Morgan Stanley Careers': 'dKxJ-7tdVz@w#f4',
            'City Bank Careers': 'LfvDgX3.cnYV9Qd',
            'Linktree': '32!q5?BRjNC7VSu',
            'AWS DeepRacer': 'Snehilseenu@2001',
            'Upwork': 'ru*tvJ.Zk#+N9_J',
            'Trellix Careers': 'J:b5Zwm3yB4dvU6',
            'Apple Careers': '6sGNb.NEEwFuWpL',
            'PIMCO Careers': '5iaC5s:z_VhTVeH',
            'COX Automotive': '8JqhdzuLfVYzB-5',
            'MasterCard': '6_idWeYqa-ZK!8N',
            'Bloomberg': 'iqjs*4QUbvne8?V',
            'VISA careers (Smartr)': '2z.E.wj?DyD-6#p',
            'PyCon': 'UG9VR78Rd2J8RZG',
            'IQVIA': 'JwWD4A!3Gqc-Nrz',
            'ETS GRE': 'm5P./Sz8$i.QgG# , y4VB#.3z?38cNBA',
            'cal.com': 'Duu92dsgAJbBDBv',
            'AWS account password': '+hxRLCR!#nW3hmy',
            'Datacamp': 'A*2iSBM7HD4#gr3',
            'SAP Careers': 'Y8b247/c9LMGM-7',
            'ArcGIS': '9._YF5c7aD?Buwb',
            'Discord new password (17.06.2023)': 'Thisismysafediscord@2023',
            'Reddit password': 'NQ-7-%!Vivy+nQ,',
            'Max Plank Society (Internship)': 'TTMxH9@QLnWyVUr',
            'HuggingFace': 'nrEa;^4rqV%7d&5',
            'Uni-assist': '+XvLc3wD7eCY@Bv',
            'Workday(Atkins)': 'Lrk!.tg3_rqvX68',
            'Workday(ASML)': 'SvLE.x85!36Mv6Y'
        }
        
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