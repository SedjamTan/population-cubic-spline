# Bulacan Population Cubic Spline and Growth Analysis
Numerical Analysis Final Project

## Overview
This repository contains coursework code that fits a cubic spline to a population data set and studies how the growth rate changes over time using the spline’s first and second derivatives.

The implementation provides:
1. A cubic spline visualization of the interpolated population curve.
2. A visualization of the spline’s growth rate (first derivative).
3. A visualization of the spline’s growth acceleration (second derivative).

The repository includes both a Python implementation (using Manim for visualization), MATLAB scripts (using MATLAB’s spline tools and piecewise polynomial expressions), as well as the results of these computations.

## Data
The spline is fitted to the following time–population pairs (units: people):

```text
Years (x):      [1903, 1918, 1939, 1948, 1960, 1970, 1975, 1980, 1990, 1995, 2000, 2007, 2010, 2015, 2020, 2024]
Population (y): [15559, 239969, 319339, 394642, 514346, 737975, 899529, 1096046, 1505219, 1784441, 2234088, 2822216, 2924433, 3292071, 3708890, 3876806]
```

## Model
Let the x-values be ordered as
`x_0 < x_1 < ... < x_n` and define the spline curve `S(x)` such that `S(x_i) = y_i` for each data point.

On each interval `(x_{i-1}, x_i]`, the spline is represented by a cubic polynomial segment `S_i(x)`. In this project, we use:

1. Growth rate: `S'(x)`
2. Growth acceleration: `S''(x)`

The Manim scenes plot `S(x)`, `S'(x)`, and `S''(x)` using the piecewise polynomial segments, and they highlight a peak on a chosen time interval.

## Python (Manim)
The Python code is located under `python/my-project/` and is mainly intended for rendering animations.

### Dependencies
Install the dependencies listed in `python/requirements.txt`, for example:

```bash
pip install -r python/requirements.txt
```

### Main entry point
The scenes are defined in `python/my-project/main.py`.

The piecewise spline functions and their derivatives are defined in `python/my-project/math_functions.py` as:

* `f1, ..., f15`: spline segments for different year intervals
* `f1p, ..., f15p`: first derivatives of the segments (growth rate)
* `f1pp, ..., f15pp`: second derivatives of the segments (growth acceleration)

### Render commands
From the repository root, you can render scenes with Manim (examples):

```bash
manim -qh "python/my-project/main.py" PopulationGraph
manim -qh "python/my-project/main.py" PopulationGrowth
manim -qh "python/my-project/main.py" PopulationAccelerate
```

Other example scenes included:

* `InterpolateExample`
* `LogisticGrowthModel`
* `GrowthFunctions`

Manim’s rendered media is written to `media/` (which is ignored by Git).

## MATLAB
The MATLAB code is located under `matlab/`.

### Key scripts
* `interpolation.m`: constructs and plots the cubic spline using MATLAB’s `csapi(x, y)`, and overlays the data points.
* `functions_of_interpolation.m`: contains hard-coded piecewise cubic formulas `f1..f15` and a combined definition `f_combined` for plotting.
* `derivative_functions.m`: provides hard-coded first and second derivative piece functions (`f1p..f15p`, `f1pp..f15pp`).
* `derivative_of_interpolation.m`: uses MATLAB’s symbolic tools (`syms`, `diff`) to differentiate the piecewise cubic segments.

To reproduce the plots, open the scripts in MATLAB and run them in the MATLAB environment.

## Notes on Reproducibility and Extension
The spline segment functions (`f1..f15`) and derivative functions are embedded in the code as generated formulas for the specific dataset listed above. If you replace the dataset, you will need to regenerate these formulas (or implement spline-coefficient computation directly in Python/MATLAB).
