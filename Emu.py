import shlex, tkinter as tk

app = tk.Tk()
app.title("Эмулятор - [user@host]")  # Можно заменить на реальные данные позже

outbox = tk.Text(app, height=20)
outbox.pack(fill="both", expand=True)
entry = tk.Entry(app)
entry.pack(fill="x")

def submit(event=None):
    line = entry.get()
    entry.delete(0, "end")
    if not line.strip():
        return
    outbox.insert("end", f"$ {line}\n")
    try:
        tokens = shlex.split(line)
    except:
        outbox.insert("end", "parse error\n")
        return
    if not tokens:
        return
    cmd, args = tokens[0], tokens[1:]
    if cmd == "exit":
        app.destroy()
        return
    if cmd in ("ls", "cd"):
        outbox.insert("end", f"{cmd} {args}\n")
    else:
        outbox.insert("end", f"{cmd}: command not found\n")
    outbox.see("end")

entry.bind("<Return>", submit)
app.mainloop()