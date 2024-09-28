# Kingery-Bulmash Blast Wave Characteristics Calculator

Python implementation of the Simplified Kingery Airblast Formulas and Coefficients from: 

> #### Simplified Kingery Airblast Calculations
> Swisdak, Jr, Michael M.  
> NAVAL SURFACE WARFARE CENTER INDIAN HEAD DIV MD  
> 1994 Aug 01  
> Accession Number: [ADA526744](https://apps.dtic.mil/sti/pdfs/ADA526744.pdf)  
> Security Classification: UNCLASSIFIED    

Applicable for TNT equivalent NEQ (Net Explosive Quantity) and hemispherical surface bursts.

## Installation

Using pip to install from [PyPI](https://pypi.org/project/kingery-bulmash/):

```bash
pip install kingery-bulmash
```

## Usage

```python
import kingery_bulmash as kb
```
Use prefix `kb.` to import all required objects. An example for a TNT eqivalent NEQ of 10,000 kg at 500 m:

```python
import kingery_bulmash as kb

# for metric units: 10000kg at 500m
res = kb.Blast_Parameters(unit_system=kb.Units.METRIC, 
                          neq=10000, 
                          distance=500)

print(res)
```
<details>
<summary>Expand to see console output</summary>

```python
Blast Parameters (Kingery-Bulmash)
NEQ: 10000 kg
Distance: 500 m
Time of Arrival: 1276.1650108864796 ms
Incident Pressure: 5.0549639655028455 kPa
Reflected Pressure: 10.244621193146642 kPa
Positive Phase Duration: 133.23344980362697 ms
Incident Impulse: 295.87689480141484 kPa-ms
Reflected Impulse: 1063.0270073779907 kPa-ms
Shock Front Velocity: 347.3295095310771 m/s
```
</details>

## kb.Units

The `kb.Units` *Enum* is how we select the units for the calculation, it needs to be passed to `kb.Blast_Parameters` as either `kb.Units.METRIC` or `kb.Units.IMPERIAL`. 

- `kb.Units.METRIC` 
    > for **neq** in *kg* and **distance**  in *m*.
- `kb.Units.IMPERIAL`
    > for **neq** in *lb* and **distance**  in *ft*.

> [!IMPORTANT]
> The library does not convert between units. Rather, it uses the metric and imperial parameters from the paper directly, therefore there might be slight differences between the results. 

## kb.Blast_Parameters

### ***class*** kb.Blast_Parameters(***unit_system***, ***neq***, ***distance***, ***safe**=True*)

The `Blast_Parameters` *dataclass* calculates all the Kingery-Bulmash parameters from the paper. 

Attributes:

- **unit_system** : ***kb.Units.METRIC*** or ***kb.Units.IMPERIAL***
    > Defines the unit system of the imput and calculated results. See `kb.Units` section [here](#kbUnits).

- **neq**: *float*
    > TNT equivalent net explosive quantity. **kg** or **lb** based on **unit_system**.

- **distance**: *float*
    > Distance from the explosive. **m** or **ft** based on **unit_system**.
 
 - **safe**: *bool, optional*
    > When `True` (default), `kb.Blast_Parameters` will raise a `ValueError` if any *attribute* is out of range. When `False` any *attribute* out of range will be set to `None` without raising a `ValueError`, this allows to significantly expand the range of values for less sensitive attributes. Default is `True`.

> [!TIP]
> `Blast_Parameters` can raise `Exception` and `ValueError`, it is recommended to use `try` and `except` to handle this this behaviour. [Python Errors Tutorial](https://docs.python.org/3/tutorial/errors.html).

\_\_post_init__ attributes:

- **time_of_arrival**: *float, None*
    > Time of arrival in **ms**.
- **incident_pressure**: *float, None*
    > Incident pressure in **kPa** or **psi** based on **unit_system**.
- **reflected_pressure**: *float, None*
    > Reflected pressure in **kPa** or **psi** based on **unit_system**.
- **positive_phase_duration**: *float, None*
    > Positive phase duration in **ms**.
- **incident_impulse**: *float, None*
    > Incident inpulse in **kPa-ms** or **psi-ms** based on **unit_system**.
- **reflected_impulse**: *float, None*
    > Reflected impulse in **kPa-ms** or **psi-ms** based on **unit_system**.
- **shock_front_velocity**: *float, None*
    > Shock front velocity in **m/s** or **ft/s** based on **unit_system**.
- **all_units**: *dict*
    > Dictionary containing *key: value* pairs where the *key* is the attribute name as a `str` and the *value* is the unit as `str`.

Methods:

- **to_dict**()
    > Returns a `dict` representation of the *dataclass*
- **\_\_repr__**()
    > Inherits the default *dataclass* behaviour
- **\_\_str__**()
    > "Pretty" representation of the data as `str`

## Examples:

### Example 1: Single Attribute
```python
import kingery_bulmash as kb

res = kb.Blast_Parameters(unit_system=kb.Units.METRIC, 
                          neq=10000, 
                          distance=500, 
                          safe=True)

#getting only incident pressure
pr = res.incident_pressure

#getting the units of incident pressure
pr_u = res.all_units['incident_pressure']

print(pr, pr_u)
```

<details>
<summary>Expand to see console output</summary>

```python
5.0549639655028455 kPa
```
</details>

### Example 2: Loop Over Range (safe=False)

In this example we set `safe=False` as the range of scaled distances allowed by *incident_impulse* is larger than *shock_front_velocity* which would cause a `ValueError` sooner if `safe=True`. `Try` and `except` used to handle when distance is 0. 

```python
import kingery_bulmash as kb

NEQ = 5000
for dist in range(0, 10000, 1000):
    try:
        RES = kb.Blast_Parameters(unit_system=kb.Units.IMPERIAL,
                                  neq=NEQ,
                                  distance=dist,
                                  safe=False)
        
        i_imp = RES.incident_impulse
        i_imp_u = RES.all_units["incident_impulse"]
        
        print(f'{dist} ft: {i_imp} {i_imp_u}')
    
    except ValueError as err:
        print(f'{dist} ft: {err}')
```

<details>
<summary>Expand to see console output</summary>

```python
0 ft: 'distance' must be > 0.
1000 ft: 26.167261959845302 psi-ms
2000 ft: 12.835212556333252 psi-ms
3000 ft: 8.344381432625331 psi-ms
4000 ft: 6.147651070542891 psi-ms
5000 ft: 4.8505476573514335 psi-ms
6000 ft: 3.99668842429768 psi-ms
7000 ft: None psi-ms
8000 ft: None psi-ms
9000 ft: None psi-ms
```
</details>

## Build/Install/Test From Source

The build-system is [Hatch](https://hatch.pypa.io/latest/).

To build and install from source, clone the repository and in the root folder run:
```bash
hatch build
```
To install with pip, also from the root folder, run:

```bash
pip install dist\kingery_bulmash-X.X.X-py3-none-any.whl
```
Adjust the file name/path accordingly.

To run tests:

```bash
hatch test
```
