import qrcode


def qrcode_generation(data, img_name):
    # Encoding data using make() function
    # qr = qrcode.QRCode(box_size=7)
    # qr.add_data('I am Lena')
    # qr.make()
    # img_qr = qr.make_image()
    img = qrcode.make(data)
    # print(type(img_qr))
    # print(img_qr.size)
    # img_name = "hello"
    # QR-code-authorization + HTML\static\images\EMP1011.png
    path = 'static/images/{}'.format(img_name + ".png")

    img.save(path)

    print("Image saved in .... \nPath : ", path)


# if __name__ == "__main__":
#     qrcode_generation("Rounak Agarwal", "rk")
