


class Employee:
  def __init__(self, employee_id,employee_name,employee_department,hourly_rate,number_of_hour_worked):


    self.employee_id = employee_id
    self.employee_name = employee_name
    self.employee_department = employee_department
    self.hourly_rate = hourly_rate
    self.number_of_hour_worked = number_of_hour_worked
def __str__(self):
    return f"{self.employee_id}{self.employee_name}{self.employee_department}{self.hourly_rate}({self.number_of_hour_worked})"

hrs = input("Enter Hours:")

rate = input("Enter hourly rate:")