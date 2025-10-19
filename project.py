import google.generativeai as genai

# API Connection
genai.configure(api_key="AIzaSyAubv_vCnUG7XBDWAYeGiohsfIw1rQ86Fs")
model = genai.GenerativeModel("gemini-2.5-flash")

# Persona Setup
print("Let's create your chatbot's personality!\n")
print("We are creating a bot specially designed for you. Everyone is unique, so your bot will be too.\n")

persona = {}
persona["YourName"] = input("Enter Your name: ").strip() or "Bro"
persona["BotName"] = input("Enter Your Bot name: ").strip() or "Sakha"
persona["tone"] = input("Enter chatbot tone (e.g., friendly, to-the-point, sarcastic, roaster mode): ").strip() or "sarcastic but caring"
persona["backstory"] = input("Enter about yourself: ").strip() or "An AI who pretends not to like humans but secretly does."
persona["goal"] = input("Enter chatbot goal (main area for the bot to focus on): ").strip() or "Help humans while dropping sarcastic remarks."

# Conversation History
conversation_history = []

def GenaiChat(user_input):
    """Generate chatbot reply using Gemini API with persona and memory."""

    # Save user message first (without extra \n)
    conversation_history.append(f"{persona['YourName']}: {user_input}")

    # Build context including all previous messages, each line separate
    context = f"""
You are {persona['BotName']}, a chatbot with the personality: {persona['tone']}.
Backstory: {persona['backstory']}
Goal: {persona['goal']}

Conversation so far:
{'\n'.join(conversation_history)}

{persona['BotName']}:
"""
    response = model.generate_content(context)
    reply = response.text.strip()

    # Save bot reply neatly
    conversation_history.append(f"{persona['BotName']}: {reply}")

    return reply

# Chat Loop
print(f"{persona['BotName']}: Hey there! Type 'exit' anytime to end the chat.\n")

while True:
    user_input = input(f"{persona['YourName']}: ").strip()
    if user_input.lower() in ["exit", "quit"]:
        print(f"{persona['BotName']}: Fine, leaving already. Goodbye.")
        break

    bot_reply = GenaiChat(user_input)
    print(f"{persona['BotName']}: {bot_reply}\n")

    # Clean display of conversation till now
    print("-" * 50) 
    print('This is your conversation till now')
    print("\n".join(conversation_history))
    print("-" * 50) 

