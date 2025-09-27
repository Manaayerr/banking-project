# 🏦 Banking System in Python

## 📌 Overview

This project is a simple **Banking System** implemented fully in **Python**.
It simulates core banking operations, including:

* Deposit
* Withdraw
* Transfer between accounts
* Customer login & registration
* Viewing customer records

The goal of this project is to demonstrate practical use of Python for handling file operations, user authentication, and basic data management.

---

## 💻 Example Code I'm Proud Of

```python
def load_customers(self):
    customers = {}
    try:
        with open(self.csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                c = Customer(
                    account_id=row['account_id'],
                    Fname=row['frst_name'],
                    Lname=row['last_name'],
                    password=row['password'],
                    check=row['balance_checking'],
                    save=row['balance_savings']
                )
                customers[c.account_id] = c
    except FileNotFoundError:
        print('CSV file not found')
    return customers


def display_customers(self):
    print("Customers \n")
    for c in self.customers.values():
        print(c)
```

I’m proud of this part because:

* It shows how I applied **`try` and `except`** to handle errors safely.
* It demonstrates structured file reading with **CSV**.
* It builds a reusable customer management system in an elegant and simple way.

---

## 📚 What I Learned

* The **fundamentals of Python programming** (functions, classes, error handling, file I/O).
* The importance of handling errors gracefully with **`try/except`**.
* How to design and implement **object-oriented concepts** in a real-world project.
* How to use **GitHub** for version control and project collaboration.
* Deeper understanding of **data structures** and how to store & manage information.

---

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/banking-system.git
   ```
2. Navigate into the project folder:

   ```bash
   cd banking-system
   ```
3. Run the program:

   ```bash
   python main.py
   ```

---

## 👩‍💻 Author

* Manayer Alabdali – Bachelor of Information Systems (2025)
* Passionate about backend development, Python, and databases.
* [LinkedIn](www.linkedin.com/in/manayer-al-abdali) | [GitHub](https://github.com/Manaayerr)

---
