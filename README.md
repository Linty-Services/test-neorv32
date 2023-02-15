* Cloned from https://github.com/stnolting/neorv32 v1.7.8 (28 nov 2022)
* Only the following files were kept: rtl/core and rtl/processor_templates/neorv32_ProcessorTop_UP5KDemo.vhd
* In core/neorv32_cpu.vhd, the following two lines have been commented out:
    * `assert not (PMP_NUM_REGIONS > 0) report "NEORV32 CPU CONFIG NOTE: Implementing ...`
    * `assert not ((CPU_EXTENSION_RISCV_Zihpm = true) and (HPM_NUM_CNTS > 0)) report "NEORV32 CPU ...`
  To apply patch execute : `patch -u ./neorv32/rtl/core/neorv32_cpu.vhd -i neorv32_cpu.vhd.patch `
* sim/run.py have been modified to enable coverage with sonarqube xml output in Vunit tests
  To apply modification execute (in the project root folder) : `patch -u ./neorv32/sim/run.py -i run.py.patch `
* build.ys file added
* linty/bugfinder analysis available on : https://sonar.linty-services.com/dashboard?id=TEST_NEORV32 

# sonarqube importation
to scan the project use command :
```
sonar-scanner -Dsonar.sources=. -Dsonar.projectKey=TEST_NEORV32 -Dsonar.host.url=https://sonar.linty-services.com -Dsonar.login=<token> -Dsonar.vhdl.topLevelEntity=neorv32_ProcessorTop_UP5KDemo -Dsonar.coverageReportPaths=./coverage.xml

```

# coverage
## GHDL coverage support
GHDL can support coverage with the help of GCC backend with gcov. 
To enable this feature you have to recompile GHDL with the official [procedure](https://ghdl.github.io/ghdl/development/building/GCC.html#build-gcc) or applie the one below if you are running Ubuntu 22.04.1 LTS (change gcc version to yours if not). The new `ghdl` application will be installed in `/opt/ghdl`. Do not forget to add it to the path with command `export PATH=/opt/ghdl/bin:$PATH` to replace your previous `ghdl version` by this one for the test.

```bash
$ sudo apt-get install gnat build-essential libmpc-dev flex bison libz-dev lcov gcc-11-source texinfo gcovr
$ git clone https://github.com/ghdl/ghdl.git
$ cd /usr/src/gcc-11
$ sudo tar xvf gcc-11.3.0.tar.xz 
$ cd gcc-11.3.0
$ ./contrib/download_prerequisites 
$ cd ghdl 
$ mdir build
$ cd build
$ ../configure --with-gcc=/usr/src/gcc-11/gcc-11.3.0 --prefix=/opt/ghdl
$ make copy-sources
$ mkdir gcc-objs; cd gcc-objs
$ /usr/src/gcc-11/gcc-11.3.0/configure  --prefix=/opt/ghdl --enable-languages=c,vhdl --disable-bootstrap --disable-lto --disable-multilib --disable-libssp --disable-libgomp --disable-libquadmath --enable-default-pie
$ make -j4 && make install MAKEINFO=true
$ cd ..
$ make ghdllib
$ make install
```

GHDL-gcc support version automatically pack the coverage support.   you can use : 

- docker version [fedora36-gcc-11.3.0](https://hub.docker.com/layers/ghdl/ghdl/fedora36-gcc-11.3.0/images/sha256-f7815c67368365533e97ae4202a2cfdad81550247ad9c20c427e8b6a800a73f2?context=explore) from GHDL docker hub.

- or daily binaires [ghdl-gha-ubuntu-22.04-gcc.tgz](https://github.com/ghdl/ghdl/releases/download/nightly/ghdl-gha-ubuntu-22.04-gcc.tgz) from ghdl but be careful with GCC version ( even if I was running on ubuntu 22.04 I got a library error `libgcov profiling error:./ghdl-coverage-master/projects/adder/adder.gcda:Version mismatch - expected 11.3 (release) (B13*) got 11.2 (release) (B12*)` trying to execute it).

## neorv32 coverage

### prerequisite
- Install:
    - VUnit with `pip install vunit_hdl`
    - ghdl gcc backend for coverage support
    - gcovr with `pip install gcovr`
    - xml python library `pip install beautifulsoup4`
- Set GHDL up in the path with `export PATH=<ghdl/bin/path>:$PATH`
- set GHDL as default simulator : `VUNIT_SIMULATOR=ghdl`

### Run
- execute `run.py` in the `neorv32-1.7.8/sim/` 
- wait for at least 20 Minutes (there is no feed back in the terminal execept at the end of simulation)
- the `coverage.xml` file will be created at the root of the project.


# NX occupation measures

## prerequisites
install `impulse` software from NanoXplore with the licence server.

## Run
execute `nxpython3 build.nxmap.py` fromthe root of the project. A `measures.json` file should be created at the root of the project.

