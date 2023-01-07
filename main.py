import transcript
import summarize

def main():
    link = input()
    text = transcript.youtubeLinkInput(link)
    summary = summarize.summarize(text)

if __name__ == "__main__":
    main()