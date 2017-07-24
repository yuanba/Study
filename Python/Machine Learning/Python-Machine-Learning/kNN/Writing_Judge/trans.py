from PIL import Image

def get_char(r, g ,b , alpha = 256):
    if alpha == 0:
        return 0
    length = 2
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    p = [0 , 1]
    return p[int(gray / unit)]


img = Image.open("./0dbfc7e94f35126f072acf211a0e38c9.jpg")

img = img.resize((32,32) , Image.NEAREST)

ans = []

HEIGHT , WEIGHT = img.size

for i in range(HEIGHT):
    for j in range(WEIGHT):
        ans.append(get_char(*img.getpixel((j,i))))

for i in range(len(ans)):
    ans[i] = int(ans[i])

import sys

for i in range(32):
    for j in range(32):
        sys.stdout.write(str(ans[i * 32 + j]))
    print()

