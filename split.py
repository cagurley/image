import os.path
from PIL import Image


for i in range(0, 10):
    with Image.open(os.path.join('in', f'{i}.png')) as f:
        for y in range(0, 7):
            for x in range(0, 4):
                b = (x*1924 + 2, y*1084 + 2, (x+1)*1924 - 2, (y+1)*1084 - 2)
                with f.crop(b) as p:
                    p.save(os.path.join('out', f'sheet{i}_image{(y*4 + x):02}.png'))
