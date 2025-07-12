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


def display_projects(projects):
    incomplete_projects_list = [p for p in projects if not p.is_complete()]
    completed_projects_list = [p for p in projects if p.is_complete()]
    incomplete_projects_list.sort()
    completed_projects_list.sort()
    print("Incomplete projects: ")
    for current_project in incomplete_projects_list:
        print(
            f"  {current_project.name}, start: {current_project.start_date}, priority {current_project.priority}, estimate: ${current_project.cost_estimate:.2f}, completion: {current_project.completion_percentage}%")
    print("Completed projects: ")
    for another_project in completed_projects_list:
        print(
            f"  {another_project.name}, start: {another_project.start_date}, priority {another_project.priority}, estimate: ${another_project.cost_estimate:.2f}, completion: {another_project.completion_percentage}%")


def add_new_project(projects):
    project_name = input("Name: ")
    start_date_value = input("Start date (dd/mm/yy): ")
    priority_level = int(input("Priority: "))
    cost_amount = float(input("Cost estimate: $"))
    completion_percent = int(input("Percent complete: "))
    projects.append(Project(project_name, start_date_value, priority_level, cost_amount, completion_percent))


def main():
    projects_data = load_projects("projects.txt")
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects_data)} projects from projects.txt")

    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        user_choice = input(">>> ").upper()

        if user_choice == 'Q':
            save_option = input(
                "Would you like to save to projects.txt? ").lower()
            if save_option.startswith('y'):
                save_projects("projects.txt", projects_data)
            print("Thank you for using custom-built project management software.")
            break
        elif user_choice == 'L':
            file_name = input("Enter filename to load from: ")
            projects_data = load_projects(file_name)
            print(f"Loaded projects from {file_name}")
        elif user_choice == 'S':
            save_file = input("Enter filename to save to: ")
            save_projects(save_file, projects_data)
            print(f"Saved projects to {save_file}")
        elif user_choice == 'D':
            display_projects(projects_data)
        elif user_choice == 'A':
            add_new_project(projects_data)


if __name__ == "__main__":
    main()