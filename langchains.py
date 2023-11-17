from langchain.llms import AzureOpenAI
import os

llm = AzureOpenAI(
    # openai_api_type="azure",
    deployment_name="depl-name-test-123", 
    model_name="gpt-35-turbo") 

print(llm("hi"))