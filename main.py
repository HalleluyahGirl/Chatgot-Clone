import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a senior Developer at openCode.hq"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "OpenCode")

demo.launch(share=True)