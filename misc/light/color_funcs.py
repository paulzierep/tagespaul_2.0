# Define the wheel function to interpolate between different hues.
def wheel(pos):
    if pos < 85:
        return Adafruit_WS2801.RGB_to_color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Adafruit_WS2801.RGB_to_color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Adafruit_WS2801.RGB_to_color(0, pos * 3, 255 - pos * 3)


def rainbow_colors(pixels, wait=0.05):
    for j in range(256):  # one cycle of all 256 colors in the wheel
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((256 // pixels.count() + j)) % 256))
        pixels.show()
        if wait > 0:
            time.sleep(wait)


def rainbow_colors_range(pixels, wait=0.05, start=0, end=64):
    for j in range(start, end):  # one cycle of all 256 colors in the wheel
        print(j)
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((256 // pixels.count() + j)) % 256))
        pixels.show()
        if wait > 0:
            time.sleep(wait)

    for j in reversed(range(start, end)):  # one cycle of all 256 colors in the wheel
        print(j)
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((256 // pixels.count() + j)) % 256))
        pixels.show()
        if wait > 0:
            time.sleep(wait)


def rainbow_colors_offset(pixels, wait=0.05, offset=3):  # 17 is full wheel, 3 is slow
    for j in range(256):  # one cycle of all 256 colors in the wheel
        for i in range(pixels.count()):
            pixels.set_pixel(
                i, wheel(((256 // pixels.count() + j + (i * offset))) % 256)
            )
        pixels.show()
        if wait > 0:
            time.sleep(wait)


def rainbow_colors_random(pixels, wait=0.05):
    for j in range(100):
        for i in range(pixels.count()):
            pixels.set_pixel(
                i, wheel(((256 // pixels.count() + (random.randint(0, 10)))) % 256)
            )
        pixels.show()
        if wait > 0:
            time.sleep(wait)


def set_color_blink(pixels, color=1):
    print(color)
    for k in range(20):
        for i in range(pixels.count()):
            pixels.set_pixel(i, wheel(((256 // pixels.count() + color)) % 256))
        pixels.show()
        time.sleep(0.1)
        for i in range(pixels.count()):
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 0, 0))
        pixels.show()
        time.sleep(0.1)
        print(k)


def set_color(pixels, color=1):
    print(color)
    for i in range(pixels.count()):
        pixels.set_pixel(i, wheel(((256 // pixels.count() + color)) % 256))
    pixels.show()


def brightness_decrease(pixels, wait=0.002, step=1):
    for j in range(int(256 // step)):
        for i in range(pixels.count()):
            r, g, b = pixels.get_pixel_rgb(i)
            r = int(max(0, r - step))
            g = int(max(0, g - step))
            b = int(max(0, b - step))
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(r, g, b))
        pixels.show()
        if wait > 0:
            time.sleep(wait)


def add_range(x, add=30, wheel=256):
    x = x + add

    x = x % wheel

    return x


def flimmer(color):
    color2 = [0, 0, 0]

    for i in range(3):
        color2[i] = add_range(color[i])

    return color2


def random_dots(pixels, j, color=[0, 0, 256]):
    if j % 2 == 0:  # do this onle every 10th iteration
        color_f = flimmer(color)

        print(color)
        print(color_f)

        for i in range(pixels.count()):
            if bool(random.getrandbits(1)):
                # color_f = flimmer(color)

                # print(color_f)

                pixels.set_pixel(
                    i, Adafruit_WS2801.RGB_to_color(color[0], color[1], color[2])
                )

            else:
                pixels.set_pixel(
                    i, Adafruit_WS2801.RGB_to_color(color_f[0], color_f[1], color_f[2])
                )

        pixels.show()
