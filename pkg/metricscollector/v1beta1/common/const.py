# Default value for interval between running processes check
DEFAULT_POLL_INTERVAL = 1
# Default value for timeout before invoke error during running processes check
DEFAULT_TIMEOUT = 0
# Default value whether wait for all other main process of container exiting
DEFAULT_WAIT_ALL_PROCESSES = "True"
# Default value for directory where TF event metrics are reported
DEFAULT_METRICS_FILE_DIR = "/log"
# Job finished marker in $$$$.pid file when main process is completed
TRAINING_COMPLETED = "completed"

# UnavailableMetricValue is the value in the DB
# when metrics collector can't parse objective metric from the training logs.
UNAVAILABLE_METRIC_VALUE = "unavailable"
