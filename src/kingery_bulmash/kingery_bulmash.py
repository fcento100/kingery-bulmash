# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 23:24:29 2024

@author: fcento
"""

from dataclasses import dataclass
from enum import Enum, auto
from math import exp, log


class Units(Enum):
    METRIC = auto()
    IMPERIAL = auto()


@dataclass
class Value:
    value: float
    unit: str


@dataclass
class Blast_Parameters:
    unit_system: Units
    neq: Value
    distance: Value
    range_z: Value
    time_of_arrival: Value
    incident_pressure: Value
    reflected_pressure: Value
    positive_phase_duration: Value
    incident_impulse: Value
    reflected_impulse: Value
    shock_front_velocity: Value

    def __str__(self):
        return (f"Distance: {round(self.distance.value, 2)} {self.distance.unit}\n"
                f"NEQ: {round(self.neq.value, 2)} {self.neq.unit}\n"
                f"Range: {round(self.range_z.value, 2)} {self.range_z.unit}\n"
                f"Time of Arrival: {round(self.time_of_arrival.value, 2)} {self.time_of_arrival.unit}\n"
                f"Incident Pressure: {round(self.incident_pressure.value, 2)} {self.incident_pressure.unit}\n"
                f"Reflected Pressure: {round(self.reflected_pressure.value, 2)} {self.reflected_pressure.unit}\n"
                f"Positive Phase Duration: {round(self.positive_phase_duration.value, 2)} {self.positive_phase_duration.unit}\n"
                f"Incident Impulse: {round(self.incident_impulse.value, 2)} {self.incident_impulse.unit}\n"
                f"Reflected Impulse: {round(self.reflected_impulse.value, 2)} {self.reflected_impulse.unit}\n"
                f"Shock Front Velocity: {round(self.shock_front_velocity.value, 2)} {self.shock_front_velocity.unit}\n")


def RANGE_Z(distance: float, mass: float) -> float:
    """
    Calculate the Range (Z) in distance/mass^(1/3).

    Parameters
    ----------
    distance : float
        distance (m) or (ft).
    mass : float
        mass in (kg) or (lb).

    Returns
    -------
    float
        Range in distance/mass^(1/3).

    """
    return distance/mass**(1/3)


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

    Parameters
    ----------
    Z : float
        Scaled Distance.
    A : float
        param A.
    B : float
        param B.
    C : float
        param C.
    D : float
        param D.
    E : float
        param E.
    F : float
        param F.
    G : float
        param G.

    Returns
    -------
    float
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


def TOA(Z: float, units: Units) -> tuple[float | None, Exception | None]:
    """
    Time of Arrival (ms/kg^1/3) or (ms/lb^1/3).

    Parameters
    ----------
    Z : float
        Range Z in (m/kg^1/3) or (ft/lb^1/3).
    units : Units
        Units Enum (metric/imperial).

    Returns
    -------
    Float | None
        Returns Time of Arrival or None.
    Error | None
        Returns an Error or None.
    """

    if units == Units.METRIC:
        if 0.06 <= Z <= 1.50:
            return KB(Z, -0.7604, 1.8058, 0.1257, -0.0437, -0.0310, -0.00669, 0), None
        elif 1.50 < Z <= 40:
            return KB(Z, -0.7137, 1.5732, 0.5561, -0.4213, 0.1054, -0.00929, 0), None
        else:
            return None, Exception("Range (Z), Out of Bounds")
    elif units == Units.IMPERIAL:
        if 0.2 <= Z <= 4.5:
            return KB(Z, -2.5671, 1.5348, 0.1313, 0.01825, 0.003656, 0.008615, 0), None
        elif 4.5 < Z <= 100:
            return KB(Z, -1.79097, -0.44021, 2.01409, -0.78101, 0.13045, -0.0081529, 0), None
        else:
            return None, Exception("Range (Z), Out of Bounds")
    else:
        return None, Exception("Unknown Units")


def PI(Z: float, units: Units) -> tuple[float | None, Exception | None]:
    """
    Incident Pressure (kPa) or (psi).

    Parameters
    ----------
    Z : float
        Range Z in (m/kg^1/3) or (ft/lb^1/3).
    units : Units
        Units Enum (metric/imperial).

    Returns
    -------
    Float | None
        Returns Incident Pressure or None.
    Error | None
        Returns an Error or None.
    """

    if units == Units.METRIC:
        if 0.2 <= Z <= 2.9:
            return KB(Z, 7.2106, -2.1069, -0.3229, 0.1117, 0.0685, 0, 0), None
        elif 2.9 < Z <= 23.8:
            return KB(Z, 7.5938, -3.0523, 0.40977, 0.0261, -0.01267, 0, 0), None
        elif 23.8 < Z <= 198.5:
            return KB(Z, 6.0536, -1.4066, 0, 0, 0, 0, 0), None
        else:
            return None, Exception("Range (Z), Out of Bounds")
    elif units == Units.IMPERIAL:
        if 0.5 <= Z <= 7.25:
            return KB(Z, 6.9137, -1.4398, -0.2815, -0.1416, 0.0685, 0, 0), None
        elif 7.25 < Z <= 60:
            return KB(Z, 8.8035, -3.7001, 0.2709, 0.0733, -0.0127, 0, 0), None
        elif 60 < Z <= 500:
            return KB(Z, 5.4233, -1.4066, 0, 0, 0, 0, 0), None
        else:
            return None, Exception("Range (Z), Out of Bounds")
    else:
        return None, Exception("Unknown Units")


def PR(Z: float, units: Units) -> tuple[float | None, Exception | None]:
    """
    Reflected Pressure (kPa) or (psi).

    Parameters
    ----------
    Z : float
        Range Z in (m/kg^1/3) or (ft/lb^1/3).
    units : Units
        Units Enum (metric/imperial).

    Returns
    -------
    Float | None
        Returns Reflected Pressure or None.
    Error | None
        Returns an Error or None.
    """

    if units == Units.METRIC:
        if 0.06 <= Z <= 2.00:
            return KB(Z, 9.006, -2.6893, -0.6295, 0.1011, 0.29255, 0.13505, 0.019736), None
        elif 2.00 < Z <= 40:
            return KB(Z, 8.8396, -1.733, -2.64, 2.293, -0.8232, 0.14247, -0.0099), None
        else:
            return None, Exception("Range (Z), Out of Bounds")
    elif units == Units.IMPERIAL:
        if 0.3 <= Z <= 4:
            return KB(Z, 9.0795, -1.7511, -0.2877, -0.2199, -0.0128, 0.0696, -0.0118), None
        elif 4 < Z <= 100:
            return KB(Z, 5.1515, 9.15826, -11.85735, 5.56754, -1.33455, 0.16333, -0.008181), None
        else:
            return None, Exception("Range (Z), Out of Bounds")
    else:
        return None, Exception("Unknown Units")


def PPD(Z: float, units: Units) -> tuple[float | None, Exception | None]:
    """
    Positive Phase Duration (ms/kg^1/3) or (ms/lb^1/3).

    Parameters
    ----------
    Z : float
        Range Z in (m/kg^1/3) or (ft/lb^1/3).
    units : Units
        Units Enum (metric/imperial).

    Returns
    -------
    Float | None
        Returns Positive Phase Duration or None.
    Error | None
        Returns an Error or None.
    """

    if units == Units.METRIC:
        if 0.2 <= Z <= 1.02:
            return KB(Z, 0.5426, 3.2299, -1.5931, -5.9667, -4.0815, -0.9149, 0), None
        elif 1.02 < Z <= 2.8:
            return KB(Z, 0.5440, 2.7082, -9.7354, 14.3425, -9.7791, 2.8535, 0), None
        elif 2.8 < Z <= 40:
            return KB(Z, -2.4608, 7.1639, -5.6215, 2.2711, -0.44994, 0.03486, 0), None
        else:
            return None, Exception("Range (Z), Out of Bounds")
    elif units == Units.IMPERIAL:
        if 0.5 <= Z <= 2.5:
            return KB(Z, -1.7221, 0.45, 1.3552, 1.1249, -0.05773, -0.608, 0), None
        elif 2.5 < Z <= 7:
            return KB(Z, -18.7701, 55.0513, -60.4348, 32.0236, -8.3256, 0.8817, 0), None
        elif 7 < Z <= 100:
            return KB(Z, -13.0597, 19.7805, -11.2975, 3.2552, -0.4647, 0.02624, 0), None
        else:
            return None, Exception("Range (Z), Out of Bounds")
    else:
        return None, Exception("Unknown Units")


def II(Z: float, units: Units) -> tuple[float | None, Exception | None]:
    """
    Incident Impulse (kPa-ms/kg^1/3) or (psi-ms/lb^1/3).

    Parameters
    ----------
    Z : float
        Range Z in (m/kg^1/3) or (ft/lb^1/3).
    units : Units
        Units Enum (metric/imperial).

    Returns
    -------
    Float | None
        Incident Impulse or None.
    Error | None
        Returns an Error or None.
    """

    if units == Units.METRIC:
        if 0.2 <= Z <= 0.96:
            return KB(Z, 5.522, 1.117, 0.6, -0.292, -0.087, 0, 0), None
        elif 0.96 < Z <= 2.38:
            return KB(Z, 5.465, -0.308, -1.464, 1.362, -0.432, 0, 0), None
        elif 2.38 < Z <= 33.7:
            return KB(Z, 5.2749, -0.4677, -0.2499, 0.0588, -0.00554, 0, 0), None
        elif 33.7 < Z <= 158.7:
            return KB(Z, 5.9825, -1.062, 0, 0, 0, 0, 0), None
        else:
            return None, Exception("Range (Z), Out of Bounds")
    elif units == Units.IMPERIAL:
        if 0.5 <= Z <= 2.41:
            return KB(Z, 2.975, -0.466, 0.963, 0.03, -0.087, 0, 0), None
        elif 2.41 < Z <= 6:
            return KB(Z, 0.911, 7.26, -7.459, 2.960, -0.432, 0, 0), None
        elif 6 < Z <= 85:
            return KB(Z, 3.2484, 0.1633, -0.4416, 0.0793, -0.00554, 0, 0), None
        elif 85 < Z <= 400:
            return KB(Z, 4.7702, -1.062, 0, 0, 0, 0, 0), None
        else:
            return None, Exception("Range (Z), Out of Bounds")
    else:
        return None, Exception("Unknown Units")


def IR(Z: float, units: Units) -> tuple[float | None, Exception | None]:
    """
    Reflected Impulse (kPa-ms/kg^1/3) or (psi-ms/lb^1/3).

    Parameters
    ----------
    Z : float
        Range Z in (m/kg^1/3) or (ft/lb^1/3).
    units : Units
        Units Enum (metric/imperial).

    Returns
    -------
    Float | None
        Reflected Impulse or None.
    Error | None
        Returns an Error or None.
    """

    if units == Units.METRIC:
        if 0.06 <= Z <= 40:
            return KB(Z, 6.7853, -1.3466, 0.101, 0.01123, 0, 0, 0), None
        else:
            return None, Exception("Range (Z), Out of Bounds")
    elif units == Units.IMPERIAL:
        if 0.2 <= Z <= 100:
            return KB(Z, 5.9313, -1.5622, 0.1322, -0.01123, 0, 0, 0), None
        else:
            return None, Exception("Range (Z), Out of Bounds")
    else:
        return None, Exception("Unknown Units")


def SFV(Z: float, units: Units) -> tuple[float | None, Exception | None]:
    """
    Shock Front Velocity (m/s) or (ft/s).

    Parameters
    ----------
    Z : float
        Range Z in (m/kg^1/3) or (ft/lb^1/3).
    units : Units
        Units Enum (metric/imperial).

    Returns
    -------
    Float | None
        Returns Shock front Velocity or None.
    Error | None
        Returns an Error or None.
    """

    if units == Units.METRIC:
        if 0.06 <= Z <= 1.50:
            return KB(Z, 0.1794, -0.956, -0.0866, 0.109, 0.0699, 0.01218, 0)*1000, None
        elif 1.50 < Z <= 40:
            return KB(Z, 0.2597, -1.326, 0.3767, 0.0396, -0.0351, 0.00432, 0)*1000, None
        else:
            return None, Exception("Range (Z), Out of Bounds")

    elif units == Units.IMPERIAL:
        if 0.2 <= Z <= 4.5:
            return KB(Z, 2.13023, -0.69169, -0.11186, -0.0578, 0.0082968, 0.017005, 0)*1000, None
        elif 4.5 < Z <= 100:
            return KB(Z, 3.1767, -2.2283, 0.3537, 0.1059, -0.03892, 0.0033157, 0)*1000, None
        else:
            return None, Exception("Range (Z), Out of Bounds")
    else:
        return None, Exception("Unknown Units")


def CALCULATE_KB(dist:float, mass: float, units: Units) -> tuple[Blast_Parameters | None, Exception | None]:
    """
    Calculate the Kingery-Bulmash Parameters for Hemispherical Surface Burst

    Parameters
    ----------
    dist : float
        distance.
    mass : float
        NET explosive quantity of Equivalent TNT.
    units : Units
        METRIC/IMPERIAL.

    Returns
    -------
    Blast_Parameters | None
        Returns Blast_Parameters of None if error.
    Exception | None
        Returns the exception if error or None.

    """
   
    z = RANGE_Z(dist, mass)
    res_list = [TOA(z, units),
                PI(z, units),
                PR(z, units),
                PPD(z, units),
                II(z, units),
                IR(z, units),
                SFV(z, units)]

    for res in res_list:
        try:
            assert res[1] is None
        except:
            return None, res[1]

    if units == Units.METRIC:
        return Blast_Parameters(*(units,
                          Value(*(mass, "kg")),
                          Value(*(dist, "m")),
                          Value(*(z, "m/kg^1/3")),
                          Value(*(res_list[0][0] * mass**(1/3), "ms")),
                          Value(*(res_list[1][0], "kPa")),
                          Value(*(res_list[2][0], "kPa")),
                          Value(*(res_list[3][0] * mass**(1/3), "ms")),
                          Value(*(res_list[4][0] * mass**(1/3), "kPa-ms")),
                          Value(*(res_list[5][0] * mass**(1/3), "kPa-ms")),
                          Value(*(res_list[6][0], "m/s")))), None
    elif units == Units.IMPERIAL:
        return Blast_Parameters(*(units,
                          Value(*(mass, "lb")),
                          Value(*(dist, "ft")),
                          Value(*(z, "ft/lb^1/3")),
                          Value(*(res_list[0][0] * mass**(1/3), "ms")),
                          Value(*(res_list[1][0], "psi")),
                          Value(*(res_list[2][0], "psi")),
                          Value(*(res_list[3][0] * mass**(1/3), "ms")),
                          Value(*(res_list[4][0] * mass**(1/3), "psi-ms")),
                          Value(*(res_list[5][0] * mass**(1/3), "psi-ms")),
                          Value(*(res_list[6][0], "ft/s")))), None
    else:
        return None, Exception("Unknown Units")


def get_results(dist, mass, units):
    res, err = CALCULATE_KB(dist, mass, units)
    
    if err is not None:
        raise err
    else:
        return res

if __name__ == "__main__":
    DIST = 500
    NEQ = 10000
    res = get_results(DIST, NEQ, Units.METRIC)
    print(res)
