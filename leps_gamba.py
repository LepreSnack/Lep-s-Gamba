import tkinter as tk
import random

COLOR_CODES = {
    "Red": "#c0392b",
    "Orange": "#e67e22",
    "Yellow": "#f4d03f",
    "Green": "#196f3d",
    "Blue": "#1f618d",
    "Purple": "#6c3483",
    "Cyan": "#5dade2",
    "Teal": "#48c9b0",
    "Pink": "#f1948a",
    "Magenta": "#af7ac5",
    "Bronze": "#9c640c",
    "Silver": "#808b96",
    "Gold": "#9a7d0a",
    "Black": "#17202a",
    "White": "#ecf0f1",
}

RARITY_COLORS = {
    "Common": "#7f8c8d",
    "Uncommon": "#58d68d",
    "Rare": "#5499c7",
    "Epic": "#a569bd",
    "Legendary": "#f8c471",
    "Ultra Rare": "#ec7063",
    "Exotic": "#d7dbdd",
}

SPECIAL_RARITY_COLORS = {
    "Super Legendary": "#d68910",
    "Mythical": "#cb4335",
    "Godlike": "#3498db",
    "Unique": "#1abc9c",
    "Mystic": "#27ae60",
    "Transcendent": "#b2babb",
}

def spin_wheel():
    button_spin.config(state=tk.DISABLED)
    for i in range(4):
        save_button [i].config(state=tk.DISABLED)
    flicker_text()
    label_result.after(1500, lambda: reset_buttons())
        
def reset_buttons ():
    button_spin.config(state=tk.NORMAL)
    for i in range(4):
        save_button [i].config(state=tk.NORMAL)

def flicker_text():
    def generate_prize():
        color = random.choices(colors, weights=color_weights)[0]
        rarity = random.choices(rares, weights=rarity_weights)[0]
        special_rarity = random.choices(special_rares, weights=special_rarity_weights)[0]
        return f"{color} {rarity} {special_rarity}".strip(), color, rarity, special_rarity

    def toggle_text():
        prize, color, rarity, special_rarity = generate_prize()
        label_result.config(
            text=prize,
            fg=COLOR_CODES.get(color, "#2E2E2E"),
            bg=RARITY_COLORS.get(rarity, "#2E2E2E"),
            highlightbackground=SPECIAL_RARITY_COLORS.get(special_rarity, "#2E2E2E"),
            highlightthickness=2 if special_rarity else 0
        )
        return prize, color, rarity, special_rarity

    def show_final_result():
        toggle_text()

    for i in range(5):
        label_result.after(i * 300, toggle_text)
    label_result.after(1500, show_final_result)

def save_to_slot(slot_index):
    slot_labels[slot_index].config(
        text=label_result.cget("text"),
        fg=label_result.cget("fg"),
        bg=label_result.cget("bg"),
        highlightbackground=label_result.cget("highlightbackground"),
        highlightthickness=label_result.cget("highlightthickness")
    )

def display_rarity_chart():
    for widget in chart_frame.winfo_children():
        widget.destroy()

    tk.Label(chart_frame, text="Colors", font=("Arial", 12, "bold"), bg="#2E2E2E", fg="#ffffff").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    tk.Label(chart_frame, text="Rarities", font=("Arial", 12, "bold"), bg="#2E2E2E", fg="#ffffff").grid(row=0, column=1, sticky="w", padx=10, pady=5)
    tk.Label(chart_frame, text="Special Rarities", font=("Arial", 12, "bold"), bg="#2E2E2E", fg="#ffffff").grid(row=0, column=2, sticky="w", padx=10, pady=5)

    for i, (color, weight) in enumerate(zip(colors, color_weights)):
        tk.Label(chart_frame, text=f"{color}: {weight}%", font=("Arial", 11), bg="#2E2E2E", fg="#ffffff").grid(row=i + 1, column=0, sticky="w", padx=10, pady=2)

    for i, (rarity, weight) in enumerate(zip(rares, rarity_weights)):
        tk.Label(chart_frame, text=f"{rarity}: {weight}%", font=("Arial", 11), bg="#2E2E2E", fg="#ffffff").grid(row=i + 1, column=1, sticky="w", padx=10, pady=2)

    for i, (special_rarity, weight) in enumerate(zip(special_rares, special_rarity_weights)):
        tk.Label(chart_frame, text=f"{special_rarity}: {weight}%", font=("Arial", 11), bg="#2E2E2E", fg="#ffffff").grid(row=i + 1, column=2, sticky="w", padx=10, pady=2)

def calculate_probability(color, rarity, special_rarity):
    def handle_none(category, weights, index):
        if category == "":
            return 1
        return weights[index] / 100

    color_index = colors.index(color)
    rarity_index = rares.index(rarity)
    special_rarity_index = special_rares.index(special_rarity)

    color_prob = handle_none(color, color_weights, color_index)
    rarity_prob = handle_none(rarity, rarity_weights, rarity_index)
    special_rarity_prob = handle_none(special_rarity, special_rarity_weights, special_rarity_index)

    combined_prob = color_prob * rarity_prob * special_rarity_prob

    probability_label.config(text=f"Probability: {combined_prob*100:.10f}%")

def on_select_combination():
    selected_color = color_var.get()
    selected_rarity = rarity_var.get()
    selected_special_rarity = special_rarity_var.get()

    calculate_probability(selected_color, selected_rarity, selected_special_rarity)

colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Cyan", "Teal", "Pink", "Magenta", "Bronze", "Silver", "Gold", "Black", "White"]
rares = ["", "Common", "Uncommon", "Rare", "Epic", "Legendary", "Ultra Rare", "Exotic"]
special_rares = ["", "Super Legendary", "Unique", "Mystic", "Godlike", "Mythical", "Transcendent"]

color_weights = [13.34, 12.39, 11.44, 10.49, 9.54, 8.59, 7.64, 6.69, 5.74, 4.79, 3.84, 2.89, 1.94, 0.99, 0.01]
rarity_weights = [52, 20, 8.32, 3.33, 1.33, 0.53, 0.21, 0.01]
special_rarity_weights = [60, 21, 7.35, 2.57, 0.90, 0.32, 0.01]

root = tk.Tk()
root.title("Lep's Gamba")
root.geometry("1000x600")
root.config(bg="#2E2E2E")

label_result = tk.Label(root, text="Click 'Roll' to start!", font=("Arial", 16), width=40, height=2, bg="#2E2E2E", fg="#ffffff",
                        activebackground="#1f618d", activeforeground="#2E2E2E",
                        highlightbackground="#2E2E2E", highlightcolor="#ffffff", bd=25)
label_result.pack(pady=20)

button_spin = tk.Button(root, text="Roll", font=("Arial", 16), command=spin_wheel,
                        bg="#2E2E2E", fg="#ffffff", activebackground="#1f618d", activeforeground="#2E2E2E",
                        highlightbackground="#2E2E2E", highlightcolor="#ffffff", bd=2)
button_spin.pack(pady=10)

save_slots_frame = tk.Frame(root, bg="#2E2E2E")
save_slots_frame.pack(pady=20, expand=True)

save_button = []

slot_labels = []
for i in range(4):
    slot_label = tk.Label(save_slots_frame, text="", font=("Arial", 12), width=20, height=2, wraplength=200, relief="flat", highlightthickness=0)
    slot_label.pack(side="left", padx=10, pady=5)
    slot_labels.append(slot_label)
    button = tk.Button(save_slots_frame, text=f"Save {i + 1}", command=lambda idx=i: save_to_slot(idx),
              bg="#2E2E2E", fg="#ffffff", activebackground="#1f618d", activeforeground="#2E2E2E",
              highlightbackground="#2E2E2E", highlightcolor="#ffffff", bd=2)
    button.pack(side="left", padx=10, pady=10)
    save_button.append (button)

side_by_side_frame = tk.Frame(root, bg="#2E2E2E")
side_by_side_frame.pack(fill="both", expand=True, padx=10, pady=10)

chart_frame = tk.Frame(side_by_side_frame, bg="#2E2E2E", width=400)
chart_frame.pack(side="left", padx=10, pady=10, expand=True)

calculator_frame = tk.Frame(side_by_side_frame, bg="#2E2E2E")
calculator_frame.pack(side="right", padx=10, pady=10, expand=True)

color_var = tk.StringVar(value=colors[0])
rarity_var = tk.StringVar(value=rares[0])
special_rarity_var = tk.StringVar(value=special_rares[0])

tk.Label(calculator_frame, text="Select Color", font=("Arial", 12), bg="#2E2E2E", fg="#ffffff").pack()
color_menu = tk.OptionMenu(calculator_frame, color_var, *colors)
color_menu.config(bg="#2E2E2E", fg="#ffffff", activebackground="#1f618d", activeforeground="#2E2E2E",
                  highlightbackground="#2E2E2E", highlightcolor="#ffffff", bd=2)
color_menu.pack(pady=5)

tk.Label(calculator_frame, text="Select Rarity", font=("Arial", 12), bg="#2E2E2E", fg="#ffffff").pack()
rarity_menu = tk.OptionMenu(calculator_frame, rarity_var, *rares)
rarity_menu.config(bg="#2E2E2E", fg="#ffffff", activebackground="#1f618d", activeforeground="#2E2E2E",
                   highlightbackground="#2E2E2E", highlightcolor="#ffffff", bd=2)
rarity_menu.pack(pady=5)

tk.Label(calculator_frame, text="Select Special Rarity", font=("Arial", 12), bg="#2E2E2E", fg="#ffffff").pack()
special_rarity_menu = tk.OptionMenu(calculator_frame, special_rarity_var, *special_rares)
special_rarity_menu.config(bg="#2E2E2E", fg="#ffffff", activebackground="#1f618d", activeforeground="#2E2E2E",
                           highlightbackground="#2E2E2E", highlightcolor="#ffffff", bd=2)
special_rarity_menu.pack(pady=5)

probability_button = tk.Button(calculator_frame, text="Calculate Probability", command=on_select_combination)
probability_button.config(bg="#2E2E2E", fg="#ffffff", activebackground="#1f618d", activeforeground="#2E2E2E",
                          highlightbackground="#2E2E2E", highlightcolor="#ffffff", bd=2)
probability_button.pack(pady=10)

probability_label = tk.Label(calculator_frame, text="Probability: ", font=("Arial", 12), bg="#2E2E2E", fg="#ffffff")
probability_label.pack(pady=5)

display_rarity_chart()

root.mainloop()
