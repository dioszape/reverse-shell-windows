import os
import time

os.system("clear")

logo = '''
     ____       __        __         
    / __ \_____/ /_____ _/ /_  ____ _
   / / / / ___/ __/ __ `/ __ \/ __ `/
  / /_/ / /__/ /_/ /_/ / /_/ / /_/ / 
 /_____/\___/\__/\__,_/_.___/\__,_/  

Git Hub > @zapeee & @t3l3machus
'''

while True:
    print(logo)
    print('Menu:')
    print('')
    print('1. Start')
    print('')
    print('2. Update and Upgrade')
    print('')
    print('3. Docker')
    print('')
    print('4. Exit')
    print('')
    choice = input('Select an option > ')

    if choice == '1' or choice.lower() == 'y':
        if not os.path.exists('requirements.txt'):
            print('File requirements.txt not found')
        else:
            os.system('pip install -r requirements.txt')

        os.system('python3 Py/generatecode.py')

        print('Redirecting to session...')
        time.sleep(5)

        print("")

        os.system('python3 Py/session.py')

    elif choice.lower() == 'update' or choice.lower() == 'upgrade' or choice == '2':
        print('Updating and upgrading...')
        os.system('sudo apt update && sudo apt upgrade -y')
        print('Update and upgrade complete!')

    elif choice.lower() == 'docker' or choice == '3':
        os.system('sudo cat Dockerfile')

    elif choice.lower() == 'exit' or choice == '4':
        print('Exiting...')
        break

    else:
        print('Invalid option!')
