import numpy as np

# The goal of this exercise is to create 2 fonctions converting degrees and radians

def d2r(degre : float) -> float :
    """Convert degrees to radians"""
    return degre * np.pi/180

def r2d(radian : float) -> float :
    """Convert radians to degrees"""
    return radian * 180/np.pi

if __name__ == "__main__":

    degrees = 180
    radians = d2r(degrees)
    print(f"{degrees}° is equal to {radians} radians")
    
    radians = np.pi
    degrees = r2d(radians)
    print(f"{radians} radians is equal to {degrees}°")