import sys
import pandas as pd
import numpy as np

from src.tasks.TasksSelector import TasksSelector


def read_data():
    pd.set_option("display.max.columns", 100)
    data_path = "https://raw.githubusercontent.com/Yorko/mlcourse.ai/main/data/"
    data = pd.read_csv(data_path + "adult.data.csv")
    print(data.head())
    return data
    pass


def main() -> int:
    task_number = 1
    dataset = read_data()
    tasks_selector = TasksSelector(dataset, task_number)
    return 0


if __name__ == '__main__':
    sys.exit(main())
