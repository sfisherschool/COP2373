import random

def write_responses_to_file(filename, responses):
    try:
        with open(filename, 'w') as file:
            for response in responses:
                file.write(response + '\n')
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def read_responses_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file]
    except Exception as e:
        print(f"An error occurred while reading from the file: {e}")
        return []

def ask_question(responses):
    while True:
        question = input("Ask a yes/no question: ")
        if question:
            print(random.choice(responses))
            while True:
                quit = input("Do you want to ask another question? (yes/no): ").lower()
                if quit in ['yes', 'no']:
                    return quit == 'no'
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
        else:
            print("Invalid input. Please ask a question.")

def magic_8_ball():
    responses = ["Yes, of course!",
                 "Without a doubt, yes.",
                 "You can count on it.",
                 "For sure!",
                 "Ask me later!",
                 "I'm not sure.",
                 "I can't tell you right now.",
                 "I'll tell you after my nap.",
                 "No way!",
                 "I don't think so.",
                 "Without a doubt, no.",
                 "The answer is clearly NO!"]

    filename = '8ball_responses.txt'
    write_responses_to_file(filename, responses)
    responses = read_responses_from_file(filename)

    while not ask_question(responses):
        pass

magic_8_ball()
