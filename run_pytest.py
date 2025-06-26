import subprocess

command = f'pytest --cov --cov-report=xml'
subprocess.run(command, shell=True, check=True)