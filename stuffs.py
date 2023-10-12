import os 
from colorama import Fore


class blackDox:
    def __init__(self):
        self.RED = Fore.RED
        self.GREEN = Fore.GREEN
        self.CYAN = Fore.CYAN
        self.YELLOW = Fore.YELLOW
        self.RESET = Fore.RESET
        self.MAGENTA = Fore.MAGENTA
    
    def banner(self):
        self.tux = """
       .--.
      |o_o |
      |:_/ |
     //   \ \\
    (|     | )
   /'\_   _/`\\
   \\___)=(___/

        .:. BlackDox - 0.1 .:.
    """
        print(self.tux)
        print(f'{self.RED}[{self.RESET}~{self.GREEN}] Tool Created by team Apocalypes {self.RESET}',end='\n\n')

    def makeItEasy(self):
        self.blackDox_art = """                                            
,-----.  ,--.              ,--.        ,------.   ,-----.,--.   ,--. 
|  |) /_ |  | ,--,--. ,---.|  |,-.     |  .-.  \ '  .-.  '\  `.'  /  
|  .-.  \|  |' ,-.  || .--'|     /     |  |  \  :|  | |  | .'    \   
|  '--' /|  |\ '-'  |\ `--.|  \  \     |  '--'  /'  '-'  '/  .'.  \  
`------' `--' `--`--' `---'`--'`--'    `-------'  `-----''--'   '--' 
"""

        
        print(f'{self.GREEN}{self.blackDox_art}',end = "")
        print(f'\t\t\t\t\t\t\t{self.RED}version 0.1 {self.RESET}')
        print(f"{self.YELLOW}[+]{self.RESET} {self.GREEN}Tool created by Apocalypse{self.RESET}")
        print(f"{self.RED}.:.{self.RESET}  {self.CYAN}Select any option:{self.RESET}")
        print(f"{self.YELLOW}[01]{self.RESET}{self.MAGENTA}internal{self.RESET} \t{self.YELLOW}[02]{self.MAGENTA}external{self.RESET}")
        print(f"{self.YELLOW}[03]{self.RESET}{self.MAGENTA}injection{self.RESET} \t{self.YELLOW}[04]{self.RESET}{self.MAGENTA}help{self.RESET}")
        print(f"{self.YELLOW}[00]{self.MAGENTA}exit{self.RESET}")


        self.choice = input(f"{self.RED}[{self.RESET}~{self.RED}]{self.RESET} {self.GREEN}Select an option:{self.RESET} ")
        if self.choice == "1" or self.choice == "01":
            self.target = input(f"{self.RED}[{self.RESET}~{self.RED}]{self.RESET} {self.GREEN}Target url:{self.RESET} ")
            os.system(f'nmap -A -vv -T4 {self.target} -oN reports/{self.target}.result')
            os.system(f'scripts/report_nmap {self.target}.result')



        elif self.choice == "2" or self.choice == "02":
            self.target = input(f"{self.RED}[{self.RESET}~{self.RED}]{self.RESET} {self.GREEN}Target :{self.RESET} ")
            os.system(f'wpscan --url {self.target} --random-user-agent -o reports/{self.target}.result')
        
        elif self.choice == "3" or self.choice == "03":
            self.target = input(f"{self.RED}[{self.RESET}~{self.RED}]{self.RESET} {self.GREEN}Target :{self.RESET} ")
            os.system(f'sqlmap -u {command} --dbs')
        
        elif self.choice == "4" or self.choice == "04":
            print('''
      .:. Black Dox help menu
    
    Current running version - 0.1
    help - To show the help command
    internal [target] - Scan internal networks / ports
    external [target] - Scan website
    injection [target] - check for sql injection attacks
    makeItEasy Converts terminal line into selection; Easy to operate
    exit - To exit the program              
''')
        elif self.choice == "00" or  self.choice == "0":
            print(f'[{self.YELLOW}!{self.RESET}] Have a good time {self.GREEN}Hax0r{self.RESET}')
            exit(0)
        
        else:
            print('command not recognized')


    def commandHandler(self,command):
        if 'exit' in command:
            print(f'[{self.YELLOW}!{self.RESET}] Have a good time {self.GREEN}Hax0r{self.RESET}')
            exit(0)
        
        elif 'help' in command:
            print('''
      .:. Black Dox help menu
    
    Current running version - 0.1
    help - To show the help command
    internal [target] - Scan internal networks / ports
    external [target] - Scan website
    injection [target] - check for sql injection attacks
    makeItEasy Converts terminal line into selection; Easy to operate
    exit - To exit the program              
''')
            



        elif 'internal' in command:
            try : 
                command = command.split(' ')[1]
                os.system(f'nmap -A -vv -T4 {command} -oN reports/{command}.result')
                os.system(f'scripts/report_nmap {command}.result')

            except:
                print(f'{self.CYAN}[{self.RED}~{self.GREEN}]{self.RED}Target not found !!!')
                print(f'{self.CYAN}[{self.YELLOW}?{self.GREEN}]{self.YELLOW}Target : {self.RESET}',end='')
                command = input()
        elif 'external' in command:
            try : 
                command = command.split(' ')[1]
                #print(f'{command}')
                os.system(f'wpscan --url {command} --random-user-agent')
            except:
                print(f'{self.CYAN}[{self.RED}~{self.GREEN}]{self.RED}Target not found !!!')
                print(f'{self.CYAN}[{self.YELLOW}?{self.GREEN}]{self.YELLOW}Target : {self.RESET}',end='')
                command = input()
        elif 'makeItEasy'in command or  'makeiteasy'in command:
            self.makeItEasy()
        elif 'injection' in command:
            command = command.split(' ')[1]
            os.system(f'sqlmap -u {command} -D acuart --tables')
        else:
            pass

