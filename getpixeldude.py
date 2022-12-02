from PIL import Image, ImageColor, ImageFont, ImageDraw
import numpy as np
import random
import time

youtube_thumbnail = Image.open("thumbnail.jpg")
pixel_dude_base = Image.open("PixelDudeBase.png")

pixel_map = [
    # row 1
    ['outline', 0],
    ['outline', 0],
    ['outline', 0],
    ['outline', 0],
    ['outline', 0],
    ['outline', 0],
    ['outline', 0],
    ['outline', 0],
    ['outline', 0],
    ['outline', 0],

    # row 2
    ['outline', 0],
    ['face', 0],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['outline', 0],

    # row 3
    ['outline', 0],
    ['face', 0],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['outline', 0],

    # row 4
    ['outline', 0],
    ['face', 0],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['outline', 0],

    # row 5
    ['outline', 0],
    ['face', 0],
    ['face', 1],
    ['eye', 0],
    ['eye', 0],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['eye', 0],
    ['outline', 0],

    # row 6
    ['outline', 0],
    ['face', 0],
    ['face', 1],
    ['eye', 0],
    ['eye', 0],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['eye', 0],
    ['outline', 0],

    # row 7
    ['outline', 0],
    ['face', 0],
    ['face', 1],
    ['face', 0],
    ['face', 0],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 0],
    ['outline', 0],

    # row 8
    ['outline', 0],
    ['face', 0],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['outline', 0],

    # row 9
    ['outline', 0],
    ['face', 0],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['face', 1],
    ['outline', 0],

    # row 10
    ['outline', 0],
    ['suit', 0],
    ['suit', 0],
    ['suit', 0],
    ['suit', 0],
    ['suit', 0],
    ['suit', 0],
    ['suit', 0],
    ['suit', 0],
    ['outline', 0],

    # row 11
    ['outline', 0],
    ['suit', 1],
    ['suit', 1],
    ['suit', 1],
    ['suit', 1],
    ['suit', 1],
    ['suit', 1],
    ['suit', 1],
    ['suit', 1],
    ['outline', 0],

    # row 12
    ['outline', 0],
    ['suit', 1],
    ['suit', 1],
    ['suit', 1],
    ['suit', 1],
    ['suit', 1],
    ['suit', 1],
    ['suit', 1],
    ['suit', 1],
    ['outline', 0],

    # row 13
    ['outline', 0],
    ['suit', 0],
    ['suit', 0],
    ['outline', 0],
    ['outline', 0],
    ['outline', 0],
    ['outline', 0],
    ['suit', 0],
    ['suit', 0],
    ['outline', 0],

    # row 14
    ['outline', 0],
    ['suit', 0],
    ['outline', 0],
    ['outline', 1],
    ['outline', 1],
    ['outline', 1],
    ['outline', 0],
    ['suit', 0],
    ['outline', 0],
    ['outline', 1],

    # row 15
    ['outline', 0],
    ['outline', 0],
    ['outline', 1],
    ['outline', 1],
    ['outline', 1],
    ['outline', 1],
    ['outline', 0],
    ['outline', 0],
    ['outline', 1],
    ['outline', 1],
]

eye_options = [
    ["222033ff"],
    ["178178ff"],
    ["7722abff"],
    ["346524ff"],
    ["5a8ca6ff"],
    ["fafafaff"],
    ["abababff"],
    ["751f20ff"],
    ["da4e38ff"],
    ["000000ff"]
]

face_options = [
    ["aaaa55ff", "cccc77ff"],
    ["d1d1c2ff", "f0f0ddff"],
    ["877d78ff", "ccccbeff"],
    ["d9af83ff", "e6d1bcff"],
    ["af8055ff", "cb9f76ff"],
    ["7c5e46ff", "a47d5bff"],
    ["56252fff", "7a3333ff"],
    ["505436ff", "686e46ff"],
    ["aa6622ff", "dcb641ff"],
    ["5d96baff", "72b8e4ff"],
    ["8a344dff", "aa4951ff"],
    ["554444ff", "887777ff"],
    ["353535ff", "434343ff"],
    ["3c8802ff", "6cb832ff"]
]

suit_options = [
    ["726641ff", "91804cff"],
    ["aa6622ff", "ccaa44ff"],
    ["ee8e2eff", "facb3eff"],
    ["aa3333ff", "d04648ff"],
    ["828a58ff", "a9b757ff"],
    ["3d734fff", "4ba747ff"],
    ["d1d1c2ff", "f0f0ddff"],
    ["5a3173ff", "944a9cff"],
    ["3d62b3ff", "447ccfff"],
    ["5698ccff", "72d6ceff"],
    ["353535ff", "3e3e3eff"],
]

outline_options = [
    ["000000ff", "00000000"],
]


def hex_to_rgb(_hex):
    return tuple(int(_hex[i:i+2], 16) for i in (0, 2, 4, 6))


def create_pixel_dude():
    rand_eye_option = random.randint(0, len(eye_options) - 1)
    rand_face_option = random.randint(0, len(face_options) - 1)
    rand_suit_option = random.randint(0, len(suit_options) - 1)
    newimdata = []
    counter = 0

    for pixel in pixel_dude_base.getdata():
        if pixel_map[counter][0] == 'outline':
            if pixel_map[counter][1] == 0:
                newimdata.append(hex_to_rgb(
                    outline_options[0][pixel_map[counter][1]]))
            else:
                newimdata.append(pixel)
        elif pixel_map[counter][0] == 'eye':
            newimdata.append(hex_to_rgb(
                eye_options[rand_eye_option][pixel_map[counter][1]]))
        elif pixel_map[counter][0] == 'face':
            newimdata.append(hex_to_rgb(
                face_options[rand_face_option][pixel_map[counter][1]]))
        elif pixel_map[counter][0] == 'suit':
            newimdata.append(hex_to_rgb(
                suit_options[rand_suit_option][pixel_map[counter][1]]))
        counter += 1

    newim = Image.new(pixel_dude_base.mode, pixel_dude_base.size)
    newim.putdata(newimdata)
    newim = newim.resize((20, 30), 0)
    return newim


def paste_pixel_dude(name, pixel_dude):
    new_im = pixel_dude
    # 10,74 | 1250, 680
    ranx = random.randint(10, 1250)
    rany = random.randint(74, 680)
    youtube_thumbnail.paste(new_im, (ranx, rany), new_im)
    draw = ImageDraw.Draw(youtube_thumbnail)
    font = ImageFont.truetype("arialbd.ttf", 10)
    word = name
    w, h = draw.textsize(word, font=font)
    draw.text((((20-w)/2) + ranx + 0.25, ((30-h)/2) + rany + 19),
              word, (255, 255, 255), font=font)


def spawn_batch(names):
    temp_lines = []
    with open('existing_users.txt', 'r') as f:
        temp_lines = f.read().splitlines()

    with open('existing_users.txt', 'a') as f:
        for name in names:
            if name not in temp_lines:
                paste_pixel_dude(name, create_pixel_dude())
                f.write('\n' + name)
    youtube_thumbnail.save("thumbnail.jpg")
