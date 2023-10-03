import os


class LogDict:
    """
    Base class for logfile dictionaries
    """

    def __init__(self, logFile):
        """
        Initialization method

        Argument
        --------
        logFile : full path to `.log` file
        """
        # Create an empty dictionary
        # object for logfile entries
        self._logDict = {}

        # Call internal method to parse
        # logfile and populate dictionary
        self._setLogDict(logFile)

    def __getitem__(self, timerKey):
        """
        Internal getter, this done to enforce that
        contents of dictionary are read-only

        Arguments
        ---------
        timerKey : key for the timer entry
        """
        return self._logDict[timerKey]

    def __repr__(self):
        """
        Internal representation method to display
        dictionary contents
        """
        return f"{self._logDict}"

    @staticmethod
    def _fileToList(filePath):
        """
        Static method to convert a file to a list of lines

        Arguments
        ---------
        filePath: string (name of file - full path)

        Returns
        -------
        fileList: list of lines
        """
        # Create an empty list
        # to populate as the file is passed
        fileList = []

        # Open the input file in read-only mode
        with open(filePath, "r") as workingFile:

            # loop over lines
            # in working file
            for line in workingFile:

                # append to
                # file list
                fileList.append(line.strip())

        return fileList

    def _setLogDict(self, logFile):
        """
        Internal method to set logfile dictionary

        Arguments
        ---------
        logFile : path to logfile
        """
        pass

    def keys(self):
        """
        return keys
        """
        return self._logDict.keys()


class FlashLogDict(LogDict):
    """
    Class to handle dictionary of Flash-X logfile entries
    """

    def __init__(self, logFile, stats=False, process=False):
        """
        Initialization method

        Argument
        --------
        logFile : full path to `.log` file
        """
        self.stats = stats
        self.process = process
        super().__init__(logFile)

    def _setLogDict(self, logFile):
        """
        Internal method to set logfile dictionary

        Arguments
        ---------
        logFile : path to logfile
        """
        # convert file to a list
        logList = self.__class__._fileToList(logFile)

        # Create empty lists for
        # parsing data from `logList`
        #
        # `accountingIndex` : list to store index of desired line
        #
        # `dashedIndex` : list to store indices of ------- lines
        #
        # `equalToIndex`  : list to store indices of ======= lines
        accountingIndex = []
        dashedIndex = []
        equalToIndex = []

        # list of reference keys to probe
        # FIXME: Need to use different logic based on how log file is
        #        structured to get different fields
        if self.stats:
            accountingList = ["max/proc", "min/proc", "avg/proc", "num calls"]
        elif self.process:
            accountingList = ["time sec"]
        else:
            raise ValueError("Set either stats or process to True")

        # enumerate line and index and get locations
        # for markers defining the boundaries of
        # datasets that need to extracted
        for index, line in enumerate(logList):
            if all(keyword in line for keyword in accountingList):
                accountingIndex.append(index)
            if "-----------------------------" in line:
                dashedIndex.append(index)
            if "==============================" in line:
                equalToIndex.append(index)

        # create a bound list to store
        # bounds of desired datasets
        boundList = []

        # loop over accountingIndex and append
        # bounds
        for index in accountingIndex:
            boundList.append(
                [
                    min([i for i in dashedIndex if index < i]) + 1,
                    min([i for i in equalToIndex if index < i]) - 1,
                ]
            )

        # Check length of the line index
        # this to enforce only one entry exists
        # for the desired fields
        if len(boundList) > 1:
            raise ValueError("[logDict] Unrecognized Logfile")

        # loop over bounds and get desired data
        for bound in boundList:

            # extract key and values
            for index in range(bound[0], bound[1] + 1):

                # extract and update accounting_dict
                timerKey = " ".join(logList[index].split()[:-4])

                # Create a value list in proper data format
                if self.stats:
                    valueList = [
                        float(value) for value in logList[index].split()[-4:-1]
                    ]
                    valueList.append(int(logList[index].split()[-1]))

                elif self.process:
                    valueList = [float(logList[index].split()[-4])]

                # Map valueList to a dictionary
                valueDict = {
                    key: value for key, value in zip(accountingList, valueList)
                }

                self._logDict.update({timerKey: valueDict})

        # Deal with `.log.csv` containing
        # data from multiple processors.
        # Start with an empty list to deal with exceptions
        csvList = []

        # check if csv path exists and
        # convert file to a list
        if os.path.exists(logFile + ".csv"):
            csvList = self.__class__._fileToList(logFile + ".csv")

        # iterate over each entry from csvList
        for csvEntry in csvList:

            # extract timer key
            timerKey = csvEntry.split(",")[0]

            # extract timer level
            timerLevel = int(csvEntry.split(",")[2])

            # extract values
            valueList = [float(value) for value in csvEntry.split(",")[3:]]

            # Blank dictionary
            valueDict = {}

            # Map valueList to a dictionary
            valueDict["all procs"] = valueList

            # Extract level of the timer
            valueDict["level"] = timerLevel

            # Update log dicitonary
            self._logDict[timerKey].update(valueDict)


class AmrexLogDict(LogDict):
    """
    Class to handle AMReX logfile dictionary
    """

    def __init__(self, logFile):
        """
        Initialization method

        Argument
        --------
        logFile : full path to amrex log file
        """
        super().__init__(logFile)

    def _setLogDict(self, logFile):
        """
        Internal method to set logfile dictionary

        Arguments
        ---------
        logFile : path to logfile
        """
        # convert file to a list
        logList = self.__class__._fileToList(logFile)

        # Create empty lists for
        # parsing data from `logList`
        #
        # `accountingIndex` : list to store index of desired line
        #
        # `dashedIndex` : list to store indices of ------- lines
        accountingIndex = []
        dashedIndex = []

        # list of reference keys to probe
        accountingList = ["NCalls", "Incl. Min", "Incl. Avg", "Incl. Max", "Max %"]

        # enumerate line and index and get locations
        # for markers defining the boundaries of
        # datasets that need to extracted
        for index, line in enumerate(logList):
            if all(keyword in line for keyword in accountingList):
                accountingIndex.append(index)
            if "-----------------------------" in line:
                dashedIndex.append(index)

        # create a bound list to store
        # bounds of desired datasets
        boundList = []

        # loop over accountingIndex and append
        # bounds
        for index in accountingIndex:
            boundListMin = min([i for i in dashedIndex if index < i]) + 1
            boundListMax = min([i for i in dashedIndex if boundListMin < i]) - 1
            boundList.append([boundListMin, boundListMax])

        # Check length of the line index
        # this to enforce only one entry exists
        # for the desired fields
        if len(boundList) > 1:
            raise ValueError("[logDict] Unrecognized Logfile")

        # loop over bounds and get desired data
        for bound in boundList:

            # extract key and values
            for index in range(bound[0], bound[1] + 1):

                # extract and update accounting_dict
                timerKey = " ".join(logList[index].split()[:-5]).split("()")[0]

                # Create a value list in proper data format
                valueList = [int(logList[index].split()[1])]
                valueList.extend(
                    [float(value) for value in logList[index].split()[-4:-1]]
                )
                valueList.append(float(logList[index].split()[-1].split("%")[0]))

                # Map valueList to a dictionary
                valueDict = {
                    key: value for key, value in zip(accountingList, valueList)
                }

                self._logDict.update({timerKey: valueDict})
