from autog import runner

reports = runner.run_grader('assignment.py', 'solution.py', 'test_desc.yaml')

for rep in reports:
    r = rep.report()
    print(r)
