from .source_helper import get_source
from .processor.parser import Parser
from .report import Report, Case
import yaml
import sys

sout = sys.stdout

class Buffer():

    def __init__(self):
        self.lines = []

    def write(self, str):
        self.lines.append(str)
    
    def get_last_line(self):
        for i in range(len(self.lines)-1, -1, -1):
            if self.lines[i] != '\n':
                return self.lines[i]

    def clear(self):
        self.lines = []

    def flush(self):
        pass

def run_grader(assignment_path, solution_path, yaml_path):
    solution_src = get_source(solution_path)
    assignment_src = get_source(assignment_path)

    test_inputs = get_test_inputs(yaml_path)
    return run_tests(assignment_src, solution_src, test_inputs)

def run_tests(asmt, sol, test_inputs):
    asmt_funcs = get_functions_in_module(asmt)
    sol_funcs = get_functions_in_module(sol)

    reports = []

    for func_name in sol_funcs:
        if func_name in asmt_funcs:
            rep = run_test_for_func(func_name, getattr(asmt, func_name), getattr(sol, func_name), test_inputs[func_name])
            reports.append(rep)
        else:
            reports.append(Report(func_name, found=False))
        
    return reports

def run_test_for_func(name, asmt, sol, test_inputs):
    num_of_cases = test_inputs['cases']
    param_info = test_inputs['parameters']
    report = Report(name)

    param_asts = []
    for p in param_info:
        parser = Parser(p['value'])
        param_asts.append(parser.parse())

    buffer = Buffer()
    sys.stdout = buffer

    for _ in range(num_of_cases):
        params = [pa.get() for pa in param_asts]
        case = Case(params)

        try:
            expected = sol(*params)
            case.expected = expected

            got = asmt(*params)
            case.got = got

            if got == None and len(buffer.lines) > 0 and expected != None:
                got = buffer.get_last_line()
                expected = str(expected)
                
                case.expected = expected
                case.got = got

            case.passed = expected == got

            buffer.clear()
        except Exception as e:
            sout.write(e)
            case.passed = False
            case.reason = e

        report.add_case(case)

    sys.stdout = sout

    return report

def get_functions_in_module(asmt):
    functions_found = []

    for name in dir(asmt):
        if not name.startswith('__'):
            if callable(attr := getattr(asmt, name)) and type(attr) != type(object):
                functions_found.append(name)
    
    return functions_found

def get_test_inputs(yaml_path):
    with open(yaml_path, "r") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            raise e            
    
    return data['functions']