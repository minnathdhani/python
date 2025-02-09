import psutil
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

THRESHOLD = 80  # CPU usage threshold percentage
CHECK_INTERVAL = 2  # Interval in seconds between checks


def monitor_cpu_usage():
    logging.info("Starting CPU usage monitoring... (Press Ctrl+C to stop)")
    try:
        while True:
            # Get the current CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=1)
            
            # Log and alert if it exceeds the threshold
            if cpu_usage > THRESHOLD:
                logging.warning(f"High CPU usage detected: {cpu_usage}% (Threshold: {THRESHOLD}%)")
            else:
                logging.info(f"CPU usage is at {cpu_usage}%")
            
            # Wait for the next check
            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        logging.info("CPU monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        THRESHOLD = int(input("Enter CPU usage threshold (default 80%): ") or THRESHOLD)
        CHECK_INTERVAL = int(input("Enter check interval in seconds (default 2): ") or CHECK_INTERVAL)
    except ValueError:
        logging.error("Invalid input. Using default threshold and interval values.")

    monitor_cpu_usage()
