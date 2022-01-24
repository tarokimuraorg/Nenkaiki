def toHankaku(zenkaku : str) -> str:

    zenkaku_data = [0xff01 + i for i in range(94)]
    hankaku_data = [0x21 + i for i in range(94)]
    data = {zenkaku_data[i]:hankaku_data[i] for i in range(94)}

    return zenkaku.translate(data)

def toZenkaku(hankaku : str) -> str:

    zenkaku_data = [0xff01 + i for i in range(94)]
    hankaku_data = [0x21 + i for i in range(94)]
    data = {hankaku_data[i]:zenkaku_data[i] for i in range(94)}

    return hankaku.translate(data)
