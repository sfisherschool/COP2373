import re

def count_sentences(text):
    # Pattern to match sentences
    # (This had to be modified from what was in section 7.4 to properly display the full sentences
    # and account for sentences that start with a number or non-capital letter)
    pat = r'[^.!?]*[.!?]'

    # Find all sentences in the text
    sentences = re.findall(pat, text, flags=re.DOTALL | re.MULTILINE)

    # Print each sentence
    for i in sentences:
        print('->', i)

    # Print the total number of sentences
    print(f'Total number of sentences: {len(sentences)}')

def main():
    # Prompt the user to enter sentences
    text = input("Enter sentences here: ")

    # Call the count_sentences function with the user's input
    count_sentences(text)

# Call the main function
main()
