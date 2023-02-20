import os
import sys
from typing import List


def getLines(filePath: str):
    return open(filePath).readlines()


def stringStartsWithKeyword(inputString: str, keywords: List[str]):
    return any(inputString.startswith(keyword) for keyword in keywords)


def filterToImportLines(lines: List[str], importKeywords: List[str]):
    return [line for line in lines if stringStartsWithKeyword(line, importKeywords)]


def getDependencyOfSingleImport(importLine: str):
    return importLine.split()[1]


def getDepenencyOfMultipleImport(importLine: str):
    return importLine[7:].strip().replace(' ', '').split(',')


def getDependencyOfFrom(fromLine: str):
    # From import lines contain one library/file name and it is the second token
    return fromLine.split()[1]


def getDependenciesOnLine(line: str):
    dependencies = []
    if line.startswith('from'):
        dependencies.append(getDependencyOfFrom(line))
    elif ',' not in line:
        dependencies.append(getDependencyOfSingleImport(line))
    else:
        dependencies.extend(getDepenencyOfMultipleImport(line))
    return dependencies


def getDependencies(dependencyLines: List[str]):
    dependencies = []

    for dependencyLine in dependencyLines:
        dependencies.extend(getDependenciesOnLine(dependencyLine))

    return dependencies


def getFileDependencies(filePath: str):
    lines = getLines(filePath)
    importLines = filterToImportLines(lines, importKeywords=['import', 'from'])
    dependencies = getDependencies(importLines)
    return dependencies


def isPythonFile(fileName: str):
    return fileName.endswith('.py')


def filterToPythonFiles(fileNames: List[str]):
    return [fileName for fileName in fileNames if isPythonFile(fileName)]


def processDirectory(directoryPath: str):
    data = {}

    pythonFileNames = filterToPythonFiles(os.listdir(directoryPath))

    for pythonFileName in pythonFileNames:
        data[pythonFileName] = getFileDependencies(
            filePath=os.path.join(directoryPath, pythonFileName))

    return data


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Requires one argument, the path to parse')
        sys.exit(-1)

    path = sys.argv[1]
    print(processDirectory(path))
