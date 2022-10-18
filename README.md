# Cyberpunk-INI-Tool

[![Support Me on Ko-fi](https://i.imgur.com/7Cm07AZ.png)](https://ko-fi.com/siriusbeck)

## What is it?

Simple script to separate sessions from INI files into separate files.

## Why?

Apparently the way Cyberpunk 2077 works with mods INI files is weird, basically the game doesn't read your entire INI file, it only reads the top of it, so if you have a huge INI with lots of sessions and settings, a huge part of those settings will be ignored by the game, so if you already have one of those huge INI's, CIT will separate all the sessions of your file into several different files, one for each session. It's also useful for you who are a modder and will still make your INI, because it's much more practical to just type everything in a single file and then run a script to separate them.

## Build guide (for devs only)

I'll pass the instructions only for windows, because I don't imagine anyone is playing Cyberpunk 2077 on linux, but if for some reason this is your case, the commands are basically the same.

### >> Standard version

The default version isn't working properly, I need to change the way it works with ini files and some silly mistakes, but I don't have time to fix it now.

But don't worry, the lite version is uglier visually speaking but it has the same function and works as expected without any problem.

In the future I fix the standard version, maybe using c# because generating binary file in python when using some graphic libraries is a huge problem, this 8mb file from the lite version became a 700mb folder in the standard version.

### >> Lite version

1. Open the power shell in the **`cit-lite`** folder and create a virtual environment.
   
   ```
   python -m venv venv
   ```

2. Ainda pelo powershell, start the virtual environment.

3. ```
   venv\Scripts\Activate.ps1
   ```

4. Install the necessary libraries.

5. ```
   python -m pip install -r requirements.txt
   ```

6. Navigate to the **`citlite`** folder

7. ```
   cd citlite
   ```
* You have two ways to run the program:
  
  1. Python file.
     
     ```
     python main.py
     ```
  
  2. Generating an executable.
     
     ```
     python -m pip install pyinstaller
     
     pyinstaller --noconfirm --onefile --windowed --icon "path_to_icon/icon.ico" --name "Cyberpunk INI Tool"  "path_to_citlite_folder/main.py"
     ```
     
     Where "path_to..." you replace with the path of each file.

## Links

- **[Discord Server](https://discord.gg/pVKQ7vzmKE)**
- **[Instagram](https://instagram.com)**
- **[Twitter](https://twitter.com/_katiorro)**
- **[NexusMods](https://www.nexusmods.com/users/73453593)**
