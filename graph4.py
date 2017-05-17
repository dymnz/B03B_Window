from PIL import Image


size = [500, 500]

n=64
box=((-1.75,1),(0.25,-1))
plus = size[1]+size[0]
uleft = box[0]
lright = box[1]
xwidth = lright[0] - uleft[0]
ywidth = uleft[1] - lright[1]


im = Image.new("L", (size[0], size[1]))
for x in range(size[0]):
    for y in range(size[1]):
        coords = (uleft[0] + (x/size[0]) * (xwidth),uleft[1] - (y/size[1]) * (ywidth))
        z = complex(coords[0],coords[1])
        o = complex(0,0)
        dotcolor = 0  # default, convergent
        for trials in range(n):
            if abs(o) <= 2.0:
                o = o**2 + z
            else:
                dotcolor = trials/n*255
                break  # diverged
        im.putpixel((x,y),dotcolor)
im.save("mandelbrot.png", "PNG")

'''
for i in range(size):
    for j in range(size):
        x,y = ( x_center + 4.0*float(i-size/2)/size,
                  y_center + 4.0*float(j-size/2)/size
                )

        a,b = (0.0, 0.0)
        iteration = 0

        while (a**2 + b**2 <= 4.0 and iteration < max_iteration):
            a,b = a**2 - b**2 + x, 2*a*b + y
            iteration += 1
        if iteration == max_iteration:
            color_value = 255
        else:
            color_value = iteration*10 % 255
        im.putpixel( (i,j), (color_value, color_value, color_value))

im.save("mandelbrot.png", "PNG")'''