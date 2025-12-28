class calculator:
    def __init__(self,a: float,b: float,operation: str):
        self.a=a
        self.b=b
        self.operation=operation

    def calculate(self):
        if self.operation=="+":
            return self.a+self.b
        elif self.operation=="-":
            return self.a-self.b
        elif self.operation=="*":
            return self.a*self.b
        elif self.operation=="/":
            if self.b!=0:
                return self.a/self.b
            else:
                return "Division by zero is not possible"
        else:
            return "Invalid operation"
        
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
operation=input("Enter operation(+,-,*,/): ")

calc=calculator(a,b,operation)
print(calc.calculate())