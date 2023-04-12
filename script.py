import openai
import os
from string import digits
from dotenv import load_dotenv

load_dotenv()

# Set up the OpenAI API client
openai.api_key = os.getenv("API_KEY")

# Set up the model and prompt
model_engine = os.getenv("MODEL")
topic = "autoimmune disorders"
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
for category in response:
    newCategory = category.translate(remove_digits).replace('-', '').replace('.', '').replace(' ', '')
    parsed.append(newCategory)
    print(newCategory)
print("----------------------------------------------------------------------------------------------")
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
    print(response)





