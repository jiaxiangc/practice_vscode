import sys
from IPython.core.ultratb import ColorTB
sys.excepthook = ColorTB()


def main():
    print('it is the fifth change')
    return None


if __name__ == '__main__':
    main()
