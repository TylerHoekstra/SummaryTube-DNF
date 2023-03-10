# DNF2023

![Logo](https://user-images.githubusercontent.com/89994695/211187122-ebcb2927-fd96-4c75-88fc-b7acae400bc0.png)

## Inspiration

As a student, time is valuable. We are constantly budgeting time for assignments, projects, and review for several classes. For students, YouTube provides a readily accessible tool to explore new topics, or provide further clarification on an old one. A study by Ryerson University from 2019 showed that for 70% of consumers, YouTube is the first place they go to learn.  

A simple title is not always enough to know whether or not a video is worth your time, and YouTube creators do not always put descriptive summaries. Providing an accurate summary of a YouTube video can be extremely useful for students to decide whether or not a video is helpful to make more effective use of out time. 

## What It Does

SummaryTube is a website that takes a YouTube video link from the user as input and outputs a brief text-based summary of the video.

## How We Built It

The summary is generated based off of the closed-captions provided by YouTube for the video (pre-written transcripts/scripts produce best results, but auto-generated transcripts still produce consistently excellent results). The summary is created by GPT-3, the AI-based software from OpenAI, the predecessor to ChatGPT.

## Challenges We Ran Into

We had trouble getting our Flask server to interact (send and receive requests) with our server-side backend but we were able to get past that roadblock by consulting with one of the mentors, Connor.

## Accomplishments That We're Proud Of

We are most proud of the fact that we saw through the whole project, especially considering that all of us have limited experience with UI work.

## What We Learned

* Flask framework
* Front-end development
* Implementing APIs
* Web hosting

## What's Next For SummaryTube

We hope to improve the UI and make the design look better. We would like to create a more robust user experience.

## Constraints

The free version of openAI's GPT-3 has some built in constraints. Obviously there is the problem that one must use their own API-key in the summarize.py file. In addition there is a constraint of a maximum of 4097 words that can be said in the video; the average video with less than 4097 words has a maximum run-time of about 25 minutes. There is also a requirements.txt file  with all of the required dependencies needed to run the program.

## Demo

https://user-images.githubusercontent.com/89994695/211188986-e522266c-65da-4995-9b5f-ce94ec888d47.mp4
