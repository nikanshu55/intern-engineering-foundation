intern_name = "Nikanshu saini"
role = "Software Engineering Intern"
department = "Engineering"

skills = ["Python", "Git", "GitHub"]


def print_profile():
    # Display the intern profile
    print("Intern Name:", intern_name)
    print("Role:", role)
    print("Department:", department)
    print("Skills:", ", ".join(skills))


if __name__ == "__main__":
    print_profile()