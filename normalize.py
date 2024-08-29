#分解するやつ

def decompose(text: str) -> str:
    r=''
    for c in text:
        if ord(c) in [0xF013, 0xF016, 0xF113, 0xF116, 0xF120]:
            c='김'
        if ord(c) in [0xF014, 0xF018, 0xF114, 0xF118]:
            c='일'
        if ord(c) in [0xF015, 0xF115]:
            c='성'
        if ord(c) in [0xF017, 0xF117, 0xF121]:
            c='정'
        if ord(c) in [0xF122]:
            c='은'
        if ord(c)in range(0xAC00, 0xD7A4):
            r+=chr((ord(c)-0xAC00)//(21*28)+0x1100)
            r+=chr(((ord(c)-0xAC00)//28)%21+0x1161)
            r+=chr((ord(c)-0xAC00)%28+0x11A7)
            if r[-1]=='\u11A7':
                r=r[:-1]
        else:
            r+=c
    return r

if __name__ == '__main__':
    print('\n'.join(decompose(input('입력: '))))