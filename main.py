from os import name
from PIL import Image, ImageFont, ImageDraw
import textwrap
from points import points

# CONSTANTS
colors = [
    (151, 193, 94),
    (249, 160, 63),
    (241, 92, 81),
    (111, 105, 176),
    (63, 184, 204)
]
distanceFactor = 350

def square_crop_image(image):
    width, height = image.size
    if width == height:
        return image
    offset  = int(abs(height-width)/2)
    if width>height:
        image = image.crop([offset,0,width-offset,height])
    else:
        image = image.crop([0,offset,width,height-offset])
    return image

# open method used to open different extension image file
img = Image.open("point-bg.png") 
draw = ImageDraw.Draw(img)

yOffset = 500;
for i in range(5):
    # if list index is less than 5
    # fillup to paint empty person
    if len(points)>=i:
        # break
        points.append({
                'name': None,
                'point': None,
                'answer': None,
                'explanation': None,
                'subject': None,
                'refer': None,
                'image': None,
        })
    
    # write name
    fontsize = 80
    namefont = ImageFont.truetype("kalpurush.ttf", fontsize)
    # portion of image width you want text width to be
    blank = Image.new('RGB',(700, 150))
    txt = points[i]['name']  or 'You can do it!'
    while (namefont.getsize(txt)[0] > blank.size[0]) or (namefont.getsize(txt)[1] > blank.size[1]):
        # iterate until the text size is just larger than the criteria
        fontsize -= 1
        namefont = ImageFont.truetype("kalpurush.ttf", fontsize)
    draw.text((700, yOffset), txt, colors[i], font=namefont)

    # write total point
    totalpoint = points[i]['point'] or ''
    txt = str(totalpoint)
    pointfont = ImageFont.truetype("kalpurush.ttf", 80)
    scoresize = pointfont.getsize(txt)[0]
    scorestart = 1457 + ((183-scoresize)/2)
    draw.text((scorestart, yOffset), txt, colors[i], font=pointfont)

    # write details
    if points[i]['answer'] != None:
        answer = points[i]['answer']
        explanation = points[i]['explanation']
        subject = points[i]['subject']
        refer = points[i]['refer']
        txt = f"Total Point: {totalpoint}.Details:- Answer: {answer},"+\
            f" Explanation: {explanation}, Subject: {subject},"+\
            f" Refer: {refer}."
        detailsfont = ImageFont.truetype("kalpurush.ttf", 40)
        margin, offset = 700, yOffset+100
        for line in textwrap.wrap(txt, width=50):
            draw.text((margin, offset), line, font=detailsfont, fill="#4a4a4a")
            offset += detailsfont.getsize(line)[1]

    # profile pic
    if points[i]['image'] != None:
        # before pasting image make image pasting area
        draw.rectangle(((1487, yOffset+110), (1587, yOffset+220)), fill="#fbfbfd")

        pp = Image.open("profile-pic.jpeg")
        pp = square_crop_image(pp)
        pp = pp.resize((120, 120))
        img.paste(pp, (1487, yOffset+110))

    yOffset += distanceFactor

# img.save('generated.png')
# This method will show image in any image viewer 
img.show()

print('COMPLETE')