import logging

class InvalidmarksError(Exception):
    pass
def check_marks(marks):
    if marks <0 or marks >100:
        raise InvalidmarksError("marks must be between 0 and 100")
try :
    check_marks(120)
except InvalidmarksError as e:
    logging.error(e)
