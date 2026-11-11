import tkinter as tk
import webbrowser

GAMES = [
    ("CS1.6 SOURCE EDITION", "https://down-cs.su/download.php?id=source&type=1"),
    ("CS1.6 CONDITION ZERO", "https://down-cs.su/download/139/direct"),
    ("CS1.6 WINTER EDITION", "https://down-cs.su/download.php?id=winter&type=1"),
    ("CS1.6 CSGO EDITION", "https://down-cs.su/download.php?id=csgo&type=1"),
    ("CS1.6 WARZONE EDITION", "https://down-cs.su/download.php?id=warzone&type=1"),
    ("CS1.8 (BEST)", "https://down-cs.su/download/78/direct"),
    ("CS1.6 PRO EDITION", "https://down-cs.su/download/172/direct"),
    ("CS1.6 FORTNITE EDITION", "https://down-cs.su/download.php?id=fortnite&type=1"),
]

BG = "#090d0b"
CARD = "#151d19"
GREEN = "#39ff14"
RED = "#ff3030"
WHITE = "#ffffff"

root = tk.Tk()
root.title("SHKTN.GAMING.SHOW")
root.geometry("1000x720")
root.configure(bg=BG)
root.minsize(800, 600)

header = tk.Frame(root, bg=BG)
header.pack(fill="x", pady=22)

tk.Label(
    header,
    text="SHKTN.GAMING.SHOW",
    font=("Arial", 28, "bold"),
    fg=GREEN,
    bg=BG
).pack()

tk.Label(
    header,
    text="SHERVAN + KASRA  |  GAMING LAUNCHER",
    font=("Arial", 11, "bold"),
    fg=RED,
    bg=BG
).pack(pady=7)

tk.Label(
    root,
    text="COUNTER STRIKES",
    font=("Arial", 19, "bold"),
    fg=WHITE,
    bg=BG
).pack(pady=12)

container = tk.Frame(root, bg=BG)
container.pack(fill="both", expand=True, padx=35, pady=10)

for index, (name, url) in enumerate(GAMES):
    row = index // 2
    col = index % 2

    card = tk.Frame(
        container,
        bg=CARD,
        highlightbackground=GREEN,
        highlightthickness=1
    )
    card.grid(row=row, column=col, padx=12, pady=12,
              sticky="nsew")

    tk.Label(
        card,
        text=name,
        font=("Arial", 12, "bold"),
        fg=WHITE,
        bg=CARD,
        wraplength=350
    ).pack(pady=(18, 12))

    tk.Button(
        card,
        text="DOWNLOAD",
        font=("Arial", 11, "bold"),
        bg=GREEN,
        fg="#000000",
        activebackground=RED,
        activeforeground=WHITE,
        relief="flat",
        cursor="hand2",
        command=lambda link=url: webbrowser.open(link)
    ).pack(pady=(0, 18), ipadx=22, ipady=5)

for col in range(2):
    container.columnconfigure(col, weight=1)

footer = tk.Label(
    root,
    text="SHKTN GAMING SHOW  |  ALL RIGHTS RESERVED",
    font=("Arial", 9),
    fg=GREEN,
    bg=BG
)
footer.pack(pady=12)

root.mainloop()
