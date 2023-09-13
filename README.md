# **Bolt** ⚡ 

> A blazing-fast CLI-tool to manage your FastAPI projects! 🚀

### Setup Locally

<details>
<summary>Mac / Linux</summary>

```bash
# Setup virtual environment
make env

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
make setup
```
</details>

<details>
<summary>Windows</summary>

```bash
# Setup virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
</details>

---

### CLI

<details>
<summary>Mac / Linux</summary>

```bash
# Start creating apps
python3 bolt.py start-app test_api
```
</details>

<details>
<summary>Windows</summary>

```bash
# Start creating apps
python bolt.py start-app test_api
```
</details>

---

### Running the Server

<details>
<summary>Mac / Linux</summary>

```bash
# Start the server
uvicorn settings:app --reload
```

Now go to http://localhost:8000/docs to see the Swagger UI.

</details>

<details>
<summary>Windows</summary>

```bash
# Start the server
python -m uvicorn settings:app --reload
```

Now go to http://localhost:8000/docs to see the Swagger UI.

</details>
