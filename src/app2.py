from agno.agent import Agent
from agno.models.ollama import Ollama
model=Ollama("llama3.2:1b")
agent=Agent(
    name="Personal python interview",
    model=model,
    instructions="""you are a personal movie reviewer 
    Rules:
    1.help me to make a movie reviewer
    2.whenever u see movie review then only response otherwise say:
    please say:it not a movie reviewer.
    """
)
print("Movie Reviewer Coach")
print("type exit to quit")
print("="*50)
while True:
    user_input=input("\nyou:") .strip()
    if user_input.lower()=="exit":
        print("goodbey!")
        break
    response=agent.run(user_input)
    print("\nmovie reviewer:")
    print(response.content)
    print("="*50)
