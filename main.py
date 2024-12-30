from datetime import datetime
from tabulate import tabulate
from application.salary import calculate_salary
from application.db.people import get_employees


def main() -> None:
    salary_list = []
    for employee in get_employees():
        salary_list.append([employee, calculate_salary(employee)])

    print(tabulate(
        salary_list,
        headers=["Employee", "Salary"],
        tablefmt="fancy_outline"
    )
    )


if __name__ == "__main__":
    print(datetime.now())
    main()
