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

# This method will show image in any image viewer 
img.save('generated.png')
# img.show()

print('COMPLETE')