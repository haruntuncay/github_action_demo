GREEN = '\033[92m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD_START = "\033[1m"
BOLD_END = "\033[0;0m"

class Case():

    def __init__(self, params=None, expected=None, got=None, passed=True, reason=None):
        self.params = params
        self.expected = expected
        self.got = got
        self.passed = passed
        self.reason = reason

class Report():

    def __init__(self, name, exception=None, failed=False, found=True):
        self.name = name
        self.passed_cases = []
        self.failed_cases = []
        self.exception = exception
        self.failed = failed
        self.found = found
        
    def add_case(self, case):
        if case.passed:
            self.passed_cases.append(case)
        else:
            self.failed_cases.append(case)

    def mark_as_failed(self):
        self.failed = True

    def mark_as_nout_found(self):
        self.found = False

    def report(self):
        funcname = self.name.upper()
        r = '-' * 40
        
        if self.failed:
            r +=  f'\n{funcname} has failed'
            if self.exception:
                r += ', exception was: ' + str(self.exception) 
            return r

        if not self.found:
            return r + f'\n{funcname} was not found'

        r += f'\n{funcname} ran {len(self.passed_cases) + len(self.failed_cases)} tests.'
        
        if len(self.passed_cases):
            r += f'\n{GREEN}{len(self.passed_cases)} tests were succesful.{ENDC}'

        if len(self.failed_cases):
            r += f'\n{RED}{len(self.failed_cases)} tests have failed.{ENDC}'

            for fc in self.failed_cases:
                r += f'\n\t- {BOLD_START}{self.name}({", ".join([str(p) for p in fc.params])}){BOLD_END}'
                r += f'\n\t  expected: {BOLD_START}{fc.expected}{BOLD_END}, but got {BOLD_START}{fc.got}{BOLD_END}\n'
      
        return r