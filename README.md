# LoggerIO
Basic logger like logging.Logger

# Creating Instance

logger = LoggerIO()

log: LoggerIO = logger.log(message = "Created instance!", level=LogLevels.INFO)

log.log(message = "Deleted instance!", level = LogLevels.WARN, io_mode = "w")

> LoggerIO.log returns LoggerIO instance with current stdout buffer.
