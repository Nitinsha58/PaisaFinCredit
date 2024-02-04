# PaisaFinCredit

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Nitinsha58/PaisaFinCredit.git
    ```

2. Navigate to the project directory:

    ```bash
    cd PaisaFinCredit
    ```

3. Create a virtual environment and activate it:

    ```bash
    pipenv install
    pipenv shell
    ```

    Commands after this will run directly in the virtual environment created by pipenv shell. 


4. Run database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run npm command to install tailwind css
    ```
    npm install -D tailwindcss
    ```
6. To update the output.css run
    ```
    npx tailwindcss -i ./src/input.css -o ./src/output.css --watch
    ```

## Usage

1. Start the development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and visit `http://localhost:8000` to view the application.

## Contributing
Contributions are welcome! Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
