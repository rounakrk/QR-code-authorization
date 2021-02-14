import qrcode


def qrcode_generation(data, img_name):
    # Encoding data using make() function
    img = qrcode.make(data)

    path = 'qr images/{}'.format(img_name + ".png")

    img.save(path)

    print("Image saved in .... \nPath : ", path)


# if __name__ == "__main__":
#     qrcode_generation("Rounak Agarwal", "rk")
