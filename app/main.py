from scheduler import Scheduler
import time
import logging


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.info("Starting the application")

    scheduler = Scheduler(interval_seconds=3)
    try:
        scheduler.start()
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.stop()

    logging.info("Application finished processing")


if __name__ == "__main__":
    main()
