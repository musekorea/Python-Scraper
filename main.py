from indeed import extract_job_indeed
from stack import extract_job_stack
from save_jobs import save_to_file

jobs_indeed = extract_job_indeed()
jobs_stack = extract_job_stack()
jobs = jobs_indeed+jobs_stack

save_to_file(jobs)