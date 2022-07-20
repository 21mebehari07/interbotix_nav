import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df1 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/def_frontiers_stats_1657034262.csv")
    df2 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/def_frontiers_stats_1657034526.csv")
    df3 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/def_frontiers_stats_1657034688.csv")
    df4 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/def_frontiers_stats_1657054083.csv")
    df5 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/def_frontiers_stats_1657035490.csv")
    df6 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/def_frontiers_stats_1657036300.csv")
    df = df1.append(df2, ignore_index=True)
    df = df.append(df3, ignore_index=True)
    df = df.append(df4, ignore_index=True)
    df = df.append(df5, ignore_index=True)
    df = df.append(df6, ignore_index=True)
    print(df)
    df["utility"] = df["info_gain"] / df["effort"]
    df["type"] = "baseline"




    df1 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/wsr_frontiers_stats_1657034262.csv")
    df2 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/wsr_frontiers_stats_1657034526.csv")
    df3 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/wsr_frontiers_stats_1657034688.csv")
    df4 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/wsr_frontiers_stats_1657054083.csv")
    df5 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/wsr_frontiers_stats_1657035490.csv")
    df6 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/wsr_frontiers_stats_1657036300.csv")

    df_wsr = df1.append(df2, ignore_index=True)
    df_wsr = df_wsr.append(df3, ignore_index=True)
    df_wsr = df_wsr.append(df4, ignore_index=True)
    df_wsr = df_wsr.append(df5, ignore_index=True)
    df_wsr = df_wsr.append(df6, ignore_index=True)
    print(df_wsr)
    df_wsr["utility"] = df_wsr["info_gain"] / df_wsr["effort"]
    df_wsr["type"] = "wsr"

    df_final = df.append(df_wsr, ignore_index=True)
    sns.relplot(data=df_final, x="j_dist", y="utility", hue="type", col="type", s=20, alpha=0.5)
    plt.show()


if __name__ == "__main__":
    main()