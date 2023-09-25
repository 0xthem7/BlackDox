from stuffs import blackDox as bd

blackDox = bd()

blackDox.banner()


while True:
    print(f'blackDox {blackDox.CYAN}~{blackDox.RESET} ',end='')
    command = input()
    if command == 'makeItEasy':
        while True:
            blackDox.makeItEasy()
    blackDox.commandHandler(command)
    


