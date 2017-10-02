import pandas as pd
import os

folder = "./in/"
onlyfiles = [str(f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

if __name__ == '__main__':
    for _file in onlyfiles:
        print(_file)
        with open(os.path.join(folder, _file), 'r') as f:
            content = f.read()
            print(content)
        #data = pd.read_csv(os.path.join(folder, _file), sep="\t")
        #print(data)
