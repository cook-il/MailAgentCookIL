from langchain.llms import LlamaCpp

llm = LlamaCpp(
    model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    temperature=0.5,
    max_tokens=128,
    n_ctx=2048,
    n_threads=6,
    verbose=True,
)

response = llm("What is the capital of France?")
print("Response:", response)
