import sys
from IPython.core.ultratb import ColorTB
sys.excepthook = ColorTB()


def run():
    print('I have run a model')


if __name__ == '__main__':
    run()
