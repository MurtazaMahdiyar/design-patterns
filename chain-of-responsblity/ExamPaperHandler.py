from abc import ABC, abstractmethod


class iExamPaperHandler(ABC):

    @abstractmethod
    def setNextExamPaperHandler(self, examPaperHandler):
        pass

    @abstractmethod
    def processExamPaper(self, paper):
        pass


class MainExamPaperHandler(iExamPaperHandler):
    nextExamPaperHandler: iExamPaperHandler = None

    def setNextExamPaperHandler(self, examPaperHandler):
        self.nextExamPaperHandler = examPaperHandler

    def processExamPaper(self, paper):
        isFound = False
        key_words = self.keywords()

        if key_words == None:
            isFound = True
        else:
            for keyword in key_words:
                if keyword in paper:
                    isFound = True
                    break

        if isFound:
            self.processExamPaperFinal(paper)
        elif self.nextExamPaperHandler != None:
            self.nextExamPaperHandler.processExamPaper(paper)
        elif isinstance(self.nextExamPaperHandler, DefaultExamPaperHandler):
            self.nextExamPaperHandler.processExamPaperFinal(paper)

    @abstractmethod
    def keywords(self):
        pass

    @abstractmethod
    def processExamPaperFinal(self, paper):
        pass


class DefaultExamPaperHandler(MainExamPaperHandler):
    def keywords(self):
        return {}

    def processExamPaperFinal(self, paper):
        print("Admin group received your Exam-Paper")


class IslamicsExamPaperHandler(MainExamPaperHandler):

    nextExamPaperHandler = DefaultExamPaperHandler()

    def keywords(self):
        return {'IS', 'Islamics'}

    def processExamPaperFinal(self, paper):
        print(f"Exam paper has been recieved by IS-Department.")


class MathExamPaperHandler(MainExamPaperHandler):
    nextExamPaperHandler = DefaultExamPaperHandler()

    def keywords(self):
        return {'math', 'mathematics', 'discrete'}

    def processExamPaperFinal(self, paper):
        print(f"Exam paper has been recieved by Math-Department.")
