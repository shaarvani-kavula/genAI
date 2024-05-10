import openai 
from prompt_template import prompt_text


# Set your API key
api_key = "YOUR_API_KEY"

# Initialize OpenAI's API client
openai.api_key = api_key

question_to_ask = "How do I ask for more support at work? Answer precisely." + prompt_text

# Generate text using the GPT model
response = openai.Completion.create(
  engine="text-davinci-003",  # Specify the engine (choose the one you have access to)
  prompt=question_to_ask,
  max_tokens=200  # Adjust as needed
)

# Print the generated text
print(response.choices[0].text.strip())
