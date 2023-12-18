import logging 

class Logger:
	def __init__(self,file_name,log_file):
		self.log_file_name = log_file 
		self.logger = logging.getLogger(file_name)
		self.logger.setLevel('DEBUG')
		self.formatter = logging.Formatter('%(asctime)s: %(levelname)s:%(name)s:%(message)s')
		self.file_handler = logging.FileHandler(self.log_file_name)
		self.file_handler.setFormatter(self.formatter)
		self.logger.addHandler(self.file_handler)

	def info(self,msg):
		self.logger.info(msg)

	def error(self,msg):
		self.logger.error(msg)

	def warning(self,msg):
		self.logger.warning(msg)

	def critical(self,msg):
		self.logger.critical(msg)
		
	def debug(self,msg)
		self.logger.debug(msg)
