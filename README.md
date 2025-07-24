# Signal Tracker

This program analyzes the movement data of an animal tracking signal device based on a text input file. The signal logs are used to determine movement patterns, time intervals, and potential data dropouts during the day.

## Functionality

**Function 1**  
Loads the data from the `signal.txt` file. Each line contains five integers: hour, minute, second, x-coordinate, and y-coordinate.

**Function 2**  
Receives a signal index from the user and prints the x and y coordinates of that signal.

**Function 3**  
Defines a function `elapsed()` that returns the time difference in seconds between two signals.

**Function 4**  
Calculates and prints the duration between the first and the last signals in the format `hours:minutes:seconds`.

**Function 5**  
Determines the smallest bounding rectangle that contains all recorded positions, and prints the coordinates of the bottom-left and top-right corners.

**Function 6**  
Calculates the total distance traveled using the Euclidean distance formula between each pair of consecutive positions.

**Function 7**  
Identifies and logs missing signals into `missed.txt`. A missing signal is inferred if:
- The time gap between consecutive signals is more than 5 minutes (300 seconds), or
- The position change in either coordinate is more than 10 units.

Each entry in `missed.txt` contains the timestamp and the type of dropout (`time-gap` or `coordinate-gap`) along with the number of missing records.

## Input

The input file `signal.txt` must contain one signal per line in the following format:

```
hour minute second x y
```

- Coordinates range from -10000 to 10000.
- A maximum of 1000 lines.

## Output

- Console messages for all task results.
- `missed.txt` will be generated to log the missing data points.

## Output files

After running the program, it generates the `missed.txt` file that contains records of missing signals based on time or coordinate gaps.  
This file is not included in the repository. It is automatically created during execution.

---
Developed by Áron Domonkos, 2024.