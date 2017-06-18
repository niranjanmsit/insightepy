import os, sys
import logging
import configparser

INI_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../conf/conf.ini')
config = configparser.ConfigParser()
config.read(INI_FILE)

# logger
fmt = '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
LOG_LEVEL = config.get('log', 'level')
log_file = config.get('log', 'log_file')
if log_file.strip() == '':
    logging.basicConfig(format=fmt, datefmt=datefmt, level=LOG_LEVEL)
else:
    logging.basicConfig(format=fmt, datefmt=datefmt, level=LOG_LEVEL, filename=log_file)

logger = logging.getLogger('Conf')

# importing dependencies
dependency_locations = filter(
    lambda d: d != '',
    map(
        lambda d: d.strip(),
        config.get('dependencies', 'locations').split(',')
    )
)
for location in dependency_locations:
    logger.debug('Injecting Dependency: "{}"'.format(location))
    sys.path.append(location)

