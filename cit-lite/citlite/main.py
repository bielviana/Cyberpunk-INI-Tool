from app import *

cmd('cls')

def main():
    app = CyberpunkINITool('Cyberpunk INI Tool [made by Sirius Beck]')
    run = True

    while run:
        app.mainWindow()
        if app.mainwindow_res:
            app.selectFile()
        else:
            run = False
    

if __name__ == '__main__':
    main()