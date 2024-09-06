"""
Assume you read data from a Temperature sensor every 10 seconds for a period
of let say 5 minutes.
Log the data to a File.
You can use the Random Generator in Python.
Make sure to log both the time and the temperature value
Create another Python Script that reads the same data.
You should also plot the data you read from the File.
"""

import random

def read_sensor() -> float:
    """Simulate reading temperature from a sensor"""
    return random.randint(0, 30)

with open("Exercises/ex7/myfile.txt", "w") as f:
    f.write("Time Value\n")

    for i in range(1, (5 * 60 // 10) + 1): 
        temperature = read_sensor()
        f.write(f"{i} {temperature}\n") 

