import sys
from os import path, system as cmd
from configparser import ConfigParser
import easygui


cmd('cls')


class CITLite():
    def __init__(self) -> None:
        pass



    def run(self):
        cmd('cls')
        print('Starting task...\n')
        self.ini_file = easygui.fileopenbox('Select the ini file to split.', 'Cyberpunk INI Tool', filetypes='(*.ini)', multiple=False)
        if path.exists(self.ini_file):

            ini_name_list = self.ini_file.split('/')
            ini_name = ini_name_list[::-1][0]
            ini_path = ''
            for y in range(len(ini_name_list)-1):
                ini_path = ini_path + ini_name_list[y] + '/'

            print('Task started!\n')

            print(f'Reading file {ini_name}...\n\n')
            cp = ConfigParser()
            cp.read(self.ini_file)

            print('Getting the session and key names...')
            file_count = 0
            for x in range(len(cp.sections())):

                print(f'\n\nSession {x}: [{cp.sections()[x]}]\n')
                ini_data = ConfigParser()
                ini_data[cp.sections()[x]] = {}
                key_names = [op for op in cp[cp.sections()[x]]]

                for y in range(len(key_names)):

                    print(f'Key {y}: {key_names[y]} | Value: {cp[cp.sections()[x]][key_names[y]]}\n')
                    ini_data[cp.sections()[x]][key_names[y]] = cp[cp.sections()[x]][key_names[y]]
            
                print(f'\nWriting a new ini file ({ini_name}_[{str(x)}].ini)...\n')
                with open(path.join(ini_path, f'{ini_name}_[{str(x)}].ini'), 'w') as config_file:
                    ini_data.write(config_file)
                print(f'File ({ini_name}_[{str(x)}].ini) saved!')
                file_count = file_count + 1
            
            print(f'\n\nTask completed successfully!\nTotal files: {file_count}')

            msg = easygui.boolbox(f'Your .ini file has been successfully split into a total of {file_count} files, do you want to delete the original file?', 'Cyberpunk INI Tool - Lite Version', ('[Y]es', '[N]o'), default_choice='[Y]es', cancel_choice='[N]o')

            if msg:
                cmd(f'del "{self.ini_file}"')
        else:
            print("The file does not exist, please check again!")
 


    def check(self):

        msg = easygui.boolbox(f'Split another file or close the program?', 'Cyberpunk INI Tool - Lite Version', ('[S]plit Another File', '[C]lose'), default_choice='[S]plit Another File', cancel_choice='[C]lose')
        
        return msg