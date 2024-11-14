import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

# Initialize Google Gemini AI
api_key = "AIzaSyCSq_m1c24gZMd10pQ6Irou6F-v5BfwxXo"
genai.configure(api_key=api_key)

# Set the generation configuration for Gemini model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Start the Gemini AI model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="",
    tools=[genai.protos.Tool(function_declarations=[])]
)

# Start a chat session with the Gemini model
chat_session = model.start_chat(history=[])

def handle_default_response(SSTinput):
    response = chat_session.send_message(SSTinput)
    print("Gemini Response:", response.text)

def start_chat():
    while True:
        SSTinput = input("Please type something: ")
        handle_default_response(SSTinput)

def Program_Init():
    print("Initializing program...")
    start_chat()

if __name__ == "__main__":
    Program_Init()
