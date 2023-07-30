def SynchronizingTables(n: int, ids: list[int], salary: list[int]) -> list[int]:
    employee_to_salary = dict(zip(sorted(ids), sorted(salary)))
    sorted_salaries = [employee_to_salary[employee_number] for employee_number in ids]

    return sorted_salaries
