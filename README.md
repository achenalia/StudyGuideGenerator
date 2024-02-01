****Preparation****

To use the generator, you first need to obtain your OpenAI API key. Follow these instructions to access your key:

  Step 1: Create an account on OpenAI and log into an account.
  
  Step 2: After login click on ‘Personal‘ on the top-right side and then click on ‘View API keys‘ as seen in the below image.
  
  Step 3: A page of API keys is then opened and we can see the button ‘Create new secret key’ click on that and a secret key is generated copy that key and save it on Notepad or anywhere else because it is required in upcoming steps.
  
  **_Next Steps for Windows (Using Command Prompt)_**
  
    Step 4: Press the Start button, type "cmd" or "Command Prompt" in the search bar, right-click on "Command Prompt" from the search results, and choose "Run as administrator" to open a Command Prompt with administrative privileges.
  
    Step 5: In the Command Prompt, enter the following command to set the environment variable: setx OPENAI_API_KEY "your_api_key_here"
      Replace "your_api_key_here" with your actual OpenAI API key.

    Step 6: Close the Command Prompt to apply the changes. You may need to reopen any command prompts or applications to see the updated environment variable.

    Note: Ensure that you run the Command Prompt as an administrator to have the necessary permissions to set system-wide environment variables.
  
  **_Next Steps for Mac_**

    Step 4: Press Command + Space to open Spotlight Search, then type "Terminal" and press Enter to open the terminal.
  
    Step 5: In the terminal, type the following command and press Enter: nano ~/.bash_profile
  
    Step 6: In the nano text editor, add the following line at the end of the file: export OPENAI_API_KEY=your_api_key_here
      Replace "your_api_key_here" with your actual OpenAI API key.
  
    Step 7: Save the changes by pressing Control + X, then press Y to confirm, and finally press Enter.

  **_Next Steps for Linux (Bash Shell)_**
  
    Step 4: Open a terminal window. You can do this by searching for "Terminal" in your application menu or using the keyboard shortcut Ctrl + Alt + T.
  
    Step 5: In the terminal, open your profile file using a text editor. Depending on your distribution and shell, this file could be ~/.bashrc, ~/.bash_profile, ~/.zshrc, or something similar. For example, using nano: nano ~/.bashrc
  
    Step 6: Add the following line at the end of the file: export OPENAI_API_KEY=your_api_key_here
          Replace "your_api_key_here" with your actual OpenAI API key.
  
    Step 7: Save the changes by pressing Ctrl + X, then press Y to confirm, and finally press Enter.
  
    Step 8: To apply the changes, either restart your terminal or run the following command: source ~/.bashrc

  **_AFTER ADDING YOUR API KEY AS ABOVE PER YOUR OS_**

  Step 9: Open your terminal and enter the directory in which you have cloned this repository, and run: pip install -r requirements.txt

  Step 10: Run StudyGuideGenerator.py, and get started with your study-guide generation! Happy studying!
