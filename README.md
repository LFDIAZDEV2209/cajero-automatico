# 💳 ATM - Automated Teller Machine

An Automated Teller Machine (ATM) system implemented in Python that allows users to authenticate, check balances, and perform deposits and withdrawals with a command-line interface.

## 📋 Description

This project simulates the operation of a traditional ATM, presenting an interactive menu where users can:
- Register in the system
- Log in to their account
- Check their current balance
- Withdraw money
- Deposit money
- Exit the application

## ✨ Features

- **User Authentication**: Login and registration system
- **Credentials Validation**: Email and password verification
- **Balance Management**: Check balance, deposits, and withdrawals
- **Input Validation**: Error handling for invalid inputs
- **Interactive Interface**: Clear and organized menus
- **Cross-Platform Compatibility**: Supports Windows, Linux, and macOS
- **Automatic Screen Clearing**: Screen clears between transactions

## 🛠️ Requirements

- Python 3.6 or higher
- No external package installations required

## 📦 Installation

1. Clone or download the repository
```bash
git clone https://github.com/LFDIAZDEV2209/cajero-automatico.git
cd cajero-automatico
```

2. Run the program
```bash
python main.py
```

## 📁 Project Structure

```
cajero-automatico/
│
├── main.py                          # Main entry point
├── data.py                          # User database
│
└── modules/
    ├── auth/                        # Authentication module
    │   ├── login.py                 # Login functionality
    │   ├── register.py              # Registration functionality
    │   └── __pycache__/
    │
    ├── ATM/                         # Main ATM module
    │   ├── module.py                # ATM main menu
    │   ├── depositAmount.py         # Deposit function
    │   ├── whithdrawAmount.py       # Withdrawal function
    │   ├── listAmount.py            # Balance inquiry
    │   └── __pycache__/
    │
    ├── utils/                       # Utilities module
    │   ├── msg.py                   # Messages and menus
    │   ├── screenController.py      # Screen control
    │   └── __pycache__/
    │
    └── __pycache__/
```

## 🚀 Usage

### Main Menu

When you run the program, the welcome menu is displayed:

```
--------------------
Welcome to the ATM
--------------------
1. Log in
2. Register
3. Exit
```

### Option 1: Log In

Enter your credentials (email and password) to access your account.

```
Log in
Enter your email: juan.perez@example.com
Enter your password: 123456
```

### Option 2: Register

Create a new account by providing your name, email, and password.

```
Register
Enter your name: Carlos Lopez
Enter your email: carlos.lopez@example.com
Enter your password: mypassword
```

### ATM Menu

Once authenticated, you'll access the main ATM menu:

```
-----------------
Automated Teller
-----------------
1. Check balance
2. Withdraw money
3. Deposit money
4. Exit
```

#### Check Balance (Option 1)
Displays your current account balance.

#### Withdraw Money (Option 2)
Allows you to withdraw money from your account.
- Validates that the amount is positive
- Verifies that you have sufficient funds
- Updates your balance

#### Deposit Money (Option 3)
Allows you to deposit money into your account.
- Validates that the amount is positive
- Updates your balance

#### Exit (Option 4)
Closes your session and returns to the main menu.

## 👥 Test Users

The system comes with two predefined users for testing:

| Email | Password | Initial Balance |
|-------|----------|-----------------|
| john.doe@example.com | 123456 | $1000 |
| juan.perez@example.com | 123456 | $1000 |

## 📚 Module Description

### `main.py`
- Application entry point
- Handles the main welcome menu
- Orchestrates the flow between authentication and ATM functionalities

### `data.py`
- Stores user information (currently in memory)
- Each user has: id, name, email, password, and balance

### `modules/auth/`

**`login.py`**
- Validates user credentials
- Searches for the user in the database
- Verifies email and password

**`register.py`**
- Allows creating new users
- Validates that the email is not already registered
- Automatically generates a new ID

### `modules/ATM/`

**`module.py`**
- Main ATM menu
- Orchestrates available operations
- Manages transaction flow

**`listAmount.py`**
- Displays the current user balance

**`whithdrawAmount.py`**
- Requests amount to withdraw
- Validates input and available funds
- Returns the amount and new balance

**`depositAmount.py`**
- Requests amount to deposit
- Validates input
- Returns the amount and new balance

### `modules/utils/`

**`msg.py`**
- Defines application menus
- Contains message constants

**`screenController.py`**
- Clears the screen based on the operating system
- Pauses the screen for reading
- Compatible with Windows, Linux, and macOS

## ⚙️ Execution Flow

```
Start
  ↓
Main Menu (Login/Register/Exit)
  ├─→ Successful Login → ATM Menu
  │     ├─→ Check Balance
  │     ├─→ Withdraw Money
  │     ├─→ Deposit Money
  │     └─→ Exit → Returns to Main Menu
  │
  ├─→ Successful Registration → Main Menu
  │
  └─→ Exit → End of application
```

## 📝 License

This project is open source and available for educational use.

## 👨‍💻 Author

Project developed as part of the Python programming course - Clan 9 RIWI - Luis Felipe Diaz

---

**Thank you for using the ATM!** 😊
