#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sep 28, 2020 8:43 AM
Filename: coffee_machine2.py
@author: Rabih Fawaz
@email: rf28@aub.edu.lb
"""


class CoffeeMachine:
    action = ""

    # the coffee machine has $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def __str__(self):
        return "\nThe coffee machine has:\n" \
               "{} of water\n" \
               "{} of milk\n" \
               "{} of coffee beans\n" \
               "{} of disposable cups\n" \
               "${} of money\n".format(self.water, self.milk, self.beans, self.cups, self.money)

    def check_ingredients(self, water, milk, beans):
        if water > self.water:
            print("Sorry, not enough water!")
            return False
        if milk > self.milk:
            print("Sorry, not enough milk!")
            return False
        if beans > self.beans:
            print("Sorry, not enough coffee beans!")
            return False
        if self.cups <= 0:
            print("Sorry, not enough cups!")
            return False
        return True

    def buy(self, water, milk, beans, money):
        if self.check_ingredients(water, milk, beans):
            print("I have enough resources, making you a coffee!")
            self.water -= water
            self.milk -= milk
            self.beans -= beans
            self.cups -= 1
            self.money += money

    def fill(self, water, milk, beans, cups):
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    def take(self):
        print("\nI gave you ${}".format(self.money))
        self.money = 0

    def exit(self):
        pass


cm = CoffeeMachine(400, 540, 120, 9, 550)
while cm.action != "exit":
    print("\nWrite action (buy, fill, take, remaining, exit):")
    cm.action = input()
    if cm.action == "buy":
        print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        choice = input()
        # For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
        # For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
        # And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee.
        # It costs $6.
        if choice == "1":
            cm.buy(250, 0, 16, 4)
        elif choice == "2":
            cm.buy(350, 75, 20, 7)
        elif choice == "3":
            cm.buy(200, 100, 12, 6)
        elif choice == "back":
            continue
    elif cm.action == "fill":
        w = int(input("\nWrite how many ml of water do you want to add:\n"))
        m = int(input("Write how many ml of milk do you want to add:\n"))
        b = int(input("Write how many grams of coffee beans do you want to add:\n"))
        c = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        cm.fill(w, m, b, c)
    elif cm.action == "take":
        cm.take()
    elif cm.action == "remaining":
        print(cm)
