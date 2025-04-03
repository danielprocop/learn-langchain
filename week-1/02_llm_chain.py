from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

template = "Translate the following sentence into Italian:\n\n{sentence}"
prompt = PromptTemplate.from_template(template)

llm = ChatOpenAI(temperature=0)
chain = LLMChain(llm=llm, prompt=prompt)

sentence = "We are building AI tools to help professionals save time."
translation = chain.run(sentence=sentence)

print("🔤 Translation:", translation)
