### Setting up IO compression

### Setup flag

```
+hdf5zfp
```

### Makefile

```
SZ_PATH    = /gpfs/alpine/csc300/world-shared/gnu_build/SZ/install
SZ3_PATH   = /gpfs/alpine/csc300/world-shared/gnu_build/SZ3/build/install
ZFP_PATH   = /gpfs/alpine/csc300/world-shared/gnu_build/zfp-0.5.5
H5Z_PATH   = /gpfs/alpine/csc300/world-shared/gnu_build/H5Z-ZFP-0.5.5/install

FFLAGS_SZ    = -I${SZ_PATH}/include
FFLAGS_SZ3   = -I${SZ3_PATH}/include
FFLAGS_ZFP   = -I${ZFP_PATH}/include -I${H5Z_PATH}/include

CFLAGS_SZ    = -I${SZ_PATH}/include
CFLAGS_SZ3   = -I${SZ3_PATH}/include
CFLAGS_ZFP   = -I${ZFP_PATH}/include -I${H5Z_PATH}/include

LIB_SZ    = -L${SZ_PATH}/lib -L${SZ_PATH}/lib64 -DFLASH_HDF5_SZ -lSZ -lhdf5sz -Wl,-rpath,${SZ_PATH}/lib -Wl,-rpath,${SZ_PATH}/lib64
LIB_SZ3   = -L${SZ3_PATH}/lib -L${SZ3_PATH}/lib64 -DFLASH_HDF5_SZ3 -lhdf5sz3 -Wl,-rpath,${SZ3_PATH}/lib -Wl,-rpath,${SZ3_PATH}/lib64
LIB_ZFP   = -L${ZFP_PATH}/lib64 -DFLASH_HDF5_ZFP -L${H5Z_PATH}/lib -lh5zzfp -lzfp -Wl,-rpath,${ZFP_PATH}/lib64 -Wl,-rpath,${H5Z_PATH}/lib
```

### Parfile variables

```
zfp_reversible=1
zfp_accuracy_plt=0.00001
```

OR

```
zfp_accuracy=0.00001
zfp_accuracy_plt=0.00001
```

### Environment flag during runtime

```
export ROMIO_HINTS=<path-to-hints-file>
```

<hints-file>

```
romio_ds_write enable
romio_cb_read enable
cb_buffer_size 16777216
cb_nodes 4
cb_config_list *:1
```
