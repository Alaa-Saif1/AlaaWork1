import openai

openai.api_key = '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'

def send_message(message):
response = openai.Completion.create(
engine='text-davinci-003',
prompt=message,
max_tokens=50,
temperature=0.7,
n=1,
stop=None,
)
return response.choices[0].text.strip()
while True:
user_input = input("Ask Me AnyThings: ")
bot_response = send_message(user_input)
print("Bot:", bot_response)