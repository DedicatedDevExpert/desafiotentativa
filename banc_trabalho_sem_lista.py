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
