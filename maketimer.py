import time

def make_timer(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret_val = func(*args, **kwargs)
        t2 = time.time()
        print('Time elapsed was', t2-t1)
        return ret_val
    return wrapper

# initiate spam words list
spam_words = ["Act Now", "Last Chance", "Claim Your Prize", "Urgent", "Free Gift",
"Earn Millions", "Instant Results", "Strongest Ever", "Cash Bonus", "Credit Score",
"Debt Relief", "Best Rates", "bankruptcy", "Click this link", "Weight loss", "No catch",
"100% free", "Additional income", "Be your own boss", "Best price", "Miracle", "You won",
"Free sample", "Consolidate debt", "Double your cash", "Double your income",
"Earn extra cash", "Earn money", "Eliminate bad credit"]


# Decorator that applies the make_timer function to check_spam
@make_timer
def check_spam(email):
    # initiate spam_score and spam_trigger variables
    spam_score = 0
    spam_triggers = []
    # loop through each word in the spam_words list
    for word in spam_words:
        # if a word in the word list is in the email message +1 to spam score and
        # add the matching word to the spam_triggers list
        if word.lower() in email.lower():
            spam_score += 1
            spam_triggers.append(word)
        # add a sleep to make the function take some time
        time.sleep(0.1)
    # initiate likelihood to low
    likelihood = "Low"
    # if more than 3 spam words found set likelihood to medium
    if spam_score > 3:
        likelihood = "Medium"
    # if more than 5 spam words found set likelihood to high
    if spam_score > 5:
        likelihood = "High"
    return spam_score, likelihood, spam_triggers

# grab the email message from the user and save to email variable
email = input("Enter your email message: ")

# initiate spam_score, likelihood, spam_triggers to the returned values from
# check_spam function worth noting these
# variables while named the same are different and in a different scope than the
# ones inside the function
spam_score, likelihood, spam_triggers = check_spam(email)

# print results
print(f"Spam Score: {spam_score}")
print(f"Likelihood of being spam: {likelihood}")
print(f"Trigger words/phrases: {spam_triggers}")
