from logger import logger
import csv
from task_extractor.extractor import AdvancedTaskExtractor

def main():
    try:
        with open("data/input.txt", "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        logger.error("Error: input.txt not found. Please create the file and add text.")
        return

    extractor = AdvancedTaskExtractor()
    tasks = extractor.extract_tasks(text)

    try:
        with open("output/output.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ['task', 'entity', 'deadline', 'category', 'processed_task']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for task in tasks:
                writer.writerow(task)
        logger.info("Tasks extracted and saved to output/output.csv")
    except Exception as e:
        logger.error(f"Error writing to CSV: {e}")

if __name__ == "__main__":
    main()
