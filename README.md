# Python API Backend Boilerplate

A clean and extensible backend boilerplate in Python, designed to speed up the development of REST APIs.  
It provides environment-aware configuration, structured logging, database adapters, and a ready-to-use testing setup.

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/andreadeluca/python-api-backend-boilerplate.git
   cd python-api-backend-boilerplate
   ```

2. **Install dependencies**  
   This project uses [Poetry](https://python-poetry.org/):
   ```bash
   poetry install
   ```

3. **Configure your environment**  
   Create a `.env` file in the project root with the following variables:
   ```env
   ENVIRONMENT=DEV
   DB_HOST=localhost
   DB_PORT=27017
   DB_NAME=testdb
   DB_USERNAME=
   DB_PASSWORD=
   ```
   Valid values for `ENVIRONMENT` are:
   - `DEV`, `DEVELOPMENT`
   - `LOC`, `LOCAL`
   - `STG`, `STAGING`, `STAGE`, `TEST`
   - `PROD`, `PRODUCTION`

4. **Run tests**
   ```bash
   poetry run pytest -v
   ```
   To see debug logs while running tests:
   ```bash
   poetry run pytest -o log_cli=true -o log_cli_level=DEBUG -v
   ```

5. **Run MongoDB (optional, for integration tests)**  
   You can quickly run MongoDB with Docker:
   ```bash
   docker run -d --name mymongo -p 27017:27017 mongo:latest
   ```

Now you’re ready to start building on top of the boilerplate 🎉
