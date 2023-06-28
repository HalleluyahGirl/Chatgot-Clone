import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": "0000 word on Nigeria Fuel Subsidy "}])
print(completion.choices[0].message.content)