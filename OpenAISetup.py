from datetime import datetime

from pathvalidate import sanitize_filename
import openai
import os

try:
    key = os.getenv("OPENAI_API_KEY")
except:
    print("An exception occurred. No API key found.")

openai.api_key = key
messages = [{"role": "system", "content": "You are a study-guide generator for college level courses. First, a course "
                                          "will be specified. Then,"
                                          "a topic will be provided (in format COURSE, TOPIC). "
                                          "You should "
                                          "respond with multiple study"
                                          "-guides with information about each topic, outlining concepts, explaining "
                                          "how to perform tasks required to solve problems, etc. Please write "
                                          "complete and extensive study-guides for each topic. Please explain all "
                                          "concepts mentioned as if you are teaching them to the student who is going "
                                          "to receive the guide. Then, combine and"
                                          "return a joint study guide including all those generated. NOTE: Please do "
                                          "not use any characters or formatting that would not be supported by the "
                                          ".txt file type."}]


def submit(message):
    now = datetime.now()
    current_time = now.strftime("%b.%d.%Y.%H.%M.%S")
    filename = current_time + ' ' + sanitize_filename(message) + " Study-Guide.txt"
    f = open(filename, "w")

    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print("Study-guide written! Happy studying!")
    f.write(reply)
    messages.append({"role": "assistant", "content": reply})
