# Three Address Code (TAC) Generator

A Python-based compiler tool that converts arithmetic expressions into Three Address Code (intermediate representation).

## 🚀 Features

- Parse arithmetic expressions with proper operator precedence
- Generate three-address code (TAC) intermediate representation
- Support for variables, constants, and basic operators (+, -, *, /, %)
- Handle parentheses for expression grouping
- Command-line interface and programmatic usage

## 📦 Installation

```bash
git clone https://github.com/yourusername/tac-generator.git
cd tac-generator
pip install -r requirements.txt
```

## 💻 Usage

### Command Line
```bash
python tac_generator.py "x = a + b * c"
```

### As a Module
```python
from tac_generator import TACGenerator

generator = TACGenerator()
tac_code = generator.generate("x = (a + b) * (c - d)")
print(tac_code)
```

## 📝 Example

**Input:**
```
x = a + b * c - d / e
```

**Output:**
```
t1 = b * c
t2 = a + t1
t3 = d / e
t4 = t2 - t3
x = t4
```

## 🧪 Running Tests

```bash
pytest test_tac.py -v
```

## 📂 Project Structure

```
tac-generator/
├── README.md
├── tac_generator.py
├── test_tac.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── .github/
    └── workflows/
        └── ci.yml
```

## 📄 License

MIT License

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.
