from ExamPaperHandler import IslamicsExamPaperHandler, MathExamPaperHandler


def processExamPaper(email):
    islamics = IslamicsExamPaperHandler()
    math = MathExamPaperHandler()

    islamics.nextExamPaperHandler = math
    islamics.processExamPaper(email)


if __name__ == '__main__':
    email = input("email: \n")
    processExamPaper(email)
