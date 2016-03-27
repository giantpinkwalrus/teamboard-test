import robot as rob

#Where are the scripts located, !!! trailing slash is important !!!
scriptLocation = "../robotTests/"
#   testFile - testFile to run
#   args - robotframework arguments, can be string or []
def runTest(testFile, args=''):
    response = rob.run(scriptLocation+testFile)
    success = (response == 0)
    return success