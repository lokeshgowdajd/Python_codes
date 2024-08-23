import unittest
import subprocess
import time

class TestSoak(unittest.TestCase):

    def setUp(self):
        # Start the web server
        self.process = subprocess.Popen(["python", "app.py"])  # Replace "app.py" with your server script
        print("Web server started with PID:", self.process.pid)
        self.url = "http://127.0.0.1:8080"  # Replace with your web application's URL

    def test_soak(self):
        # Run the test for a specified duration (e.g., 1 hour)
        duration = 10  # 1 hour in seconds
        start_time = time.time()
        while time.time() - start_time < duration:
            # Check if the process is still running
            if self.process.poll() is not None:
                print("Application crashed with return code:", self.process.returncode)
                self.fail("Application crashed during soak test")
            time.sleep(1)  # Check every second
        print("Soak test completed successfully")

    def tearDown(self):
        # Terminate the application
        self.process.terminate()
        self.process.wait()
        print("Application terminated")

if __name__ == "__main__":
    unittest.main()
