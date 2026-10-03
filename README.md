# Python Bill Splitter

A simple, lightweight, and crash-proof Command Line Interface (CLI) application written in Python to split a total bill evenly among multiple members with robust input validation.

---

## Repository Details
* **Suggested Repository Title:** `python-bill-splitter`
* **Suggested Description:** A Python CLI tool to calculate and split total bills among members with strict whole-number and sign validation.

---

## Project Overview
This application prompts the user for the total bill amount and the number of members splitting the bill. It features comprehensive input validation using `.isdigit()` and negative sign checks to prevent crashes, ensuring only valid whole numbers are accepted.

## The Formula
The per-person share is calculated by dividing the total bill by the number of participating members:

$$\text{Per Person Amount} = \frac{\text{Total Bill}}{\text{Number of Members}}$$

## Code Features
* **Strict Input Validation:** Safely validates inputs against alphabets, decimals, and negative numbers using custom conditional checks.
* **Error Prevention:** Automatically exits and displays an error message if zero or negative values are entered.
* **Precise Rounding:** Utilizes Python's `round()` function to format the final per-person amount up to 2 decimal places.

## Prerequisites
Ensure you have Python installed on your system. You can verify your installation by running:
```bash
python --version
