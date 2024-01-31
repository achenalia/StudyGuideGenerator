from datetime import datetime

import openai
import os

try:
    key = os.getenv("OPENAI_API_KEY")
except:
    print("An exception occurred. No API key found.")

openai.api_key = key
messages = [{"role": "system", "content": "You are a study-guide generator for college level courses. First, a course "
                                          "will be specified. Then,"
                                          "a topic will be provided (in format COURSE, TOPIC) or a list of topics for "
                                          "that course (in format COURSE, [TOPIC1, TOPIC2, TOPIC3]. You should "
                                          "respond with multiple study"
                                          "-guides with information about each topic, outlining concepts, explaining "
                                          "how to perform tasks required to solve problems, etc. Please write "
                                          "complete and extensive study-guides for each topic. Please explain  all "
                                          "concepts mentioned as if you are teaching them to the student who is going "
                                          "to receive the guide. Then, combine and"
                                          "return a joint study guide including all those generated."}]


# message = input("Please enter a topic following a course (ex. Computer Science, big-o notation).\nYou may also "
#                 "provide a list of topics by placing them between brackets (ex. Computer Science, [data structures, "
#                 "big-o notation, tuples]).\nNOTE: For more detailed and extensive guides, please run the program one "
#                 "at a time for each topic using the first method described.\nEnter <COURSE, TOPIC> or <COURSE, "
#                 "[TOPIC1, TOPIC2, TOPIC3]>:")

def submit(message):
    now = datetime.now()
    current_time = now.strftime("%b.%d.%Y.%H.%M.%S")
    filename = current_time + ' ' + ''.join([message]) + " Study-Guide.txt"
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