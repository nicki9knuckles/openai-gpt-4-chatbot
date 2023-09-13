import openai
import os
from dotenv import load_dotenv
import os
import argparse
from query import query

load_dotenv(".env")

openai.api_key = os.getenv("OPENAI_API_KEY")


def bold(text):
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    return bold_start + text + bold_end


def blue(text):
    blue_start = "\033[34m"
    blue_end = "\033[0m"
    return blue_start + text + blue_end


def red(text):
    red_start = "\033[31m"
    red_end = "\033[0m"
    return red_start + text + red_end


def main():
    parser = argparse.ArgumentParser(description="Simple command line chatbot")
    parser.add_argument(
        "--personality",
        type=str,
        help="A brief summary of the chatbot's personality",
        default="Friendly and helpful",
    )
    args = parser.parse_args()

    initial_prompt = f"You are a conversation chatbot. Your personality is: {args}"
    messages = [
        {
            "role": "system",
            "content": initial_prompt,
        }
    ]

    while True:
        try:
            # Get user input
            user_input = input(bold(blue("You: ")))
            # Add user input to messages
            messages.append({"role": "user", "content": user_input})

            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )
            # Add chatbot response to messages
            messages.append(res["choices"][0]["message"].to_dict())

            print(bold(red("Assistant: ")), res["choices"][0]["message"]["content"])
        except KeyboardInterrupt:
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
