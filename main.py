from PIL import Image, ImageOps


def main():
    with Image.open('images/guido-van-rossum.jpg') as im:
        im_rotate = im.rotate(90)
        im_rotate = ImageOps.flip(im_rotate)
        width, height = im_rotate.size
        im_resized = im_rotate.resize((600, int(height * 600 / width)))
        im_resized.save('images/guido-van-rossum_90.jpg', quality=95)


if __name__ == "__main__":
    main()
