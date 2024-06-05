import colorgram

object_colors = colorgram.extract("Image.jpg", 30)
colors = []
for each in object_colors:
    r = each.rgb.r
    g = each.rgb.g
    b = each.rgb.b
    colors.append((r, g, b))

print(colors)
