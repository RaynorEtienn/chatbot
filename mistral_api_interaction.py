from mistralai import Mistral
from dotenv import load_dotenv
import os

def mistral_answer_question(question):
  """Get answer of Mistral latest large model for the given question.

  Args:
    question (str): Question asked by the user.

  Returns:
    (str): Answer of Mistral latest large model.
  """
  load_dotenv()
  API_KEY = os.getenv("MISTRAL_API_KEY")
  model = "mistral-large-latest"

  client = Mistral(api_key=API_KEY)

  chat_response = client.chat.complete(
    model = model,
    messages = [
      {
        "role": "user",
        "content": f"{question}",
      },
    ]
  )

  return chat_response.choices[0].message.content

if __name__ == "__main__":
  print(mistral_answer_question("What is pip in financial context ?"))