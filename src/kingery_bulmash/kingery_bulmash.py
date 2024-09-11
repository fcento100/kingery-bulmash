# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 23:24:29 2024

@author: fcento
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from math import exp, log


class Units(Enum):
    METRIC = auto()
    IMPERIAL = auto()


def KB(Z: float,
       A: float,
       B: float,
       C: float,
       D: float,
       E: float,
       F: float,
       G: float) -> float:
    """
    Common Logarithm of the Distance.

    """
    param = [A,
             B*log(Z),
             C*log(Z)**2,
             D*log(Z)**3,
             E*log(Z)**4,
             F*log(Z)**5,
             G*log(Z)**6]
    return exp(sum(param))


@dataclass(frozen=True)
class Blast_Parameters():
    unit_system: Units
    neq: float
    distance: float
    time_of_arrival: float = field(init=False)
    incident_pressure: float = field(init=False)
    reflected_pressure: float = field(init=False)
    positive_phase_duration: float = field(init=False)
    incident_impulse: float = field(init=False)
    reflected_impulse: float = field(init=False)
    shock_front_velocity: float = field(init=False)
    all_units: dict = field(init=False)

    def __post_init__(self):
        if self.neq <= 0:
            raise ValueError("'neq' must be a positive number")
        if self.distance <= 0:
            raise ValueError("'distance' must be a positive number")

        # Z in (m/kg^1/3) or (ft/lb^1/3)
        range_z = self.distance/self.neq**(1/3)

        if self.unit_system == Units.METRIC:
            # Time of Arrival (ms)
            if 0.06 <= range_z <= 1.50:
                time_of_arrival = KB(range_z, -0.7604, 1.8058, 0.1257, -0.0437, -0.0310, -0.00669, 0) * self.neq**(1/3)
            elif 1.50 < range_z <= 40:
                time_of_arrival = KB(range_z, -0.7137, 1.5732, 0.5561, -0.4213, 0.1054, -0.00929, 0) * self.neq**(1/3)
            else:
                raise ValueError("Scaled-Distance out of range: Change 'neq' or 'distance'")

            # Incident Pressure (kPa)
            if 0.2 <= range_z <= 2.9:
                incident_pressure = KB(range_z, 7.2106, -2.1069, -0.3229, 0.1117, 0.0685, 0, 0)
            elif 2.9 < range_z <= 23.8:
                incident_pressure = KB(range_z, 7.5938, -3.0523, 0.40977, 0.0261, -0.01267, 0, 0)
            elif 23.8 < range_z <= 198.5:
                incident_pressure = KB(range_z, 6.0536, -1.4066, 0, 0, 0, 0, 0)
            else:
                raise ValueError("Scaled-Distance out of range: Change 'neq' or 'distance'")

            # Reflected Pressure (kPa)
            if 0.06 <= range_z <= 2.00:
                reflected_pressure = KB(range_z, 9.006, -2.6893, -0.6295, 0.1011, 0.29255, 0.13505, 0.019736)
            elif 2.00 < range_z <= 40:
                reflected_pressure = KB(range_z, 8.8396, -1.733, -2.64, 2.293, -0.8232, 0.14247, -0.0099)
            else:
                raise ValueError("Scaled-Distance out of range: Change 'neq' or 'distance'")

            # Positive Phase Duration (ms)
            if 0.2 <= range_z <= 1.02:
                positive_phase_duration = KB(range_z, 0.5426, 3.2299, -1.5931, -5.9667, -4.0815, -0.9149, 0) * self.neq**(1/3)
            elif 1.02 < range_z <= 2.8:
                positive_phase_duration = KB(range_z, 0.5440, 2.7082, -9.7354, 14.3425, -9.7791, 2.8535, 0) * self.neq**(1/3)
            elif 2.8 < range_z <= 40:
                positive_phase_duration = KB(range_z, -2.4608, 7.1639, -5.6215, 2.2711, -0.44994, 0.03486, 0) * self.neq**(1/3)
            else:
                raise ValueError("Scaled-Distance out of range: Change 'neq' or 'distance'")

            # Incident Impulse (kPa-ms)
            if 0.2 <= range_z <= 0.96:
                incident_impulse = KB(range_z, 5.522, 1.117, 0.6, -0.292, -0.087, 0, 0) * self.neq**(1/3)
            elif 0.96 < range_z <= 2.38:
                incident_impulse = KB(range_z, 5.465, -0.308, -1.464, 1.362, -0.432, 0, 0) * self.neq**(1/3)
            elif 2.38 < range_z <= 33.7:
                incident_impulse = KB(range_z, 5.2749, -0.4677, -0.2499, 0.0588, -0.00554, 0, 0) * self.neq**(1/3)
            elif 33.7 < range_z <= 158.7:
                incident_impulse = KB(range_z, 5.9825, -1.062, 0, 0, 0, 0, 0) * self.neq**(1/3)
            else:
                raise ValueError("Scaled-Distance out of range: Change 'neq' or 'distance'")

            # Reflected Impulse (kPa-ms)
            if 0.06 <= range_z <= 40:
                reflected_impulse = KB(range_z, 6.7853, -1.3466, 0.101, 0.01123, 0, 0, 0) * self.neq**(1/3)
            else:
                raise ValueError("Scaled-Distance out of range: Change 'neq' or 'distance'")

            # Shock Front Velocity (m/s).
            if 0.06 <= range_z <= 1.50:
                shock_front_velocity = KB(range_z, 0.1794, -0.956, -0.0866, 0.109, 0.0699, 0.01218, 0) * 1000
            elif 1.50 < range_z <= 40:
                shock_front_velocity = KB(range_z, 0.2597, -1.326, 0.3767, 0.0396, -0.0351, 0.00432, 0) * 1000
            else:
                raise ValueError("Scaled-Distance out of range: Change 'neq' or 'distance'")

            all_units = {'neq': 'kg',
                         'distance': 'm',
                         'time_of_arrival': 'ms',
                         'incident_pressure': 'kPa',
                         'reflected_pressure': 'kPa',
                         'positive_phase_duration': 'ms',
                         'incident_impulse': 'kPa-ms',
                         'reflected_impulse': 'kPa-ms',
                         'shock_front_velocity': 'm/s'}

        elif self.unit_system == Units.IMPERIAL:
            # Time of Arrival (ms).
            if 0.2 <= range_z <= 4.5:
                time_of_arrival = KB(range_z, -2.5671, 1.5348, 0.1313, 0.01825, 0.003656, 0.008615, 0) * self.neq**(1/3)
            elif 4.5 < range_z <= 100:
                time_of_arrival = KB(range_z, -1.79097, -0.44021, 2.01409, -0.78101, 0.13045, -0.0081529, 0) * self.neq**(1/3)
            else:
                raise ValueError("Scaled-Distance out of range: Change 'neq' or 'distance'")

            # Incident Pressure (psi).
            if 0.5 <= range_z <= 7.25:
                incident_pressure = KB(range_z, 6.9137, -1.4398, -0.2815, -0.1416, 0.0685, 0, 0)
            elif 7.25 < range_z <= 60:
                incident_pressure = KB(range_z, 8.8035, -3.7001, 0.2709, 0.0733, -0.0127, 0, 0)
            elif 60 < range_z <= 500:
                incident_pressure = KB(range_z, 5.4233, -1.4066, 0, 0, 0, 0, 0)
            else:
                raise ValueError("Scaled-Distance out of range: Change 'neq' or 'distance'")

            # Reflected Pressure (psi).
            if 0.3 <= range_z <= 4:
                reflected_pressure = KB(range_z, 9.0795, -1.7511, -0.2877, -0.2199, -0.0128, 0.0696, -0.0118)
            elif 4 < range_z <= 100:
                reflected_pressure = KB(range_z, 5.1515, 9.15826, -11.85735, 5.56754, -1.33455, 0.16333, -0.008181)
            else:
                raise ValueError("Scaled-Distance out of range: Change 'neq' or 'distance'")

            # Positive Phase Duration (ms).
            if 0.5 <= range_z <= 2.5:
                positive_phase_duration = KB(range_z, -1.7221, 0.45, 1.3552, 1.1249, -0.05773, -0.608, 0) * self.neq**(1/3)
            elif 2.5 < range_z <= 7:
                positive_phase_duration = KB(range_z, -18.7701, 55.0513, -60.4348, 32.0236, -8.3256, 0.8817, 0) * self.neq**(1/3)
            elif 7 < range_z <= 100:
                positive_phase_duration = KB(range_z, -13.0597, 19.7805, -11.2975, 3.2552, -0.4647, 0.02624, 0) * self.neq**(1/3)
            else:
                raise ValueError("Scaled-Distance out of range: Change 'neq' or 'distance'")

            # Incident Impulse (psi-ms).
            if 0.5 <= range_z <= 2.41:
                incident_impulse = KB(range_z, 2.975, -0.466, 0.963, 0.03, -0.087, 0, 0) * self.neq**(1/3)
            elif 2.41 < range_z <= 6:
                incident_impulse = KB(range_z, 0.911, 7.26, -7.459, 2.960, -0.432, 0, 0) * self.neq**(1/3)
            elif 6 < range_z <= 85:
                incident_impulse = KB(range_z, 3.2484, 0.1633, -0.4416, 0.0793, -0.00554, 0, 0) * self.neq**(1/3)
            elif 85 < range_z <= 400:
                incident_impulse = KB(range_z, 4.7702, -1.062, 0, 0, 0, 0, 0) * self.neq**(1/3)
            else:
                raise ValueError("Scaled-Distance out of range: Change 'neq' or 'distance'")

            # Reflected Impulse (psi-ms).
            if 0.2 <= range_z <= 100:
                reflected_impulse = KB(range_z, 5.9313, -1.5622, 0.1322, -0.01123, 0, 0, 0) * self.neq**(1/3)
            else:
                raise ValueError("Scaled-Distance out of range: Change 'neq' or 'distance'")

            # Shock Front Velocity (ft/s).
            if 0.2 <= range_z <= 4.5:
                shock_front_velocity = KB(range_z, 2.13023, -0.69169, -0.11186, -0.0578, 0.0082968, 0.017005, 0) * 1000
            elif 4.5 < range_z <= 100:
                shock_front_velocity = KB(range_z, 3.1767, -2.2283, 0.3537, 0.1059, -0.03892, 0.0033157, 0) * 1000
            else:
                raise ValueError("Scaled-Distance out of range: Change 'neq' or 'distance'")

            all_units = {'neq': 'lb',
                         'distance': 'ft',
                         'time_of_arrival': 'ms',
                         'incident_pressure': 'psi',
                         'reflected_pressure': 'psi',
                         'positive_phase_duration': 'ms',
                         'incident_impulse': 'psi-ms',
                         'reflected_impulse': 'psi-ms',
                         'shock_front_velocity': 'ft/s'}

        else:
            raise Exception("Units Error")

        object.__setattr__(self, 'time_of_arrival', time_of_arrival)
        object.__setattr__(self, 'incident_pressure', incident_pressure)
        object.__setattr__(self, 'reflected_pressure', reflected_pressure)
        object.__setattr__(self, 'positive_phase_duration', positive_phase_duration)
        object.__setattr__(self, 'incident_impulse', incident_impulse)
        object.__setattr__(self, 'reflected_impulse', reflected_impulse)
        object.__setattr__(self, 'shock_front_velocity', shock_front_velocity)
        object.__setattr__(self, 'all_units', all_units)

    def __str__(self):
        return (f"Blast Parameters (Kingery-Bulmash)\n"
                f"NEQ: {self.neq} {self.all_units['neq']}\n"
                f"Distance: {self.distance} {self.all_units['distance']}\n"
                f"Time of Arrival: {round(self.time_of_arrival, 2)} {self.all_units['time_of_arrival']}\n"
                f"Incident Pressure: {round(self.incident_pressure, 2)} {self.all_units['incident_pressure']}\n"
                f"Reflected Pressure: {round(self.reflected_pressure, 2)} {self.all_units['reflected_pressure']}\n"
                f"Positive Phase Duration: {round(self.positive_phase_duration, 2)} {self.all_units['positive_phase_duration']}\n"
                f"Incident Impulse: {round(self.incident_impulse, 2)} {self.all_units['incident_impulse']}\n"
                f"Reflected Impulse: {round(self.reflected_impulse, 2)} {self.all_units['reflected_impulse']}\n"
                f"Shock Front Velocity: {round(self.shock_front_velocity, 2)} {self.all_units['shock_front_velocity']}")

    def to_dict(self) -> dict:
        return {'neq': (self.neq, self.all_units['neq']),
                'distance': (self.distance, self.all_units['distance']),
                'time_of_arrival': (self.time_of_arrival, self.all_units['time_of_arrival']),
                'incident_pressure': (self.incident_pressure, self.all_units['incident_pressure']),
                'reflected_pressure': (self.reflected_pressure, self.all_units['reflected_pressure']),
                'positive_phase_duration': (self.positive_phase_duration, self.all_units['positive_phase_duration']),
                'incident_impulse': (self.incident_impulse, self.all_units['incident_impulse']),
                'reflected_impulse': (self.reflected_impulse, self.all_units['reflected_impulse']),
                'shock_front_velocity': (self.shock_front_velocity, self.all_units['shock_front_velocity'])}


if __name__ == "__main__":
    DIST = 500
    NEQ = 10000
    RES1 = Blast_Parameters(unit_system=Units.METRIC, neq=NEQ, distance=DIST)
    print(RES1)
    print("-"*80)
    res1 = RES1.to_dict()
    print(res1['time_of_arrival'])
    print("-"*80)
    RES2 = Blast_Parameters(unit_system=Units.IMPERIAL, neq=NEQ, distance=DIST)
    print(RES2)
    print("-"*80)