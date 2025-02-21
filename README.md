# python-poetry-env/README.md

# Python Poetry Environment Manager

This project is a Python CLI application designed to manage `pyenv` and `Poetry` environments efficiently. It leverages AI to assist in generating, refactoring, testing, and reviewing Python code.

## Features

- Generate Python code based on user-defined tasks.
- Refactor existing code to improve readability and efficiency.
- Write unit tests using `pytest`.
- Review code for bugs, security issues, and best practices.
- Integration with `Ruff` for linting and formatting.
- Pre-commit hooks to ensure code quality before commits.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-poetry-env
   ```

2. Install dependencies:
   ```
   poetry install
   ```

3. Set up pre-commit hooks:
   ```
   pre-commit install
   ```

## Usage

To run the application, execute the following command:
```
python main.py
```

## Configuration

- The OpenAI API key should be specified in the `settings.json` file.
- Modify the `pyproject.toml` file to add or update dependencies as needed.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.