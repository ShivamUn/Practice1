import sys
import csv
from csvvalidator import *

field_names = ('slno',
               'empId',
               'empName',
               'empSalary',
               'dateOfJoining'
               )

validator = CSVValidator(field_names)

# basic header and record length checks
validator.add_header_check('EX1', 'Bad Header')
validator.add_record_length_check('EX2', 'Unexpected Record Length')

# slno integer data type check
validator.add_value_check('slno', int,
                          'EX3', 'slno must be an integer')

# validator.add_unique_check('slno')
# empId integer data type check
validator.add_value_check('empId', int,
                          'EX4', 'empId must be an integer')

# empName string data type check
validator.add_value_check('empName', str,
                          'EX5', 'empId must be string')

# empSalary integer data type check
validator.add_value_check('empSalary', int,
                          'EX5_1', 'empId must be an integer')
# empSalary range check
validator.add_value_check('empSalary', number_range_inclusive(1000, 50000, int),
                          'EX5_2', 'Salary not in range')

# dateOfJoining date format check
validator.add_value_check('dateOfJoining', datetime_string('%d-%m-%Y'),
                          'EX6', 'invalid date')

try:
    with open('src/employees.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quotechar='|')
        try:
            problems = validator.validate(data)
            for i in problems:
                print(i)
            write_problems(problems, sys.stdout)
        except Exception as e:
            print(e)

except Exception as e:
    print(e)




