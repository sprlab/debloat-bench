import subprocess

result = subprocess.run(['python3', 'test.py'], capture_output=True, text=True)
print(result.stdout)