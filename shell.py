#!/usr/bin/env python3
import subprocess

def execute_command(command_input):
    command_input_args = command_input.split(" ")

    print(command_input_args)

    # try:
    #     result = subprocess.run(command_input_args, shell=True, capture_output=True, text=True, check=True)
        
    #     print(result.stdout)
    # except subprocess.CalledProcessError as e:
    #     print(e.stderr)
    # except Exception as e:
    #     print("Unexpected error:", e)

    try:
        # Open a subprocess with the command
        process = subprocess.Popen(command_input_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Communicate with the subprocess (send input, receive output)
        stdout, stderr = process.communicate()

        # Print the output
        print(stdout)

        # Check for errors
        if process.returncode != 0:
            print("Error:", stderr)
    except Exception as e:
        print("Unexpected error:", e)


def startup_shell():

    while True:
        command_input = input("cgsh> ").strip()

        if command_input == "exit":
            print("Exiting shell...")
            break

        # split with | for bigger commands

        execute_command(command_input)

         

        

    return


if __name__ == "__main__":
    startup_shell()