# ATM – Automated Teller Machine

## Description

Command-line ATM application in Python. Users can register, log in, check balance, deposit, and withdraw. Data is stored in a JSON file (`data/db.json`). The interface is menu-based and runs in the terminal.

---

## Technologies

- Python 3
- JSON (file-based storage)
- Standard library only (no external frameworks)

---

## Installation

```bash
git clone https://github.com/LFDIAZDEV2209/cajero-automatico.git
cd cajero-automatico
python -m venv venv
# Activate venv (see section 2 above)
python main.py
```

---

## Configuration

Edit `config.py` to change the database path if needed:

```python
DB_PATH = "data/db.json"
```

---

## Execution

```bash
python main.py
```

---

## Project Structure

```
cajero-automatico/
├── main.py
├── config.py
├── .gitignore
├── README.md
├── data/
│   └── db.json
└── modules/
    ├── auth/
    │   ├── login.py
    │   └── register.py
    ├── ATM/
    │   ├── module.py
    │   ├── depositAmount.py
    │   ├── whithdrawAmount.py
    │   └── listAmount.py
    └── utils/
        ├── corefiles.py
        ├── msg.py
        └── screenController.py
```

---

## Features / Usage

| Action        | Description                                      |
|---------------|--------------------------------------------------|
| Log in        | Authenticate with email and password             |
| Register      | Create account (name, email, password)           |
| Check balance | View current balance                             |
| Withdraw      | Withdraw money (validates amount and funds)      |
| Deposit       | Deposit money (validates amount)                 |
| Exit          | Return to main menu or close the application     |

Main menu: **1** Log in · **2** Register · **3** Exit.  
After login: **1** Check balance · **2** Withdraw · **3** Deposit · **4** Exit.

---

## Good Practices

- Modular layout (auth, ATM, utils).
- Single config file for paths.
- Input validation and error messages.
- User data and balance refreshed from storage after each operation.
- Cross-platform (Windows, Linux, macOS).

---

## Author

Luis Felipe Diaz – Python / Clan 9 RIWI