#!/usr/bin/env python3

import rospy
from gazebo_msgs.msg import ModelStates
from nav_msgs.msg import OccupancyGrid
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
import time
import csv
from std_msgs.msg import Bool

class ExplorationEval:
    def __init__(self):
        rospy.init_node('wsr_exploration_eval', anonymous=True)
        self.total_iterations = 0
        self.check_itr = 0
        self.distance = []
        self.iteration = []
        self.x_lim = 50
        self.itr = 1

        plt.ion()
        fig = plt.figure()
        # for stopping simulation with the esc key.
        fig.canvas.mpl_connect('key_release_event',
                lambda event: [exit(0) if event.key == 'escape' else None])
        
        self.ax = fig.add_subplot(111)
        rospy.Subscriber("/gazebo/model_states", ModelStates, self.modelState_cb)
        rospy.Subscriber("/world_map", OccupancyGrid, self.world_map_cb)
        rospy.Subscriber("/map_merge/map", OccupancyGrid, self.merged_map_cb)
        self.got_world_map = False
        self.got_merged_map = False
        self.start = time.time()
        self.merged_map_count = 0
        self.world_map_count = 0
        self.exploration_stats = []
        self.current_distance = 0
        self.details = ['coverage_percent', 'time_elapsed', 'inter_agent_distance']
        self.exploration_threshold = rospy.get_param('explore_threshold', 95)
        self.pub = rospy.Publisher('true_exploration_status', Bool, queue_size=10)
        self.status = Bool()
        self.status.data = True

    def world_map_cb(self, msg):
        if(not self.got_world_map):
            print(msg.info.height, " x ", msg.info.width)
            # self.world_ogrid = np.array(msg.data).reshape((msg.info.height, msg.info.width))
            self.world_ogrid = np.array(msg.data)
            self.merged_ogrid = np.empty(0)
            # self.ogrid_origin = np.array([msg.info.origin.position.x, msg.info.origin.position.y])
            # self.ogrid_cpm = 1 / msg.info.resolution
            self.got_world_map = True

    def merged_map_cb(self, msg):
            self.merged_ogrid = np.array(msg.data)
            time.sleep(1)

    def modelState_cb(self, msg):
        self.total_iterations +=1
        
        if(self.total_iterations%1000 == 0 and not rospy.is_shutdown()): #gazebo topic publishing frequency
            self.check_itr+=1
            self.iteration.append(self.check_itr)
            names = msg.name
            n_count = 0
            robot_id_list = []
            robot_positions = []
            for val in names:
                if "tb3" in val:
                    robot_id_list.append(n_count)
                n_count+=1

            #DO we use average distance when testing with muliple robots??
            robot_1 = msg.pose[robot_id_list[0]].position
            robot_2 = msg.pose[robot_id_list[1]].position
            
            self.current_distance = sqrt(pow(robot_1.x - robot_2.x ,2) + pow(robot_1.y - robot_2.y ,2))
            self.distance.append(self.current_distance)
           
                
    def plot_dist(self):
        while not rospy.is_shutdown():
            # print(self.check_itr, ": ", self.distance)
            plt.cla()
            self.ax.plot(self.iteration, self.distance, 'k', marker=".", markersize=10)
            
            if self.check_itr > self.x_lim:
                self.x_lim +=50

            plt.xlim(0, self.x_lim)
            plt.ylim(0, 15)
            plt.xlabel("x-axis")
            plt.ylabel("y-axis")
            plt.pause(0.001)
        
    def compare_maps(self):
        while not rospy.is_shutdown():
            if(self.got_world_map):
                exploration_time = time.time() - self.start
                self.world_map_count = np.count_nonzero(self.world_ogrid > -1)
                self.merged_map_count = np.count_nonzero(self.merged_ogrid > -1)
                map_coverage_percentage = self.merged_map_count*100/self.world_map_count
                print("Current map coverage = {} %".format(map_coverage_percentage))
                
                if(map_coverage_percentage/5 > self.itr):
                    print("*****************************************")
                    print("Exploration time to cover {} % of map = {} seconds".format(map_coverage_percentage, exploration_time))
                    print("*****************************************")
                    self.itr+=1
                
                current_data = [map_coverage_percentage, exploration_time, self.current_distance]
                self.exploration_stats.append(current_data)

                if(map_coverage_percentage > self.exploration_threshold):
                    ts = str(time.time()).split(".")[0]
                    op_name = 'exploration_test_'+ts+'.csv'
                    with open('/home/jadhav/catkin_ws/src/wsr_exploration/data/'+op_name, 'w') as f: 
                        write = csv.writer(f) 
                        write.writerow(self.details) 
                        write.writerows(self.exploration_stats) 
                    
                    print("Output filename: {}".format(op_name))
                    self.pub.publish(self.status)
                    rospy.signal_shutdown("Finished 95% exploration. Exiting")

            plt.cla()
            self.ax.plot(self.iteration, self.distance, 'k', marker=".", markersize=10)
            
            if self.check_itr > self.x_lim:
                self.x_lim +=50

            plt.xlim(0, self.x_lim)
            plt.ylim(0, 15)
            plt.xlabel("x-axis")
            plt.ylabel("y-axis")
            plt.pause(0.001)


            time.sleep(1)

def main(): 
    obj = ExplorationEval()
    obj.compare_maps()
    # obj.plot_dist()
    # rospy.spin()

if __name__=="__main__":
    main()
        
            