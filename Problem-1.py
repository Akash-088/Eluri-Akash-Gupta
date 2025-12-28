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
                return "Division by zero not possible"
        else:
            return "Invalid operation"
        
calc=calculator(10.5,3.5,"+")
print(calc.calculate())