# CS212-FinalProject System & Architecture Documentation

## File Structure
```
CS212-FinalProject/
├── assets/                       # All visual graphics and game images
│   ├── base/                     # Character base sprites, skin tones, and default poses
│   ├── clothing/                 # Wearable clothing assets categorized by slot
│   │   ├── accessories/          # Hats, glasses, bags, and jewelry PNGs
│   │   ├── bottoms/              # Pants, skirts, and shorts PNGs
│   │   └── tops/                 # Shirts, jackets, and dresses PNGs
│   └── ui/                       # Buttons, navigation arrows, icons, and background frames
│
├── algorithms/                   # Custom Algorithm implementations (e.g., Merge Sort, Linear Search)
├── core/                         # Custom Data Structures (e.g., Doubly Linked List, Stack, Queue)
├── models/                       # Game object classes (e.g., Character state, Item metadata)
└── utils/                        # Helper scripts (e.g., Pygame asset loader, constants, button UI)
└── project-guide/                # CS212 official guidelines
```

---

## Getting Started & Local Setup

Follow these steps to set up and run the project locally on your machine.

### Prerequisites
* **Python 3.8 or higher** must be installed on your system. Verify by running:
  ```bash
  python --version
  ```

---

### Step 1: Clone the Repository
Clone the team repository and navigate into the project directory:
```bash
git clone <repository-url>
cd CS212-FinalProject
```

---

### Step 2: Create & Activate Virtual Environment
Setting up a virtual environment ensures everyone on the team uses isolated packages and avoids version mismatches.

* **On Windows (Command Prompt / PowerShell):**
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```

* **On macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

*Note: Once activated, your terminal prompt should show `(venv)` at the start.*

---

### Step 3: Install Dependencies
Install all required libraries specified in the project:

```bash
pip install -r requirements.txt
```

> **Note for new setups:** If `requirements.txt` is not yet available, install `pygame-ce` directly:
> ```bash
> pip install pygame-ce
> ```

---

### Step 4: Run the Application
Start the main game or application entry point:

```bash
python main.py
```

---

## 1. Executive Summary & Project Charter
* **Project Name:**
* **Lead:**
**Other roles:**
**Core Objective:**
* **Scope Boundary:**
  * **In-Scope:** 
  * **Out-of-Scope:** 

---

## 2. High-Level Architecture & Data Flow

### 2.1 System Overview