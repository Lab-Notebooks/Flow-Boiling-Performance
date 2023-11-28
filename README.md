## Computational Enviroment for Deploying Production-Ready Three-Dimensional Flow Boiling Simulations

The corresponding data repository is hosted here:
- https://anl.box.com/s/crqngvtj7t4dvgys6iag3f5xg3suc852

For instructions on how to use the notebook please see the README for these repositories:
- https://github.com/Lab-Notebooks/Outflow-Forcing-BubbleML
- https://github.com/akashdhruv/Jobrunner

### Quickstart

- Install Jobrunner, `pip install pyjobrunner`, make sure your pip points to python3 installer

- Create a new site for your machine under `sites/<your-sites>` and create `Makefile.h` and `environment.sh`
  specific to that site. You can copy files under existing and edit them. Make sure you have MPI and HDF5
  available 

- Configure your experiment by running `./configure -s <your-site>`

- Build software stack `jobrunner setup software/amrex software/flashkit software/flashx`

- Setup an experiment using `jobrunner setup simulation/FlowBoiling/<experiment-name>`. `Example2D` is a lightweight
  two-dimensional simulations and `Example3D` and `WeakScaling` are production 3D simulations

- Run the experiment using `jobrunner submit simulation/FlowBoiling/<experiment-name>`. Edit the `Jobfile` in root directory
  to set schedular specific options or just `bash` if you want to run it interactively.

- You can postprocess results using `flashkit`. See the instructions here: https://github.com/Lab-Notebooks/Outflow-Forcing-BubbleML

### Performance results 

- October, 2023: The intial tests (https://github.com/Lab-Notebooks/Flow-Boiling-Performance/blob/main/analysis/performance/profile-oct-2023.ipynb) showed that
  communication time during guard-cell filling dominated the performance. Also the re-nucleation algorithm scaled poorly due to linear search that was being performed
  over all nucleation sites. This lead to developments on the Flash-X side to enable masked guard-cell filling. Re-evaluation of the performance
  (https://github.com/Lab-Notebooks/Flow-Boiling-Performance/blob/main/analysis/performance/profile-oct-2023-gc-optimized.ipynb) resulted in reduced communication time

- November, 2023: Futher improvements in performance were achieved by tweaking runtime parameters and avoiding conditional statements in Amrex/Grid_fillGuardCells. The
  renucleation algorithm was also optimized (https://github.com/Lab-Notebooks/Flow-Boiling-Performance/blob/main/analysis/performance/profile-nov-2023.ipynb)


<p align="center"> <img src="analysis/performance/performance.gif" width="1500" style="border:none;background:none;"/> </p>

### Citation

```
@software{akash_dhruv_2023_10211775,
  author       = {Akash Dhruv},
  title        = {{Lab-Notebooks/Flow-Boiling-Performance: zenodo 
                   archive}},
  month        = nov,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {zenodo},
  doi          = {10.5281/zenodo.10211775},
  url          = {https://doi.org/10.5281/zenodo.10211775}
}
```
