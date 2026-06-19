import math

def forward_kinematics(theta1, theta2, theta3, L1, L2, L3):
    """
    Calculate the foot position of a simplified 3-DOF hexapod leg.

    Parameters:
        theta1 : Coxa angle (degrees)
        theta2 : Femur angle (degrees)
        theta3 : Tibia angle (degrees)
        L1 : Coxa length
        L2 : Femur length
        L3 : Tibia length

    Returns:
        (x, y, z)
    """

    # Convert degrees to radians
    theta1 = math.radians(theta1)
    theta2 = math.radians(theta2)
    theta3 = math.radians(theta3)

    # Horizontal distance from body
    reach = L1 + L2 * math.cos(theta2) + L3 * math.cos(theta2 + theta3)

    # Calculate coordinates
    x = reach * math.cos(theta1)
    y = reach * math.sin(theta1)
    z = -(L2 * math.sin(theta2) + L3 * math.sin(theta2 + theta3))

    return x, y, z