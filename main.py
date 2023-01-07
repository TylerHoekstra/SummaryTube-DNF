from youtube_transcript_api import YouTubeTranscriptApi

link = input()

if link.find("youtube") != -1:
    yID = link.split('=')[1]
    yID = yID.split('&')[0]
elif link.find("youtu.be") != -1:
    yID = link.split('be')[1]
    yID = yID.split('/')[1]

transcriptWithTime = YouTubeTranscriptApi.get_transcript(yID)

string = ""
for trans in transcriptWithTime:
    if trans['text'].find('[') == -1:
        string += trans["text"] + ' '

print(string)