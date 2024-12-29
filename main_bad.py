from datetime import *
from tabulate import *
from application.salary import *
from application.db.people import *


if __name__ == "__main__":
    print(datetime.now())
    salary_list = []
    for employee in get_employees():
        salary_list.append([employee, calculate_salary(employee)])

    print(tabulate(
        salary_list,
        headers=["Employee", "Salary"],
        tablefmt="fancy_outline"
        )
    )
