from google import genai

client = genai.Client(api_key="paste-your-gemini-key-here")

message = input("You: ")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=message
)

print("AI:", response.text)
