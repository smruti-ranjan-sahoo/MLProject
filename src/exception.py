import sys
import logging

def error_message_details(error,error_detail:sys):
    """
    This function takes an error and its details and returns a formatted string with the error message.
    """
    
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        """
        This function initializes the CustomException class with an error message and its details.
        """
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)
    def __str__(self):
        return self.error_message
    