
import logging

logging.basicConfig(
    filename="program.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

logging.debug("Debugging information")
logging.info("Program execution started")

try:
    a = 10
    b = 0
    result = a / b

except ZeroDivisionError:
    logging.exception("An error occurred")

logging.info("Program execution completed")

print("Check program.log file")
