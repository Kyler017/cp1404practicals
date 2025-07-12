from project import Project
from datetime import datetime


def load_projects(filename):
    projects_collection = []
    with open(filename, 'r') as input_file_handle:
        next(input_file_handle)
        for data_line in input_file_handle:
            name, start_date, priority, cost, completion = data_line.strip().split('\t')
            projects_collection.append(Project(name, start_date, int(priority), float(cost), int(completion)))
    return projects_collection


