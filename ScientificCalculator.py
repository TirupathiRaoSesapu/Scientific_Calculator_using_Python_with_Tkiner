from tkinter import *
import math

# Global variables
expression = ""
last_answer = ""
memory = 0

root = Tk()
root.title("Scientific Calculator")
root.configure(bg="#1e1e1e")
root.geometry("600x500")

equation = StringVar()

# Responsive layout
for i in range(6):
    root.columnconfigure(i, weight=1)
for i in range(7):
    root.rowconfigure(i, weight=1)

def press(key):
    global expression
    expression += str(key)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def evaluate():
    global expression, last_answer
    try:
        result = str(eval(expression))
        last_answer = result
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def scientific_function(func):
    global expression
    try:
        result = str(eval(f"math.{func}({expression})"))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def square_root():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def square():
    global expression
    try:
        result = str(float(expression) ** 2)
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def factorial():
    global expression
    try:
        result = str(math.factorial(int(float(expression))))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def absolute():
    global expression
    try:
        result = str(abs(float(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def memory_store():
    global memory
    try:
        memory = float(equation.get())
    except:
        memory = 0

def memory_recall():
    global expression
    expression += str(memory)
    equation.set(expression)

# Entry widget
entry = Entry(root, textvariable=equation, font=("Arial", 26), bg="#2e2e2e", fg="white",
              insertbackground="white", relief="ridge", borderwidth=4, justify="right")
entry.grid(row=0, column=0, columnspan=6, sticky="nsew", padx=2, pady=2)
entry.focus_set()

# Tooltip support
def create_tooltip(widget, text):
    tooltip = Toplevel(widget)
    tooltip.wm_overrideredirect(True)
    tooltip.withdraw()
    label = Label(tooltip, text=text, bg="yellow", fg="black", padx=5, pady=2, font=("Arial", 9))
    label.pack()

    def enter(event):
        tooltip.deiconify()

    def move_tooltip(event):
        x = event.x_root + 30
        y = event.y_root + 30
        tooltip.geometry(f"+{x}+{y}")
    
    def leave(event):
        tooltip.withdraw()

    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)
    widget.bind("<Motion>", move_tooltip)

# Button definitions
buttons = [
    ('C', 1, 0, clear, 'Clear all'), 
    ('⌫', 1, 1, backspace, 'Backspace'), 
    ('%', 1, 2, lambda: press('%'), 'Modulus'), 
    ('/', 1, 3, lambda: press('/'), 'Divide'),
    ('sqrt', 1, 4, square_root, 'Square root'), 
    ('x²', 1, 5, square, 'Square'),
    ('7', 2, 0, lambda: press('7'), 'Number 7'), 
    ('8', 2, 1, lambda: press('8'), 'Number 8'), 
    ('9', 2, 2, lambda: press('9'), 'Number 9'), 
    ('*', 2, 3, lambda: press('*'), 'Multiply'),
    ('(', 2, 4, lambda: press('('), 'Open braces'), 
    (')', 2, 5, lambda: press(')'), 'Closed braces'),
    ('4', 3, 0, lambda: press('4'), 'Number 4'), 
    ('5', 3, 1, lambda: press('5'), 'Number 5'), 
    ('6', 3, 2, lambda: press('6'), 'Number 6'), 
    ('-', 3, 3, lambda: press('-'), 'Subtract'),
    ('sin', 3, 4, lambda: scientific_function('sin'), 'Sine'), 
    ('cos', 3, 5, lambda: scientific_function('cos'), 'Cosine'),
    ('1', 4, 0, lambda: press('1'), 'Number 1'), 
    ('2', 4, 1, lambda: press('2'), 'Number 2'), 
    ('3', 4, 2, lambda: press('3'), 'Number 3'), 
    ('+', 4, 3, lambda: press('+'), 'Add'),
    ('tan', 4, 4, lambda: scientific_function('tan'), 'Tangent'), 
    ('log', 4, 5, lambda: scientific_function('log10'), 'Log base 10'),
    ('0', 5, 0, lambda: press('0'), 'Number 0'), 
    ('.', 5, 1, lambda: press('.'), 'Decimal'), 
    ('=', 5, 2, evaluate, 'Evaluate'),
    ('exp', 5, 3, lambda: scientific_function('exp'), 'Exponential'), 
    ('pi', 5, 4, lambda: press(str(math.pi)), 'Pi'), 
    ('!', 5, 5, factorial, 'Factorial'),
    ('Ans', 6, 0, lambda: press(last_answer), 'Last answer'), 
    ('|x|', 6, 1, absolute, 'Absolute value'),
    ('xʸ', 6, 2, lambda: press('**'), 'Power (x^y)'),
    ('ln', 6, 3, lambda: scientific_function('log'), 'Natural log'),
    ('M+', 6, 4, memory_store, 'Memory store'), 
    ('MR', 6, 5, memory_recall, 'Memory recall'),
]

for (text, row, col, cmd, tooltip_text) in buttons:
    btn = Button(root, text=text, command=cmd, padx=10, pady=10, font=("Arial", 20),
                 bg="#333", fg="white", activebackground="#555", activeforeground="white", bd=2)
    btn.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
    create_tooltip(btn, tooltip_text)

# Key bindings
def key_input(event):
    global expression
    if event.char in '0123456789+-*/%.()':
        press(event.char)
    elif event.keysym == 'Return':
        evaluate()
    elif event.keysym == 'BackSpace':
        backspace()

root.bind("<Key>", key_input)

# Run the GUI loop
root.mainloop()