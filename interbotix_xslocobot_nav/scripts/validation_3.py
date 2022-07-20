import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    df1 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/wsr_frontiers_stats_1657034262.csv")
    df1["sim"] = "sim1"
    df1_top_wsr=df1.query("index == 1.0")
    df1_top_wsr.insert(0, 'timestep', range(0, 0 + len(df1_top_wsr)))

    df2 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/wsr_frontiers_stats_1657034526.csv")
    df2["sim"] = "sim2"
    df2_top_wsr=df2.query("index == 1.0")
    df2_top_wsr.insert(0, 'timestep', range(0, 0 + len(df2_top_wsr)))

    df3 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/wsr_frontiers_stats_1657034688.csv")
    df3["sim"] = "sim3"
    df3_top_wsr=df3.query("index == 1.0")
    df3_top_wsr.insert(0, 'timestep', range(0, 0 + len(df3_top_wsr)))
    
    df4 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/wsr_frontiers_stats_1657054083.csv")
    df4["sim"] = "sim4"
    df4_top_wsr=df4.query("index == 1.0")
    df4_top_wsr.insert(0, 'timestep', range(0, 0 + len(df4_top_wsr)))

    df5 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/wsr_frontiers_stats_1657035490.csv")
    df5["sim"] = "sim5"
    df5_top_wsr=df5.query("index == 1.0")
    df5_top_wsr.insert(0, 'timestep', range(0, 0 + len(df5_top_wsr)))

    df6 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_all/wsr_frontiers_stats_1657036300.csv")
    df6["sim"] = "sim6"
    df6_top_wsr=df6.query("index == 1.0")
    df6_top_wsr.insert(0, 'timestep', range(0, 0 + len(df6_top_wsr)))

    df_top_wsr = df1_top_wsr.append(df2_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df3_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df4_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df5_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df6_top_wsr, ignore_index=True)

    # df = df.append(df6, ignore_index=True)
    df_top_wsr["utility"] = df_top_wsr["info_gain"] / df_top_wsr["effort"]
    df_top_wsr["type"] = "wsr"
    
    sns.lineplot(data=df_top_wsr, x="timestep", y="j_dist", hue="sim")
    plt.show()

    sns.lineplot(data=df_top_wsr, x="timestep", y="utility", hue="sim")
    plt.show()


    '''
    Utility using only just information gain formulation
    '''
    df1 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_info_gain_only/wsr_frontiers_stats_1657037149.csv")
    df1["sim"] = "sim1"
    df1_top_wsr=df1.query("index == 1.0")
    df1_top_wsr.insert(0, 'timestep', range(0, 0 + len(df1_top_wsr)))

    df2 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_info_gain_only/wsr_frontiers_stats_1657037451.csv")
    df2["sim"] = "sim2"
    df2_top_wsr=df2.query("index == 1.0")
    df2_top_wsr.insert(0, 'timestep', range(0, 0 + len(df2_top_wsr)))

    df3 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_info_gain_only/wsr_frontiers_stats_1657038046.csv")
    df3["sim"] = "sim3"
    df3_top_wsr=df3.query("index == 1.0")
    df3_top_wsr.insert(0, 'timestep', range(0, 0 + len(df3_top_wsr)))
    
    df4 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_info_gain_only/wsr_frontiers_stats_1657038572.csv")
    df4["sim"] = "sim4"
    df4_top_wsr=df4.query("index == 1.0")
    df4_top_wsr.insert(0, 'timestep', range(0, 0 + len(df4_top_wsr)))

    df5 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_info_gain_only/wsr_frontiers_stats_1657038883.csv")
    df5["sim"] = "sim5"
    df5_top_wsr=df5.query("index == 1.0")
    df5_top_wsr.insert(0, 'timestep', range(0, 0 + len(df5_top_wsr)))

    df6 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_info_gain_only/wsr_frontiers_stats_1657039087.csv")
    df6["sim"] = "sim6"
    df6_top_wsr=df6.query("index == 1.0")
    df6_top_wsr.insert(0, 'timestep', range(0, 0 + len(df6_top_wsr)))

    df_top_wsr = df1_top_wsr.append(df2_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df3_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df4_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df5_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df6_top_wsr, ignore_index=True)

    # df = df.append(df6, ignore_index=True)
    df_top_wsr["utility"] = df_top_wsr["info_gain"] / df_top_wsr["effort"]
    df_top_wsr["type"] = "wsr"
    
    sns.lineplot(data=df_top_wsr, x="timestep", y="j_dist", hue="sim")
    plt.show()

    sns.lineplot(data=df_top_wsr, x="timestep", y="utility", hue="sim")
    plt.show()


    '''
    Utility using only just information gain formulation
    '''
    df1 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_effort_only/wsr_frontiers_stats_1657039604.csv")
    df1["sim"] = "sim1"
    df1_top_wsr=df1.query("index == 1.0")
    df1_top_wsr.insert(0, 'timestep', range(0, 0 + len(df1_top_wsr)))

    df2 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_effort_only/wsr_frontiers_stats_1657039856.csv")
    df2["sim"] = "sim2"
    df2_top_wsr=df2.query("index == 1.0")
    df2_top_wsr.insert(0, 'timestep', range(0, 0 + len(df2_top_wsr)))

    df3 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_effort_only/wsr_frontiers_stats_1657040191.csv")
    df3["sim"] = "sim3"
    df3_top_wsr=df3.query("index == 1.0")
    df3_top_wsr.insert(0, 'timestep', range(0, 0 + len(df3_top_wsr)))
    
    df4 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_effort_only/wsr_frontiers_stats_1657040785.csv")
    df4["sim"] = "sim4"
    df4_top_wsr=df4.query("index == 1.0")
    df4_top_wsr.insert(0, 'timestep', range(0, 0 + len(df4_top_wsr)))

    df5 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_effort_only/wsr_frontiers_stats_1657041223.csv")
    df5["sim"] = "sim5"
    df5_top_wsr=df5.query("index == 1.0")
    df5_top_wsr.insert(0, 'timestep', range(0, 0 + len(df5_top_wsr)))

    df6 = pd.read_csv ("/home/jadhav/catkin_ws/src/wsr_exploration/data/mexplore_data/wsr_effort_only/wsr_frontiers_stats_1657041435.csv")
    df6["sim"] = "sim6"
    df6_top_wsr=df6.query("index == 1.0")
    df6_top_wsr.insert(0, 'timestep', range(0, 0 + len(df6_top_wsr)))

    df_top_wsr = df1_top_wsr.append(df2_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df3_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df4_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df5_top_wsr, ignore_index=True)
    df_top_wsr = df_top_wsr.append(df6_top_wsr, ignore_index=True)

    # df = df.append(df6, ignore_index=True)
    df_top_wsr["utility"] = df_top_wsr["info_gain"] / df_top_wsr["effort"]
    df_top_wsr["type"] = "wsr"
    
    sns.lineplot(data=df_top_wsr, x="timestep", y="j_dist", hue="sim")
    plt.xlim((0,70))
    plt.show()

    sns.lineplot(data=df_top_wsr, x="timestep", y="utility", hue="sim")
    plt.xlim((0,70))
    plt.show()




if __name__ == "__main__":
    main()