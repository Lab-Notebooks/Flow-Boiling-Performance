import numpy
from types import SimpleNamespace


def console(title, namespace):
    print(f"\n{title}")
    print(f'{" "*2}- {namespace.blocks} Blocks')
    print(f'{" "*2}- {namespace.procs} MPI ranks')
    print(f'{" "*2}- {int(namespace.blocks/namespace.procs)} Blocks Per Rank')
    print(f'{" "*2}- Volume {namespace.lx}x{namespace.ly}x{namespace.lz} mm\u00b3')
    print(
        f'{" "*2}- {namespace.nxb*namespace.nyb*namespace.nzb*namespace.blocks} Points'
    )
    print(f'{" "*2}- Resolution {namespace.resolution} mm')
    print(f'{" "*2}- Physical Time {namespace.simtime} ms')
    print(f'{" "*2}- Wall Time {round(namespace.walltime_hours,1)} hours')


length_scale_mm = 1
time_scale_mm = 10

summit25 = SimpleNamespace(
    blocks=10000,
    procs=1050,
    resolution=0.03 * length_scale_mm,
    simtime=2 * time_scale_mm,
    walltime_hours=8,
    nxb=16,
    nyb=16,
    nzb=16,
    lx=50 * length_scale_mm,
    ly=5 * length_scale_mm,
    lz=5 * length_scale_mm,
)

summit12 = SimpleNamespace(
    blocks=4800,
    procs=504,
    resolution=0.03 * length_scale_mm,
    simtime=0.5 * time_scale_mm,
    walltime_hours=2,
    nxb=16,
    nyb=16,
    nzb=16,
    lx=24 * length_scale_mm,
    ly=5 * length_scale_mm,
    lz=5 * length_scale_mm,
)

summit05 = SimpleNamespace(
    blocks=2000,
    procs=210,
    resolution=0.03 * length_scale_mm,
    simtime=0.5 * time_scale_mm,
    walltime_hours=2,
    nxb=16,
    nyb=16,
    nzb=16,
    lx=10 * length_scale_mm,
    ly=5 * length_scale_mm,
    lz=5 * length_scale_mm,
)


hpc3 = SimpleNamespace(
    blocks=1000,
    procs=40,
    resolution=0.05 * length_scale_mm,
    simtime=1 * time_scale_mm,
    walltime_hours=(20000 / 60) / 60,
    nxb=10,
    nyb=10,
    nzb=10,
    lx=5 * length_scale_mm,
    ly=5 * length_scale_mm,
    lz=5 * length_scale_mm,
)

console("Flow Boiling Run on SUMMIT 25 Nodes", summit25)
console("Flow Boiling Run on SUMMIT 12 Nodes", summit12)
console("Flow Boiling Run on SUMMIT 5 Nodes", summit05)
console("Pool Boiling Run on HPC3", hpc3)
print("\n")
