import math

def generate_joint_angles(num_steps, phase):

    joint_trajectory = []

    for step in range(num_steps):

        theta1 = 20 * math.sin(step * 0.1 + phase)

        theta2 = 30 + 15 * math.sin(step * 0.1 + phase)

        theta3 = 40 + 20 * math.cos(step * 0.1 + phase)

        joint_trajectory.append((theta1, theta2, theta3))

    return joint_trajectory