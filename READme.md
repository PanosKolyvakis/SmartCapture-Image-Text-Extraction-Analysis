Keyboard-SnippingTool-Extraction-ToGPT

## Overview
The present is a macOS Quick Action automation tool that captures a selected screen area, performs OCR (Optical Character Recognition) to extract text from the image, and then processes the text using OpenAI's GPT-3.5-turbo model or GPT-4 (or any other model available on the API). The actionable insights or answers generated by the AI are then displayed in a text file, creating an end-to-end workflow from image capture to insightful analysis. The bash script can be bound to the MacOS keyboard (e.g. cmd + shift + m) to generate a snipping tool that directly selects the desired text and produces a GPT response which automatically opens on a textbox.

Added - IDE- like code functionality. A lot of processing of GPT responses to seperate the result nicely into a tk GUI
Example use:
Using the snipping tool to rewrite an email:


<img width="427" alt="Screenshot 2024-01-26 at 20 06 50" src="https://github.com/PanosKolyvakis/Keyboard-SnippingTool-Extraction-ToGPT/assets/114179217/dedb9176-8c2b-4973-bf92-2b5bfae8b649">


*** Modify the prompt on the main.py according to what you are trying to do ***
## Setup
To use SmartCapture, follow these steps to set up the environment and dependencies on your Mac:

### Prerequisites
- macOS with Automator.

- Python 3 installed and accessible within a Conda environment.
- Tesseract OCR installed (`brew install tesseract` using Homebrew).
- An OpenAI API key with access to the GPT-3.5-turbo model.

### Step 1: After creating and activating your conda environment Clone the Repository (should work with venv as well)
```bash
git clone https://github.com/PanosKolyvakis/Keyboard-SnippingTool-Extraction-ToGPT
cd -to directory
```

### Step 2: Install Python Dependencies
Install the required Python dependencies using the provided requirements.txt file:

```bash
conda install -r requirements.txt
```
### Step 3: Set the OpenAI API Key
Set your OpenAI API key as an environment variable on your Mac for security:

```bash
export OPENAI_API_KEY='your-api-key-here'
```
For a permanent setup, add this line to your ~/.zshrc or ~/.bash_profile and run source on the respective file or restart your terminal.

### Step 4: Automator Service
Save the provided Automator workflow as a Quick Action on your Mac. Check Screenshot file for help.
## Step 4: Automator Service


      1. **Open Automator**:
         - Find Automator in your Applications folder and open it.
         - Choose "New Document" when prompted.
      
      2. **Create a Quick Action**:
         - Select "Quick Action" as the type of your new Automator document.
      
      3. **Configure the Quick Action**:
         - In the top panel, set the "Workflow receives" dropdown to "no input" to ensure that the Quick Action doesn't expect any file or text input.
         - Choose "any application" or a specific application from which you want the Quick Action to be available.
      
      4. **Add a Run Shell Script Action**:
         - Search for the "Run Shell Script" action in the Actions library on the left side.
         - Drag the "Run Shell Script" action to the workflow area on the right.
         - Set "Shell" to `/bin/zsh`.
         - Paste your shell script into the text area provided in the "Run Shell Script" action.
      
      5. **Save the Quick Action**:
         - Go to File > Save and give your Quick Action a meaningful name, like "SmartCapture."
      
      6. **Test the Quick Action**:
         - You can test the Quick Action within Automator by pressing the "Run" button at the top right corner of the window.
         - Alternatively, access the Quick Action from the Services menu by right-clicking on the desktop or Finder and navigating to Services > SmartCapture (or whatever name you've given).
  



### Step 5: Keyboard Shortcut
Bind the Quick Action to a keyboard shortcut in System Preferences:

Go to System Preferences > Keyboard > Shortcuts.
Select Services from the sidebar and find your saved Quick Action.
Add a Shortcut by clicking on none and then pressing your desired key combination.


