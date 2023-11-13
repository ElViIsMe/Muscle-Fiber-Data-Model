# Muscle Data Model

Muskeln sind toll!

## Objects

Sie sind wirklich toll!

### Root

Main reference variables for center of tree-like model structure

<details>
  <summary>Inspect attributes</summary>
  
- muscles
  - Type: Muscle
  - Description: All muscles
  - Multiple: True
- measurements
  - Type: Measurement
  - Description: Type of measurement
  - Multiple: True
</details>

### Muscle

Summary of information on different muscles. 

<details>
  <summary>Inspect attributes</summary>

- name
  - Type: string
  - Description: Name of the muscle

</details>

### Measurement

Different measurement information on muscles

<details>
  <summary>Inspect attributes</summary>

- muscle
  - Type: @Muscle.name
  - Description: The muscle that has been measured
- isometric_measurements
  - Type: Measurement
  - Description: Measurements at same muscle length
  - Multiple: True
- isokinetic_measurements
  - Type: Measurement
  - Description: Measurements with constant muscle movement
  - Multiple: True
- force_length_relationship
  - Type: float
  - Description: Force exerted at different muscle lengths, isometric measurement
  - Multiple: True
- force_velocity_relationship
  - Type: float
  - Description: Force exerted at different contraction velocities, isokinetic measurement
  - Multiple: True
- contraction_history_dependent_effects
  - Type: ContractionHistoryDependentEffects
  - Description: Information on whether (residual) force-enhancement and/or force-depression have been recorded for the respective muscle, combination of isometric and isokinetic measurement
- stretch-shortening cycle
  - Type: StretchShorteningCycle
  - Description: Information on whether data on the stretch-shortening cycle of the respective muscle has been recorded, combination of isometric and isokinetic measurement
- force
  - Type: float
  - Description: Maximum isometric contraction force
- contraction time
  - Type: float
  - Description: contraction time for the different contraction protocolls
- velocity
  - Type: float
  - Description: Maximum isokinetic contraction velocity
- position
  - Type: Position
  - Description: Spatial data on measurement device (e.g. ISOMED)
- live_position
  - Type: Position
  - Description: Live positions deviating from the measurement device through soft-tissue movement
  - Multiple: True
- joint angle
  - Type: float
  - Description: angle of the joint(s) the muscle contracts over
  - Multiple: True
- leverarm
  - Type: float
  - Description: Leverarm of the muscle in [m]
- fiber
  - Type: MuscleFiber
  - Description: Current state of the fiber
- muscle_thickness
  - Type: float
  - Description: Information on the muscle thickness of the respective muscle, for bipenate/segmented muscles information of the different compartments as well as the sum is included
  - Multiple: True
- architectural gearing ratio
  - Type: float
  - Description: Ratio of the contraction velocity of the muscle-tendon-unit over the the contraction velocity of the muscle fascicle

</details>

### ContractionHistoryDependentEffects

<details>
  <summary>Inspect attributes</summary>

- residual force-enhancement
  - Type: float
  - Description: Amount of force-enhancement in % of maximum isometric contraction force measured x seconds after ramp, combination of isometric and isokinetic measurement
- residual force-depression
  - Type: float
  - Description: Amount of force-depression in % of maximum isometric contraction force measured x seconds after ramp, combination of isometric and isokinetic measurement
- force-enhancement
  - Type: float
  - Description: Amount of force-enhancement in % of maximum isometric contraction force at peak
- force-depression
  - Type: float
  - Description: Amount of force-depression in % of maximum isometric contraction force at peak
- range of motion
  - Type: float
  - Description: Range of motion/ramp used for the protocolls
  - Multiple: True
- rampspeed
  - Type: float
  - Description: Speed at which the ramps have been performed in [°/s] or [m/s]

</details>

### StretchShorteningCycle

<details>
  <summary>Inspect attributes</summary>

- SSC
  - Type: float
  - Description: Data on stretch-shortening cycle of the respective muscle

</details>

### Position

Planar position data and joint angle(s)(in case of muscles spanning over multiple joints) of muscle for certain measurement criteria. Depending on future measurements a third axis variable for 3D-measurements should be included.

<details>
  <summary>Inspect attributes</summary>

- x
  - Type: float
  - Description: X-coordinate of the point
- y
  - Type: float
  - Description: X-coordinate of the point
- degree
  - Type: float
  - Description: Degree in relation to zero-position of the foot

</details>

### MuscleFiber

Information on the characteristics of muscle fibres of the respective muscles. Pennation angle should include information of whether their are multiple muscle segements/where and how the angle is measured.

<details>
  <summary>Inspect attributes</summary>

- force
  - Type: float
  - Description: Force of the fiber
- length
  - Type: float
  - Description: Length of the fiber
- pennation_angle
  - Type: {segment: PennationSegment, reference: string, value: float}
  - Description: Angle of pennation

</details>

## Enumerations

### PennationSegment

```python
SURFACE = "surface segment"
DEEP = "deep segment"
```
