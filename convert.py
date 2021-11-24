import os
from PIL import Image


def rec_convert(x=''):
    for _ in os.scandir(os.path.join('in', x)):
        if _.is_dir():
            os.makedirs(os.path.join('out', x, _.name))
            rec_convert(os.path.join(x, _.name))
        elif _.is_file():
            n, e = _.name.rsplit(os.extsep, 1)
            if e == 'webp':
                with Image.open(os.path.join('in', x, _.name)) as f:
                    f.save(os.path.join('out', x, (n + os.extsep + 'png')), 'PNG')


if __name__ == '__main__':
    rec_convert()
