from agno.agent import Agent
from agno.models.ollama import Ollama
model=Ollama("llama3.2:1b")
agent=Agent(
    name="Personal diet planner",
    model=model,
    instructions="""you are a personal diet coach
    Rules:
    1.help me to make a diet plan
    2.whenever u see diet then only response otherwise say:
    please say:it not a diet plan.
    """
)
print("Diet planner coach")
print("type exit to quit")
print("="*50)
while True:
    user_input=input("\nyou:") .strip()
    if user_input.lower()=="exit":
        print("goodbey!")
        break
    response=agent.run(user_input)
    print("\n Agent:")
    print(response.content)
    print("="*50)
