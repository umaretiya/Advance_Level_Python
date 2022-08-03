# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging

extData = {
    "user": "keshav@example.com",
}

def main():
    # TODO: Use basicConfig to configure logging
    logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode="w")
    # Try out each of the log levels
    logging.debug("This is a debug message")
    logging.info("This is a info message")
    logging.warning("This is a warning message")
    logging.error("This is a error message")
    logging.critical("This is a critical message")

    # TODO: Output formatted strings to the log
    logging.info("Here is a {} variable and an int:".format('string', 10))

def anotherFunction():
    logging.debug("This is a debug-level message", extra=extData)


def customized_logging():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output_custom.log",
                        level=logging.DEBUG, filemode="w", format=fmtstr, datefmt=datestr)

    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)
    anotherFunction()


if __name__ == "__main__":
    customized_logging()
