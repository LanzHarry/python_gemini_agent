import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

# parse input arguments
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args() # gives access to args.user_prompt

# load dotenv and read the gemini API key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("API key not found")

# use the API key to get a response from gemini
client = genai.Client(api_key=api_key)

# list of types.Content to hold message history
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

model_response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = messages)

if model_response.usage_metadata is not None:
    prompt_token_count = model_response.usage_metadata.prompt_token_count
    candidates_token_count = model_response.usage_metadata.candidates_token_count
else:
    raise RuntimeError("No usage metadata, API request has likely failed")

if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {prompt_token_count}\nResponse tokens: {candidates_token_count}")

print(model_response.text)

