from __future__ import annotations

def clean_dependencies_list():
    pyproject_path = "pyproject.toml"

    try:
        with open(pyproject_path, "r") as file:
            content = file.read()

        # Find the start and end of the dependencies section
        dependencies_start = content.find("dependencies = [")
        dependencies_end = content.find("]", dependencies_start) + 1

        if dependencies_start != -1 and dependencies_end != -1:
            # Extract only the content inside the brackets
            dependencies_section = content[dependencies_start + len("dependencies = ["):dependencies_end - 1]

            # Split and clean dependencies, removing empty entries and extra quotes
            dependencies_list = [dep.strip().strip('"') for dep in dependencies_section.split(",") if dep.strip()]
            dependencies_list = [dep for dep in dependencies_list if dep != "dependencies = ["]  # Ensure no duplicate key

            # Format the dependencies properly
            if dependencies_list:
                formatted_dependencies = "dependencies = [\n"
                formatted_dependencies += ",\n".join([f'    "{dep}"' for dep in dependencies_list])
                formatted_dependencies += "\n]\n"
            else:
                formatted_dependencies = "dependencies = []\n"

            # Replace the original dependencies section with the formatted one
            content = content[:dependencies_start] + formatted_dependencies + content[dependencies_end:]

        # Write the cleaned content back to pyproject.toml
        with open(pyproject_path, "w") as file:
            file.write(content)

        print("Cleaned up pyproject.toml successfully.")

    except FileNotFoundError:
        print(f"{pyproject_path} not found, skipping cleanup.")
    except Exception as e:
        print(f"An error occurred while cleaning up {pyproject_path}: {e}")


def post_gen_project():
    # Call the function to clean the dependencies list in the pyproject.toml file
    clean_dependencies_list()

    # Any additional post-generation logic can go here
    print("Post-generation setup complete.")

if __name__ == "__main__":
    post_gen_project()
