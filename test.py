import transcript
import summarize

def main():
    link = input("Enter a link: ")
    text = transcript.youtubeLinkInput(link)
    summary = summarize.summarize(text)
    print(summary)

if __name__ == "__main__":
    main()
