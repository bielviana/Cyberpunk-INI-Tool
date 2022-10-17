from app import *

def main():
    run = True
    app = CITLite()
    
    while run:
        app.run()
        run = app.check()

if __name__ == '__main__':
    main()