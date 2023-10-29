import subprocess

# Run a Python script with the -u flag
cmd = ["python", "-u", "hello.py"]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Read the output from the script
output, errors = proc.communicate()

# Check if the output contains the expected text
assert b"hello world" in output

# Check if there were any errors
assert not errors, errors
