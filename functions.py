# Function to create the chatbot
def create_bot(name):
    """
        Create and return a ChatBot instance with the given name.
        The bot uses BestMatch logic adapter and persists data in SQLite.
    """
    from chatterbot import ChatBot  # Import the ChatBot class from the ChatterBot library
    return ChatBot(
        name=name,  # Set the name of the bot (e.g., EduBot)
        read_only=False,  # Allow the bot to learn from user input during conversations
        logic_adapters=[
            "chatterbot.logic.BestMatch"
        ],  # Use the BestMatch logic adapter for dynamic responses
        storage_adapter="chatterbot.storage.SQLStorageAdapter",  # Store data persistently in an SQLite database
        database_uri="sqlite:///db.sqlite3",  # Set the database URI
    )


def train_all_data(bot):
    """
    Train the bot with ChatterBot's English corpus.
    """
    from chatterbot.trainers import ChatterBotCorpusTrainer  # Import the corpus trainer class
    corpus_trainer = ChatterBotCorpusTrainer(bot)  # Initialize the trainer with the bot
    corpus_trainer.train("chatterbot.corpus.english")  # Train the bot using ChatterBot's English corpus


def custom_train(bot, conversation):
    """
    Train the bot with a custom conversation list.
    """
    from chatterbot.trainers import ListTrainer  # Import the list-based trainer class
    trainer = ListTrainer(bot)  # Initialize the trainer with the bot
    trainer.train(conversation)  # Train the bot with the custom conversation list


# Start and interact with the chatbot
def start_chatbot(bot):
    """
    Start and interact with the chatbot.
    """
    print('\033c')  # Clear the terminal screen
    print(f"Hello! I'm {bot.name}! How can I help you today?")
    bye_list = ["bye", "goodbye", "quit", "exit"]

    while True:
        user_input = input("You: ")  # Take user input
        if user_input.lower() in bye_list:  # Check if the user wants to exit
            print(f"{bot.name}: Goodbye! Have a great day!")
            break

        response = bot.get_response(user_input)  # Generate a response
        print(f"{bot.name}: {response}")  # Display the bot’s response
