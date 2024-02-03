import turtle

def pifagor_tree(t: turtle.Turtle, i, rec_level, max_rec_level):
    if rec_level > max_rec_level:
        return
    else:
        t.forward(i)
        t.left(45)
        pifagor_tree(t, 3/4*i, rec_level+1, max_rec_level)
        t.right(90)
        pifagor_tree(t, 3/4*i, rec_level+1, max_rec_level)
        t.left(45)
        t.backward(i)

def draw_tree(rec_level, size=150):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(0, -size)
    t.pendown()
    t.left(90)

    pifagor_tree(t, size, 0, rec_level)

    window.mainloop()


def main():
    # Виклик функції
    try:
        i = int(input('Please input recursion level number >>> '))
        draw_tree(i)
    except:
        print('Error: recursion level incorrect...')

if __name__ =='__main__':
    main()