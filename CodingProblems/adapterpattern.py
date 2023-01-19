class phoneCameraApp:

    def __init__(self):
        shareAlgo = shareAlgorithmInterface()

    def take(self):
        pass
    def edit(self):
        pass
    def save(self):
        pass
    def setShareAlgo(self):
        pass
    def performShare(self):
        pass

class basicCameraApp(phoneCameraApp):

    def __init__(self):
        super.__init__(self,)
    def edit(self):
        pass

class cameraPlusApp(phoneCameraApp):

    def __init__(Self):
        super.__init__(self,)
    def edit(self):
        pass

import abc   ##Formal interface defintion where implementation of abstract methods are enforced
# formally using a class in module 'abc' called AbstractBaseClasses(or ABC)
class shareAlgorithmInterface(abc.ABC):

    @abc.abstractmethod
    def share(self):
        pass
    
class shareByEmail(shareAlgorithmInterface):

    def share(self):

class shareByText(shareAlgorithmInterface):

    def share(self):

class shareBySocialmedia(shareAlgorithmInterface):

    def share(self):

        
