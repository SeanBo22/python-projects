import tkinter as tk
from tkinter import ttk

def show_selection():
    # Get selected values from the dropdowns
    selection1 = dropdown1.get()
    selection2 = dropdown2.get()
    selection3 = dropdown3.get()
    
    # Update the label with the selected values
    result_label.config(text=f"Selected values: {selection1}, {selection2}, {selection3}")

    

def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)

# Create the main window
root = tk.Tk()

# Get screen width and height
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

# Set the window size to full screen initially
root.geometry(f"{width}x{height}")
root.title("Testing")

# Create three dropdown menus with their labels
options1 = ["Option 1", "Option 2", "Option 3"]
options2 = ["Choice A", "Choice B", "Choice C"]
options3 = ["Item X", "Item Y", "Item Z"]

# Create StringVar for each dropdown
selected1 = tk.StringVar()
selected2 = tk.StringVar()
selected3 = tk.StringVar()

# Create and place the labels and dropdowns
label1 = tk.Label(root, text="Select an Option:")
label1.pack(pady=5)
dropdown1 = ttk.Combobox(root, textvariable=selected1, values=options1, state='readonly')
dropdown1.pack(pady=5)

label2 = tk.Label(root, text="Select a Choice:")
label2.pack(pady=5)
dropdown2 = ttk.Combobox(root, textvariable=selected2, values=options2, state='readonly')
dropdown2.pack(pady=5)

label3 = tk.Label(root, text="Select an Item:")
label3.pack(pady=5)
dropdown3 = ttk.Combobox(root, textvariable=selected3, values=options3, state='readonly')
dropdown3.pack(pady=5)

# Create a label to display the result
result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.pack(pady=20)

# Create and place the button
button = tk.Button(root, text="Send Command", command=show_selection)
button.pack(pady=10)

# Run the application
root.mainloop()
