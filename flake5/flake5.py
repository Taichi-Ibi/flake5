import platform
import subprocess
import sys

from .parse_nb import parse_nb


def flake5(path):
    py = parse_nb(path)
    with open(file := "__flake5__.py", mode="w") as f:
        f.write(py)
    os = platform.system()
    grep = "findstr" if os == "Windows" else "grep"
    cmd = f"flake8 {file} | {grep} import && rm {file}"
    subprocess.call(cmd, shell=True)


def main():
    flake5(path=sys.argv[1])
