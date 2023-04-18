import openai
import os
from string import digits
from dotenv import load_dotenv

load_dotenv()


if os.path.exists("../../prompts.txt"):
    os.remove("../../prompts.txt")
else:
    pass
f = open("../../prompts.txt", "w")

openai.api_key = input("Enter API Key: ")
topic = input("Enter topic: ")


# Set up the model and prompt
model_engine = os.getenv("MODEL")
prompt = "Think of 10 one word subtopics around " + topic


# Generate a response
completion = openai.ChatCompletion.create(
    model=model_engine,
      messages=[
    {"role": "system", "content": "Do not include numbers in your response"},
    {"role": "user", "content": prompt}
    ],   
    max_tokens=4000,
    temperature=0,
)   

response = completion['choices'][0]['message']['content'].split('\n')
parsed = []
remove_digits = str.maketrans('', '', digits)
print("Generating prompts into a prompts.txt files. Please do not close the console")
f.write(completion['choices'][0]['message']['content'].translate(remove_digits).replace('-', '').replace('.', ''))
f.write("\n")

for category in response:
    newCategory = category.translate(remove_digits).replace('-', '').replace('.', '').replace(' ', '')
    parsed.append(newCategory)

f.write("----------------------------------------------------------------------\n")

for filtered in parsed:
    prompt = "Generate 20 open ended but engaging one sentence prompts for a support group about " + filtered + " and " + topic + ". Remove the numbering from your response "
    completion = openai.ChatCompletion.create(
    model=model_engine,
      messages=[
    {"role": "system", "content": "Do not include numbers in your response"},
    {"role": "user", "content": prompt}
    ],   
    max_tokens=4000,
    temperature=0,)   
    response = completion['choices'][0]['message']['content'].translate(remove_digits).replace('-', '').replace('.', '')
    f.write(response)

f.close()
print("done")






