import pickle


def savepickle(name, object):
    with open(name, "wb") as oFile:
        pickle.dump(object, oFile)


def loadpickle(name):
    with open(name, "rb") as iFile:
        return pickle.load(iFile)


