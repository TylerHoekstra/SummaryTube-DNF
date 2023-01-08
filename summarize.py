import os
import openai

def summarize(text_to_summarize):
    openai.api_key = "<INSERT API-KEY>"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Summarize this text:\n\n" + text_to_summarize,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response["choices"][0]["text"]
