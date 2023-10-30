import subprocess

def httpd_funct():
    script_path = "/home/vagrant/vagrant_data/TestCases/httpd_test_cases/test.sh"
    try:
        result = subprocess.check_output(["bash", script_path])
        output_lines = result.decode().strip().split('\n')
        last_line = output_lines[-1]
        return int(last_line)
    except subprocess.CalledProcessError as e:
        #print(f"Error: {e}")
        return None

if __name__ == "__main__":
    result = httpd_funct()
