#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/exploration_test_1656540985.csv")
    sns.lineplot(data=df, x="time_elapsed", y="coverage_percent")
    plt.show()

    sns.lineplot(data=df, x="time_elapsed", y="inter_agent_distance")
    plt.show()

if __name__ == "__main__":
    main()