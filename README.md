# Kingery-Bulmash 1984 Blast Parameters Calculator

This implementation in python follows the original unclassified paper: 
>**Simplified Kingery Airblast Calculations**, Aug 1994

It is applicable for TNT equivalent NEQs and hemispherical surface bursts.

### Installation

Using pip:

```bash
pip install kingery-bulmash
```

### Usage

The `Blast_Parameters` dataclass calculates all the parameters on creation. Three *field*s are required to create the ***dataclass***:

> `Units` (Enum): `Units.METRIC` or `Units.IMPERIAL`, defines the unit system.

>`neq`(float): TNT equivalent quantity in **kg** or **lb** depending on the `Units` of the first *field*.

>`distance` (float): Distance from the explosive in **m** or **ft**  depending on the `Units` of the first *field*.

Example Metric usage:

```python
import kingery_bulmash as kb

# for metric units: 10000kg at 500m
res_metric = kb.Blast_Parameters(
    unit_system=kb.Units.METRIC, neq=10000, distance=500)

print(res_metric)
```
Prints:

```bash
Blast Parameters (Kingery-Bulmash)
NEQ: 10000 kg
Distance: 500 m
Time of Arrival: 1276.17 ms
Incident Pressure: 5.05 kPa
Reflected Pressure: 10.24 kPa
Positive Phase Duration: 133.23 ms
Incident Impulse: 295.88 kPa-ms
Reflected Impulse: 1063.03 kPa-ms
Shock Front Velocity: 347.33 m/s
```

> [!NOTE]
> The *fields* are rounded to 2 decimal places when printing (except for neq and distance). Extraction of the raw output will be shown further down.

Alternatively `kb.` can be omitted by changing the way the library is imported. For example (also using imperial units):

```python
from kingery_bulmash import Units, Blast_Parameters

# for imperial units: 5000 lb at 300 ft
res_imperial = Blast_Parameters(
    unit_system = Units.IMPERIAL, neq=5000, distance=300)

print(res_imperial)
```

Prints:

```bash
Blast Parameters (Kingery-Bulmash)
NEQ: 5000 lb
Distance: 300 ft
Time of Arrival: 175.43 ms
Incident Pressure: 3.65 psi
Reflected Pressure: 8.0 psi
Positive Phase Duration: 55.98 ms
Incident Impulse: 83.3 psi-ms
Reflected Impulse: 166.67 psi-ms
Shock Front Velocity: 1226.43 ft/s
```

The following *field*s are available in the `Blast_Parameters` ***dataclass***: 

```
unit_system
neq
distance
time_of_arrival
incident_pressure
reflected_pressure
positive_phase_duration
incident_impulse
reflected_impulse
shock_front_velocity
all_units
```

If for example, only the `incident_pressure` is required, it can be extracted as such:

```python
from kingery_bulmash import Units, Blast_Parameters

res = Blast_Parameters(
    unit_system=Units.METRIC, neq=10000, distance=500)

#getting the incident pressure
incident_pr = res.incident_pressure

#getting the units of incident pressure
incident_pr_units = res.all_units['incident_pressure']

#printing both incident pressure and the units
print(incident_pr, incident_pr_units)
```

Prints:

```python
5.0549639655028455 kPa
```

The results can also be extracted as a ***dict*** for convenince with the `to_dict()` class method. Each ***dict*** *key* represents a `Blast_Parameters` *field* while the ***dict*** *value* is a ***tuple*** containing the *field* value and its unit as ***str*** for convenience. 

An example is provided below:

```python
from kingery_bulmash import Units, Blast_Parameters

res = Blast_Parameters(
    unit_system=Units.METRIC, neq=10000, distance=500)

print(res.to_dict())
```

Prints:

```python
{'neq': (10000, 'kg'), 'distance': (500, 'm'), 'time_of_arrival': (1276.1650108864796, 'ms'), 'incident_pressure': (5.0549639655028455, 'kPa'), 'reflected_pressure': (10.244621193146642, 'kPa'), 'positive_phase_duration': (133.23344980362697, 'ms'), 'incident_impulse': (295.87689480141484, 'kPa-ms'), 'reflected_impulse': (1063.0270073779907, 'kPa-ms'), 'shock_front_velocity': (347.3295095310771, 'm/s')}
```

> [!TIP]
> As `Blast_Parameters` is a ***dataclass***, the special method `__repr__` is available:

```python
print(res.__repr__())
```

Prints:

```python
Blast_Parameters(unit_system=<Units.METRIC: 1>, neq=10000, distance=500, time_of_arrival=1276.1650108864796, incident_pressure=5.0549639655028455, reflected_pressure=10.244621193146642, positive_phase_duration=133.23344980362697, incident_impulse=295.87689480141484, reflected_impulse=1063.0270073779907, shock_front_velocity=347.3295095310771, all_units={'neq': 'kg', 'distance': 'm', 'time_of_arrival': 'ms', 'incident_pressure': 'kPa', 'reflected_pressure': 'kPa', 'positive_phase_duration': 'ms', 'incident_impulse': 'kPa-ms', 'reflected_impulse': 'kPa-ms', 'shock_front_velocity': 'm/s'})
```