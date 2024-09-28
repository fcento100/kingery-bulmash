# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:53:18 2024

@author: fcento100
"""

import pytest
import kingery_bulmash as kb


@pytest.mark.parametrize("sr, toa, ip, rp, ppd, ii, ri, sfv, slope", [
    (0.2, 0.037, 17310.36, 185301, 0.243, 369.5, 10520, 3.962, -1.342),
    (0.3, 0.066, 10180, 97546, 0.222, 215.7, 5285, 3.098, -1.322),
    (0.4, 0.101, 6853, 59549, 0.234, 175.1, 3336, 2.561, -1.445),
    (0.5, 0.143, 4888, 39422, 0.281, 166.2, 2371, 2.178, -1.59),
    (0.6, 0.193, 3613, 27381, 0.378, 170.9, 1810, 1.887, -1.726),
    (0.7, 0.25, 2744, 19624, 0.548, 183.4, 1449, 1.658, -1.846),
    (0.8, 0.315, 2129, 14390, 0.818, 201.5, 1201, 1.473, -1.949),
    (0.9, 0.387, 1684, 10746, 1.211, 223.9, 1021, 1.322, -2.035),
    (1, 0.467, 1354, 8152, 1.72, 236.3, 884.7, 1.196, -2.107),
    (1.5, 0.989, 551.4, 2511, 2.148, 177.4, 520.7, 0.808, -2.295),
    (2, 1.693, 283.7, 1058, 2.053, 134.6, 363.8, 0.623, -2.302),
    (2.5, 2.557, 171.3, 547.3, 2.305, 107.5, 278, 0.532, -2.207),
    (3, 3.546, 115.7, 330.7, 2.819, 92.7, 224.3, 0.48, -2.125),
    (3.5, 4.63, 84.2, 223, 3.177, 81.35, 187.7, 0.447, -2.002),
    (4, 5.785, 64.89, 162.6, 3.436, 72.42, 161.2, 0.425, -1.901),
    (4.5, 6.993, 52.14, 125.5, 3.634, 65.22, 141.2, 0.409, -1.815),
    (5, 8.242, 43.23, 100.9, 3.793, 59.31, 125.6, 0.398, -1.742),
    (5.5, 9.521, 36.73, 83.84, 3.929, 54.37, 113, 0.389, -1.679),
    (6, 10.82, 31.81, 71.37, 4.048, 50.19, 102.7, 0.383, -1.624),
    (6.5, 12.14, 27.99, 61.96, 4.157, 46.6, 94.16, 0.377, -1.576),
    (7, 13.48, 24.94, 54.64, 4.258, 43.48, 86.89, 0.373, -1.534),
    (7.5, 14.82, 22.47, 48.8, 4.354, 40.76, 80.66, 0.37, -1.498),
    (8, 16.18, 20.42, 44.05, 4.445, 38.35, 75.25, 0.368, -1.465),
    (8.5, 17.54, 18.7, 40.11, 4.533, 36.22, 70.53, 0.365, -1.437),
    (9, 18.91, 17.24, 36.8, 4.618, 34.31, 66.35, 0.363, -1.411),
    (9.5, 20.28, 15.98, 33.97, 4.7, 32.59, 62.64, 0.362, -1.389),
    (10, 21.66, 14.89, 31.54, 4.779, 31.04, 59.33, 0.361, -1.369),
    (11, 24.43, 13.09, 27.55, 4.931, 28.33, 53.63, 0.358, -1.336),
    (12, 27.21, 11.67, 24.43, 5.074, 26.07, 48.93, 0.357, -1.31),
    (13, 30.01, 10.51, 21.91, 5.208, 24.13, 44.98, 0.355, -1.29),
    (14, 32.82, 9.561, 19.84, 5.334, 22.47, 41.62, 0.354, -1.276),
    (15, 35.64, 8.758, 18.11, 5.452, 21.02, 38.72, 0.353, -1.265),
    (16, 38.47, 8.074, 16.64, 5.563, 19.75, 36.19, 0.352, -1.258),
    (17, 41.32, 7.482, 15.37, 5.666, 18.62, 33.97, 0.351, -1.254),
    (18, 44.18, 6.964, 14.27, 5.763, 17.61, 32, 0.351, -1.253),
    (19, 47.05, 6.508, 13.3, 5.855, 16.71, 30.24, 0.35, -1.254),
    (20, 49.93, 6.102, 12.44, 5.94, 15.89, 28.67, 0.349, -1.257),
    (22, 55.72, 5.411, 10.99, 6.097, 14.47, 25.95, 0.348, -1.268),
    (24, 61.54, 4.871, 9.802, 6.238, 13.29, 23.7, 0.347, -1.407),
    (26, 67.38, 4.353, 8.815, 6.367, 12.28, 21.8, 0.346, -1.407),
    (28, 73.22, 3.922, 7.979, 6.487, 11.41, 20.17, 0.345, -1.407),
    (30, 79.07, 3.559, 7.261, 6.601, 10.65, 18.76, 0.345, -1.407),
    (32, 84.89, 3.25, 6.637, 6.712, 9.982, 17.53, 0.344, -1.407),
    (34, 90.69, 2.984, 6.088, 6.821, 9.37, 16.45, 0.344, -1.407),
    (36, 96.44, 2.754, 5.602, 6.932, 8.818, 15.49, 0.344, -1.407),
    (38, 102.1, 2.552, 5.167, 7.045, 8.326, 14.63, 0.344, -1.407),
    (40, 107.8, 2.375, 4.775, 7.162, 7.885, 13.85, 0.344, -1.407),
    (42, None, 2.217, None, None, 7.486, None, None, -1.407),
    (44, None, 2.077, None, None, 7.126, None, None, -1.407),
    (46, None, 1.951, None, None, 6.797, None, None, -1.407),
    (48, None, 1.837, None, None, 6.497, None, None, -1.407),
    (50, None, 1.735, None, None, 6.221, None, None, -1.407),
    (60, None, 1.342, None, None, 5.126, None, None, -1.407),
    (70, None, 1.081, None, None, 4.352, None, None, -1.407),
    (80, None, 0.896, None, None, 3.776, None, None, -1.407),
    (90, None, 0.759, None, None, 3.332, None, None, -1.407),
    (100, None, 0.654, None, None, 2.98, None, None, -1.407),
    (110, None, 0.572, None, None, 2.693, None, None, -1.407),
    (120, None, 0.506, None, None, 2.455, None, None, -1.407),
    (130, None, 0.452, None, None, 2.255, None, None, -1.407),
    (140, None, 0.408, None, None, 2.084, None, None, -1.407),
    (150, None, 0.37, None, None, 1.937, None, None, -1.407),
    (160, None, 0.338, None, None, None, None, None, -1.407),
])
def test_metric(sr, toa, ip, rp, ppd, ii, ri, sfv, slope):
    """
    Test against ADA526744 metric units tables
    """
    REL = 0.001
    NEQ = 10000
    NEQ3 = NEQ ** (1/3)
    DIST = sr * NEQ3
    RES = kb.Blast_Parameters(unit_system=kb.Units.METRIC, neq=NEQ, distance=DIST, safe=False)

    if toa is None:
        assert RES.time_of_arrival is None
    else:
        assert round(RES.time_of_arrival/NEQ3, 3) == pytest.approx(toa, rel=REL)

    if ip is None:
        assert RES.incident_pressure is None
    else:
        assert round(RES.incident_pressure, 3) == pytest.approx(ip, rel=REL)

    if rp is None:
        assert RES.reflected_pressure is None
    else:
        assert round(RES.reflected_pressure, 3) == pytest.approx(rp, rel=REL)

    if ppd is None:
        assert RES.positive_phase_duration is None
    else:
        assert round(RES.positive_phase_duration/NEQ3, 3) == pytest.approx(ppd, rel=REL)

    if ii is None:
        assert RES.incident_impulse is None
    else:
        assert round(RES.incident_impulse/NEQ3, 3) == pytest.approx(ii, rel=REL)

    if ri is None:
        assert RES.reflected_impulse is None
    else:
        assert round(RES.reflected_impulse/NEQ3, 3) == pytest.approx(ri, rel=REL)

    if sfv is None:
        assert RES.shock_front_velocity is None
    else:
        assert round(RES.shock_front_velocity/1000, 3) == pytest.approx(sfv, rel=REL)


@pytest.mark.parametrize("sr, toa, ip, rp, ppd, ii, ri, sfv, slope", [
    (0.5, 0.028, 2539, 27252, 0.188, 41.7, 1190, 13.12, -1.345),
    (0.6, 0.036, 1997, 20430, 0.177, 31.64, 867.2, 11.73, -1.3),
    (0.7, 0.045, 1634, 15946, 0.172, 26.07, 669, 10.65, -1.305),
    (0.8, 0.055, 1370, 12814, 0.171, 22.79, 537.3, 9.773, -1.338),
    (0.9, 0.065, 1167, 10520, 0.173, 20.8, 444.7, 9.042, -1.386),
    (1, 0.077, 1006, 8774, 0.179, 19.59, 376.6, 8.417, -1.44),
    (1.1, 0.089, 874.6, 7404, 0.189, 18.9, 324.9, 7.871, -1.497),
    (1.2, 0.102, 765.9, 6307, 0.204, 18.58, 284.5, 7.39, -1.555),
    (1.3, 0.116, 674.7, 5412, 0.225, 18.53, 252.2, 6.959, -1.612),
    (1.4, 0.131, 597.6, 4673, 0.252, 18.68, 225.9, 6.572, -1.667),
    (1.5, 0.146, 531.7, 4056, 0.286, 18.99, 204.2, 6.221, -1.72),
    (1.6, 0.163, 475.1, 3537, 0.329, 19.44, 185.9, 5.902, -1.77),
    (1.7, 0.18, 426.1, 3097, 0.381, 20.01, 170.4, 5.609, -1.817),
    (1.8, 0.199, 383.6, 2722, 0.445, 20.69, 157, 5.341, -1.862),
    (1.9, 0.218, 346.5, 2401, 0.52, 21.45, 145.5, 5.094, -1.904),
    (2, 0.238, 313.9, 2124, 0.61, 22.3, 135.4, 4.867, -1.943),
    (2.5, 0.354, 199.8, 1204, 1.297, 26.4, 99.71, 3.955, -2.102),
    (3, 0.493, 134.9, 727, 1.671, 24.04, 78.23, 3.313, -2.208),
    (3.5, 0.657, 95.44, 463.8, 1.69, 21.23, 64.05, 2.85, -2.273),
    (4, 0.844, 70.28, 310.6, 1.624, 18.75, 54.04, 2.51, -2.307),
    (4.5, 1.054, 53.52, 216.7, 1.576, 16.73, 46.64, 2.256, -2.315),
    (5, 1.283, 41.95, 156.8, 1.57, 15.12, 40.96, 2.06, -2.304),
    (5.5, 1.532, 33.72, 117.6, 1.612, 13.82, 36.48, 1.915, -2.277),
    (6, 1.8, 27.71, 90.99, 1.699, 12.77, 32.85, 1.802, -2.236),
    (6.5, 2.083, 23.21, 72.34, 1.833, 11.69, 29.87, 1.712, -2.185),
    (7, 2.38, 19.78, 58.87, 2.016, 11.01, 27.36, 1.64, -2.125),
    (7.5, 2.69, 17.09, 48.88, 2.161, 10.4, 25.24, 1.581, -2.131),
    (8, 3.011, 14.92, 41.3, 2.276, 9.854, 23.42, 1.531, -2.079),
    (8.5, 3.342, 13.17, 35.43, 2.378, 9.36, 21.83, 1.489, -2.031),
    (9, 3.683, 11.74, 30.79, 2.468, 8.911, 20.45, 1.454, -1.987),
    (9.5, 4.031, 10.56, 27.05, 2.549, 8.503, 19.23, 1.424, -1.945),
    (10, 4.387, 9.562, 24.04, 2.621, 8.129, 18.14, 1.397, -1.907),
    (11, 5.117, 8, 19.45, 2.747, 7.471, 16.29, 1.355, -1.837),
    (12, 5.867, 6.837, 16.19, 2.854, 6.91, 14.78, 1.321, -1.775),
    (13, 6.635, 5.944, 13.78, 2.946, 6.426, 13.53, 1.295, -1.721),
    (14, 7.416, 5.242, 11.95, 3.029, 6.005, 12.46, 1.274, -1.672),
    (15, 8.208, 4.678, 10.52, 3.105, 5.635, 11.56, 1.257, -1.629),
    (16, 9.009, 4.216, 9.373, 3.174, 5.308, 10.77, 1.244, -1.59),
    (17, 9.817, 3.833, 8.441, 3.24, 5.017, 10.08, 1.232, -1.555),
    (18, 10.631, 3.51, 7.669, 3.302, 4.756, 9.48, 1.222, -1.524),
    (19, 11.451, 3.235, 7.021, 3.361, 4.52, 8.944, 1.214, -1.495),
    (20, 12.274, 2.998, 6.47, 3.418, 4.307, 8.464, 1.207, -1.469),
    (22, 13.932, 2.612, 5.584, 3.525, 3.936, 7.644, 1.196, -1.425),
    (24, 15.601, 2.311, 4.905, 3.626, 3.624, 6.968, 1.187, -1.388),
    (26, 17.279, 2.071, 4.369, 3.721, 3.357, 6.401, 1.18, -1.358),
    (28, 18.965, 1.874, 3.935, 3.812, 3.128, 5.919, 1.175, -1.333),
    (30, 20.657, 1.711, 3.577, 3.898, 2.927, 5.504, 1.17, -1.312),
    (32, 22.356, 1.573, 3.276, 3.979, 2.751, 5.143, 1.166, -1.296),
    (34, 24.06, 1.455, 3.019, 4.057, 2.595, 4.825, 1.163, -1.283),
    (36, 25.77, 1.352, 2.798, 4.131, 2.456, 4.545, 1.16, -1.272),
    (38, 27.486, 1.263, 2.605, 4.201, 2.331, 4.295, 1.157, -1.265),
    (40, 29.207, 1.183, 2.436, 4.268, 2.218, 4.071, 1.155, -1.259),
    (42, 30.933, 1.113, 2.285, 4.332, 2.115, 3.868, 1.152, -1.256),
    (44, 32.665, 1.05, 2.151, 4.393, 2.021, 3.685, 1.15, -1.254),
    (46, 34.401, 0.993, 2.03, 4.451, 1.936, 3.518, 1.148, -1.253),
    (48, 36.142, 0.941, 1.921, 4.506, 1.857, 3.365, 1.146, -1.254),
    (50, 37.887, 0.894, 1.822, 4.559, 1.784, 3.225, 1.145, -1.257),
    (60, 46.667, 0.71, 1.436, 4.793, 1.492, 2.666, 1.138, -1.282),
    (70, 55.502, 0.575, 1.169, 4.988, 1.281, 2.269, 1.132, -1.407),
    (80, 64.336, 0.477, 0.972, 5.161, 1.121, 1.972, 1.129, -1.407),
    (90, 73.107, 0.404, 0.821, 5.325, 0.991, 1.742, 1.128, -1.407),
    (100, 81.752, 0.348, 0.7, 5.488, 0.886, 1.559, 1.129, -1.407),
    (150, None, 0.197, None, None, 0.576, None, None, -1.407),
    (200, None, 0.131, None, None, 0.425, None, None, -1.407),
    (250, None, 0.096, None, None, 0.335, None, None, -1.407),
    (300, None, 0.074, None, None, 0.276, None, None, -1.407),
    (328, None, 0.066, None, None, 0.251, None, None, -1.407),
    (350, None, 0.06, None, None, 0.234, None, None, -1.407),
    (400, None, 0.05, None, None, 0.203, None, None, -1.407),
    (450, None, 0.042, None, None, None, None, None, -1.407),
    (500, None, 0.036, None, None, None, None, None, -1.407),
])
def test_imperial(sr, toa, ip, rp, ppd, ii, ri, sfv, slope):
    """
    Test against ADA526744 english units tables
    """
    REL = 0.001
    NEQ = 10000
    NEQ3 = NEQ ** (1/3)
    DIST = sr * NEQ3
    RES = kb.Blast_Parameters(unit_system=kb.Units.IMPERIAL, neq=NEQ, distance=DIST, safe=False)

    if toa is None:
        assert RES.time_of_arrival is None
    else:
        assert round(RES.time_of_arrival/NEQ3, 3) == pytest.approx(toa, rel=REL)

    if ip is None:
        assert RES.incident_pressure is None
    else:
        assert round(RES.incident_pressure, 3) == pytest.approx(ip, rel=REL)

    if rp is None:
        assert RES.reflected_pressure is None
    else:
        assert round(RES.reflected_pressure, 3) == pytest.approx(rp, rel=REL)

    if ppd is None:
        assert RES.positive_phase_duration is None
    else:
        assert round(RES.positive_phase_duration/NEQ3, 3) == pytest.approx(ppd, rel=REL)

    if ii is None:
        assert RES.incident_impulse is None
    else:
        assert round(RES.incident_impulse/NEQ3, 3) == pytest.approx(ii, rel=REL)

    if ri is None:
        assert RES.reflected_impulse is None
    else:
        assert round(RES.reflected_impulse/NEQ3, 3) == pytest.approx(ri, rel=REL)

    if sfv is None:
        assert RES.shock_front_velocity is None
    else:
        assert round(RES.shock_front_velocity/1000, 3) == pytest.approx(sfv, rel=REL)


@pytest.mark.parametrize("neq, dist, toa, ip, rp, ppd, ii, ri, sfv", [
    (2, 0.5, 0.13, 6907.65, 60186.76, 0.29, 221.36, 4255.88, 2556.69),
    (5000, 50, 57.92, 122.12, 354.22, 47.34, 1622.32, 3951.86, 485.79),
    (1000, 50, 82.45, 43.18, 100.68, 37.85, 592.56, 1255.69, 397.66),
    (10000, 50, 48.11, 202.42, 678.94, 46.8, 2518.76, 6545.98, 560.13),
    (100000, 50, 24.85, 1157.19, 6644.99, 93., 10644.48, 37173.90, 1112.25),
])
def test_unsaferguard(neq, dist, toa, ip, rp, ppd, ii, ri, sfv):
    """
    Test against unsaferguard web tool
    https://unsaferguard.org/un-saferguard/kingery-bulmash
    Please note values for shock front velocity taken from
    "Formulae for ammunition management, IATG 01.80, March 2021"
    due to error on website as of 28/09/2024
    """
    REL=0.01
    RES = kb.Blast_Parameters(unit_system=kb.Units.METRIC, neq=neq, distance=dist, safe=False)
    
    if toa is None:
        assert RES.time_of_arrival is None
    else:
        assert round(RES.time_of_arrival, 2) == pytest.approx(toa, rel=REL)

    if ip is None:
        assert RES.incident_pressure is None
    else:
        assert round(RES.incident_pressure, 2) == pytest.approx(ip, rel=REL)

    if rp is None:
        assert RES.reflected_pressure is None
    else:
        assert round(RES.reflected_pressure, 2) == pytest.approx(rp, rel=REL)

    if ppd is None:
        assert RES.positive_phase_duration is None
    else:
        assert round(RES.positive_phase_duration, 2) == pytest.approx(ppd, rel=REL)

    if ii is None:
        assert RES.incident_impulse is None
    else:
        assert round(RES.incident_impulse, 2) == pytest.approx(ii, rel=REL)

    if ri is None:
        assert RES.reflected_impulse is None
    else:
        assert round(RES.reflected_impulse, 2) == pytest.approx(ri, rel=REL)

    if sfv is None:
        assert RES.shock_front_velocity is None
    else:
        assert round(RES.shock_front_velocity, 2) == pytest.approx(sfv, rel=REL)
