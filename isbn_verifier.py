def verify(isbn):
    if isbn:
        isbn_num = [int(c) for c in isbn if c.isnumeric()]
        if len(isbn_num) != 10:
            if isbn[-1] == 'X':
                isbn_num.append(10)
            else:
                return False
        if sum((i*j) for i,j in zip(isbn_num, range(10, 0, -1))) % 11:
            return False
        else:
            return True
    else:
        return False

print(verify('3-598-21508-8'))
