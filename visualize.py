import matplotlib.pyplot as plt


def plot_results(
    terrain_x,
    terrain_z,
    terrain_points,
    reconstruction,
    x_new
):

    fig, axes = plt.subplots(3, 1, figsize=(10, 12))

    # ------------------------------------
    # Plot 1 : Original Terrain
    # ------------------------------------

    axes[0].plot(terrain_x, terrain_z)

    axes[0].set_title("Original Terrain")

    axes[0].set_xlabel("X Position")

    axes[0].set_ylabel("Height")

    axes[0].grid(True)

    # ------------------------------------
    # Plot 2 : Contact Points
    # ------------------------------------

    x_points = [p[0] for p in terrain_points]

    z_points = [p[2] for p in terrain_points]

    axes[1].scatter(x_points, z_points)

    axes[1].set_title("Terrain Points Collected by Hexapod")

    axes[1].set_xlabel("X Position")

    axes[1].set_ylabel("Height")

    axes[1].grid(True)

    # ------------------------------------
    # Plot 3 : Reconstructed Terrain
    # ------------------------------------

    z_new = reconstruction(x_new)

    axes[2].plot(x_new, z_new)

    axes[2].set_title("Reconstructed Terrain")

    axes[2].set_xlabel("X Position")

    axes[2].set_ylabel("Height")

    axes[2].grid(True)

    plt.tight_layout()

    plt.show()