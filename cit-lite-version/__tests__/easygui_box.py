import easygui

# r = easygui.ynbox('Make a backup of the original file?', 'CIT - Backup', ('Yes', 'No'), cancel_choice='No')

r = easygui.fileopenbox('Select the ini file to split.', 'Select File', filetypes='(*.ini)', multiple=False)















print(r)