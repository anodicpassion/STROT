import subprocess
import time


class ScriptRunner:
    def __init__(self, script_path):
        # Initialize the subprocess to run the specified script
        self.process = subprocess.Popen(
            [script_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

    def send_inputs(self, input):
        # Send two inputs to the subprocess, simulating user input
        self.process.stdin.write(f"{input}\n")
        self.process.stdin.flush()  # Ensure inputs are sent

        # Capture and return the output for these inputs
        output = self.process.stdout.readline().strip()
        return output

    def get_output(self):
        output = self.process.stdout.readlines()
        output_ = ""
        for i in output:
            output_ = output_ + i
        return output_

    def close(self):
        # Properly close the subprocess
        self.process.terminate()
        self.process.wait()  # Wait for the subprocess to fully close


if __name__ == "__main__":
    runner = ScriptRunner(input("Enter script name: "))
    time.sleep(0.5)
    print(runner.get_output())
    try:
        result = runner.send_inputs(input("Enter the thing to enter"))
        print("Output:", result)
        time.sleep(0.5)

    finally:
        runner.close()

