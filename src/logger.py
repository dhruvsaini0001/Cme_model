import logging
import os
from datetime import datetime

# Create a logs directory and a timestamped log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def main() -> str:
    """Write a test INFO log entry and return the log file path."""
    logging.info("Logging has started")
    return LOG_FILE_PATH


if __name__ == "__main__":
    path = main()
    print(f"Wrote log to: {path}")