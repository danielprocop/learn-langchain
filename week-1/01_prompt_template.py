from langchain.prompts import PromptTemplate

template = "What is a good name for a company that makes {product}?"
prompt = PromptTemplate.from_template(template)

formatted_prompt = prompt.format(product="artificial intelligence tools")
print(formatted_prompt)
