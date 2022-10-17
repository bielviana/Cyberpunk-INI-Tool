from os import system as cmd

cmd('cls')

print('Converting the .ui and .qrc files...')

# try:
#     cmd('pyuic5 cit\\interface\\main.ui -o cit\\interface\\main_ui.py')
#     print('main_ui.py generated!')
# except:
#     print('Error to generate the main_ui.py file.')

try:
    cmd('pyrcc5 cit\\interface\\res.qrc -o cit\\interface\\res.py')
    print('res.py generated!')
except:
    print('Error to generate the res.py file.')