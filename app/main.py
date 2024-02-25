from scheduler import Scheduler
import time

def main():
    scheduler = Scheduler(interval_seconds=3) 
    try:
        scheduler.start()
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.stop()

if __name__ == "__main__":
    main()
