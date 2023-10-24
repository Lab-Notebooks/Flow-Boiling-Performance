# Source the spack environment file
. /home/akash/spack/share/spack/setup-env.sh

# Load hpc toolkit profiler
spack load hpctoolkit@2023.03.01%gcc@12.3.0
export HPC_TOOLKIT_HOME=$(which hpcrun | sed s/'\/bin\/hpcrun'//)

# Load MPI module. This should be available as standard module on a cluster.
# If not, build your own MPI and update PATH, LD_LIBRARY_PATH
spack load openmpi@4.1.5/qjohmjm%gcc@12.3.0

# Set MPI_HOME by quering path loaded by site module
export MPI_HOME=$(which mpicc | sed s/'\/bin\/mpicc'//)

# Load HDF5 module in desired configuration if available. If not specified
# the HDF5 will be built when setting up software
spack load hdf5@1.14.2/uz6gtx4%gcc@12.3.0

# Path to parallel HDF5 installtion with fortran support
export HDF5_HOME=$(which h5pfc | sed s/'\/bin\/h5pfc'//)

# Load required python packages from spack
spack load py-toml%gcc@12.3.0
spack load py-numpy%gcc@12.3.0
spack load py-scipy%gcc@12.3.0
spack load py-h5py%gcc@12.3.0
