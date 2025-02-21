import re
from openai import OpenAI
import json


# Load settings from a config file
def load_settings():
    with open("settings.json", "r") as f:
        return json.load(f)


settings = load_settings()
api_key = settings.get("OPENAI_API_KEY", "")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)


def call_ai_agent(prompt: str, model="gpt-4", temperature=0.5):
    """Calls an AI agent with a given prompt and logs the response."""
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful AI coding assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
    )
    response_content = response.choices[0].message.content.strip()
    # Log the entire response
    with open("output.log", "a") as log_file:
        log_file.write(
            f"\n--- Prompt ---\n{prompt}\n\n--- Response ---\n{response_content}\n"
        )
    return response.choices[0].message.content.strip()


def extract_code(content: str):
    """Extracts code blocks from the AI response."""
    code_blocks = re.findall(r"```(?:python)?\n(.*?)```", content, re.DOTALL)
    return "\n\n".join(code_blocks) if code_blocks else content


def generate_code(task_description: str):
    prompt = f"{task_description}. Keep it clean and efficient."
    response = call_ai_agent(prompt)
    code = extract_code(response)
    return code


def refactor_code(code: str):
    prompt = f"Refactor the following Python code to improve readability and efficiency:\n\n{code}"
    response = call_ai_agent(prompt)
    code = extract_code(response)
    return code


def write_tests(code: str):
    prompt = f"Write unit tests for the following Python code using pytest:\n\n{code}"

    response = call_ai_agent(prompt)
    tests = extract_code(response)
    return tests


def review_code(code: str):
    prompt = f"Review the following Python code for bugs, security issues, and best practices:\n\n{code}"
    return call_ai_agent(prompt)


def write_to_file(filename: str, content: str):
    """Writes content to a file."""
    with open(filename, "w") as f:
        f.write(content)


def main():
    task = "Write a Python cli programm that manages pyenv and Poetry environments"
    max_iterations = 5
    iteration = 0
    file_name = "python_poetry_env_manager.py"
    test_file_name = "test_python_poetry_env_manager.py"
    code = generate_code(task)
    write_to_file(file_name, code)

    while iteration < max_iterations:
        print(f"\n--- Iteration {iteration + 1} ---")

        # Refactor code
        refactored_code = refactor_code(code)
        write_to_file(file_name, refactored_code)
        print("Refactored code saved to refactored_code.py")

        # Write tests
        tests = write_tests(refactored_code)
        write_to_file(test_file_name, tests)
        print("Tests saved to test_code.py")

        # Review code
        review = review_code(refactored_code)
        print("Review:\n", review)

        # Check for completion condition
        if "no issues found" in review.lower() or "looks good" in review.lower():
            print("\n✅ Code passed the review. Task completed.")
            break

        # Prepare for next iteration
        code = refactored_code
        iteration += 1

    if iteration == max_iterations:
        print("\n⚠️ Reached maximum iterations without passing the review.")


if __name__ == "__main__":
    main()
