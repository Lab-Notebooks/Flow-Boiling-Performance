# cache the value of current working directory

FlashOptions="incompFlow/FlowBoiling -auto -maxblocks=100 -2d -nxb=16 -nyb=16 \
              +amrex +parallelIO -site=$SiteHome SimForceInOut=True IOWriteGridFiles=True"

if [ $Profile = True ]; then
	FlashOptions="$FlashOptions +hpctoolkit"
fi
