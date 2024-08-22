import threading
import time

class MyTask:
    def print_numbers(self):
        for i in range(1, 6):
            print(f"Number: {i}")
            time.sleep(1)  # Simulate some work with a sleep

    def print_letters(self):
        for letter in 'abcde':
            print(f"Letter: {letter}")
            time.sleep(1)  # Simulate some work with a sleep

    def start_threads(self):
        # Create threads targeting the class methods
        thread1 = threading.Thread(target=self.print_numbers)
        thread2 = threading.Thread(target=self.print_letters)

        # Start the threads
        thread1.start()
        thread2.start()

        # Wait for both threads to finish
        thread1.join()
        thread2.join()

        print("Both threads have finished execution.")

my_task = MyTask()

# Start the threads from within the class
my_task.start_threads()
