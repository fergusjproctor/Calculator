import string


class Calculator:
    # initialise dict of variables
    def __init__(self):
        self.vars = dict()

    # evaluate an expression
    def expression(self, exp):
        exp = self.extract_val(exp)
        if any(i in exp for i in string.ascii_letters):
            return 'Unknown variable'
        if '**' in exp or '//' in exp:
            return 'Invalid expression'
        try:
            return str(int(eval(exp)))
        except:
            return 'Invalid expression'

    # process assignment
    def assign(self, ass):
        if ass.count('=') > 1:
            return 'Invalid assignment'
        else:
            # split equation
            lhs = ass[:ass.find('=')]
            rhs = ass[ass.find('=') + 1:]
            lhs = lhs.rstrip(' ')
            rhs = rhs.lstrip(' ')
            # check for numbers in variable name
            if any(char.isdigit() for char in lhs):
                return 'Invalid identifier'
            else:
                # calculate result of rhs
                val = self.expression(rhs)
                if val.isnumeric():
                    self.vars[lhs] = val
                else:
                    return 'Invalid assignment'
                return

    def run(self):
        while True:
            inp = input()
            if not inp:
                continue
            if '/' == inp[0]:
                # should be command
                if inp == '/help':
                    print('The program calculates the sum of numbers')
                elif inp == '/exit':
                    print('Bye!')
                    break
                else:
                    print('Unknown command')
            elif '=' in inp:
                val = self.assign(inp)
                if not val:
                    pass
                else:
                    print(val)
            else:
                # should be expression
                print(self.expression(inp))

    # replace variables with value
    def extract_val(self, str):
        for variable in self.vars.keys():
            if variable in str:
                str = str.replace(variable, self.vars[variable])
        return str


calc = Calculator()
calc.run()

