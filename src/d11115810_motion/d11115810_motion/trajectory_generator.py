#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math

class TrajectoryGenerator(Node):

    def __init__(self):
        super().__init__('trajectory_generator')
        
        # Create publisher for the /joint_states topic
        self.publisher_ = self.create_publisher(JointState, '/joint_states', 10)
        
        # Periodically call the timer loop every 50ms (20 Hz)
        self.timer_period = 0.05  
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        
        # Define the exact joint names from your Assignment 3 URDF
        self.joint_names = [
            'arm_0_joint', 
            'arm_1_joint', 
            'arm_2_joint', 
            'gripper_1_joint', 
            'gripper_2_joint'
        ]
        
        # Define 5 discrete trajectory waypoints in joint space
        # Format: [arm_0, arm_1, arm_2, gripper_1, gripper_2]
        self.waypoints = [
            [0.0,   0.0,   0.0,   0.0,   0.0],    # Waypoint 1: Home/Center
            [1.0,   0.5,   0.8,  -0.03,  0.03],   # Waypoint 2: Reaching out & opening jaws
            [1.5,  -0.5,   1.2,   0.0,   0.0],    # Waypoint 3: High pose & closed jaws
            [-1.0,  0.8,  -0.5,  -0.02,  0.02],   # Waypoint 4: Swung left & semi-open
            [-2.0,  0.0,   0.5,   0.0,   0.0]     # Waypoint 5: Swung far back
        ]
        
        self.current_waypoint_idx = 0
        self.next_waypoint_idx = 1
        
        # Time variables for interpolation
        self.time_per_segment = 3.0  # Seconds to move from one waypoint to the next
        self.elapsed_time = 0.0

    def timer_callback(self):
        # Progress time step
        self.elapsed_time += self.timer_period
        
        # Calculate interpolation factor alpha (clamped between 0.0 and 1.0)
        alpha = self.elapsed_time / self.time_per_segment
        if alpha >= 1.0:
            alpha = 1.0
            
        # Get the starting and ending positions for interpolation
        start_pose = self.waypoints[self.current_waypoint_idx]
        end_pose = self.waypoints[self.next_waypoint_idx]
        
        # Linearly interpolate each joint angle
        current_positions = []
        for i in range(len(self.joint_names)):
            pos = start_pose[i] + alpha * (end_pose[i] - start_pose[i])
            current_positions.append(pos)
            
        # Build and populate the standard JointState message layout
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = self.joint_names
        msg.position = current_positions
        
        # Publish the joint message
        self.publisher_.publish(msg)
        
        # If the target waypoint is reached, cycle smoothly to the next segment loop
        if alpha >= 1.0:
            self.elapsed_time = 0.0
            self.current_waypoint_idx = self.next_waypoint_idx
            self.next_waypoint_idx = (self.next_waypoint_idx + 1) % len(self.waypoints)

def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryGenerator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
