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


def save_projects(filename, projects):
    output_file = open(filename, 'w')
    output_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
    for project_instance in projects:
        output_file.write(
            f"{project_instance.name}\t{project_instance.start_date}\t{project_instance.priority}\t{project_instance.cost_estimate}\t{project_instance.completion_percentage}\n")


