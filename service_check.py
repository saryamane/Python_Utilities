import subprocess
import logging
import sys

# This script will take the service name as the input parameter.

svc = str(sys.argv[1])

# Let's set the format of the logging format.

logging.basicConfig(filename = 'service_check.log', 
					level = logging.DEBUG,
					format = '%(asctime)s - %(levelname)s: %(message)s')

logging.info('Checking if the process' + svc + 'is running')

# call method takes the array of strings to build the command itself.
service_is_running = subprocess.call(["ps", "-C", svc])

if service_is_running == 1:
	# This means something went wrong.
	logging.warning('Process: ' + svc + 'is not running')
	logging.info('Attempting to restart: ' + svc)
	restart_sts = subprocess.call(["sudo", "/etc/init.d/%s" %svc, "start"])
	if restart_sts == 1:
		# this means that the restart has failed, when we tried to.
		logging.error("Unable to restart %s, please check the logs" %svc)
	else:
		# restart worked
		logging.info("%s sucessfully restarted" %svc)
else:
	logging.info("%s is currently running" %svc)
