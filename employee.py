"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, monthly_salary=0, contract_hours=0, hourly_wage=0):
        self.name = name
        self.monthly_salary = monthly_salary
        self.hourly_wage = hourly_wage
        self.contract_hours = contract_hours


    def get_pay(self):
        if self.contract_hours:
            return self.contract_hours * self.hourly_wage
        else:
            return self.monthly_salary

    def __str__(self):
        if self.contract_hours:
            return f"{self.name} works on a contract of {self.contract_hours} hours at {self.hourly_wage}/hour.  Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a monthly salary of {self.monthly_salary}.  Their total pay is {self.get_pay()}."

class ComissionedEmployee(Employee):
    def __init__(self, name, monthly_salary=0, contract_hours=0, hourly_wage=0, contract_number=0, commission_per_contract=0, bonus=0):
        super().__init__(name, monthly_salary, contract_hours, hourly_wage)
        self.contract_number = contract_number
        self.commission_per_contract = commission_per_contract
        self.bonus = bonus

    def get_bonus(self):
        if self.bonus:
            return self.bonus
        else:
            return self.commission_per_contract * self.contract_number

    def get_pay(self): #override parent method
        return super().get_pay() + self.get_bonus()

    def __str__(self):
        explanatory_string = ""
        if self.contract_hours:
            explanatory_string += f"{self.name} works on a contract of {self.contract_hours} hours at {self.hourly_wage}/hour"
        else:
            explanatory_string += f"{self.name} works on a monthly salary of {self.monthly_salary}"
        if self.bonus:
            explanatory_string += f" and receives a bonus commission of {self.bonus}."
        else:
            explanatory_string += f" and receives a commission for {self.contract_number} contract(s) at {self.commission_per_contract}/contract."
        explanatory_string += f"  Their total pay is {self.get_pay()}."
        return explanatory_string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', monthly_salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', contract_hours=100, hourly_wage=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = ComissionedEmployee('Renee', monthly_salary=3000, contract_number=4, commission_per_contract=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ComissionedEmployee('Jan', contract_hours=150, hourly_wage=25, contract_number=3, commission_per_contract=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = ComissionedEmployee('Robbie', monthly_salary=2000, bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ComissionedEmployee('Ariel', contract_hours=120, hourly_wage=30, bonus=600)
