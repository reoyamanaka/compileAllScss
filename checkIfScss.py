def checkIfScss (inputFileName: str) -> bool:
    """Checks if inputFileName is a SCSS file.
    """
    splitAtPeriods = inputFileName.split (".")

    return splitAtPeriods[len (splitAtPeriods) - 1].lower () == "scss"
