import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df1 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/def_frontiers_stats_1657120183.csv")
    df2 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/def_frontiers_stats_1657120450.csv")
    df3 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/def_frontiers_stats_1657120655.csv")
    df4 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/def_frontiers_stats_1657120837.csv")
    df5 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/def_frontiers_stats_1657121018.csv")
    df6 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/def_frontiers_stats_1657121019.csv")
    df = df1.append(df2, ignore_index=True)
    df = df.append(df3, ignore_index=True)
    df = df.append(df4, ignore_index=True)
    df = df.append(df5, ignore_index=True)
    df = df.append(df6, ignore_index=True)
    print(df)
    df["utility"] = df["info_gain"] / df["effort"]
    df["type"] = "baseline"
    df["j_dist_avg"] = df["j_dist"] / df["j_count"]



    df1 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/wsr_frontiers_stats_1657120183.csv")
    df2 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/wsr_frontiers_stats_1657120450.csv")
    df3 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/wsr_frontiers_stats_1657120655.csv")
    df4 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/wsr_frontiers_stats_1657120837.csv")
    df5 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/wsr_frontiers_stats_1657121018.csv")
    df6 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/wsr_frontiers_stats_1657121019.csv")

    df_wsr_a = df1.append(df2, ignore_index=True)
    df_wsr_a = df_wsr_a.append(df3, ignore_index=True)
    df_wsr_a = df_wsr_a.append(df4, ignore_index=True)
    df_wsr_a = df_wsr_a.append(df5, ignore_index=True)
    df_wsr_a = df_wsr_a.append(df6, ignore_index=True)
    print(df_wsr_a)
    df_wsr_a["utility"] = df_wsr_a["info_gain"] / df_wsr_a["effort"]
    df_wsr_a["type"] = "wsr_a"
    df_wsr_a["j_dist_avg"] = df_wsr_a["j_dist"] / df_wsr_a["j_count"]


    df1 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_1/wsr_frontiers_stats_1657206693.csv")
    df2 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_1/wsr_frontiers_stats_1657207084.csv")
    df3 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_1/wsr_frontiers_stats_1657207442.csv")
    df4 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_1/wsr_frontiers_stats_1657207820.csv")
    df5 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_1/wsr_frontiers_stats_1657208632.csv")
    df6 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_1/wsr_frontiers_stats_1657208913.csv")

    df_wsr_b = df1.append(df2, ignore_index=True)
    df_wsr_b = df_wsr_b.append(df3, ignore_index=True)
    df_wsr_b = df_wsr_b.append(df4, ignore_index=True)
    df_wsr_b = df_wsr_b.append(df5, ignore_index=True)
    df_wsr_b = df_wsr_b.append(df6, ignore_index=True)
    print(df_wsr_b)
    df_wsr_b["utility"] = df_wsr_b["info_gain"] / df_wsr_b["effort"]
    df_wsr_b["type"] = "wsr_b"
    df_wsr_b["j_dist_avg"] = df_wsr_b["j_dist"] / df_wsr_b["j_count"]


    df_final = df.append(df_wsr_a, ignore_index=True)
    df_final = df_final.append(df_wsr_b, ignore_index=True)
    sns.relplot(data=df_final, x="j_dist_avg", y="utility", hue="type", col="type", s=20, alpha=0.5)
    plt.show()


if __name__ == "__main__":
    main()