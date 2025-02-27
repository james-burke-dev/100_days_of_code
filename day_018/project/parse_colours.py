import colorgram

extraction = colourgram.extract("image.jpg", 30)
colours = []

for colour in extraction:
    data = (colour.rgb.r, colour.rgb.g, colour.rgb.b)
    colours.append(data)

print(colours)