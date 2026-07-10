class PersonAccoun():
    def __init__(self, firstname, lastname, incomes,
                 expenses, properties):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
        self.properties = properties

    def total_income(self):
        return sum(self.incomes)
    def total_expenses(self):
        return sum(self.expenses)
    def account_info(self):
        return self.firstname, self.lastname
    def add_income(self, i):
        self.incomes.append(i)
    def add_expense(self, e):
        self.expenses.append(e)
    def account_balance(self):
        return self.total_income() - self.total_expenses()
    