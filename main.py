from openai import OpenAI
import json


# Load settings from a config file
def load_settings():
    with open("settings.json", "r") as f:
        return json.load(f)


settings = load_settings()

client = OpenAI(api_key=settings.get("OPENAI_API_KEY", ""))


def call_ai_agent(prompt: str, model="gpt-4", temperature=0.5):
    """Calls an AI agent with a given prompt."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful AI coding assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content.strip()


def generate_code(task_description: str):
    prompt = (
        f"Write a Python function that {task_description}. Keep it clean and efficient."
    )
    return call_ai_agent(prompt)


def refactor_code(code: str):
    prompt = f"Refactor the following Python code to improve readability and efficiency:\n\n{code}"
    return call_ai_agent(prompt)


def write_tests(code: str):
    prompt = f"Write unit tests for the following Python code using pytest:\n\n{code}"
    return call_ai_agent(prompt)


def review_code(code: str):
    prompt = f"Review the following Python code for bugs, security issues, and best practices:\n\n{code}"
    return call_ai_agent(prompt)


def main():
    task = "manages pyenv and Poetry environments"
    print("Generating initial code...")
    code = generate_code(task)
    print(code, "\n")

    print("Refactoring code...")
    refactored_code = refactor_code(code)
    print(refactored_code, "\n")

    print("Writing tests...")
    tests = write_tests(refactored_code)
    print(tests, "\n")

    print("Reviewing code...")
    review = review_code(refactored_code)
    print(review, "\n")


if __name__ == "__main__":
    main()
