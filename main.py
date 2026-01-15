import os
from dotenv import load_dotenv
from google import genai

# load dotenv and read the gemini API key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("API key not found")

# use the API key to get a response from gemini
client = genai.Client(api_key=api_key)

model_response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")

if model_response.usage_metadata is not None:
    prompt_token_count = model_response.usage_metadata.prompt_token_count
    candidates_token_count = model_response.usage_metadata.candidates_token_count
else:
    raise RuntimeError("No usage metadata, API request has likely failed")

print(f"Prompt tokens: {prompt_token_count}\nResponse tokens: {candidates_token_count}")

print(model_response.text)
