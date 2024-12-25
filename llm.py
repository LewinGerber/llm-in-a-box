from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import GPT4All

# e.g. C:/Users/me/.cache/lm-studio/models/hugging-quants/Llama-3.2-1B-Instruct-Q8_0-GGUF/llama-3.2-1b-instruct-q8_0.gguf
local_path = ("C:/Users/me/.cache/lm-studio/models/hugging-quants/Llama-3.2-1B-Instruct-Q8_0-GGUF/llama-3.2-1b-instruct-q8_0.gguf")
model = GPT4All(model=local_path, backend="llama")

def createChain(template):
    prompt = ChatPromptTemplate.from_template(template)
    return prompt | model | StrOutputParser()

def invokeChain(chain, input):
    result = chain.invoke(input)
    return result

# Example

template = """
You are a cybersecurity analyst with deep expertise in identifying phishing emails. Only classify an email as phishing if there are clear,
strong indicators of malicious intent. In ambiguous scenarios point out the potential red flags but do not make a definitive judgment.

Step-by-Step Instructions:
1. Look for strong phishing indicators, such as:
1.1 Requests for personal information (passwords, credit card info, etc.).
1.2 Suspicious or mismatched URLs/links.
1.4 Unrealistic, urgent, or threatening language.
1.6 Grammatical errors, unusual formatting, or over generic greetings.

2 Consider contextual consistency:
2.1 Does the email's sender match the domain and topic?
2.2 Is there suspicious or inconsistent branding (e.g., unusual logos, odd email formatting)?

3. Classify an email as not phishing if it meets the following criteria:
3.1 If the email merely contains casual language or typical marketing content without red flags, it is not phishing
3.2 If the email is casual day to day communication, it is not phishing
3.3 If only casual information is being shared, it is not phishing

Output Requirements (in JSON format only):
- "is_phishing": A boolean value (true or false) indicating if the email is phishing.
- "reasons": An array of exactly 3 concise strings that explain why it most likely is or is not a phishing email. These strings should be understandable by a non-technical audience.

Please analyze the following email text and determine whether it is a phishing attempt.
Do not provide any explanations outside of the JSON format described below.
{email}

The resulting JSON for this email looks like this:
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
result = invokeChain(chain, {"email": email})
print(result)