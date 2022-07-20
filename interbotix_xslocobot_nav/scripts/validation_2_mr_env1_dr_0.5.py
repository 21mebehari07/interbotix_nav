import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df1 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/base_line_mr_env1/def_frontiers_stats_1657118301.csv")
    df1["sim"] = "sim1"
    df1_top_bs=df1.query("index == 1.0")
    df1_top_bs.insert(0, 'timestep', range(0, 0 + len(df1_top_bs)))

    df2 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/base_line_mr_env1/def_frontiers_stats_1657118507.csv")
    df2["sim"] = "sim2"
    df2_top_bs=df2.query("index == 1.0")
    df2_top_bs.insert(0, 'timestep', range(0, 0 + len(df2_top_bs)))

    df3 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/base_line_mr_env1/def_frontiers_stats_1657118740.csv")
    df3["sim"] = "sim3"
    df3_top_bs=df3.query("index == 1.0")
    df3_top_bs.insert(0, 'timestep', range(0, 0 + len(df3_top_bs)))    
    
    df4 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/base_line_mr_env1/def_frontiers_stats_1657119384.csv")
    df4["sim"] = "sim4"
    df4_top_bs=df4.query("index == 1.0")
    df4_top_bs.insert(0, 'timestep', range(0, 0 + len(df4_top_bs)))

    df5 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/base_line_mr_env1/def_frontiers_stats_1657119705.csv")
    df5["sim"] = "sim5"
    df5_top_bs=df5.query("index == 1.0")
    df5_top_bs.insert(0, 'timestep', range(0, 0 + len(df5_top_bs)))

    df6 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/base_line_mr_env1/def_frontiers_stats_1657119914.csv")
    df6["sim"] = "sim6"
    df6_top_bs=df6.query("index == 1.0")
    df6_top_bs.insert(0, 'timestep', range(0, 0 + len(df6_top_bs)))

    df_top_bs = df1_top_bs.append(df2_top_bs, ignore_index=True)
    df_top_bs = df_top_bs.append(df3_top_bs, ignore_index=True)
    df_top_bs = df_top_bs.append(df4_top_bs, ignore_index=True)
    df_top_bs = df_top_bs.append(df5_top_bs, ignore_index=True)
    df_top_bs = df_top_bs.append(df6_top_bs, ignore_index=True)
    df_top_bs["utility"] = df_top_bs["info_gain"] / df_top_bs["effort"]
    df_top_bs["type"] = "baseline"
    df_top_bs["utility"] = df_top_bs["info_gain"] / df_top_bs["effort"]
    df_top_bs["type"] = "wsr"
    df_top_bs["j_dist_avg"] = df_top_bs["j_dist"] / df_top_bs["j_count"]
    
    sns.lineplot(data=df_top_bs, x="timestep", y="j_dist_avg", hue="sim")
    plt.show()

    sns.lineplot(data=df_top_bs, x="timestep", y="utility", hue="sim")
    plt.show()



    df1 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/wsr_frontiers_stats_1657120183.csv")
    df2 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/wsr_frontiers_stats_1657120450.csv")
    df3 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/wsr_frontiers_stats_1657120655.csv")
    df4 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/wsr_frontiers_stats_1657120837.csv")
    df5 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/wsr_frontiers_stats_1657121018.csv")
    df6 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all_mr_env1_dr_0.5/wsr_frontiers_stats_1657121019.csv")
    
    df1["sim"] = "sim1"
    df1_top_wsr=df1.query("index == 1.0")
    df1_top_wsr.insert(0, 'timestep', range(0, 0 + len(df1_top_wsr)))

    # df2["sim"] = "sim2"
    df2_top_wsr=df2.query("index == 1.0")
    df2_top_wsr.insert(0, 'timestep', range(0, 0 + len(df2_top_wsr)))

    df3["sim"] = "sim3"
    df3_top_wsr=df3.query("index == 1.0")
    df3_top_wsr.insert(0, 'timestep', range(0, 0 + len(df3_top_wsr)))
    
    df4["sim"] = "sim4"
    df4_top_wsr=df4.query("index == 1.0")
    df4_top_wsr.insert(0, 'timestep', range(0, 0 + len(df4_top_wsr)))

    df5["sim"] = "sim5"
    df5_top_wsr=df5.query("index == 1.0")
    df5_top_wsr.insert(0, 'timestep', range(0, 0 + len(df5_top_wsr)))

    df6["sim"] = "sim6"
    df6_top_wsr=df6.query("index == 1.0")
    df6_top_wsr.insert(0, 'timestep', range(0, 0 + len(df6_top_wsr)))

    df_top_wsr = df1_top_wsr.append(df2_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df3_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df4_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df5_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df6_top_wsr, ignore_index=True)

    df_top_wsr["utility"] = df_top_wsr["info_gain"] / df_top_wsr["effort"]
    df_top_wsr["type"] = "wsr"
    df_top_wsr["j_dist_avg"] = df_top_wsr["j_dist"] / df_top_wsr["j_count"]
    
    sns.lineplot(data=df_top_wsr, x="timestep", y="j_dist_avg", hue="sim")
    plt.show()

    sns.lineplot(data=df_top_wsr, x="timestep", y="utility", hue="sim")
    plt.show()

if __name__ == "__main__":
    main()