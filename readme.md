## Llama Quick Start

**Requirements:**

- Python 3 (https://www.python.org/downloads/)
- `llama_cpp` library: `pip install llama_cpp`

**1. Download Model:**

Get your LLM model from a source like https://gpt4all.io/index.html (example: `mistral-7b-openorca.gguf2.Q4_0.gguf`).

**2. Run a Test (Optional):**

If you have a script (`test.py`) showing LLM usage, run it with `python3 test.py`.

**3. Start the Server:**

- Navigate to the directory with your downloaded model.
- Run the server:

  ```bash
  pip install 'llama-cpp-python[server]'
  python3 -m llama_cpp.server --model <model_path>
  ```
