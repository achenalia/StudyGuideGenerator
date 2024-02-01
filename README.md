****Preparation****

To use the generator, you first need to obtain your OpenAI API key. Follow these instructions to access your key:

  Step 1: Create an account on OpenAI and log into an account.
  
  Step 2: After login click on ‘Personal‘ on the top-right side and then click on ‘View API keys‘ as seen in the below image.
  
  Step 3: A page of API keys is then opened and we can see the button ‘Create new secret key’ click on that and a secret key is generated copy that key and save it on Notepad or anywhere else because it is required in upcoming steps.
  
  **_Next Steps for Windows_**
  
    Step 4: Press the Windows button and type "environment variables" and select this option:
    
  ![image](https://github.com/ngholomennod/StudyGuideGenerator/assets/116604264/a276c973-7066-4b19-a5a6-a4170c894a40)
    
    Step 5: Click on 'Environment Variables':
    
  ![image](https://github.com/ngholomennod/StudyGuideGenerator/assets/116604264/a882af74-6e8a-43b4-b6f6-3c1498b2e2b7)
    
    Step 6: Under the user variables list (the table on the top), click 'new,' then input OPENAI_API_KEY as the name, with your api-key as the variable value.

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

  Step 10: Run App.py, and get started with your study-guide generation! Happy studying!
