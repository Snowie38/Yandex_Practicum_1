class Employee:
    vacation_days = 28

    def __init__ (self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, days_to_consume):
        self.remaining_vacation_days -= days_to_consume
    
    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

        

employee1 = Employee(first_name='Александр',second_name='Яшин',gender='м')
employee1.consume_vacation(7)
print(employee1.get_vacation_details())



#print(f'Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, Пол: {employee1.gender}, Отпускных дней в году: {employee1.vacation_days}.')
