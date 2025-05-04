import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_, exc_tb=error_details.exc_info()
        
        # while raising custom exception we will pass sys as arg,
        # in that we will find below information in clean.
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        
    def __str__(self):
        return " Error occured in python script name [{0}] line number [{1}] error_message [{2}]".format(
        self.file,self.lineno,str(self.error_message))
    
if __name__=='__main__':
    try: 
        logger.logging.info("Enter the try block")
        a=1999/0
    except Exception as e :
        logger.logging.info("This will not be printed",e)
        raise NetworkSecurityException(e,sys)