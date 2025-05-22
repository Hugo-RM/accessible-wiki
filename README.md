Team 8242
- Team Members: [Redacted for privacy, was 4 members total]  
- Class: Multimedia Design & Programming
- GitHub Repository Link: [Removed for Privacy]
- Trello Board: [Removed for Privacy]

To run program:
1. Unzip to folder of your choosing
2. (if you have one) Activate your python environment
   Note: some dependecies may be needed; Used are: Flask, Bootstrap-Flask, wikipedia-api, gTTs, etc.
3. install dependecies (preferably in environment)
   - pip install Flask
   - pip install bootstrap-flask
   - pip install wikipedia-api
   - pip install gTTs
   - pip install SpeechRecognition
   - pip install PyAudio
4. Run Program and copy given http address to put in search bar
   flask --app main.py --debug run

Example process:
   # Open PowerShell or terminal
   ```.sh
   PS C:\Users\YourUsername>
   ```
   
   # (Optional) Open Virtual Environment with dependencies installed
   ```.sh
   ./venv_name/Scripts/Activate.ps1
   ```
   
   # Navigate to your project directory
   ```.sh
   PS C:\Users\YourUsername> cd "C:\Users\YourUsername\Documents\accessible-wiki"
   ```
   
   # Run the Flask application
   ```.sh
   (yourenv) PS C:\Users\YourUsername\Documents\accessible-wiki> flask --app main.py --debug run
   ```
   
   # Output:
   ```.sh
      * Serving Flask app 'main.py'
      * Debug mode: on
   WARNING: This is a development server. Do not use it in a production deployment.
      * Running on http://127.0.0.1:5000
   # -> Copy this address into your web browser
   Press CTRL+C to quit
   ```

Future Work:
- Could add a feature to delete audio files in order to save memory space
- Add other potential languages that the text to speech could use
- Improve the speech to text in order to search for more complex pages
- Implement the speech to text for the topic's sections
- Add some sort of aspect to check for images within the sections
- Allow some way to track the user for a set amount of time with the files
- Create a more streamlined design
