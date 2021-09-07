import csv

def save_to_file(jobs):
  file = open("jobs.csv", mode="w", encoding="utf-8", newline="")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "location", "links"])
  for job in jobs:
    writer.writerow(job.values())
  file.close()
  return
