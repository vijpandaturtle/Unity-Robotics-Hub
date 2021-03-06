#!/usr/bin/env python

import rospy

from ros_tcp_endpoint import TcpServer, RosPublisher, RosSubscriber, RosService

from robotics_demo.msg import PosRot, UnityColor
from robotics_demo.srv import PositionService

def main():
    ros_node_name = rospy.get_param("/TCP_NODE_NAME", 'TCPServer')
    buffer_size = rospy.get_param("/TCP_BUFFER_SIZE", 1024)
    connections = rospy.get_param("/TCP_CONNECTIONS", 10)
    tcp_server = TcpServer(ros_node_name, buffer_size, connections)

    tcp_server.source_destination_dict = {
        'pos_srv': RosService('position_service', PositionService),
        'pos_rot': RosPublisher('pos_rot', PosRot, queue_size=10),
        'color': RosSubscriber('color', UnityColor, tcp_server)
    }

    rospy.init_node(ros_node_name, anonymous=True)
    tcp_server.start()
    rospy.spin()


if __name__ == "__main__":
    main()
