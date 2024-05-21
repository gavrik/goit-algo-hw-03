import turtle

def koch_curve(fig, order, size):
    if order == 0:
        fig.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(fig, order-1, size / 3)
            fig.left(angle)

def draw_koch_fig(order, size = 300):
    window = turtle.Screen()
    window.bgcolor("white")

    fig = turtle.Turtle()
    fig.speed(10)
    fig.penup()
    fig.goto(-size / 2, 0)
    fig.pendown()
    for i in range(3):
        koch_curve(fig, order, size)
        fig.right(120)

    window.mainloop()

if __name__ == "__main__":
    print("Введіть глибину рекурсії:")
    inp = int(input())
    draw_koch_fig(inp)
