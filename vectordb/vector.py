import os 
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-Coder-Next",
    task="text-generation",
    max_new_tokens=100
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("Hi how are you")
print(result.content)
