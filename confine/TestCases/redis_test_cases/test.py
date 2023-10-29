import subprocess

def redis_funct():
    script_path = "redis_test_cases.sh"
    try:
        result = subprocess.check_output(["bash", script_path])
        output_lines = result.decode().strip().split('\n')
        last_line = output_lines[-1]
        return int(last_line)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    result = redis_funct()
    if result is not None:
        print(f"Last line of the output is: {result}")

