import os

if __name__ == '__main__':
    print("Welcome to RoboReader 1.1. Created by Eternity2003: ")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            os.system("say 'bye bye friend'")
            break
        command = f"say {x}"
        os.system(command)