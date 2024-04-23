from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
tokens = []
loop = True
print("AI CHAT-BOT")
while loop:
    print("\n")
    inputTest = input()
    with model.chat_session():
        for token in model.generate(inputTest, streaming=True):
            tokens.append(token)

    output = "".join(tokens)     
    print(output)
    inputTest = ""
    tokens.clear()