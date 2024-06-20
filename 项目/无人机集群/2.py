from multi_robomaster import multi_robot


def takeoff_land_task1(robot_group):
    robot_group.takeoff().wait_for_completed()
    robot_group.forward(50).wait_for_completed()
    robot_group.land().wait_for_completed()


def takeoff_land_task2(robot_group):
    robot_group.takeoff().wait_for_completed()
    robot_group.backward(50).wait_for_completed()
    robot_group.land().wait_for_completed()


if __name__ == '__main__':
    # get drone sn by run the expamles of /15_multi_robot/multi_drone/01_scan_ip.py

    robot_sn_list = ["0TQZM4ACNT06Y7", "0TQZM4CCNT087A","0TQZM4DCNT09K1",
                     "0TQZM47CNT046C","0TQZM4DCNT09Z4","0TQZM4CCNT08MW"
                     ] # 设置组网模式时记下来的机器SN码
    multi_drone = multi_robot.MultiDrone()
    multi_drone.initialize(robot_num=6)
    multi_drone.number_id_by_sn([0, robot_sn_list[0]], [1, robot_sn_list[1]],
                                [2, robot_sn_list[2]],
                                [3, robot_sn_list[3]],
                                [4, robot_sn_list[4]],
                                [5, robot_sn_list[5]],
                                )
    multi_drone_group1 = multi_drone.build_group([0])
    multi_drone_group2 = multi_drone.build_group([1])
    multi_drone_group3 = multi_drone.build_group([2])
    multi_drone_group4 = multi_drone.build_group([3])
    multi_drone_group5 = multi_drone.build_group([4])
    multi_drone_group6 = multi_drone.build_group([5])
    multi_drone.run([multi_drone_group1, takeoff_land_task2],
                    [multi_drone_group2, takeoff_land_task2],
                    [multi_drone_group3, takeoff_land_task2],
                    [multi_drone_group4, takeoff_land_task2],
                    [multi_drone_group5, takeoff_land_task2],
                    [multi_drone_group6, takeoff_land_task2],)
    multi_drone.close()