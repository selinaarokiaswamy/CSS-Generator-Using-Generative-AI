import os
# import openai
import os
import sys
from langchain.llms import AzureOpenAI
chatgpt_model_name = "gpt-35-turbo"
chatgpt_deployment = "depl-name-test-123"

# openai.api_type = "azure"
# openai.api_key= os.environ.get("API_KEY")
# if openai.api_key == None:
#     print("Please set API_KEY environment variable")
#     sys.exit(1)
# openai.api_base = "https://4sept-test-open-ai-1212.openai.azure.com/"
# openai.api_version = "2023-05-15"

llm = AzureOpenAI(
    # openai_api_type="azure",
    deployment_name=chatgpt_deployment, 
    model_name=chatgpt_model_name) 

def send_stuff(content):
  try:
    response = openai.ChatCompletion.create(
                  engine=chatgpt_model_name,
                  messages=[
                        {"role": "system", "content": "Act as a Frontend developer who is trained HTML, CSS and SCSS styling."},
                        {"role": "user", "content": content},
                        {"role": "user", "content": "Give only the CSS styles and no explanation"}
                    ]
                )

    # print the response
    return response['choices'][0]['message']['content']
  except openai.error.APIError as e:
      # Handle API error here, e.g. retry or log
      print(f"OpenAI API returned an API Error: {e}")

  except openai.error.AuthenticationError as e:
      # Handle Authentication error here, e.g. invalid API key
      print(f"OpenAI API returned an Authentication Error: {e}")

  except openai.error.APIConnectionError as e:
      # Handle connection error here
      print(f"Failed to connect to OpenAI API: {e}")

  except openai.error.InvalidRequestError as e:
      # Handle connection error here
      print(f"Invalid Request Error: {e}")

  except openai.error.RateLimitError as e:
      # Handle rate limit error
      print(f"OpenAI API request exceeded rate limit: {e}")

  except openai.error.ServiceUnavailableError as e:
      # Handle Service Unavailable error
      print(f"Service Unavailable: {e}")

  except openai.error.Timeout as e:
      # Handle request timeout
      print(f"Request timed out: {e}")
      
  except BaseException as e:
      # Handles all other exceptions
      print(f"An exception has occured.: {e}")

if __name__ == "__main__":
    # question = "How to Configure snmpv3 on cisco ios router"
    # answer = send_stuff(question)
    questions = []
    with open("scenarios.txt", "r") as s:
        questions = s.readlines()
    for i, question in enumerate(questions, 1):
        print("working...")
        answer = llm(question)
        print(answer)
        with open("nlp_question_answer.txt", "a+") as f:
            f.write(f"Question {i}: {question} \n")
            f.write(f"Answer {i}: {answer} \n")
            f.write("\n===============================================\n")
  #  send_stuff("Who won the world series in 2020?")
