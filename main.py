import math

from kinematics import forward_kinematics
from simulator import generate_joint_angles
from terrain import (
    generate_terrain,
    terrain_height,
    reconstruct_terrain,
)
from visualize import plot_results


# -----------------------------
# Robot Parameters
# -----------------------------

L1 = 5
L2 = 8
L3 = 12

STEP_SIZE = 1

LEG_PHASES = {
    "LF": 0,
    "RM": 0,
    "LR": 0,

    "RF": math.pi,
    "LM": math.pi,
    "RR": math.pi,
}


# -----------------------------
# Generate Terrain
# -----------------------------

terrain_x, terrain_z = generate_terrain()

foot_positions = []
terrain_points = []



# -----------------------------
# Simulate Walking
# -----------------------------

BODY_HEIGHT = 17
NUM_STEPS = 100

body_x = 0

# Generate joint trajectories for all legs
joint_trajectories = {}

for leg_name, phase in LEG_PHASES.items():
    joint_trajectories[leg_name] = generate_joint_angles(
        NUM_STEPS,
        phase
    )

# Simulate walking
for step in range(NUM_STEPS):

    for leg_name in LEG_PHASES:

        theta1, theta2, theta3 = joint_trajectories[leg_name][step]

        x, y, z = forward_kinematics(
            theta1,
            theta2,
            theta3,
            L1,
            L2,
            L3,
        )

        world_x = x + body_x
        world_y = y
        world_z = BODY_HEIGHT + z

        if len(foot_positions) < 5:
            print(f"x = {x:.2f}, y = {y:.2f}, z = {z:.2f}")

        foot_positions.append(
            (world_x, world_y, world_z)
        )

        ground = terrain_height(
            world_x,
            terrain_x,
            terrain_z,
        )

        if len(foot_positions) < 5:
            print(f"Ground = {ground:.2f}")
            print(f"Difference = {abs(world_z - ground):.2f}")
            print("----------------------")

        if abs(world_z - ground) < 5:
            terrain_points.append(
                (world_x, world_y, ground)
            )

    # Move the robot body forward after all six legs complete one time step
    body_x += STEP_SIZE

# -----------------------------
# Reconstruct Terrain
# -----------------------------
print("Foot Positions:", len(foot_positions))
print("Terrain Points:", len(terrain_points))
if len(terrain_points) < 4:
    print("Not enough terrain points collected.")
    exit()
reconstruction, x_new = reconstruct_terrain(
    terrain_points
)


# -----------------------------
# Display Results
# -----------------------------

plot_results(
    terrain_x,
    terrain_z,
    terrain_points,
    reconstruction,
    x_new,
)