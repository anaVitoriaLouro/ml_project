import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    # Extracting information from the exception traceback
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    # Constructing the error message with script name, line number, and error message
    error_message = "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error))

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call the parent class constructor and store the detailed error message
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        # Override the __str__ method to return the detailed error message
        return self.error_message
