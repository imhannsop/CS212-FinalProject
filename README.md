# CS212 Final Project

## Project Structure
```
CS212-FinalProject/
├── assets/                 # Game sprites and visual assets
│   ├── base/               # Base character model / skin
│   ├── clothing/
│   │   ├── accessories/    # Hats, glasses, bags, etc.
│   │   ├── bottoms/        # Pants, skirts, shorts
│   │   └── tops/           # Shirts, jackets
│   └── ui/                 # Buttons, panels, icons
├── algorithms/             # Sorting and searching algorithms
├── core/                   # Custom data structures (LinkedList, Stack, etc.)
├── models/                 # Game entity and item classes
├── utils/                  # Helper functions and constants
├── project-guide/          # Course guidelines and specs
├── main.py                 # Game entry point
└── requirements.txt        # Dependencies
```

## Setup Instructions

### 1. Virtual Environment Setup
Create and activate your venv:

- **Windows:**
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```

- **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run
```bash
python main.py
```
