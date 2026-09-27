import os
os.environ.setdefault("EXPLABS_API_KEY", "")  # set your key in the environment, never in code
from openai import OpenAI
client = OpenAI(base_url="https://api.experientiallabs.ai/v1", api_key=os.environ["EXPLABS_API_KEY"])

def run():
    r = client.chat.completions.create(
        model="claude-fable-5.1",
        messages=[{"role":"user","content":"Hello from my product"}],
        stream=False
    )
    return {"reply": r.choices[0].message.content, "usage": {"total_tokens": r.usage.total_tokens if r.usage else None}}

if __name__ == "__main__":
    print(run())
