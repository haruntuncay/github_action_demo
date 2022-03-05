import importlib

GREEN = '\033[92m'
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
    for t in successful_tests:
        print(f'{GREEN}Test {t} was succesfully ran{ENDC}')
    for t in failed_tests:
        print(f'{FAIL}Test {t} has failed{ENDC}')

report()