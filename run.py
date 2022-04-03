from autog import runner

reports = runner.run_grader('assignment.py', 'full_src.py', 'test_desc.yaml')

for r in reports:
    print(r.report())
