## FlowBoiling 3D simulation performance

There are at total of 100 x 10 x 10 = 10000 blocks in the simulation.
Performance run on summit used 25 nodes with 42 processes per node resulting 
in 1050 processes.

Scaling parameters:
- length scale: 1mm
- velocity scale: 0.1 m/s
- time scale: 10 milliseconds

Performance metrics:

- time per iteration: 1 second wall time
- simulation start time: 4. 
- simulation end time: 6.
- wall time: 2+2+2+2 = 8 hours
- node hours: 25*(wall time) = 200 node-hours 
- physical time: 20 milliseconds

Length scales:
- Domain: 50 mm x 5 mm x 5mm = 5 cm x 0.5 cm x 0.5 cm
- Grid spacing: 0.031 mm = 31 micrometers
- Nucleation radius: 0.1 mm = 100 micrometers

## simulation/FlowBoiling/Example3D/jobnode.archive/2023-07-19/images/flow_boiling.gif

- 60 milliseconds, 24 hours of wall time
- 2.5 millisecond/hour
