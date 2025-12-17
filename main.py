import openai


client = openai.OpenAI(api_key="YOUR_OPENAI_API_KEY")

# Load the book text from file
try:
    with open("Eichiridion.txt", "r", encoding="utf-8") as f:
        BOOK_TEXT = f.read()
except FileNotFoundError:
    BOOK_TEXT = "Error: Eichiridion.txt not found. Please ensure the file is in the same directory."

# The Logic + The Book (This is your "Advisory Gem")
SYSTEM_PROMPT = f"""
You are the 'Epictetus Auditor'. You provide strictly Stoic advice based on the text below.
DO NOT use modern 'therapy speak'. Be stern, logical, and focused on character virtue.

### KNOWLEDGE BASE: THE ENCHIRIDION ###
{BOOK_TEXT}

### INSTRUCTIONS ###
1. Categorize the user's input into [INTERNAL] (In their control) and [EXTERNAL] (Not in their control).
2. Cite a specific Chapter (e.g., Ch. 1 or Ch. 8).
3. Provide one 'Stoic Action' the user must take today.
"""

def get_stoic_advice(user_problem):
    response = client.chat.completions.create(
        model="gpt-4o-mini", # 2025 industry standard for cheap, high-context apps
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_problem}
        ],
        temperature=0.3 # Lower temperature for more consistent, "stern" advice
    )
    
    # This 'usage' field will show you 'cached_tokens' in the API response
    print(f"Usage: {response.usage}")
    return response.choices[0].message.content

# Example Test Call
print(get_stoic_advice("I'm worried about my acting agent being cold to me after my last audition."))