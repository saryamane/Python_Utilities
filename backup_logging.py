import zipfile
import sys
import os
import logging

logging.basicConfig(filename='file_ex.log', level = logging.DEBUG)

logging.info("checking to see if the backup.zip exists")

if os.path.exists('backup.zip'):
	logging.info("backup exists")
try:
	zip_zipfile = zipfile.ZipFile('backup.zip', 'a')
except:
	err = sys.exc_info()
	logging.error("unable to open backup.zip in append mode")
	logging.error("error num: " + str(err[1].args[0]))
	logging.error("error msg: " + err[1].args[1])
	sys.exit()
else:
	logging.info("creating backup.zip")

	try:
		zip_file = zipfile.ZipFile('backup.zip', 'w')
	except:
		err = sys.exc_info()
		logging.error("unable to create backup.zip")
		logging.error("error num: " + str(err[1].args[0]))
		logging.error("error msg: " + err[1].args[1])
		sys.exit()

logging.info("adding code to backup.zip")

try:
	zip_file.write('test.txt', 'test.txt', zipfile.ZIP_DEFLATED)
except:
	err = sys.exc_info()
	logging.error("failed to add code to backup.zip")
	logging.error("error num: " + str(err[1].args[1]))

zip_file.close()
