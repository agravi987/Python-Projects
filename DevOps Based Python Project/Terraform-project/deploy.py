import subprocess


def run_command(command):

    print(f"\nRunning: {' '.join(command)}\n")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:

        print("Error:")
        print(result.stderr)

        return False

    return True


def deploy_infrastructure():

    commands = [

        ["terraform", "init"],

        ["terraform", "fmt"],

        ["terraform", "validate"],

        ["terraform", "plan"],

        ["terraform", "apply", "-auto-approve"]
    ]

    for command in commands:

        success = run_command(command)

        if not success:
            break


def destroy_infrastructure():

    commands = [

        ["terraform", "destroy", "-auto-approve"]
    ]

    for command in commands:

        success = run_command(command)

        if not success:
            break


if __name__ == "__main__":

    print("\n========= TERRAFORM AUTOMATION =========\n")

    print("1. Deploy Infrastructure")
    print("2. Destroy Infrastructure")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        print("\nStarting Infrastructure Deployment...\n")

        deploy_infrastructure()

    elif choice == "2":

        print("\nDestroying Infrastructure...\n")

        destroy_infrastructure()

    else:

        print("\nInvalid choice.")