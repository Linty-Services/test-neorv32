* Cloned from https://github.com/stnolting/neorv32 v1.7.8 (28 nov 2022)
* Only the following files were kept: rtl/core and rtl/processor_templates/neorv32_ProcessorTop_UP5KDemo.vhd
* In core/neorv32_cpu.vhd, the following two lines have been commented out:
    * `assert not (PMP_NUM_REGIONS > 0) report "NEORV32 CPU CONFIG NOTE: Implementing ...`
    * `assert not ((CPU_EXTENSION_RISCV_Zihpm = true) and (HPM_NUM_CNTS > 0)) report "NEORV32 CPU ...`
* build.ys file added
* linty/bugfinder aanalysis available on : https://sonar.linty-services.com/dashboard?id=TEST_NEORV32