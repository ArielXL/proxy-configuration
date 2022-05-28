# run it as sudo

'''
Three files will be modified
1) /etc/apt/apt.conf
2) /etc/environment
3) /etc/bash.bashrc
'''

# This files takes the location as input and writes the proxy authentication

import os
import sys
import shutil   # for copying file
import getpass  # for taking password input
import os.path  # for checking if file is present or not

apt_        = r'/etc/apt/apt.conf'
apt_backup  = r'./.backup_proxy/apt.txt'
bash_       = r'/etc/bash.bashrc'
bash_backup = r'./.backup_proxy/bash.txt'
env_        = r'/etc/environment'
env_backup  = r'./.backup_proxy/env.txt'


def write_to_apt(proxy, port, username, password, flag):
    '''
    This function directly writes to the apt.conf file
    '''
    filepointer = open(apt_, "w")
    if not flag:
        filepointer.write(
            f'Acquire::http::proxy "http://{username}:{password}@{proxy}:{port}/";\n')
        filepointer.write(
            f'Acquire::https::proxy "https://{username}:{password}@{proxy}:{port}/";\n')
        filepointer.write(
            f'Acquire::ftp::proxy "ftp://{username}:{password}@{proxy}:{port}/";\n')
        filepointer.write(
            f'Acquire::socks::proxy "socks://{username}:{password}@{proxy}:{port}/";\n')
    filepointer.close()


def write_to_env(proxy, port, username, password, flag):
    '''
    This function writes to the environment file. Fist deletes the 
    lines containng http:// , https://, ftp://
    '''
    # find and delete line containing http://, https://, ftp://
    with open(env_, 'r+') as opened_file:
        lines = opened_file.readlines()
        opened_file.seek(0)  # moves the file pointer to the beginning
        for line in lines:
            if r"http://" not in line and r"https://" not in line and r"ftp://" not in line and r"socks://" not in line:
                opened_file.write(line)
        opened_file.truncate()

    # writing starts
    if not flag:
        filepointer = open(env_, 'a')
        filepointer.write(
            f'http_proxy="http://{username}:{password}@{proxy}:{port}/"\n')
        filepointer.write(
            f'https_proxy="https://{username}:{password}@{proxy}:{port}/"\n')
        filepointer.write(
            f'ftp_proxy="ftp://{username}:{password}@{proxy}:{port}/"\n')
        filepointer.write(
            f'socks_proxy="socks://{username}:{password}@{proxy}:{port}/"\n')
        filepointer.close()


def write_to_bashrc(proxy, port, username, password, flag):
    # find and delete http:// , https://, ftp://
    with open(bash_, 'r+') as opened_file:
        lines = opened_file.readlines()
        opened_file.seek(0)
        for line in lines:
            if r"http://" not in line and r'"https://' not in line and r"ftp://" not in line and r"socks://" not in line:
                opened_file.write(line)
        opened_file.truncate()

    # writing starts
    if not flag:
        filepointer = open(bash_, "a")
        filepointer.write(
            f'export http_proxy="http://{username}:{password}@{proxy}:{port}/"\n')
        filepointer.write(
            f'export https_proxy="https://{username}:{password}@{proxy}:{port}/"\n')
        filepointer.write(
            f'export ftp_proxy="ftp://{username}:{password}@{proxy}:{port}/"\n')
        filepointer.write(
            f'export socks_proxy="socks://{username}:{password}@{proxy}:{port}/"\n')
        filepointer.close()


def set_proxy(flag):
    proxy, port, username, password = '', '', '', ''
    if not flag:
        proxy = input('Enter proxy : ')
        port = input('Enter port : ')
        username = input('Enter username : ')
        password = getpass.getpass('Enter password : ')
    write_to_apt(proxy, port, username, password, flag)
    write_to_env(proxy, port, username, password, flag)
    write_to_bashrc(proxy, port, username, password, flag)


def view_proxy():
    # finds the size of apt file
    size = os.path.getsize(apt_)
    if size:
        filepointer = open(apt_, 'r')
        string = filepointer.readline()
        print('\nHTTP Proxy: ' + string[string.rfind('@')+1 : string.rfind(':')])
        print('Port: ' + string[string.rfind(':')+1 : string.rfind('/')])
        print('Username: ' + string.split('://')[1].split(':')[0])
        print('Password: ' + '*' * len(string[string.rfind(':',0,string.rfind('@'))+1 : string.rfind('@')]))
        filepointer.close()
    else:
        print('No proxy is set')


def restore_default():
    '''
    Copy from backup to main
    ''' 
    shutil.copy(apt_backup, apt_)
    shutil.copy(env_backup, env_)
    shutil.copy(bash_backup, bash_)


def main():
    # create backup	if not present
    if not os.path.isdir('./.backup_proxy'):
        os.makedirs('./.backup_proxy')
        if os.path.isfile(apt_):
            shutil.copyfile(apt_, apt_backup)
        shutil.copyfile(env_, env_backup)
        shutil.copyfile(bash_, bash_backup)

    # choice
    print('Please run this program as super user(sudo)\n')
    print('1:) Set Proxy')
    print('2:) Remove Proxy')
    print('3:) View Current Proxy')
    print('4:) Restore Default')
    print('5:) Exit')
    choice = int(input('\nChoice (1/2/3/4/5) : '))

    if(choice == 1):
        set_proxy(flag=0)
    elif(choice == 2):
        set_proxy(flag=1)
    elif(choice == 3):
        view_proxy()
    elif(choice == 4):
        restore_default()
    else:
        sys.exit()

    print('\nDONE!')


if __name__ == "__main__":
    main()
