from PIL import Image, ImageDraw, ImageFont


def image_font(img_text,img_path):
    image = Image.open(img_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("msyh.ttc", size=50)
    draw.text((1850, 0),text=img_text, fill="#777777", font=font)
    print(image.format, image.size, image.mode)
    image.show()
    image.save(img_path)


if __name__ == '__main__':
    image_font(img_text="fff",img_path=r"./1.jpg")
