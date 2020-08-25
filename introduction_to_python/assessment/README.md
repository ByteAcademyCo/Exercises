# Week 2 Project - Vending Machine Assignment

The goal of this assessment is to put together all the concepts learned until now into a cumulative project that implements the basic software of a vending machine.

## Problem Description

You are hired as a software engineer at VendMachineCo, a start-up that sells vending machines. You are tasked to implement the basic functionality to allow vending machines to be deployed at university campuses. Your manager is non-technical and has described the task with the bullet points below.

### Vending Machine
* Vending machines contain Coca-Cola, Sprite, and Mountain Dew
  * Initialized to contain 5 of each type soda costing $2 each
  * Vending machines can hold a maximum of 10 bottles per type of soda

### Soda Shop
* Soda shop contains the quantity for each of the sodas they create
  * Initialized to contain 10 of each soda costing $1 each
* Soda shop has the capacity to create sodas
* Soda shop has the capacity to change the cost for each of the sodas in their shop

### Student
* A student has an ID-card with money on it
  * Initialized to $10
* A student has the capacity to add funds to their ID card
* A student has the capacity to buy sodas from a vending machine
  * This money is taken from the student funds and added to the university funds

### University Administrator
* University has funds that they receieve from students and spend on sodas
  * Initialized to $100
* University has the capacity to enroll students into the university, providing them a new ID-card
* University has the capacity to change the cost for each of the sodas in the vending machine
* University has the capacity to refill the vending machine by buying sodas from the soda shop
  * This money is taken from the university funds and added to the soda shop funds

## Specification

Thankfully your team lead has a technical background. He has turned the description above into a formalized specification for a Python program described below.

Write a program `vending_machine.py` that reads a file called `input.txt` that will contain a sequence of the commands below (one per line) and output corresponding messages (one per line) in `output.txt`. You are provided with the code to read and write to the files. You are also provided a command line interface to test your code. 

| Method       | Input | Output | Description |
|:-----------:|:----------:|:------:|:-----------:|
| `enroll_student` | `student` | * `'{student} Enrolled.'` if `student` successfully enrolled<br>* `'Error: {student} Already Enrolled.'` if `student` already enrolled | Enrolls the student `student` into the university | 
| `add_funds` | `student`, `funds` | * `'${funds} Added to {student}.'` if funds successfully added<br>* `'Error: {student} Not Enrolled.'` if `student` is not enrolled | Adds `funds` funds to the student `student` |
| `buy_soda`  | `student`, `soda`   | * `'{student} Bought {soda}.'` if sucessfully bought soda<br>* `'Error: Insufficient Funds.'` if `student` does not have enough `funds`<br>* `Error: {student} Not Enrolled.` if `student` is not enrolled | Buys the soda `soda` for student `student`   |
| `create_soda` | `soda`, `amount` | * `'{amount} {soda} Created.'` | Creates `{amount}` `{soda}` in the soda shop. |
| `set_machine_cost` | `soda`, `cost` | * `'Vending Machine cost for {soda} is ${cost}.'` | Sets the cost of `soda` to be `cost` for the vending machine |
| `set_shop_cost` | `soda`, `cost` | * `'Soda Shop cost for {soda} is ${cost}.'` | Sets the cost of `soda` to be `cost`  for the soda shop|
| `get_student_funds` | `student` | * `'{student} has ${funds}.'` if succesfully get student funds<br>* `'Error: {student} Not Enrolled.'` if `student` is not enrolled | Gets the `funds` from student `student` |
| `get_university_funds` | `None` | * `'University has ${funds}.'` | Gets the `funds` for the university |
| `get_vending_machine_stock` | `None` | * `'Vending Machine has {amount} Coca-Cola, {amount} Sprite, and {amount} Mountain-Dew.'` | Gets the stock remaining in the vending machine |
| `get_shop_stock` | `None` | * `'Soda Shop has {amount} Coca-Cola, {amount} Sprite, and {amount} Mountain-Dew.'` | Gets the stock remaining in the soda shop |
| `refill_vm` | `{soda} {amount}, {soda} {amount}, {soda} {amount}`  | * `'Error: Shop out of soda.'` if shop is out of a specific soda<br>* `'Error: Insufficient Funds.'` if university does not have enough funds<br>* `'Error: Over Max Quantity.'` if refilling makes machine have more than 10 of any kind of `soda`<br>* `'Refilled Machine with {amount} {soda}, {amount} {soda}, {amount} {soda}.'` if successfully refilled machine<br> | Refills the vending machine with the amounts specified.<br> You should check each condition in the given order. |
| `quit` | `None` | * `None` | Exits the program

### Types
| Name   | Type  | Description |
|:------:|:-----:|:-----------:|
| `student`    | `string`   | The name of the student |
| `funds`      | `float` | Representing funds for a student or university |
| `cost`       | `float` | Representing the cost of a soda for the university or soda shop |
| `soda`       | `string` (1 of `Coca-Cola`, `Sprite`, `Mountain-Dew`) | A string specifying the kind of soda |
| `amount`     | `int`   | Representing the quantity of a soda for the university or soda shop |

## Example

| input.txt | output.txt |
|:------:|:------:|
| enroll_student Wasif | Wasif Enrolled. |
| add_funds Wasif 100 | $100.0 Added to Wasif. |
| buy_soda Wasif Sprite | Wasif Bought Sprite. |
| get_university_funds | University has $102.0. |
| get_student_funds Wasif | Wasif has $108.0. |
| get_vending_machine_stock | Vending Machine has 5 Coca-Cola, 4 Sprite, and 5 Mountain Dew. |
| quit | |


## Testing
We have provided 3 basic tests located in the `testing/` subdirectory called `test_1`, `test_2`, and `test_3` that test for basic functionality. These contain sample `input.txt` to run your code with, as well as `expected_output.txt` to check your answer against. Be sure to do comprehensive testing on your own as the majority of our tests are hidden from you that will test all sorts of interactions. 

## FAQ
* Can you pass in invalid types to input?
  * No, you can assume only valid types will be passed in
  * Ie. cannot call `add_funds Wasif some_string` or `add_funds 10 10`
* Does the output have to match *exactly*?
  * Yes, incorrect capitalizations and missing punctuation will be considered errors
