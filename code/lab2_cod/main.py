from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

from colorama import Fore, Back, Style


def get_colorText():
    print(Fore.YELLOW + 'Желтый текст')
    print(Back.BLUE + 'Синий фон')
    print(Style.RESET_ALL)
    print('Снова обычный текст')


def main():
    r = Rectangle("синего", 4, 4)
    c = Circle("зеленого", 4)
    s = Square("красного", 4)
    print(r)
    print(c)
    print(s)

    get_colorText()


if __name__ == "__main__":
    main()
