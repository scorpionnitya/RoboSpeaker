import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

def speak():
    text = entry.get("1.0", tk.END)
    engine.say(text)
    engine.runAndWait()

root = tk.Tk()
root.title("Robo Speaker")
root.geometry("400x300")

label = tk.Label(root, text="Robo Speaker", font=("Arial", 18))
label.pack(pady=10)

entry = tk.Text(root, height=8, width=40)
entry.pack(pady=10)

button = tk.Button(root, text="Speak", command=speak)
button.pack(pady=10)

root.mainloop()