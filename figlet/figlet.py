import sys
from pyfiglet import Figlet

figlet = Figlet()
list = figlet.getFonts()


def main():
    if len(sys.argv) == 3:
        # If the user provides two command-line arguments and the first is not -f or --font or the
        # second is not the name of a font, the program should exit via sys.exit with an error message.
        if sys.argv[1] == "-f" and sys.argv[2] in list:
            f = sys.argv[2]
            figlet.setFont(font=f)
            print(figlet.renderText(input()))
        else:
            sys.exit("Invalid usage")
    elif len(sys.argv) == 1:
        print(figlet.renderText(sys.argv[1]))
    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
