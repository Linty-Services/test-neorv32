#!/opt/NanoXplore/nxmap/nxdesignsuite-22.3.0.2/bin/nxpython3
from nxpython import *
import glob
import os

intial_path=os.getcwd()

p = createProject('buildNX')
p.setVariantName('NG-MEDIUM')


file_list = glob.glob("../neorv32/rtl/core/*.vhd")
p.addFiles('neorv32',file_list)
file_list = glob.glob("../neorv32/rtl/core/mem/*.vhd")
p.addFiles('neorv32',file_list)
p.addFile('../neorv32/rtl/processor_templates/neorv32_ProcessorTop_UP5KDemo.vhd')

p.setTopCellName('neorv32_ProcessorTop_UP5KDemo')

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