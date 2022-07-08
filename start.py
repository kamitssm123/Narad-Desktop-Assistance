from input_module import take_input
from process_module import process
from output_module import output
import os
from welcome import greet

os.system("clear")

greet()

while(True):
    i = take_input()
    o = process(i)
    output(o)
