from os import path, mkdir
import json



config_folder = path.expanduser('~/appdata/local/Cyberpunk INI Tool')
if path.exists(config_folder) == False:
    mkdir(config_folder)

# config_file = path.join(config_folder, 'config.ini')
# if path.exists(config_file) == False:
#     with open(config_file, 'w') as file:
#         pass


json_style = config_file = path.join(config_folder, 'ui.json')

json_data = {
    "QMainWindow":[
        {
            "frameless": True,
            "transluscentBg": True,
            "sizeGrip": "sizegrip",
            "navigation":[
                {
                    "close": "btn_close",
                    "minimize": "btn_minimize",
                    "restore": [
                        {
                            "buttonName": "btn_maximize"
                        }
                    ],
                    "moveWindow": "titlebar",
                    "titleBar": "titlebar"
                }
            ]
        }
    ],
    "CITConfig":[
        {
            "theme": "light"
        }
    ]
}

json_data = json.dumps(json_data, indent=4)

if path.exists(json_style) == False:
    with open(json_style, 'w') as file:
        file.write(json_data)



with open(json_style, 'r') as file:
    config = json.load(file)
    selected_theme = config['CITConfig'][0]['theme']


# Themes available, the keys of the respective themes need to have the same name that will go in the json file, otherwise only the Light theme will work.
themes = {
    "dark": """
    #centralwidget {
        border-radius: 10px;
        background-color: #404040;
    }

    QFrame, #input_log, #input_file {
        color: #ffffff;
    }

    #btn_theme {
        image: url(:/icons/assets/icons_white/light-mode.svg);
        border: 0;
    }

    #btn_theme:hover {
        image: url(:/icons/assets/icons_purple/light-mode.svg);
        border: 0;
    }

    #frame_file {
        background-color: #303030;
        border-radius: 10px;
        border: 2px solid #202020;
        padding-left: 5px;
    }

    #input_file {
        border: 0;
        background-color: transparent;
    }

    #btn_file {
        image: url(:/icons/assets/icons_purple/file.svg);
        border: 0;
    }

    #btn_file:hover {
        image: url(:/icons/assets/icons_white/file.svg);
        border: 0;
    }

    #btn_minimize {
        image: url(:/icons/assets/icons_purple/minimize.svg);
        border: 0;
    }

    #btn_minimize:hover {
        image: url(:/icons/assets/icons_white/minimize.svg);
        border: 0;
    }

    #btn_maximize {
        image: url(:/icons/assets/icons_purple/maximize.svg);
        border: 0;
    }

    #btn_maximize:hover {
        image: url(:/icons/assets/icons_white/maximize.svg);
        border: 0;
    }

    #btn_close {
        image: url(:/icons/assets/icons_purple/close.svg);
        border: 0;
    }

    #btn_close:hover {
        image: url(:/icons/assets/icons_white/close.svg);
        border: 0;
    }

    #frame_app_icon{
        border-image: url(:/icons/assets/icon.png) 0 0 0 0 stretch stretch;
        border-radius: 10px;
    }

    #titlebar{
        background-color: #202020;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
    }

    #input_log {
        background-color: #303030;
        border-radius: 10px;
        border: 2px solid #202020;
        padding: 5px;
    }
    """,



    "light": """
    #centralwidget {
        border-radius: 10px;
        background-color: #ffffff;
    }

    QFrame, #input_log, #input_file {
        color: #404040;
    }

    #btn_theme {
        image: url(:/icons/assets/icons_black/dark-mode.svg);
        border: 0;
    }

    #btn_theme:hover {
        image: url(:/icons/assets/icons_purple/dark-mode.svg);
        border: 0;
    }

    #frame_file {
        background-color: #F7F7F7;
        border-radius: 10px;
        border: 2px solid #EBEBEB;
        padding-left: 5px;
    }

    #input_file {
        border: 0;
        background-color: transparent;
    }

    #btn_file {
        image: url(:/icons/assets/icons_purple/file.svg);
        border: 0;
    }

    #btn_file:hover {
        image: url(:/icons/assets/icons_black/file.svg);
        border: 0;
    }

    #btn_minimize {
        image: url(:/icons/assets/icons_purple/minimize.svg);
        border: 0;
    }

    #btn_minimize:hover {
        image: url(:/icons/assets/icons_black/minimize.svg);
        border: 0;
    }

    #btn_maximize {
        image: url(:/icons/assets/icons_purple/maximize.svg);
        border: 0;
    }

    #btn_maximize:hover {
        image: url(:/icons/assets/icons_black/maximize.svg);
        border: 0;
    }

    #btn_close {
        image: url(:/icons/assets/icons_purple/close.svg);
        border: 0;
    }

    #btn_close:hover {
        image: url(:/icons/assets/icons_black/close.svg);
        border: 0;
    }

    #frame_app_icon{
        border-image: url(:/icons/assets/icon.png) 0 0 0 0 stretch stretch;
        border-radius: 10px;
    }

    #titlebar{
        background-color: #EBEBEB;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
    }

    #input_log {
        background-color: #F7F7F7;
        border-radius: 10px;
        border: 2px solid #EBEBEB;
        padding: 5px;
    }
    """
}
