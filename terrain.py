import numpy as np

def generate_terrain(length=100, step=0.5):
    """
    Generates a simple terrain profile.
    """

    x = np.arange(0, length, step)

    z = (
        2*np.sin(0.15*x)
        + 1*np.sin(0.5*x)
        + 0.5*np.cos(0.3*x)
    )

    return x, z

def terrain_height(x_world, terrain_x, terrain_z):
    """
    Returns terrain height at a given x position.
    """

    return np.interp(x_world, terrain_x, terrain_z)

from scipy.interpolate import interp1d

def reconstruct_terrain(terrain_points):

    terrain_points.sort(key=lambda p: p[0])

    unique_points = {}

    for point in terrain_points:
        unique_points[point[0]] = point[2]

    x = list(unique_points.keys())
    z = list(unique_points.values())

    reconstruction = interp1d(
        x,
        z,
        kind='cubic',
        fill_value="extrapolate"
    )


    x_new = np.linspace(min(x), max(x), 300)

    return reconstruction, x_new