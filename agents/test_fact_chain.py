from langchain import PromptTemplate, LLMChain
from llm_engine import get_llm

llm = get_llm()

prompt = PromptTemplate.from_template("Explain this simply:\n{topic}")
chain = LLMChain(prompt=prompt, llm=llm)

response = chain.run(topic="black holes")
print("Response:", response)
