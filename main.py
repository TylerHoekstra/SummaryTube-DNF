#import transcript
#import summarize

def main():
    #link = input()
    #text = transcript.youtubeLinkInput(link)
    #summary = summarize.summarize(text)
    #return summary
    return "This proves that all this works"

from flask import Flask, request
import json

# start of David's code 

app = Flask(__name__, static_url_path='')

# pull static files(index.html) using our flask server 
@app.route('/', methods=['GET'])
def root():
    return app.send_static_file('index.html')

@app.route('/api/process_video', methods=['POST'])
def process_text():
  # Parse the request body
  data = request.get_json()
  
  # Extract the text from the request body
  text = data['inputUrl']
  
  # Process the text
  processed_text = main()
  
  # Return the processed text as a response
  return processed_text

if __name__ == '__main__':
  app.run(port = 8000)