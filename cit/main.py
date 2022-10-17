from interface.main_ui import *
from classes.config import *
from configparser import ConfigParser
from os import system as cmd

cmd('cls')

class CyberpunkINITool(QMainWindow):

    global json_style, selected_theme



    def __init__(self) -> None:
        QMainWindow.__init__(self)
        self.ui = Ui_CyberpunkINITool()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles={json_style})

        self.mode = ''
        self.theme = selected_theme
        self.config = config

        self.change_theme(self.theme, False)

        # Buttons actions
        self.ui.btn_theme.clicked.connect(lambda: self.change_theme(self.mode, True))
        self.ui.btn_file.clicked.connect(self.search_file)
        self.ui.btn_split.clicked.connect(self.split_ini)



    def change_theme(self, theme, update_config):

        self.ui.centralwidget.setStyleSheet('')
        self.ui.centralwidget.setStyleSheet(themes[theme])

        if theme == 'dark':
            self.mode = 'light'
            config['CITConfig'][0]['theme'] = 'dark'
        else:
            self.mode = 'dark'
            config['CITConfig'][0]['theme'] = 'light'
        
        if update_config:
            with open(json_style, 'w') as file:
                json.dump(config, file, indent=4)

    def search_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select the INI file to split', '', 'ini files (*.ini)', options=options)
        if file_name:
            file_name = file_name.replace('/', '\\')
            self.ui.input_file.setText(file_name)
    
    def split_ini(self):

        self.ui.input_log.clear()

        self.ui.input_log.insertPlainText('Starting task...\n')
        self.ini_file = self.ui.input_file.text()
        if path.exists(self.ini_file):

            ini_name_list = self.ini_file.split('\\')
            ini_name = ini_name_list[::-1][0]
            ini_path = ''
            for y in range(len(ini_name_list)-1):
                ini_path = ini_path + ini_name_list[y] + '/'

            self.ui.input_log.insertPlainText('Task started!\n')

            self.ui.input_log.insertPlainText(f'Reading file {ini_name}...\n\n')
            cp = ConfigParser()
            cp.read(self.ini_file)

            self.ui.input_log.insertPlainText('Getting the session and key names...')
            file_count = 0
            for x in range(len(cp.sections())):

                self.ui.input_log.insertPlainText(f'\n\nSession {x}: [{cp.sections()[x]}]\n')
                ini_data = ConfigParser()
                ini_data[cp.sections()[x]] = {}
                key_names = [op for op in cp[cp.sections()[x]]]

                for y in range(len(key_names)):

                    self.ui.input_log.insertPlainText(f'Key {y}: {key_names[y]} | Value: {cp[cp.sections()[x]][key_names[y]]}\n')
                    ini_data[cp.sections()[x]][key_names[y]] = cp[cp.sections()[x]][key_names[y]]
            
                self.ui.input_log.insertPlainText(f'\nWriting a new ini file ({ini_name}_[{str(x)}].ini)...\n')
                with open(path.join(ini_path, f'{ini_name}_[{str(x)}].ini'), 'w') as config_file:
                    ini_data.write(config_file)
                self.ui.input_log.insertPlainText(f'File ({ini_name}_[{str(x)}].ini) saved!')
                file_count = file_count + 1
            
            self.ui.input_log.insertPlainText(f'\n\nTask completed successfully!\nTotal files: {file_count}')

            msg = QMessageBox()
            msg.setWindowTitle('Cyberpunk INI Tool')
            msg.setText(f'Your .ini file has been successfully split into a total of {file_count} files, do you want to delete the original file?')
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            msg.setDefaultButton(QMessageBox.Yes)
            msg.buttonClicked.connect(self.delete_original_file)
            msg.exec_()
        else:
            self.ui.input_log.insertPlainText("The file does not exist, please check again!")
        
        self.ui.input_file.setText("")
    
    def delete_original_file(self, x):
        if "Yes" in x.text() or "yes" in x.text():
            cmd(f'del "{self.ini_file}"')



def main() -> None:
    app = QApplication(sys.argv)
    window = CyberpunkINITool()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()