# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# tokenizer = AutoTokenizer.from_pretrained("pszemraj/long-t5-tglobal-base-16384-book-summary")

# model = AutoModelForSeq2SeqLM.from_pretrained("pszemraj/long-t5-tglobal-base-16384-book-summary")
# model.predict("The impedance transformer is intended to maximize power transfer from the amplifier to the speaker. The speaker has a very small impedance of only 8 Ω, and designing an amplifier with an output resistance this small would be a difficult task. It would require very low resistances throughout the circuit, leading to very high currents and an increase in dissipated heat (and, therefore, wasted energy). It is necessary for the amplifier to have a much larger output resistance than 8 Ω, but connecting the speaker and amplifier directly would result in very poor power transfer. Maximum power transfer theorem states that maximum power is transferred from source to load when the impedance of the source and load match - thus, to match the impedance of the source (amplifier circuit) and load (speaker), an impedance transformer is required.")

import os
import openai

def summarize(text_to_summarize):
    openai.api_key = "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"

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
