def checkIfScss (inputFileName: str) -> bool:
    """Checks if inputFileName is a SCSS file.
    """
    splitAtPeriods = inputFileName.split (".")

    return splitAtPeriods[len (splitAtPeriods) - 1].lower () == "scss"


def getNameWithoutScssExtension (inputFileName: str) -> str:
    """Returns the string of the input file name without the extension.
    """
    if "scss" not in inputFileName.lower ():
        return inputFileName

    splitAtPeriods = inputFileName.split (".")
    scssRemovedList = splitAtPeriods [:len (splitAtPeriods) - 1]
    return ".".join (scssRemovedList)
