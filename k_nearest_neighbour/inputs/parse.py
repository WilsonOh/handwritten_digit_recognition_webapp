with open('train100.in') as f:
    n = int(f.readline())
    res = {
        i: {
           f.readline().strip(): [list(f.readline().strip()) for _ in range(28)]
        } for i in range(n)
    }

    with open('training_samples.py', 'w') as w:
        w.write("training_samples = {\n")
        for num, sample in res.items():
            w.write(f"\t{num}: " + "{\n")
            for k, v in sample.items():
                w.write(f"\t\t{k}: \n")
                w.write("\t\t[\n")
                for row in v:
                    w.write("\t\t" + str(row) + ',\n')
                w.write('\n')
                w.write("]\n")
            w.write("\t},\n")
        w.write("}")
