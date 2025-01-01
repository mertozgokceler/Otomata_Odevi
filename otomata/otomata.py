import tkinter as tk
from tkinter import messagebox

dfa_transitions = {
    'q0': {'a': 'q2', 'b': 'q1'},
    'q1': {'a': 'q4', 'b': 'q3'},
    'q2': {'a': 'q5', 'b': 'q4'},
    'q3': {'a': 'q6', 'b': 'q3'},
    'q4': {'a': 'q7', 'b': 'q6'},
    'q5': {'a': 'q5', 'b': 'q7'},
    'q6': {'a': 'q8', 'b': 'q6'},
    'q7': {'a': 'q7', 'b': 'q8'},
    'q8': {'a': 'q8', 'b': 'q8'},
}


dfa_accept_states = {'q8'}

def simulate_dfa_step_by_step(input_string):
    state = 'q0'  
    steps = []    
    for char in input_string:
        
        if state not in dfa_transitions:
            steps.append(f"'{char}' okundu: Geçersiz geçiş! (Durum: {state})")
            return steps, False
        
        if char in dfa_transitions[state]:
            next_state = dfa_transitions[state][char]
            steps.append(f"'{char}' okundu: {state} -> {next_state}")
            state = next_state
        else:
            steps.append(f"'{char}' okundu: Geçersiz geçiş!")
            return steps, False

    steps.append(f"Son durum: {state}")
    return steps, state in dfa_accept_states

def step_by_step_simulation():
    input_string = entry.get()  
    if not input_string:
        messagebox.showerror("Hata", "Lütfen bir dizge girin!")
        return

    steps, result = simulate_dfa_step_by_step(input_string)

    result_text.delete("1.0", tk.END)

    for step in steps:
        result_text.insert(tk.END, step + "\n")

    result_text.insert(tk.END, f"\nSonuç: {'Kabul' if result else 'Reddedildi'}")

root = tk.Tk()
root.title("DFA Simülatörü")
root.geometry("300x300")
root.configure(bg="black")
root.resizable(False, False)

input_frame = tk.Frame(root, bg="black")
input_frame.place(relx=0.5, rely=0.25, anchor="center")

entry = tk.Entry(input_frame, font=("Arial", 12, "bold"), bg="white", fg="black", width=20)
entry.pack(pady=5)

simulate_button = tk.Button(input_frame, text="Simüle Et", command=step_by_step_simulation, font=("Arial", 12, "bold"), bg="white", fg="black")
simulate_button.pack(pady=10)

result_text = tk.Text(root, height=10, bg="black", fg="white", font=("Courier", 10, "bold"))
result_text.pack(fill="both", padx=10, pady=10, side="bottom")

root.mainloop()