import json

notebook_content = '''{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Functions in Python (I)\\n\\nBased on slides by Hyunji So, McGill Desautels."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## What is a Function?\\n\\nA **function** is a named block of reusable code designed to perform a specific task. Using functions helps organize code, makes it more readable, and avoids repetition (following the DRY principle - Don't Repeat Yourself).\\n\\nKey concepts:\\n*   **Define:** The process of creating a function, giving it a name, specifying any inputs it needs (parameters), and writing the code block it will execute.\\n*   **Call:** The action of executing or running a function at a specific point in the program.\\n*   **Return:** (Optional) A function can send a value or result back to the part of the program that called it using the `return` statement. If a function doesn't have an explicit `return` statement that returns a value, it implicitly returns `None`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Why Use Functions?\\n\\nThe main idea is to **organize** and **encapsulate** a set of instructions so they can be easily reused multiple times within a program just by calling the function's name."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Defining a Function\\n\\nDefining a function describes specifically how a named block of code behaves.\\n\\n**Syntax:**\\n```python\\ndef function_name(parameter1, parameter2, ...):\\n    \\"\\"\\"Optional docstring explaining what the function does.\\"\\"\\"\\n    # Code Block: Indented statements that perform the task\\n    statement1\\n    statement2\\n    # ...\\n    return result # Optional: returns a value back to the caller\\n```\\n*   **`def`**: Keyword indicating the start of a function definition.\\n*   **`function_name`**: A unique name following standard variable naming rules.\\n*   **`()`**: Parentheses are required. They contain the parameters.\\n*   **`parameter1, parameter2, ...`** (Optional): Variables representing the input values the function expects to receive. If a function doesn't need input, the parentheses are empty: `def my_function():`.\\n*   **`:`**: Colon marks the end of the function definition line.\\n*   **Docstring** (Optional but recommended): A string literal (`\\"\\"\\"...\\"\\"\\"`) right after the `def` line explaining the function's purpose.\\n*   **Code Block**: One or more indented statements that make up the function's body.\\n*   **`return result`** (Optional): Sends the `result` value back to where the function was called. If omitted, the function implicitly returns `None`."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Function Examples"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Case 1: Function without Parameters and Return Values\\n\\nThis function performs a fixed action (printing a message) every time it's called. It doesn't need any input and doesn't send any result back (other than performing the print action)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the function\\ndef promo():\\n    print(\\"Spend over $50 for a 10% discount coupon.\\")\\n\\n# Call the function (multiple times)\\nprint(\\"Calling promo() the first time:\\")\\npromo()\\nprint(\\"\\\\nCalling promo() the second time:\\")\\npromo()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Case 2: Function with Parameters, No Explicit Return Value\\n\\nThis function takes inputs (parameters `min_amount`, `discount_rate`) to customize its action (the printed message). It still doesn't explicitly `return` a value."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the function with parameters\\ndef promo(min_amount, discount_rate):\\n    print(f\\"Spend over ${min_amount} for a {discount_rate}% discount coupon.\\")\\n\\n# Call the function with different arguments\\nprint(\\"Calling promo(50, 30):\\")\\npromo(50, 30)\\n\\nprint(\\"\\\\nCalling promo(30, 10):\\")\\npromo(30, 10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Case 3: Function with Parameters and a Return Value\\n\\nThis function takes inputs, performs a calculation based on a condition, and uses `return` to send the calculated result (`pay_amount`) back to the caller. The caller can then store this returned value in a variable or use it directly in further calculations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define the function with parameters and return\\ndef promo_order_pay(order_amount, min_amount, discount_rate):\\n    if order_amount > min_amount:\\n        # Apply discount\\n        pay_amount = order_amount * (100 - discount_rate) / 100\\n    else:\\n        # No discount\\n        pay_amount = order_amount\\n    return pay_amount"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Calling Case 3 Function and Using the Return Value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Call the function and store the returned value\\namount_after_discount = promo_order_pay(100, 50, 10) # Qualifies for 10% discount\\nprint(f\\"Amount after potential discount: ${amount_after_discount}\\")\\n\\n# Use the returned value in another calculation\\nsales_tax_rate = 14.975\\npay_amount_tax = amount_after_discount * (1 + (sales_tax_rate / 100))\\n\\nprint(f\\"Final amount including tax: ${pay_amount_tax:.4f}\\") \\n\\n# Example where discount is not applied\\namount_no_discount = promo_order_pay(40, 50, 10) # Doesn't meet min_amount\\nprint(f\\"\\\\nAmount for a $40 order: ${amount_no_discount}\\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Discussion: `return` vs. `print`\\n\\nWhat's the difference between using `return` and `print` inside a function?\\n\\n*   **`print()`:** Displays information to the console/output. It's for showing things to the user. It does *not* send a value back to the part of the code that called the function. The function implicitly returns `None` if it only contains `print` and no `return` statement.\\n*   **`return`:** Sends a value back from the function to the calling code. This returned value can be stored in a variable, used in calculations, passed to another function, etc. It does *not* automatically display anything to the console."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Example: `abs` with `return`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def abs_with_return(arg):\\n    if arg < 0:\\n        result = -1 * arg\\n    else:\\n        result = arg\\n    return result\\n\\n# Call and store the returned value\\nvalue = abs_with_return(-10)\\nprint(f\\"Result from abs_with_return(-10): {value}\\") \\nprint(f\\"Can use the result: {value * 2}\\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Example: `abs` with `print`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def abs_with_print(arg):\\n    if arg < 0:\\n        result = -1 * arg\\n    else:\\n        result = arg\\n    print(result) # Prints directly, doesn't return the value\\n\\n# Call the function\\nprint(\\"Calling abs_with_print(-10):\\")\\nvalue2 = abs_with_print(-10) # Function executes and prints 10\\n\\n# Check what value2 holds\\nprint(f\\"\\\\nValue stored in value2: {value2}\\")\\nprint(f\\"Type of value2: {type(value2)}\\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As you can see, `abs_with_print` displays the result (10), but the variable `value2` that tried to capture the result actually holds `None`. This is because the function didn't explicitly `return` the calculated `result`. Trying to use `value2` in a calculation would likely cause an error (e.g., `value2 * 2` would fail)."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}'''

# Parse the JSON string
notebook_data = json.loads(notebook_content)

# Write the notebook data to a file
with open('functions_in_python.ipynb', 'w') as f:
    json.dump(notebook_data, f, indent=2)

print("Notebook 'functions_in_python.ipynb' created successfully!") 