import os
from PIL import Image


CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


def watermark(im, mark, position):
    """Adds a watermark to an image."""
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    # create a transparent layer the size of the image and draw the
    # watermark in that layer.
    layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
    layer.paste(mark, position)
    # composite the watermark with the layer
    return Image.composite(layer, im, layer)


def watermark_with_emotion(im, emotion):
    mark = Image.open(os.path.join(CURRENT_PATH, 'emotions/%s.png' % emotion))
    im_with_watermark = watermark(im, mark, (im.width - (mark.width + 12), 12))
    return im_with_watermark


def test():
    im = Image.open('input.jpg')
    t = watermark_with_emotion(im, 'neutral')
    output = 'output.jpg'
    t.save(output, format='JPEG')


if __name__ == '__main__':
    test()
