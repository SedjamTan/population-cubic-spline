# Presenting Bulacan’s Population as a
Function Using Cubic Spline Interpolation
And an Analysis of Bulacan’s
Population Dynamics
Numerical Analysis Final Project

## Overview
This repository contains coursework code for constructing a cubic spline interpolant of a population time series and analyzing its qualitative dynamics through the first and second derivatives of the spline.

The implementation provides:
1. A cubic spline visualization of the interpolated population curve.
2. A visualization of the spline’s growth rate (first derivative).
3. A visualization of the spline’s growth acceleration (second derivative).

The repository includes both a Python implementation (using Manim for visualization) and MATLAB scripts (using MATLAB’s cubic spline tools and explicit piecewise polynomials).

## Data
The spline is fitted to the following pairs of time and population size (units: people):

```text
Years (x):      [1903, 1918, 1939, 1948, 1960, 1970, 1975, 1980, 1990, 1995, 2000, 2007, 2010, 2015, 2020, 2024]
Population (y): [15559, 239969, 319339, 394642, 514346, 737975, 899529, 1096046, 1505219, 1784441, 2234088, 2822216, 2924433, 3292071, 3708890, 3876806]
```

## Mathematical Model
Let the data abscissae be ordered as
`x_0 < x_1 < ... < x_n` and define the cubic spline interpolant `S(x)` such that `S(x_i) = y_i` for each data point.

On each interval `(x_{i-1}, x_i]`, the spline can be represented as a cubic polynomial segment `S_i(x)`. The growth-rate and growth-acceleration proxies used in this project are:

1. Growth rate: `S'(x)`
2. Growth acceleration: `S''(x)`

The Manim scenes plot `S(x)`, `S'(x)`, and `S''(x)` using the piecewise representations and annotate a local maximum of the derivative on a selected subrange.

## Python (Manim)
The Python portion is located under `python/my-project/` and is primarily intended for rendering animations.

### Dependencies
Install the dependencies listed in `python/requirements.txt`, for example:

```bash
pip install -r python/requirements.txt
```

### Main entry point
Animations/scenes are defined in `python/my-project/main.py`.

The piecewise spline functions and their derivatives are defined in `python/my-project/math_functions.py` as:

* `f1, ..., f15`: spline segments for different year intervals
* `f1p, ..., f15p`: first derivatives of the segments (growth rate)
* `f1pp, ..., f15pp`: second derivatives of the segments (growth acceleration)

### Render commands
From the repository root, you can render a scene with Manim (examples):

```bash
manim -qh "python/my-project/main.py" PopulationGraph
manim -qh "python/my-project/main.py" PopulationGrowth
manim -qh "python/my-project/main.py" PopulationAccelerate
```

Additional scenes included for pedagogical context:

* `InterpolateExample`
* `LogisticGrowthModel`
* `GrowthFunctions`

Manim’s rendered media is written to `media/` (which is ignored by Git).

## MATLAB
The MATLAB implementation is located under `matlab/`.

### Key scripts
* `interpolation.m`: constructs and plots the cubic spline interpolant using MATLAB’s `csapi(x, y)` and overlays the data points.
* `functions_of_interpolation.m`: contains explicit piecewise cubic polynomial segments `f1..f15` and a combined piecewise definition `f_combined` for plotting and verification.
* `derivative_functions.m`: provides explicit first and second derivative piece functions (`f1p..f15p`, `f1pp..f15pp`).
* `derivative_of_interpolation.m`: uses the symbolic engine (`syms`, `diff`) to differentiate the piecewise cubic segments.

To reproduce the plots, open the scripts in MATLAB and run them in the MATLAB environment.

## Notes on Reproducibility and Extension
The spline segment functions (`f1..f15`) and derivative functions are embedded in the code as precomputed expressions for the specific dataset listed above. If you replace the dataset, you will need to regenerate these coefficients (or implement spline-coefficient computation directly in Python/MATLAB).
