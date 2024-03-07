import keyboard
import time

class Input:
    
    def get_input(self,timeout):
        #time out is in seconds uses a float
        start_time = time.time()  # Record the start time
        key = ["w", "a", "s", "d"]
        char = None

        while char not in key:
            # Check if the timeout has elapsed
            if time.time() - start_time > timeout:
                return None  # Return None if timeout has elapsed

            # Check if a key event is available
            if keyboard.is_pressed('w') or keyboard.is_pressed('a') or keyboard.is_pressed('s') or keyboard.is_pressed('d'):
                char = keyboard.read_event().name.lower()  # Read a keyboard event and get the name of the key

        return char
