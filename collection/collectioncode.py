import random
import turtle

window = turtle.Screen()
window.setup(1500, 800)

window.title("коллекция")
myPen = turtle.Turtle()
myPen.speed(0)
myPen.hideturtle()
myPen.color("#000000")

window.tracer(100, 1)

boxSize = 10

def box(intDim, color):
    myPen.color(color)
    myPen.begin_fill()
    myPen.forward(intDim)
    myPen.left(90)
    myPen.forward(intDim)
    myPen.left(90)
    myPen.forward(intDim)
    myPen.left(90)
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)

def load_matrix(file_path):
    matrix = []
    file = open(file_path, "r", encoding="utf-8")
    for line in file:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            row = []
            for x in parts:
                if x.strip() != "":
                    row.append(int(x.strip()))
            if row:
                matrix.append(row)
    file.close()
    return matrix

def merge_layers(eyes_file, hair_file, dress_file):
    body = load_matrix("шаблончики/body_base.txt")
    eyes = load_matrix("шаблончики/" + eyes_file)

    if hair_file == "none":
        hair = [[0 for _ in range(32)] for _ in range(32)]
    else:
        hair = load_matrix("шаблончики/" + hair_file)

    if dress_file == "none":
        dress = [[0 for _ in range(32)] for _ in range(32)]
    else:
        dress = load_matrix("шаблончики/" + dress_file)

    final_matrix = [[0 for _ in range(32)] for _ in range(32)]

    for r in range(32):
        for c in range(32):
            try:
                if dress[r][c] != 0:
                    final_matrix[r][c] = dress[r][c]
                elif eyes[r][c] != 0:
                    final_matrix[r][c] = eyes[r][c]
                elif hair[r][c] != 0:
                    final_matrix[r][c] = hair[r][c]
                else:
                    final_matrix[r][c] = body[r][c]
            except:
                final_matrix[r][c] = 0

    return final_matrix

def generate_collection(meow):
    eye_styles = [
        "eyes_style1.txt",
        "eyes_style2.txt",
        "eyes_style3.txt",
        "eyes_style4.txt",
        "eyes_style5.txt",
        "eyes_style6.txt"
        
    ]
    hair_styles = [
        "hair_style1.txt",
        "hair_style2.txt",
        "hair_style3.txt",
        "hair_style4.txt",
        "hair_style5.txt",
        "hair_style6.txt",
        "hair_style7.txt",
        "hair_style8.txt",
    ]
    dress_styles = [
        "dress_style1.txt",
        "dress_style2.txt",
        "dress_style3.txt",
        "dress_style4.txt",
        "dress_style5.txt",
        "dress_style6.txt",
        "dress_style7.txt",
        "dress_style8.txt",
        "dress_style9random.txt",
        "dress_style10random.txt",
    ]

    pupil_colors = [
        "#00FFFF",
        "#0000FF",
        "#FF0000",
        "#00FF00",
        "#FF00FF",
        "#FFA500",
        "#85929E",
    ]
    hair_colors = ["#6e5160",
                   "#B72441",
                   "#87338E",
                   "#464451",
                   "#E67E22",
                   "#FF69B4"
                   ]
    spacing = 32 * boxSize + 40
    start_x = -(meow * spacing) / 2

    for k in range(meow):
        rand_eyes = random.choice(eye_styles)
        rand_hair = random.choice(hair_styles)
        rand_dress = random.choice(dress_styles)

        now_pupil = random.choice(pupil_colors)
        now_hair = random.choice(hair_colors)

        character_matrix = merge_layers(rand_eyes, rand_hair, rand_dress)

        x_pos = start_x + (k * spacing)
        y_pos = 120

        myPen.penup()
        myPen.goto(x_pos, y_pos)
        myPen.setheading(0)
        myPen.pendown()

        for i in range(0, len(character_matrix)):
            for j in range(0, len(character_matrix[i])):
                pixel = character_matrix[i][j]
                # база тело
                if pixel == 1:
                    box(boxSize, "#000000")
                elif pixel == 2:
                    box(boxSize, "#ffe6ea")
                elif pixel == 3:
                    box(boxSize, now_hair)
                elif pixel == 4:
                    box(boxSize, now_pupil)
                elif pixel == 5:
                    box(boxSize, now_hair)
                elif pixel == 6:
                    box(boxSize, "#FFFFFF")
                elif pixel == 7:
                    box(boxSize, "#ffd7dd")
                elif pixel == 8:
                    box(boxSize, "#ffc6ce")
                elif pixel == 9:
                    box(boxSize, "#d095a8")

                # врач
                elif pixel == 10:
                    box(boxSize, "#8b9bb4")
                elif pixel == 11:
                    box(boxSize, "#262b44")
                elif pixel == 12:
                    box(boxSize, "#181425")
                elif pixel == 15:
                    box(boxSize, "#ff0044")
                elif pixel == 16:
                    box(boxSize, "#c0cbdc")

                # форма полицейского
                elif pixel == 21:
                    box(boxSize, "#0b0538")
                elif pixel == 22:
                    box(boxSize, "#2B2A4C")
                elif pixel == 23:
                    box(boxSize, "#fee761")
                elif pixel == 24:
                    box(boxSize, "#8b9bb4")
                elif pixel == 25:
                    box(boxSize, "#010103")
                    
                # военный
                elif pixel == 26:
                    box(boxSize, "#132d17")
                elif pixel == 27:
                    box(boxSize, "#265c42")

                # школьная форма
                elif pixel == 31:
                    box(boxSize, "#5e151d")
                elif pixel == 32:
                    box(boxSize, "#a22633")
                elif pixel == 33:
                    box(boxSize, "#bdaaa2")
                elif pixel == 34:
                    box(boxSize, "#7d6459")
                elif pixel == 35:
                    box(boxSize, "#262b44")

                # рукоять ножа у повара
                elif pixel == 36:
                    box(boxSize, "#733e39")

                else:
                    myPen.penup()
                    myPen.forward(boxSize)
                    myPen.pendown()
                    continue
                myPen.penup()
                myPen.forward(boxSize)
                myPen.pendown()
            myPen.setheading(270)
            myPen.penup()
            myPen.forward(boxSize)
            myPen.setheading(180)
            myPen.forward(boxSize * len(character_matrix[i]))
            myPen.setheading(0)
            myPen.pendown()
    window.update()
generate_collection(4)
turtle.done()

