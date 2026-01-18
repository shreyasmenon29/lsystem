import tkinter as tk
import turtle

def expand(a, r, i):
    current = a
    for _ in range(i):
        new = []
        for ch in current:
            new.append(r.get(ch, ch))
        current = "".join(new)
    return current

def draw(commands, angle, step):
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    pen.pendown()

    stack = []
    colors = ["red", "orange", "green", "blue", "purple"]

    for ch in commands:
        pen.pencolor(colors[len(stack) % len(colors)])

        if ch == "F":
            pen.forward(step)
        elif ch == "+":
            pen.right(angle)
        elif ch == "-":
            pen.left(angle)
        elif ch == "[":
            stack.append((pen.xcor(), pen.ycor(), pen.heading()))
        elif ch == "]":
            if stack:
                x, y, h = stack.pop()
                pen.penup()
                pen.goto(x, y)
                pen.setheading(h)
                pen.pendown()

    screen.update()

def generate():
    a = axiom_entry.get().strip()
    rule_text = rules_entry.get().strip()
    angle = float(angle_entry.get().strip())
    i = int(iter_entry.get().strip())
    step = float(step_entry.get().strip())

    r = {}
    if rule_text:
        for part in rule_text.split(";"):
            part = part.strip()
            if ":" in part:
                k, v = part.split(":", 1)
                r[k.strip()] = v.strip()

    commands = expand(a, r, i)
    draw(commands, angle, step)

def clear():
    pen.clear()
    screen.update()

def preset(name):
    if name == "Koch":
        axiom_entry.delete(0, "end")
        axiom_entry.insert(0, "F")
        rules_entry.delete(0, "end")
        rules_entry.insert(0, "F:F+F-F-F+F")
        angle_entry.delete(0, "end")
        angle_entry.insert(0, "90")
        iter_entry.delete(0, "end")
        iter_entry.insert(0, "3")
        step_entry.delete(0, "end")
        step_entry.insert(0, "6")

    elif name == "Tree":
        axiom_entry.delete(0, "end")
        axiom_entry.insert(0, "F")
        rules_entry.delete(0, "end")
        rules_entry.insert(0, "F:F[+F]F[-F]F")
        angle_entry.delete(0, "end")
        angle_entry.insert(0, "25")
        iter_entry.delete(0, "end")
        iter_entry.insert(0, "4")
        step_entry.delete(0, "end")
        step_entry.insert(0, "5")

    elif name == "Pentagon":
        axiom_entry.delete(0, "end")
        axiom_entry.insert(0, "F+F+F+F+F")
        rules_entry.delete(0, "end")
        rules_entry.insert(0, "")
        angle_entry.delete(0, "end")
        angle_entry.insert(0, "72")
        iter_entry.delete(0, "end")
        iter_entry.insert(0, "1")
        step_entry.delete(0, "end")
        step_entry.insert(0, "50")

root = tk.Tk()
root.title("L-System Fractal Architect")
root.geometry("1000x650")

left = tk.Frame(root, padx=10, pady=10)
left.pack(side="left", fill="y")

right = tk.Frame(root)
right.pack(side="right", fill="both", expand=True)

canvas = tk.Canvas(right, bg="white")
canvas.pack(fill="both", expand=True)

screen = turtle.TurtleScreen(canvas)
screen.tracer(0, 0)

pen = turtle.RawTurtle(screen)
pen.hideturtle()
pen.speed(0)

tk.Label(left, text="Axiom:").pack(anchor="w")
axiom_entry = tk.Entry(left, width=28)
axiom_entry.pack(anchor="w")
axiom_entry.insert(0, "F")

tk.Label(left, text="Rules (example: F:F+F-F-F+F):").pack(anchor="w", pady=(10, 0))
rules_entry = tk.Entry(left, width=28)
rules_entry.pack(anchor="w")
rules_entry.insert(0, "F:F+F-F-F+F")

tk.Label(left, text="Angle (degrees):").pack(anchor="w", pady=(10, 0))
angle_entry = tk.Entry(left, width=28)
angle_entry.pack(anchor="w")
angle_entry.insert(0, "90")

tk.Label(left, text="Iterations:").pack(anchor="w", pady=(10, 0))
iter_entry = tk.Entry(left, width=28)
iter_entry.pack(anchor="w")
iter_entry.insert(0, "3")

tk.Label(left, text="Step size (line length):").pack(anchor="w", pady=(10, 0))
step_entry = tk.Entry(left, width=28)
step_entry.pack(anchor="w")
step_entry.insert(0, "6")

tk.Button(left, text="Generate", command=generate).pack(anchor="w", pady=(15, 5))
tk.Button(left, text="Clear", command=clear).pack(anchor="w")

tk.Label(left, text="Presets:").pack(anchor="w", pady=(15, 5))
tk.Button(left, text="Koch", command=lambda: preset("Koch")).pack(anchor="w")
tk.Button(left, text="Tree", command=lambda: preset("Tree")).pack(anchor="w")
tk.Button(left, text="Pentagon", command=lambda: preset("Pentagon")).pack(anchor="w")

root.mainloop()
