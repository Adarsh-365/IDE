
import subprocess

class Compiler:
    def __init__(self,code):
        self.code = code
      
    def run(self):
        try: 
            self.op = subprocess.check_output(
                    ['python', '-c', self.code],
                    stderr=subprocess.STDOUT,
                    universal_newlines=True
                )
        except subprocess.CalledProcessError as e:
            # Capture the error message and the return code
            self.op = f"Error: {e.output.strip()} | Return Code: {e.returncode}"
        except Exception as e:
            # For any other exceptions, return the exception message
            self.op = f"Unexpected Error: {str(e)}"
    def output(self):
        print(self.op)
        return self.op