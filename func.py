def repeat(s, exclaim):
    result = s + s + s
    if exclaim:
        result = result + '!!!'
    return result

def main():
    print repeat('YoYo', True)
    print repeat('Tik', False)

if __name__ == '__main__':
    main()