import subprocess
import sys


def test_hello_world(capsys):
    exec(open("main.py").read())
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"


def test_hello_world_subprocess():
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
    )
    assert result.stdout.strip() == "Hello, World!"
