def parse_and_write(digit):
    with open('digit', 'w') as f:
        for row in digit:
            for n in row:
                if n:
                    f.write('#')
                else:
                    f.write('.')
            f.write('\n')
     