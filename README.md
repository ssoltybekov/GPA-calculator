# GPA Calculator Bot 🎓

Telegram bot for calculating GPA based on course credits and grades.

## Features

- Add multiple courses with name, credits and grade
- Calculates weighted GPA automatically
- Simple step-by-step dialog with keyboard buttons

## Project Structure

```
GPA-calculator/
├── main.py
├── .env
├── requirements.txt
└── app/
    ├── models/
    │   └── course.py       # Course dataclass
    ├── calculator/
    │   └── gpa.py          # GPA calculation logic
    └── bot/
        ├── handlers.py     # FSM handlers
        ├── states.py       # FSM states
        └── keyboards.py    # Reply keyboards
```

## Setup

1. Clone the repository
```bash
git clone https://github.com/yourusername/GPA-calculator.git
cd GPA-calculator
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create `.env` file
```
TELEGRAM_BOT=your_token_here
```

5. Run the bot
```bash
python main.py
```

## Usage

1. Start the bot with `/start`
2. Enter course name
3. Select credits (6 or 8)
4. Select grade (A to F)
5. Add more courses or calculate GPA

## Commands

- `/start` — start the bot
- `/cancel` — reset and start over

## Grade Scale

| Grade | Points |
|-------|--------|
| A     | 4.0    |
| A-    | 3.7    |
| B+    | 3.3    |
| B     | 3.0    |
| B-    | 2.7    |
| C+    | 2.3    |
| C     | 2.0    |
| C-    | 1.7    |
| D+    | 1.3    |
| D     | 1.0    |
| F     | 0.0    |
