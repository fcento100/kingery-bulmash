# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:53:18 2024

@author: fcento
"""

import pytest
import kingery_bulmash as kb

# NEQ = 100
# DIST = 40 * NEQ ** (1/3)
# res = kb.Blast_Parameters(unit_system=kb.Units.METRIC, neq=NEQ, distance=DIST, safe=False)

# print(res)


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
    NEQ = 1000
    DIST = sr * NEQ ** (1/3)
    res = kb.Blast_Parameters(unit_system=kb.Units.METRIC, neq=NEQ, distance=DIST, safe=False)
    
    REL = 0.01
    
    if toa is None:
        assert res.time_of_arrival is None
    else:
        assert res.time_of_arrival == pytest.approx((toa * NEQ ** (1/3)), rel=REL)
    
    if ip is None:
        assert res.incident_pressure is None
    else: 
        assert res.incident_pressure == pytest.approx(ip, rel=REL)
    
    if rp is None:
        assert res.reflected_pressure is None
    else:
        assert res.reflected_pressure == pytest.approx(rp, rel=REL)
    
    if ppd is None:
        assert res.positive_phase_duration is None
    else:
        assert res.positive_phase_duration == pytest.approx((ppd * NEQ ** (1/3)), rel=REL)
    
    if ii is None:
         assert res.incident_impulse is None
    else:
        assert res.incident_impulse == pytest.approx((ii * NEQ ** (1/3)), rel=REL)
    
    if ri is None:
        assert res.reflected_impulse is None
    else:
        assert res.reflected_impulse == pytest.approx((ri * NEQ ** (1/3)), rel=REL)
    
    if sfv is None:
        assert res.shock_front_velocity is None
    else:
        assert res.shock_front_velocity == pytest.approx((sfv*1000), rel=REL)