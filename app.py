import pandas as pd
import simple_chalk as chalk

dataset = pd.read_csv("./data.csv")


class Reader:
    def __init__(self):
        data = pd.DataFrame(dataset)
        print(chalk.green(f"\n {data} \n"))


if __name__ == "__main__":
    reader = Reader()
