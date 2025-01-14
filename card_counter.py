import tkinter as tk


# Hi-Opt II Card Counting Logic
def hi_opt_ii_count(card):
    if card in [2, 3, 6, 7]:
        return 1
    elif card in [4, 5]:
        return 2
    elif card == 10:  # 10 count as -2
        return -2
    return 0


# Hi-Lo Card Counting Logic
def hi_lo_count(card):
    if card in [2, 3, 4, 5, 6]:
        return 1
    elif card == 10 or card == "A":  # Both 10 and Aces are counted as -1
        return -1
    return 0


# Update True Count and Expected Aces Label Colors
def update_true_count_color(true_count):
    if true_count >= 1:
        true_count_label.config(fg="lime")
    elif true_count <= -1:
        true_count_label.config(fg="red")
    else:
        true_count_label.config(fg="white")


def update_ace_label_color(aces_expected, aces_dealt):
    if (aces_expected - aces_dealt) >= 1:
        ace_count_label.config(fg="lime")
    elif (aces_dealt - aces_expected) >= 1:
        ace_count_label.config(fg="red")
    else:
        ace_count_label.config(fg="white")


# Create the main window
window = tk.Tk()
window.title("Card Counter")
window.geometry("700x600")
window.configure(bg="#1e1e1e")

# Variables to track counts and card history
running_count = 0
deck_count = 8
cards_dealt = 0
aces_dealt = 0
card_history = []
counting_system = "Hi-Opt II"


# Update the counts and deck penetration percentage
def update_counts(card):
    global running_count, cards_dealt, aces_dealt, card_history

    if counting_system == "Hi-Opt II":
        running_count += hi_opt_ii_count(card)
    elif counting_system == "Hi-Lo":
        running_count += hi_lo_count(card)

    cards_dealt += 1
    if card == "A":
        aces_dealt += 1

    remaining_decks = max(0, deck_count - (cards_dealt / 52))
    true_count = running_count / (remaining_decks if remaining_decks > 0 else 1)
    deck_penetration = (cards_dealt / (deck_count * 52)) * 100
    decks_dealt = deck_count - remaining_decks
    aces_expected = decks_dealt * 4

    running_count_label.config(text=f"Running Count: {running_count}")
    true_count_label.config(text=f"True Count: {true_count:.2f}")
    update_true_count_color(true_count)
    deck_penetration_label.config(
        text=f"Deck Penetration: {deck_penetration:.2f}% | Cards Dealt: {cards_dealt} | Remaining Decks: {remaining_decks:.2f}"
    )

    if counting_system == "Hi-Lo":
        ace_count_label.config(text="Aces are not counted separately in Hi-Lo")
    else:
        ace_count_label.config(
            text=f"Aces Dealt: {aces_dealt} (Expected: {aces_expected:.2f})"
        )
        update_ace_label_color(aces_expected, aces_dealt)

    card_history.append(card)
    if len(card_history) > 20:
        card_history.pop(0)
    card_history_label.config(text="Card History: " + ", ".join(map(str, card_history)))


# Reset the counts and deck information
def reset_counts():
    global running_count, cards_dealt, aces_dealt, card_history
    running_count = 0
    cards_dealt = 0
    aces_dealt = 0
    card_history = []
    running_count_label.config(text="Running Count: 0", fg="white")
    true_count_label.config(text="True Count: 0.00", fg="white")
    deck_penetration_label.config(
        text=f"Deck Penetration: 0.00% | Cards Dealt: 0 | Remaining Decks: {deck_count}",
        fg="white",
    )
    ace_count_label.config(text="Aces are not counted separately in Hi-Lo", fg="white")
    card_history_label.config(text="Card History: ", fg="white")


#Remove the most recent card from the history and adjust the count accordingly.
def delete_last_hand():
    global running_count, cards_dealt, aces_dealt, card_history

    if len(card_history) > 0:
        last_card = card_history.pop()

        # Update counts based on the last card
        if counting_system == "Hi-Opt II":
            running_count -= hi_opt_ii_count(last_card)
        elif counting_system == "Hi-Lo":
            running_count -= hi_lo_count(last_card)

        if last_card == "A":
            aces_dealt -= 1
        cards_dealt -= 1

        remaining_decks = max(0, deck_count - (cards_dealt / 52))
        true_count = running_count / (remaining_decks if remaining_decks > 0 else 1)
        deck_penetration = (cards_dealt / (deck_count * 52)) * 100
        decks_dealt = deck_count - remaining_decks
        aces_expected = decks_dealt * 4

        # Update the labels
        running_count_label.config(text=f"Running Count: {running_count}")
        true_count_label.config(text=f"True Count: {true_count:.2f}")
        update_true_count_color(true_count)
        deck_penetration_label.config(
            text=f"Deck Penetration: {deck_penetration:.2f}% | Cards Dealt: {cards_dealt} | Remaining Decks: {remaining_decks:.2f}"
        )

        if counting_system == "Hi-Lo":
            ace_count_label.config(text="Aces are not counted separately in Hi-Lo")
        else:
            ace_count_label.config(
                text=f"Aces Dealt: {aces_dealt} (Expected: {aces_expected:.2f})"
            )
            update_ace_label_color(aces_expected, aces_dealt)

        card_history_label.config(text="Card History: " + ", ".join(map(str, card_history)))


# Update the counting system based on selection
def set_counting_system(new_system):
    global counting_system
    counting_system = new_system
    reset_counts()


# Update the deck count based on selection
def set_deck_count(new_count):
    global deck_count
    deck_count = int(new_count)
    reset_counts()


# Counting System and Deck Selection Row
options_frame = tk.Frame(window, bg="#1e1e1e")
options_frame.pack(pady=10)

# Counting System Label and Dropdown
counting_system_label = tk.Label(
    options_frame,
    text="Counting Technique:",
    font=("Arial", 14),
    bg="#1e1e1e",
    fg="white",
)
counting_system_label.grid(row=0, column=0, padx=10, pady=5)

counting_system_var = tk.StringVar(value="Hi-Opt II")
counting_system_dropdown = tk.OptionMenu(
    options_frame,
    counting_system_var,
    "Hi-Opt II",
    "Hi-Lo",
    command=set_counting_system,
)
counting_system_dropdown.config(width=10)
counting_system_dropdown.grid(row=0, column=1, padx=10, pady=5)

# Deck Count Label and Dropdown
deck_count_label = tk.Label(
    options_frame, text="Number of Decks:", font=("Arial", 14), bg="#1e1e1e", fg="white"
)
deck_count_label.grid(row=0, column=2, padx=10, pady=5)

deck_count_var = tk.StringVar(value="8")
deck_count_dropdown = tk.OptionMenu(
    options_frame,
    deck_count_var,
    *[str(i) for i in range(1, 9)],
    command=set_deck_count,
)
deck_count_dropdown.config(width=10)
deck_count_dropdown.grid(row=0, column=3, padx=10, pady=5)

# Labels for Key Metrics
label_font = ("Arial", 18, "bold")
running_count_label = tk.Label(
    window, text="Running Count: 0", font=label_font, bg="#1e1e1e", fg="white"
)
running_count_label.pack(pady=10)

true_count_label = tk.Label(
    window, text="True Count: 0.00", font=label_font, bg="#1e1e1e", fg="white"
)
true_count_label.pack(pady=10)

deck_penetration_label = tk.Label(
    window,
    text=f"Deck Penetration: 0.00% | Cards Dealt: 0 | Remaining Decks: {deck_count}",
    font=label_font,
    bg="#1e1e1e",
    fg="white",
)
deck_penetration_label.pack(pady=10)

ace_count_label = tk.Label(
    window,
    text="Aces are not counted separately in Hi-Lo",
    font=label_font,
    bg="#1e1e1e",
    fg="white",
)
ace_count_label.pack(pady=10)

card_history_label = tk.Label(
    window, text="Card History: ", font=label_font, bg="#1e1e1e", fg="white"
)
card_history_label.pack(pady=10)

# Buttons for each card type
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A"]
button_frame = tk.Frame(window, bg="#1e1e1e")
button_frame.pack(pady=20)

for idx, value in enumerate(card_values):
    button = tk.Button(
        button_frame,
        text=str(value),
        command=lambda value=value: update_counts(value),
        font=("Arial", 14, "bold"),
        bg="#333333",
        fg="white",
        width=5,
        height=2,
    )
    button.grid(row=idx % 5, column=idx // 5, padx=5, pady=5)

# Reset button
reset_button = tk.Button(
    window,
    text="Reset",
    command=reset_counts,
    font=("Arial", 16, "bold"),
    bg="#333333",
    fg="white",
    width=10,
    height=2,
)
reset_button.pack(pady=20)

#Delete Last Card Button
# Delete Last Hand Button
delete_button = tk.Button(
    window,
    text="Delete Last Hand",
    command=delete_last_hand,
    font=("Arial", 16, "bold"),
    bg="#333333",
    fg="white",
    width=15,
    height=2,
)
delete_button.pack(pady=10)


# Start the Tkinter event loop
window.mainloop()
