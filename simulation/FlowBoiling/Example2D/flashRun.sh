# chdir into working directory
cd $JobWorkDir

if [ $Profile = True ]; then
	echo Running on $SiteName with HPC TooKit Profiler
	mpirun hpcrun -ds -t -e CYCLES -e CACHE-MISSES $JobWorkDir/job.target
else
	echo Running on $SiteName
	mpirun $JobWorkDir/job.target
fi
