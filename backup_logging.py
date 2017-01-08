import zipfile
import sys
import os
import logging

# Setting the basic configuration settings for the logging detail level.
logging.basicConfig(filename='file_ex.log', level = logging.DEBUG,
		   format = '%(asctime)s - %(levelname)s: %(message)s')

# Info log to check if the file already exists
logging.info("checking to see if the backup.zip exists")

if os.path.exists('backup.zip'):
	logging.info("backup exists")
	try:
		# Opening the already existant file in an append mode.
		zip_zipfile = zipfile.ZipFile('backup.zip', 'a')
	except:
		# Capture the error into err, which we are going to parse to a much readable format.
		err = sys.exc_info()
		logging.error("unable to open backup.zip in append mode")
		logging.error("error num: " + str(err[1].args[0]))
		logging.error("error msg: " + err[1].args[1])
		sys.exit()
else:
	# Now that the backup file does not exists, lets log to create one.
	logging.info("creating backup.zip")

	try:
		# Open the backup file in a write format.
		zip_file = zipfile.ZipFile('backup.zip', 'w')
	except:
		# Same boilerplate code we saw above with the error capturing
		err = sys.exc_info()
		logging.error("unable to create backup.zip")
		logging.error("error num: " + str(err[1].args[0]))
		logging.error("error msg: " + err[1].args[1])
		sys.exit()

# Now let's try to add the file to the backup.zip
logging.info("adding code to backup.zip")

try:
	# zipfile.ZIP_DEFLATED if not used, then the files into the backup.zip will be left uncompressed.
	zip_file.write('test.txt', 'test.txt', zipfile.ZIP_DEFLATED)
except:
	err = sys.exc_info()
	logging.error("failed to add code to backup.zip")
	logging.error("error num: " + str(err[1].args[1]))

# In the end we close the zipped file handler, and we are done.
zip_file.close()
