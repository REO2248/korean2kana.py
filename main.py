if __name__ == '__main__':
    import inputter
    import output_korean_char
    import output_kana
    while True:
        input_text = inputter.convert(input('입력: '))
        print('조선글자:', output_korean_char.convert(input_text))
        print('가다가나:', output_kana.convert(input_text))