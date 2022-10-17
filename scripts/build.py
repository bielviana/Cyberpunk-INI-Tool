from cx_Freeze import setup, Executable

files = [
    '',
    ''
]

target = Executable(
    script = 'main.py',
    base = 'Win32GUI',
    icon = 'interface/assets/icon.ico',   
)

setup(
    name = 'Cyberpunk INI Tool',
    version = '0.0.1',
    description = '',
    author = 'Gabriel Viana',
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
)