from youtube_transcript_api import YouTubeTranscriptApi

link = input()
#yID = link.
#https://youtu.be/sy54UlVjTTA
yID = "sy54UlVjTTA"

# assigning srt variable with the list
# of dictionaries obtained by the get_transcript() function
srt = YouTubeTranscriptApi.get_transcript(yID)

# prints the result
print(srt)