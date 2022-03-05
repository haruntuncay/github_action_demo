import importlib
#import fpdf
import math
import os
from turtle import bgcolor

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


src = importlib.import_module('workspace.demo')
tst = importlib.import_module('tests')

ass = src.Assignment()
test_functions = dir(tst)

tests_found = []
successful_tests = []
failed_tests = []

for tf in test_functions:
    if not tf.startswith('__') and not tf.endswith('__'):
        if callable(func := getattr(tst, tf)):
            tests_found.append(tf)
            try:
                func(ass)
                successful_tests.append(tf)
            except:
                failed_tests.append(tf)

def report():
    print('REPORTING')
    '''
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 11)  
    pdf.cell(200, 10, txt = "Report for your assignment", ln = 1, align = 'C')

    pdf.set_text_color( 46, 204, 113 )
    for ts in successful_tests:
        pdf.cell(200, 10, txt = f'+ {ts}', ln = 1)

    pdf.set_text_color(  231, 76, 60 )
    for ts in failed_tests:
        pdf.cell(200, 10, txt = f'x {ts}', ln = 1)
  
    pdf.set_text_color( 0,0,0 )
    txt = f'Your total performance was {len(successful_tests)}/{len(failed_tests)}'
    pdf.cell(200, 10, txt = txt, ln = 1)

    ratio = len(successful_tests)/len(failed_tests)
    txt = f'Your score is {math.ceil(ratio*100)}'
    pdf.cell(200, 10, txt = txt, ln = 1)
    
    pdf.output("a.pdf")
    '''
    for t in successful_tests:
        print(f'{bcolors.OKGREEN}Test {t} was succesful{bcolors.ENDC}')
    for t in failed_tests:
        print(f'fail {t}')

report()