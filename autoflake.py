import os
import re

rundir = os.path.dirname(__file__)
flake_executable = os.path.join(rundir, 'venv/Scripts/autoflake')
pep_executable = os.path.join(rundir, 'venv/Scripts/autopep8')


def run():
    for root, dirs, files in os.walk(rundir):
        for name in files:
            filepath = os.path.join(root, name)
            if re.match('.*.py$', filepath) and 'venv' not in filepath:
                flake_command = ' '.join([flake_executable,
                                          '--in-place',
                                          '--remove-all-unused-imports',
                                          '--remove-unused-variables',
                                          filepath])
                flake_status = os.system(flake_command)
                pep_command = ' '.join([pep_executable,
                                        '--in-place',
                                        filepath])
                pep_status = os.system(pep_command)
                print(filepath, 'Status',
                      f'pep: {pep_status}', f'flake: {flake_status}')


if __name__ == "__main__":
    run()
