# Muscle Data Model

Muskeln sind toll!

## Objects

Aute duis do ad non laboris. Quis aliqua cillum ullamco do aute dolor incididunt. Sint sit mollit voluptate deserunt consectetur. Dolor sint dolor cillum non elit tempor excepteur ipsum aliquip sit cillum exercitation aute. Aliquip quis Lorem dolore qui ullamco ipsum culpa nisi anim. Nulla magna anim qui sint et Lorem quis ut nulla. Occaecat amet nulla ea id reprehenderit deserunt sit veniam.

### Root

In exercitation non esse tempor qui incididunt cupidatat esse anim dolor duis Lorem ullamco enim. Incididunt enim do labore pariatur aliquip proident elit nostrud dolore laboris labore ad tempor ad. Labore duis exercitation adipisicing velit id ea eiusmod aliquip enim ullamco.

<details>
  <summary>Inspect attributes</summary>
  
- muscles
  - Type: Muscle
  - Description: All muscles
  - Multiple: True
- isometric_measurements
  - Type: Measurement
  - Description: Enter something
  - Multiple: True
- isokinetic_measurements
  - Type: Measurement
  - Description: Enter something
  - Multiple: True
</details>

### Muscle

Nostrud amet incididunt est veniam aliqua mollit voluptate sint. Incididunt non deserunt tempor aute labore tempor duis magna ad culpa. Incididunt ea qui veniam duis aliqua enim exercitation ea. Culpa officia ipsum in aliqua reprehenderit eu sunt quis incididunt veniam irure sunt. Nostrud velit laborum quis mollit adipisicing fugiat exercitation deserunt adipisicing magna. Id cupidatat minim anim minim minim nostrud.

<details>
  <summary>Inspect attributes</summary>

- name
  - Type: string
  - Description: Name of the muscle
- isometric_measurements
  - Type: Measurement
  - Description: Measurements with regard to the muscle
- isokinetic_measurements
  - Type: Measurement
  - Description: Measurements with regard to the muscle
</details>

### Measurement

In cupidatat mollit ipsum mollit. Do reprehenderit minim consequat mollit sit ad incididunt. Irure ullamco qui nulla consequat duis sit veniam. Nulla cupidatat enim pariatur mollit aliqua commodo deserunt non enim qui tempor est excepteur labore. Ex aliqua minim eu id laboris.

<details>
  <summary>Inspect attributes</summary>

- force
  - Type: float
  - Description: Contraction force
- velocity
  - Type: float
  - Description: Contraction velocity
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
</details>

### Position

Mollit quis proident nisi magna. Exercitation excepteur eu amet est ex reprehenderit ullamco ipsum occaecat do ut. Commodo magna anim laborum nostrud aute id ipsum velit laborum. Eiusmod qui sunt laborum elit dolor incididunt est commodo eu sint labore culpa officia. Ex laboris excepteur ad duis reprehenderit consectetur amet.

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

Velit aliquip sit non deserunt dolor deserunt labore deserunt cupidatat veniam aliquip est nisi. Sit fugiat do voluptate cupidatat amet aute sint. Est Lorem duis sint est deserunt eiusmod ad duis officia. Incididunt nulla proident sint duis nulla cupidatat cillum proident. Do ad consectetur cupidatat pariatur laborum. Eiusmod labore dolor mollit nisi do dolore ad amet. Id laborum aliqua enim pariatur tempor culpa adipisicing ad aliquip.

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
