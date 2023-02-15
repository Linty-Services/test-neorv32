# this script change sonarqube coverage.xml location from sim folder to the root project folder
# to make sonarqube works , wehave to change the file path accordingly and make it relative
# 
# sonarqube coverage xml schéma is described there https://docs.sonarqube.org/latest/analyzing-source-code/test-coverage/generic-test-data/
# basically we change the attribute path in each file element

from bs4 import BeautifulSoup
from pathlib import Path

def replace_sonarqube_coverage():
    #neorv32 source folder
    Neorv32Folder='neorv32-1.7.8'
    #Vunit sonarqube coverage report file location
    Neorv32CovFile='./coverage.xml'
    #sonarqube target location
    SonarqubeCovFile='../../coverage.xml'


    #get current location
    CurrentPath=Path().resolve()
    print(CurrentPath)
    # identify stage to trim
    ## count number of stage
    StageDir=len(CurrentPath.parts)
    ## remove neorv32/sim in the count 
    StageDir=StageDir-2


    with open(Neorv32CovFile, 'r') as f:
        data = f.read()

    # Passing the stored data inside file
    xml_data = BeautifulSoup(data, "xml")
    for attr in xml_data.select('file'):
        FilePathname=Path(attr['path'])
        FileNewPathname='/'.join(FilePathname.parts[StageDir:])
        print(FileNewPathname)
        attr['path']=FileNewPathname

    with open(SonarqubeCovFile, 'w') as f:
        f.write(str(xml_data.prettify()))
        f.close()
