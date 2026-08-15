import numpy as np

def calculate_special_bonus(employees):
    employees["bonus"] = np.where(
        (employees["employee_id"] % 2 == 1) &
        (~employees["name"].str.startswith("M")),
        employees["salary"],
        0
    )

    result_table = employees[["employee_id", "bonus"]].sort_values("employee_id")

    return result_table
    