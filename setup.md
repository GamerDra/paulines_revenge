# Setup Instructions


## Prerequisites
- Python 3.x installed (check with `python --version` or `python3 --version`)
- Optional: [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager, included with most Python installations)

---

## Step-by-Step Setup

### 1. Clone the Repository
If this project is in a repository, clone it using:
```bash
git clone <repository_url>
cd <repository_name>
```

---

### 2. Create a Virtual Environment
Use the following command to create a virtual environment in the project directory:

```bash
python -m venv venv
```

---

### 3. Activate the Virtual Environment (optional )
It is a good practice for bigger repos but you can just skip it here
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

You should now see the virtual environment’s name (`venv`) in your terminal prompt.

---

### 4. Install Dependencies
With the virtual environment activated, run the following command:

```bash
pip install -r requirements.txt
```

This will install the necessary Python packages (in this case, `requests`).

---

### 5. Verify Installation
You can verify the installed packages with:

```bash
pip freeze
```

You should see output similar to:

```
requests==2.31.0
```

---

## 6. Run the Application
When you're done, deactivate the virtual environment with:

```bash
deactivate
```

---

## Troubleshooting
- **Module Not Found Error**: Make sure you have activated the virtual environment before running the script.
- **pip Not Recognized**: Ensure Python and pip are installed and added to your system’s PATH.

---
