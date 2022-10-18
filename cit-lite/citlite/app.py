from os import path, mkdir, system as cmd
from configparser import ConfigParser
from easygui import buttonbox, fileopenbox, msgbox, ynbox, exceptionbox

class CyberpunkINITool():

    def __init__(self, app_name) -> None:
        self.app_name = app_name
        self.mainwindow_res = ''
        self.run('start', True)

    def mainWindow(self):
        self.mainwindow_res = ynbox(
        msg="""TUTORIAL

        1. Click "Select File".

        2. Browse for the ini file you want to split and click open.

        3. If you choose to backup the original file,
           it will be saved inside the "backups" folder,
           located in the root folder of this program.
           (The folder will be created automatically if it does not exist.)
        """,
        title=f'{self.app_name} - Home',
        choices=['Select File', 'Close'],
        default_choice='Select File',
        cancel_choice='Close'
        )
    
    def selectFile(self):
        file = fileopenbox(title=f'{self.app_name} - Select File', filetypes='(*.ini)', multiple=False)
        self.run(file, False)

    def run(self, file, dir):
        if dir == False:
            print('Starting task...\n')
            self.ini_file = file
            if self.ini_file != None:
                if path.exists(self.ini_file):

                    ini_name_list = self.ini_file.split('\\')
                    ini_name = ini_name_list[::-1][0]
                    ini_path = ''
                    for y in range(len(ini_name_list)-1):
                        ini_path = ini_path + ini_name_list[y] + '\\'

                    print('Task started!\n')

                    print(f'Reading file {ini_name}...\n\n')
                    try:
                        cp = ConfigParser(strict=False)
                        cp.read(self.ini_file)
                    except:
                        exceptionbox('Error reading file!', f'{self.app_name} - Error')

                    print('Getting the session and key names...')
                    try:
                        file_count = 0
                        for x in range(len(cp.sections())):

                            print(f'\n\nSession {x}: [{cp.sections()[x]}]\n')
                            ini_data = ConfigParser(strict=False)
                            ini_data[cp.sections()[x]] = {}
                            try:
                                key_names = [op for op in cp[cp.sections()[x]]]
                            except:
                                exceptionbox(f'Error getting the {cp.sections()[x]} session key names!', f'{self.app_name} - Error')

                            for y in range(len(key_names)):

                                print(f'Key {y}: {key_names[y]} | Value: {cp[cp.sections()[x]][key_names[y]]}\n')
                                ini_data[cp.sections()[x]][key_names[y]] = cp[cp.sections()[x]][key_names[y]]
                        
                            new_file_name = f'{ini_name.replace(".ini", "")}_[{cp.sections()[x].replace("/", "-")}].ini'
                            print(f'\nWriting a new ini file ({new_file_name})...\n')
                            try:
                                with open(path.join(ini_path, new_file_name), 'w') as config_file:
                                    ini_data.write(config_file)
                                print(f'File ({new_file_name}) saved!')
                                file_count = file_count + 1
                            except:
                                exceptionbox(f'Error saving file {new_file_name}].ini', f'{self.app_name} - Error')
                        
                        print(f'\n\nTask completed successfully!\nTotal files: {file_count}')
                    except:
                        exceptionbox('Error getting session name!', f'{self.app_name} - Error')

                    r = ynbox('Make a backup of the original file?', f'{self.app_name} - Backup', ('Yes', 'No'), cancel_choice='No')

                    if r:
                        if path.exists('./backup') == False:
                            mkdir('./backup')

                        file_n = 1
                        while path.exists(f'./backup/{ini_name}'):
                            ini_name = ini_name.replace('.ini', '') + f'[{str(file_n)}].ini'
                            file_n += 1

                        # print(f'"backup\\{ini_name}"')
                        cmd(f'move "{self.ini_file}" "backup\\{ini_name}"')
                    else:
                        cmd('del "{}"'.format(self.ini_file))
                else:
                    print("The file does not exist, please check again!")
                    msgbox('The file does not exist, please check again!', f'{self.app_name} - Error', 'Ok')
                    self.selectFile()
            else:
                pass
        else:
            if 'Sirius Beck' in self.app_name:
                print('')
            else:
                exit()