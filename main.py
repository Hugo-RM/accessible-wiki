# Course: Python Multimedia Programming
# Title: Wikipedia Accessibility Webpage
# Group: [Removed for Privacy]
# Date: 5/15/2025
# Abstract:
# This is a website that allows user to access wikipedia pages that will automatically relay the information in audio format.
# The website is meant to be for people who learn better through audio or those that have trouble visually, such as blind people.

from flask import (Flask, render_template, request, redirect, url_for)
from flask_bootstrap import Bootstrap5
from speech_to_text import SpeechToText
from gtts import gTTS
import tts as tts
import wikipediaapi

# The base app is run with bootstrap.
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# The wikipediaAPI is called upon
wiki_wiki = wikipediaapi.Wikipedia(user_agent='Eperegoy', language='en')
stt = SpeechToText()

# The initial route for the index page.
@app.route('/', methods=('GET', 'POST')) # assuming we'll pass info this way, added methods
def home():
   if request.method == 'POST':

      # This is to make sure that the button to head back to index works accurately
      if request.form.get('topic') is None: 
            return redirect(url_for('home'))

      # This will take the user from whatever topic given to the proper wikipage
      topic = request.form.get('topic')
      return redirect(url_for('wikipage', topic=topic))
   
   return render_template('index.html')

# The code for the wikipage in order to also take you to the section page.
@app.route('/wikipage', methods=('GET', 'POST'))
def wikipage():

   # This makes sure that the information of the topic and section are passed through to the wection page
   if request.method == 'POST':
      topic = request.form.get('topic')
      section_title = request.form.get('section')
      return redirect(url_for('section', section_title = section_title, topic = topic))
   
   # This gains the topic, in order to search within the wikipedia api with the various information
   topic = request.args.get('topic', '')
   page = wiki_wiki.page(topic)
   
   topic = page.title
   summary = page.summary
   sections = page.sections
   
   # This determines that if there's no information found, it will give a brief statement and audio file for it
   if summary.strip() == '':
      summary = f'Sorry, there is no wikipedia page for {topic}'
   tts.convertText(topic,summary)
   
   return render_template('wikipage.html', topic=topic, summary=summary, sections=sections)

# The section page in order to have all information given.
@app.route('/section', methods=('GET', 'POST'))
def section():
   # This is to place back the topic information to head back into the wikipage
   if request.method == 'POST':
      topic = request.form.get('topic')
      return redirect(url_for('wikipage', topic=topic))

   # This gets the section title and various information from the wikipediaAPI
   section_title = request.args.get('section_title', '')
   topic = request.args.get('topic', '')
   page = wiki_wiki.page(topic)
   section = page.section_by_title(section_title)

   # Old code kept for safety. In the case no such section exists, a brief explanation would be given
   if not section:
      return render_template('section.html', title="Section Not Found", summary="No such section in this page.", topic=topic)

   title = f"{topic} - {section_title}"
   summary = section.text

   # If there is no information in the section, will give a brief explanation instead
   if summary.strip() == '':
      summary = 'Sorry, there is no text in this section'
   tts.convertText(title,summary)

   return render_template('section.html', title=title, summary = summary, topic = topic)

# The section for the mic in order to use the speech-to-text function. Worked on by Hugo
@app.route('/mic', methods=('POST',))
def mic_button():
   stt.toggle()
   return redirect(url_for('home'))

# Uses the mic to check for text through the speech-to-text function. Worked on by Hugo
@app.route('/check_for_text', methods=('GET',))
def check_for_text():
    recognized_text = stt.get_recognized_text()
    if recognized_text:
        stt.toggle()
        return {'found': True, 'topic': recognized_text}
    else:
        return {'found': False}