def function_with_uncommon_error_solution(a, b):
    if a == 0:
        return float('inf') # Handle division by zero gracefully
    else:
        return a + b

result = function_with_uncommon_error_solution(0, 10)
print(result)

#Alternative solution: using try-except block
def function_with_uncommon_error_solution_try_except(a,b):
    try:
        if a == 0:
            return b / a
        else:
            return a + b
    except ZeroDivisionError:
        return float('inf')
result = function_with_uncommon_error_solution_try_except(0,10)
print(result)