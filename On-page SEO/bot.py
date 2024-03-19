import pandas as pd
import pyautogui
import pyperclip
import webbrowser
import time
from pynput.keyboard import Key, Controller as KeyboardController
from bs4 import BeautifulSoup
import requests


# Initialize keyboard controller from pynput
keyboard = KeyboardController()

# List to store the new SEO changes
seo_changes_data = []
# Load the CSV file
df = pd.read_csv('docsSEO.csv')

# List to store the new SEO changes
seo_changes_data = []

# Set a delay for each operation to ensure the UI responds as expected
pyautogui.PAUSE = 2

# Image file name for the element to be clicked
target_image = 'screenshot.png'  # Replace with the path to your screenshot

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Prepare the text to be pasted
    url = row['URLS']
    focus_keyword = row['Focus keyword']
    text_to_paste = f"in this url \"{url}\" use the keyword \"{focus_keyword}\" to write a Meta Title and Meta Description . Also add '| Dyte Docs' at the end of each Meta title"

    # Open the web browser and navigate to the website
    webbrowser.open('https://chat.openai.com')
    time.sleep(5)  # Wait for the page to load

    # Copy the text to the clipboard
    pyautogui.write(text_to_paste)
    pyautogui.hotkey('ctrl', 'c')

    # Short delay to ensure the page is ready
    time.sleep(2)

    # Simulate Ctrl+V to paste the text
    pyautogui.hotkey('ctrl', 'v')

    # Allow time for the text to be pasted and any action to be taken
    time.sleep(4)

    # Press Enter to submit the query
    pyautogui.press('enter')

    # Wait for the response
    time.sleep(18)

   
     # Send the key strokes for holding down Control, Shift, and C
    with keyboard.pressed(Key.cmd_l):  # Use 'cmd' instead of 'ctrl' for Mac
        with keyboard.pressed(Key.shift):
            keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.shift)

    
    

    # Allow time for the action to be processed
    time.sleep(5)
    
    # Get the copied text from the clipboard
    copied_text = pyperclip.paste()

    # Store the copied text in the "SEO Changes" column of the DataFrame
    df.at[index, 'SEO Changes'] = copied_text

    # Save the updated DataFrame back to the CSV file
    df.to_csv('docsSEO.csv', index=False)

    # Print progress
    print(f"Processed URL: {url}. Moving to the next one...")
    time.sleep(5)

# Create a DataFrame from the seo_changes_data list
seo_changes_df = pd.DataFrame(seo_changes_data)

print("Script completed.")
