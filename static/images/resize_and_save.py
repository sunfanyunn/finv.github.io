from PIL import Image, ImageOps
from glob import glob

for im_pth in glob('*.png'):
    if 'method' in im_pth:
        continue

    print(im_pth)
    desired_size = 512

    im = Image.open(im_pth)
    old_size = im.size  # old_size[0] is in (width, height) format

    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    # use thumbnail() or resize() method to resize the input image

    # thumbnail is a in-place operation

    # im.thumbnail(new_size, Image.ANTIALIAS)

    im = im.resize(new_size, Image.ANTIALIAS)
    # create a new image and paste the resized on it

    new_im = Image.new("RGB", (desired_size, desired_size), color=(255,255,255))
    new_im.paste(im, ((desired_size-new_size[0])//2,
                        (desired_size-new_size[1])//2))

    # new_im.show()

    with open('{}_new.png'.format(im_pth.split('.')[0]), 'wb') as fp:
        new_im.save(fp)
