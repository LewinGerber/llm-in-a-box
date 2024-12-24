from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import GPT4All

# e.g. C:/Users/me/.cache/lm-studio/models/hugging-quants/Llama-3.2-1B-Instruct-Q8_0-GGUF/llama-3.2-1b-instruct-q8_0.gguf
local_path = ("<path to the model>")
model = GPT4All(model=local_path, backend="llama")

def createChain(template):
    prompt = ChatPromptTemplate.from_template(template)
    return prompt | model | StrOutputParser()

def invokeChain(chain, input):
    result = chain.invoke(input)
    return result

# Example

template = """
You are a cybersecurity analyst with deep expertise in identifying phishing emails.

Please analyze the following email text and determine whether it is a phishing attempt: 
{email}

Step-by-Step Instructions:
1. Examine the email for suspicious links, requests for personal information, unusual sender addresses, or any red flags.
2. Check the style, grammar, and tone of the email for common signs of phishing (e.g., urgent language, unusual formatting).
3. Identify any inconsistencies between sender identity and the content of the email.

Output Requirements (in JSON format only):
- "is_phishing": A boolean value (true or false) indicating if the email is phishing.
- "reasons": An array of exactly 3 concise strings that explain why it is or why it is most likely not a phishing email.

Please answer only with the valid JSON.
"""

email = """
Dear Peter,

I hope this email finds you well.

I am writing to request a meeting to discuss the upcoming [Project Name]. We are in the initial planning phase, and it would be great to align on the goals, timeline, and any potential challenges we might encounter. I believe your input would be valuable to ensure the project's success.

Could you kindly let me know your availability next week? I am flexible and happy to adjust to a time that suits you best.

Looking forward to hearing from you.

Best regards,
Jake
"""

chain = createChain(template=template)
result = invokeChain(chain, {"email": "What animal is the symbol of the United States?"})
print(result)