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
- force
  - Type: float
  - Description: Maximum isometric contraction force
- velocity
  - Type: float
  - Description: Maximum isokinetic contraction velocity
- position
  - Type: Position
  - Description: Spatial data
- live_position
  - Type: Position
  - Description: Live positions
  - Multiple: True
- fiber
  - Type: MuscleFiber
  - Description: Current state of the fiber
- muscle_thickness
  - Type: float
  - Description: Information on the muscle thickness of the respective muscle, for bipenate/segmented muscles information of the different compartments as well as the sum is included
  - Multiple: True

</details>

### ContractionHistoryDependentEffects

- residual force-enhancement
  - Type: float
  - Description: Amount of force-enhancement in % of maximum isometric contraction force, combination of isometric and isokinetic measurement
- residual force-depression
  - Type: float
  - Description: Amount of force-depression in % of maximum isometric contraction force, combination of isometric and isokinetic measurement

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
  - Type: float
  - Description: Angle of pennation
  - Min: 0
  - Max: 89
</details>
