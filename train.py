import sys
from IPython.core.ultratb import ColorTB
sys.excepthook = ColorTB()


def run():
    print('I have create a new dataset')
    print('I have run a model')
    print('I have create a branch')


if __name__ == '__main__':
    run()
