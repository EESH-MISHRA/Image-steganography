end_hex = b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"
with open(r"IMAGE PATH HERE","rb") as file:
    content =file.read()
    offset = content.index(end_hex)
    file.seek(offset+len(end_hex))
    msg = file.read()
    print(msg)

    