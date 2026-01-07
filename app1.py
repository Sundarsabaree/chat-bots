from agno.agent import Agent
from agno.models.ollama import Ollama
model=Ollama("llama3.2:1b")
agent=Agent(
    name="Personal python interview",
    model=model,
    instructions="""you are a personal python interview 
    Rules:
    1.help me to make a python interview
    2.whenever u see python interview then only response otherwise say:
    please say:it not a python interview.
    """
)
print("Python Interview Coach")
print("type exit to quit")
print("="*50)
while True:
    user_input=input("\nyou:") .strip()
    if user_input.lower()=="exit":
        print("goodbey!")
        break
    response=agent.run(user_input)
    print("\npython interview mentor:")
    print(response.content)
    print("="*50)
