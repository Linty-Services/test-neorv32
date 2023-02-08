#!/opt/NanoXplore/nxmap/nxdesignsuite-22.3.0.2/bin/nxpython3
from nxpython import *
import glob
import os

intial_path=os.getcwd()

p = createProject('buildNX')
p.setVariantName('NG-MEDIUM')
p.setTopCellName('neorv32_ProcessorTop_UP5KDemo')


#
p.addFile('neorv32','../core/neorv32_application_image.vhd')
p.addFile('neorv32','../core/neorv32_bootloader_image.vhd')
p.addFile('neorv32','../core/neorv32_boot_rom.vhd')
p.addFile('neorv32','../core/neorv32_bus_keeper.vhd')
p.addFile('neorv32','../core/neorv32_busswitch.vhd')
p.addFile('neorv32','../core/neorv32_cfs.vhd')
p.addFile('neorv32','../core/neorv32_cpu_alu.vhd')
p.addFile('neorv32','../core/neorv32_cpu_bus.vhd')
p.addFile('neorv32','../core/neorv32_cpu_control.vhd')
p.addFile('neorv32','../core/neorv32_cpu_cp_bitmanip.vhd')
p.addFile('neorv32','../core/neorv32_cpu_cp_cfu.vhd')
p.addFile('neorv32','../core/neorv32_cpu_cp_fpu.vhd')
p.addFile('neorv32','../core/neorv32_cpu_cp_muldiv.vhd')
p.addFile('neorv32','../core/neorv32_cpu_cp_shifter.vhd')
p.addFile('neorv32','../core/neorv32_cpu_decompressor.vhd')
p.addFile('neorv32','../core/neorv32_cpu_regfile.vhd')
p.addFile('neorv32','../core/neorv32_cpu.vhd')
p.addFile('neorv32','../core/neorv32_debug_dm.vhd')
p.addFile('neorv32','../core/neorv32_debug_dtm.vhd')
p.addFile('neorv32','../core/neorv32_dmem.entity.vhd')
p.addFile('neorv32','../core/neorv32_fifo.vhd')
p.addFile('neorv32','../core/neorv32_gpio.vhd')
p.addFile('neorv32','../core/neorv32_gptmr.vhd')
p.addFile('neorv32','../core/neorv32_icache.vhd')
p.addFile('neorv32','../core/neorv32_imem.entity.vhd')
p.addFile('neorv32','../core/neorv32_mtime.vhd')
p.addFile('neorv32','../core/neorv32_neoled.vhd')
p.addFile('neorv32','../core/neorv32_onewire.vhd')
p.addFile('neorv32','../core/neorv32_package.vhd')
p.addFile('neorv32','../core/neorv32_pwm.vhd')
p.addFile('neorv32','../core/neorv32_slink.vhd')
p.addFile('neorv32','../core/neorv32_spi.vhd')
p.addFile('neorv32','../core/neorv32_sysinfo.vhd')
p.addFile('neorv32','../core/neorv32_top.vhd')
p.addFile('neorv32','../core/neorv32_trng.vhd')
p.addFile('neorv32','../core/neorv32_twi.vhd')
p.addFile('neorv32','../core/neorv32_uart.vhd')
p.addFile('neorv32','../core/neorv32_wdt.vhd')
p.addFile('neorv32','../core/neorv32_wishbone.vhd')
p.addFile('neorv32','../core/neorv32_xip.vhd')
p.addFile('neorv32','../core/neorv32_xirq.vhd')
p.addFile('neorv32','../core/mem/neorv32_dmem.default.vhd')
p.addFile('neorv32','../core/mem/neorv32_imem.default.vhd')

p.addFile('../processor_templates/neorv32_ProcessorTop_UP5KDemo.vhd')



##########################################PROJECT SYNTHESIZE########################################
p.synthesize()
 
############################################PROJECT PLACE###########################################
p.place()
############################################PROJECT ROUTE###########################################
p.route()

############################################PROJECT REPORT##########################################
p.reportInstances()
############################################TIMING ANALYSIS#########################################

#Bestcase
#Timing_analysis = p.createAnalyzer()
#Timing_analysis.launch({'conditions': 'bestcase', 'maximumSlack': 500, 'searchPathsLimit': 10})
#standard
Timing_analysis = p.createAnalyzer()
Timing_analysis.launch({'conditions': 'typical', 'maximumSlack': 500, 'searchPathsLimit': 10})
#Worstcase
#Timing_analysis = p.createAnalyzer()
#Timing_analysis.launch({'conditions': 'worstcase', 'maximumSlack': 500, 'searchPathsLimit': 10})

##########################################BISTREAM GENERATION#######################################


################################################SUMMARY#############################################
print('Errors: ', getErrorCount())
print('Warnings: ', getWarningCount())
printText('Design successfully generated')


################################################export measures#######################################
#go back to project root folder
os.chdir(intial_path)

import json

# Open JSON file
f = open('buildNX/buildNX/logsPython/hierarchy.json')

# returns JSON object as
# a dictionary
data = json.load(f)

count4Lut = data['m_moduleCollection'][0]['contentReport']['count4Lut']
countXLut = data['m_moduleCollection'][0]['contentReport']['countXLut']
countDff = data['m_moduleCollection'][0]['contentReport']['countDff']
count1Cy = data['m_moduleCollection'][0]['contentReport']['count1Cy']
countRegFileBlock = data['m_moduleCollection'][0]['contentReport']['countRegFileBlock']
countCrossDomainClock = data['m_moduleCollection'][0]['contentReport']['countCrossDomainClock']
countClockBuffer = data['m_moduleCollection'][0]['contentReport']['countClockBuffer']
countClockSwitch = data['m_moduleCollection'][0]['contentReport']['countClockSwitch']
countDsp = data['m_moduleCollection'][0]['contentReport']['countDsp']
countMemBlock = data['m_moduleCollection'][0]['contentReport']['countMemBlock']
countWfg = data['m_moduleCollection'][0]['contentReport']['countWfg']
countPll = data['m_moduleCollection'][0]['contentReport']['countPll']
# Closing file
f.close()

f_target=open('measures.json', "w") 

measures = '{"NX_4LUT":' + str(count4Lut) + ','\
    '"NX_XLUT":'         + str(countXLut) +',' \
    '"NX_DFF":'          + str(countDff) + ','\
    '"NX_Carry":'        + str(count1Cy) + ','\
    '"NX_RFB":'          + str(countRegFileBlock) + ','\
    '"NX_CDC":'          + str(countCrossDomainClock) + ','\
    '"NX_CB":'           + str(countClockBuffer) + ','\
    '"NX_CS":'           + str(countClockSwitch) + ','\
    '"NX_DSP":'          + str(countDsp) +',' \
    '"NX_MB":'           + str(countMemBlock) + ','\
    '"NX_WFG":'          + str(countWfg) + ','\
    '"NX_PLL":'          + str(countPll)+ ','  \
    '"NX_Log_Remarks":'  + str(getRemarkCount())+  ','\
    '"NX_Log_Warnings":'  + str(getWarningCount())+  ','\
    '"NX_Log_Errors":'  + str(getErrorCount())+  \
    '}'
f_target.write(measures)
f_target.close() 