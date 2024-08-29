ph=[
    ('ᄭ','ᄁ'),
    ('ᄯ','ᄄ'),
    ('ᄲ','ᄈ'),
    ('ᄴ','ᄊ'),
    ('ᄶ','ᄍ'),
    ('ᄙ','ᄅ'),
    ('ᄘ','ᄂ'),
    ('ᅝ','ᄂ'),
    ('ᄚ','ᄅ'),
    ('ᄝ','ᄆ'),
    ('ᄛ','ᄅ'),
    ('ퟋ','ᆯ'),
    ('’',''),
]

def convert(text: str) -> str:
    for c in ph:
        text=text.replace(c[0], c[1])
    for j in range(19):
        for m in range(21):
            for p in range(1,28):
                text=text.replace(chr(0x1100+j)+chr(0x1161+m)+chr(0x11A7+p), chr(0xAC00+(j*21+m)*28+p))
            text=text.replace(chr(0x1100+j)+chr(0x1161+m), chr(0xAC00+(j*21+m)*28))
    return text

if __name__ == '__main__':
    import inputter
    while True:
        print(convert(inputter.convert(input('입력: '))))