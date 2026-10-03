# Python Bill Splitter

A simple, lightweight, and user-friendly Command Line Interface (CLI) application written in Python to split a total bill evenly among multiple members.

---

## Repository Details
* **Suggested Repository Title:** `python-bill-splitter`
* **Suggested Description:** A Python CLI tool to calculate and split total bills among members with robust error handling and clean formatting.

---

## About the Project
When dining out or sharing expenses with friends, calculating individual shares manually can sometimes be tedious. This CLI tool allows users to input the total bill amount and the number of members sharing it, automatically computing the exact amount each person needs to pay.

## The Formula
The per-member share is calculated by dividing the total bill by the number of participating members:

$$\text{Per Person Share} = \frac{\text{Total Bill}}{\text{Number of Members}}$$

If applicable, a tip percentage can also be factored into the total before splitting:

$$\text{Total with Tip} = \text{Total Bill} \times \left(1 + \frac{\text{Tip \%}}{100}\right)$$

## Features
* Quick and accurate per-person share calculations.
* Built-in input validation to handle decimal values (for currency) and integer values (for member counts safely).
* Division-by-zero prevention (checks if the number of members is greater than zero).
* Clean output formatting showing exact currency values up to two decimal places.

## Prerequisites
Ensure you have Python installed on your system. You can verify the installation by running:
```bash
python --version
