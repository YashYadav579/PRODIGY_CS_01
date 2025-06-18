import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

def process():
    text = text_input.get("1.0", tk.END).strip()
    shift_str = shift_input.get().strip()
    mode = mode_var.get()

    if not text:
        messagebox.showwarning("Input Needed", "Please enter some text.")
        return

    if not shift_str.isdigit():
        messagebox.showerror("Invalid Shift", "Shift must be a positive integer.")
        return

    shift = int(shift_str)
    result = caesar_cipher(text, shift, mode)
    output_display.config(state='normal')
    output_display.delete("1.0", tk.END)
    output_display.insert(tk.END, result)
    output_display.config(state='disabled')

def clear_all():
    text_input.delete("1.0", tk.END)
    shift_input.delete(0, tk.END)
    output_display.config(state='normal')
    output_display.delete("1.0", tk.END)
    output_display.config(state='disabled')

def copy_result():
    result = output_display.get("1.0", tk.END).strip()
    if result:
        pyperclip.copy(result)
        messagebox.showinfo("Copied", "Result copied to clipboard.")

# GUI setup
root = tk.Tk()
root.title("Advanced Caesar Cipher")
root.geometry("500x450")
root.resizable(False, False)

# Input frame
frame_input = ttk.LabelFrame(root, text="Input")
frame_input.pack(padx=20, pady=10, fill="both")

tk.Label(frame_input, text="Enter your message:").pack(anchor='w', padx=10, pady=(5, 0))
text_input = tk.Text(frame_input, height=5, width=60)
text_input.pack(padx=10, pady=5)

tk.Label(frame_input, text="Enter shift value:").pack(anchor='w', padx=10, pady=(5, 0))
shift_input = tk.Entry(frame_input, width=10)
shift_input.pack(padx=10, pady=5)

mode_var = tk.StringVar(value="encrypt")
ttk.Radiobutton(frame_input, text="Encrypt", variable=mode_var, value="encrypt").pack(side="left", padx=10)
ttk.Radiobutton(frame_input, text="Decrypt", variable=mode_var, value="decrypt").pack(side="left")

# Button frame
frame_buttons = ttk.Frame(root)
frame_buttons.pack(pady=10)

ttk.Button(frame_buttons, text="Process", command=process).pack(side="left", padx=10)
ttk.Button(frame_buttons, text="Clear", command=clear_all).pack(side="left", padx=10)
ttk.Button(frame_buttons, text="Copy Result", command=copy_result).pack(side="left", padx=10)

# Output frame
frame_output = ttk.LabelFrame(root, text="Output")
frame_output.pack(padx=20, pady=10, fill="both", expand=True)

output_display = tk.Text(frame_output, height=6, width=60, state='disabled', wrap='word')
output_display.pack(padx=10, pady=10)

# Run GUI
root.mainloop()
