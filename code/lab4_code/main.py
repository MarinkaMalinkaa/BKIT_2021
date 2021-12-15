from composite import ComplexPart, Part, Comp

if __name__ == '__main__':

    print('Pattern Composite \n')
    ControlDivices = ComplexPart('Control divices')
    ControlDivices.add_product(Part('Mouse', 800))
    ControlDivices.add_product(Part('Keyboard', 1920))
    Monitor = Part('Monitor HP', 50700)
    SystemUnit = Part('System unit HP', 23400)
    Equipment = Comp ('HP')
    Equipment.add_product(ControlDivices)
    Equipment.add_product(Monitor)
    Equipment.add_product(SystemUnit)
    print(Equipment.cost())
