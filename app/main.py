from scheduler import Scheduler
import time
import logging

INTERVAL_SECONDS = 3
SLEEP_SECONDS = 1


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.info("Starting the application")

    scheduler = Scheduler(INTERVAL_SECONDS)
    try:
        scheduler.start()
        while True:
            time.sleep(SLEEP_SECONDS)
    except (KeyboardInterrupt, SystemExit):
        scheduler.stop()

    logging.info("Application finished processing")


if __name__ == "__main__":
    main()
