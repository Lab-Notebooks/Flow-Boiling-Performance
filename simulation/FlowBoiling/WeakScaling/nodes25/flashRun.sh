if [[ $SiteName == "summit" ]]; then

	echo Running on $SiteName

	stdbuf -o0 jsrun -n ${NRS} \
		-r ${NRS_PER_NODE} \
		-a ${NMPI_PER_RS} \
		-c ${NCORES_PER_RS} \
		-b packed:${NCORES_PER_MPI} \
		-d packed \
		./job.target
else

	echo Running on $SiteName
	mpirun ./job.target
fi
