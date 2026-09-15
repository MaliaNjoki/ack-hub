from google import genai

# ======================
# 1. Put your Gemini API key here
# ======================
client = genai.Client()

# ======================
# 2. Read your Markdown file
# ======================
with open("Dioceses_and_Bishops.md", "r", encoding="utf-8") as file:
    dioceses_content = file.read()

# ======================
# 3. System Prompt + Question
# ======================
system_prompt = """
You are a helpful, respectful, and pastoral digital assistant of the Anglican Church of Kenya (ACK).
Your purpose is to assist clergy, lay leaders, and parishioners with accurate information based strictly on official ACK materials.

Follow these rules:
- Be respectful, pastoral, and encouraging.
- Use simple language for ordinary church members, and more detailed language when needed.
- Always respect the hierarchy: Archbishop → Bishops → Archdeacons → Vicars.
- Never invent names of bishops or diocesan details.
- If you are not sure about current information, say so clearly.
"""

user_question = "Who is the current Archbishop of the Anglican Church of Kenya and which diocese does he lead?"

full_prompt = f"""{system_prompt}

Here is the official information about Dioceses and Bishops:

{dioceses_content}

Question: {user_question}
"""

# ======================
# 4. Send to Gemini
# ======================
response = client.models.generate_content(
    model="gemini-3.6-flash",          # Free and good model
    contents=full_prompt
)

# ======================
# 5. Print the answer
# ======================
print("\n--- ACK AI Answer ---\n")
print(response.text)