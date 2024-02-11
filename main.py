import tkinter as tk

def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + str(value))
    
def clear_entry():
    entry_var.set("")

def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")
        
window = tk.Tk()
window.geometry("400x300")
window.title("Máy tính")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x_position}+{y_position}")

center_window(window, 400, 300)

entry_var = tk.StringVar()

entry = tk.Entry(window, 
                 textvariable=entry_var, 
                 font=("Helvetica", 17), 
                 justify="right", 
                 bd=1, 
                 width=30)
entry.place(height=50)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
for (text, row, col) in buttons:
    button = tk.Button(window, text=text, font=("Helvetica", 11), command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, sticky="nsew")

# Thiết lập các cột và hàng để tự động co giãn
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Thiết lập chức năng cho nút "C" và "="
tk.Button(window, text="C", font=("Helvetica", 14), command=clear_entry).grid(row=4, column=1, sticky="nsew")
tk.Button(window, text="=", font=("Helvetica", 14), command=calculate_result).grid(row=4, column=2, sticky="nsew")


window.mainloop()