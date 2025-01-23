
# Banking System Script

## Overview

This Python script simulates a simple banking application. It enables users to perform basic operations such as depositing funds, withdrawing funds (with limits), viewing transaction history, and exiting the program. The program uses a text-based interface for user interaction.

---

## Features

1. **Deposit**:  
   - Users can deposit any positive amount to their balance.  
   - Transactions are logged in the transaction history.

2. **Withdrawal**:  
   - Users can withdraw up to R$ 500.00 per transaction.  
   - A maximum of 3 withdrawals is allowed per day.  
   - Insufficient balance or invalid amounts are handled gracefully.  

3. **Transaction History**:  
   - Users can view a detailed list of their deposits and withdrawals.  
   - Displays the current balance.  

4. **Exit**:  
   - Users can terminate the program.

---

## Code Implementation

```python
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:11:10 2025

@author: Admin
"""

# Inicializa as variáveis
saldo = 0.0
saques_diarios = 0
extrato = ""

while True:
    print("\nEscolha uma operação:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")

    opcao = input()

    if opcao == "1":
        # Depósito
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "2":
        # Saque
        if saques_diarios < 3:
            valor = float(input("Informe o valor do saque: R$ "))
            if valor <= saldo and valor <= 500:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                saques_diarios += 1
                print("Saque realizado com sucesso.")
            elif valor > 500:
                print("O valor do saque não pode exceder R$ 500,00.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de 3 saques diários excedido.")

    elif opcao == "3":
        # Extrato
        print("\nExtrato")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "4":
        # Sair do programa
        break

    else:
        print("Opção inválida. Tente novamente.")
```

---

## How It Works

1. The program initializes with a zero balance (`saldo`), zero daily withdrawals (`saques_diarios`), and an empty transaction history (`extrato`).

2. Users interact with the program through a menu that provides four options:
   - Deposit (Option 1)
   - Withdrawal (Option 2)
   - Transaction History (Option 3)
   - Exit (Option 4)

3. Each operation is handled as follows:
   - **Deposit**: Validates the deposit amount and updates the balance and transaction history.
   - **Withdrawal**: Checks the balance, transaction limit, and withdrawal amount before updating the balance and transaction history.
   - **Transaction History**: Displays all recorded transactions and the current balance.
   - **Exit**: Ends the program loop.

4. Error messages guide the user for invalid inputs or failed transactions.

---

## Example Usage

### Menu Display
```text
Escolha uma operação:
1. Depósito
2. Saque
3. Extrato
4. Sair
```

### Example Transactions
- Deposit R$ 100.00:  
  "Depósito realizado com sucesso."

- Attempt withdrawal of R$ 600.00:  
  "O valor do saque não pode exceder R$ 500,00."

- View transaction history:
```text
Extrato
Depósito: R$ 100.00
Saldo atual: R$ 100.00
```

- Exit: The program terminates gracefully.

---

## Customization

This script can be customized to include:
- Persistent storage for balance and transaction history.
- User authentication for multiple accounts.
- Enhanced error handling and input validation.
- A graphical user interface (GUI) for better usability.
