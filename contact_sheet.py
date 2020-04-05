from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



image = Image.open("readonly/msi_recruitment.gif")
image = image.convert('RGBA')

# retrieve color channel data from image
color_data = image.getdata()

drawing_object = ImageDraw.Draw(image)

# TODO put course font below
font = ImageFont.truetype(r'/usr/share/fonts/truetype/freefont/FreeSerif.ttf', 40)

## creating image list
images = []

for row in range(3):
    intensity = 0
    row_color = None

    # assign color of each row in contact sheet
    if   row % 3 == 0:  row_color = 'blue'
    elif row % 3 == 1:  row_color = 'red'
    elif row % 3 == 2:  row_color = 'yellow'


    for column in range(3):

        # paint black background box for text on bottom of image
        drawing_object.rectangle((0, image.height, image.width, 400), fill='black')

        # assign intensity per column
        # and print color channel being changed and its intensity
        if   column % 3 == 0:
            intensity = 0.1
            drawing_object.text((0, 410), 'channel {row} intensity {intensity}'.format(row= row, intensity= intensity), fill='white', font= font)

        elif column % 3 == 1:
            intensity = 0.5
            drawing_object.text((0, 410), 'channel {row} intensity {intensity}'.format(row= row, intensity= intensity), fill='white', font= font)

        elif column % 3 == 2:
            intensity = 0.9
            drawing_object.text((0, 410), 'channel {row} intensity {intensity}'.format(row= row, intensity= intensity), fill='white', font= font)


        # create each color scaled image in grid
        # scaling each respective RGB channel based on what row the image is on
        color_scaled_image = None
        if row_color == 'blue':
            color_scaled_image = [(int(d[0]*intensity),                d[1],                d[2]) for d in color_data]

        elif row_color == 'red':
            color_scaled_image = [(               d[0], int(d[1]*intensity),                d[2]) for d in color_data]

        elif row_color == 'yellow':
            color_scaled_image = [(               d[0],                d[1], int(d[2]*intensity)) for d in color_data]

        # make copy of original image and put color scale on the new image
        new_image = image.copy()
        new_image.putdata(color_scaled_image)

        images.append(new_image)


contact_sheet = Image.new(image.mode, (image.width*3,image.height*3))
x = 0
y = 0

# TODO do something about shadowing iterator var?
for image in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(image, (x, y))

    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x + image.width == contact_sheet.width:
        x = 0
        y = y + image.height
    else:
        x = x + image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet.show()








# image.load()
# image2 = image.copy()
# image3 = image.copy()

## Suppress specific bands (e.g. (255, 120, 65) -> (0, 120, 0) for g)
# intensity = 0.9
# blue    = [(int(d[0]*intensity),                d[1],                d[2]) for d in data]
# magenta = [(               d[0], int(d[1]*intensity),                d[2]) for d in data]
# yellow  = [(               d[0],                d[1], int(d[2]*intensity)) for d in data]
#
# image.putdata(blue)
# image.show()
# # img.save('magenta.png')
# image2.putdata(magenta)
# image2.show()
# # img.save('g.png')
# image3.putdata(yellow)
# image3.show()
# # img.save('yellow.png')
