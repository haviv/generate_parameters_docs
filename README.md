# Parameter Documentation Generator

Automatically generates markdown documentation for parameters in your codebase using OpenAI's GPT-4.

## Setup

1. Clone and install dependencies:
```bash
git clone <repository-url>
cd parameter-documentation-generator
python3 -m venv venv
source venv/bin/activate  # On Unix/macOS
pip install -r requirements.txt
```

2. Configure OpenAI API:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Usage

1. List your parameters in `params.txt` (one per line):
```
ParameterName1
ParameterName2
```

2. Edit `main.py` and set your code folder:
```python
code_folder = "/path/to/your/code"  # Path to your C# codebase
```

3. Run the generator:
```bash
python main.py
```

Documentation will be generated in the `docs/` folder.

## Note
- Only searches in `.cs` files
- Requires OpenAI API key
- Set `code_folder` to the root of your C# project 