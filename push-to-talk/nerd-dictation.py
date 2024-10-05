import time
from pynput import keyboard

# Global variable to track if dictation is active
is_dictating = False


# Function to handle key press
def on_press(key):
    global is_dictating
    if key == keyboard.Key.alt_l and not is_dictating:
        is_dictating = True
        nerd_dictation_resume()


# Function to handle key release
def on_release(key):
    global is_dictating
    if key == keyboard.Key.alt_l and is_dictating:
        is_dictating = False
        nerd_dictation_suspend()
        time.sleep(0.1)  # Small delay to ensure dictation is suspended
        keyboard.Controller().press(keyboard.Key.enter)
        keyboard.Controller().release(keyboard.Key.enter)


# Set up the keyboard listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()


# Function to process dictation input
def nerd_dictation_process(text):
    global is_dictating
    if is_dictating:
        return text
    return ""


# Function to resume dictation (to be called by nerd-dictation)
def nerd_dictation_resume():
    pass  # nerd-dictation will handle the actual resuming


# Function to suspend dictation (to be called by nerd-dictation)
def nerd_dictation_suspend():
    pass  # nerd-dictation will handle the actual suspending


# Keep the script running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    listener.stop()
