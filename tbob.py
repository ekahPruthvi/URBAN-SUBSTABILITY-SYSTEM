import os
import time 
import re
from groq import Groq
from dotenv import load_dotenv
import Location
import Weather
import AQI

city=Location.gps_locator()
Weather.get_weather()
aqi=AQI.get_AQI()

print("\n")

if aqi:
    if aqi > 300:
        print(f"AQI:{aqi},Unhealthy BAD")
    elif aqi > 250:
        print(f"AQI:{aqi},BAD")
    elif aqi > 100:
        print(f"AQI:{aqi},Satisfactory")
    elif aqi > 50:
        print(f"AQI:{aqi},Good")
else:
    print("City not in registory(URBAN ONLY)")

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

if not api_key:
    print("no api key found")
    exit()

client=Groq(api_key=api_key)

def clean_response(text):
    text = re.sub(r"(?:Alright|Okay|Hmm).*?Let me start by .*?", "", text, flags=re.IGNORECASE).strip()
    return text

messages = []
pre = []

print("\n💬 Welcome to NoPlanetB (Groq - LLaMA 70B)")
print("Type 'exit' to end the conversation.\n")

pre=f"Pretend you are an sustanibility expert, \"URBAN SUBSTABILITY SYSTEM\" and I live in {city} with AQI {aqi} and only answer to questions related to my city and Sustanibility. Help me with managing my house and my city. Don't answer any other questions unrelated give a very short reply saying the question is unrelated. Don't reply back to this promt. "

while True:
    user_input = input("You: ")
    full_response = ""
    if user_input.lower() == "exit":
        end="Exiting"
        for char in end:
            full_response += char
            print(char, end="", flush=True)
            time.sleep(0.1)
        print("\n")
        time.sleep(1)
        break

    messages.append({"role": "user", "content": pre + user_input})

    print("URBAN SUBSTABILITY SYSTEM: ", end="", flush=True)
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=messages,
            max_tokens=500,
        )
        ai_reply = response.choices[0].message.content
    except Exception as e:
        ai_reply = f"❌ Error: {e}"

    ai_reply = clean_response(ai_reply)

    full_response = ""
    for char in ai_reply:
        full_response += char
        print(char, end="", flush=True)
        time.sleep(0.01)
    print("\n")

    messages.append({"role": "assistant", "content": ai_reply})