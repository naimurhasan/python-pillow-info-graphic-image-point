from os import name
from PIL import Image, ImageFont, ImageDraw
import textwrap
  
# open method used to open different extension image file
img = Image.open("point-bg.png") 

draw = ImageDraw.Draw(img)


# write name
fontsize = 80
namefont = ImageFont.truetype("kalpurush.ttf", fontsize)
# portion of image width you want text width to be
blank = Image.new('RGB',(700, 150))
txt = "Ariful Islam Arifin"
while (namefont.getsize(txt)[0] > blank.size[0]) or (namefont.getsize(txt)[1] > blank.size[1]):
    # iterate until the text size is just larger than the criteria
    fontsize -= 1
    namefont = ImageFont.truetype("kalpurush.ttf", fontsize)
draw.text((700, 500), txt,(151, 193, 94), font=namefont)

# write total point
totalpoint = 995
txt = str(totalpoint)
scoresize = namefont.getsize(txt)[0]
scorestart = 1457 + ((183-scoresize)/2)
draw.text((scorestart, 500), txt,(151, 193, 94), font=namefont)

# write details
answer = 1625
explanation = 15
subject = 785
refer = 0
txt = f"Total Point: {totalpoint}.Details:- Answer: {answer},"+\
    f" Explanation: {explanation}, Subject: {subject},"+\
    f" Refer: {refer}."
detailsfont = ImageFont.truetype("kalpurush.ttf", 40)
margin, offset = 700, 600
for line in textwrap.wrap(txt, width=50):
    draw.text((margin, offset), line, font=detailsfont, fill="#4a4a4a")
    offset += detailsfont.getsize(line)[1]

# draw point
# draw.rectangle(((700, 618), (1403, 760)), fill="black")


# profile pic

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

# before pasting image make image pasting area
draw.rectangle(((1487, 610), (1587, 720)), fill="#fbfbfd")

pp = Image.open("profile-pic.jpeg")
pp = square_crop_image(pp)
pp = pp.resize((120, 120))
img.paste(pp, (1487, 610))

# second point achiver distance calculate
txt = "Ariful Islam Arifin"
factor = 350
for i in range(1, 5):
    draw.text((700, 500+(factor*i)), txt,(151, 193, 94), font=namefont)
    draw.text((700, 500+(factor*i)), txt,(151, 193, 94), font=namefont)

# This method will show image in any image viewer 
# img.save('generated.png')
img.show()

print('COMPLETE')