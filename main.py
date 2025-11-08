import os
import time

from functions import *

# Create chatbot
home_bot = create_bot("Jordan")
db_path = "db.sqlite3"

is_trained = os.path.exists(db_path)

if not is_trained:
    print("First run detected - training bot...")
    train_all_data(home_bot)

    custom_train(home_bot, [
        "Who is the owner of this house?",
        "Mark Nicholas is the owner of this house."
    ])
else:
    print("Database found - skipping training.")

# Train the bot with general data
train_all_data(home_bot)

identity = input("State your identity please: ")
# Rules for responding to different identities
if identity == "Mark":
    print("Welcome, Mark. Happy to have you at home.")
    time.sleep(3)  # Add a delay to let the welcome message display

elif identity == "Jane":
    print("Mark is out right now, but you are welcome to the house.")
    time.sleep(3)  # Add a delay here as well

else:
    print("Your access is denied here.")
    exit()

# Train the bot with custom data
house_owner = [
    "Who is the owner of this house?",
    "Mark Nicholas is the owner of this house."
]

custom_train(home_bot, house_owner)

print("------ Training custom data ------")
if identity == 'Mark':
    personal_data = {
        "Where was I born?": "Mark, you were born in Seattle.",
        "What is my favourite book?": "Your favourite book is The Great Gatsby.",
        "What is my favourite movie?": "You have watched Interstellar more times than I can count.",
        "What is my favourite sport?": "You have always loved baseball.",
    }

    # Train chatbot with your custom data
    for q, a in personal_data.items():
        custom_train(home_bot, [q, a])

# Start the chatbot
start_chatbot(home_bot)
