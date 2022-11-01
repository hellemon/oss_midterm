# Program make a simple calculator
import sys
import os.path 
import select_input as si

# make error_log object
if os.path.isfile("cal_log.txt"):
    cal_log = open('cal_log.txt', 'a')
else:
    cal_log = open('cal_log.txt', 'w')
if os.path.isfile('error_log.txt'):
    error_log = open('error_log.txt', 'a')
else:
    error_log = open('error_log.txt', 'w')

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 

si.process_function()
