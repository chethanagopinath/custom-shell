#!/usr/bin/env python3
import subprocess
import os

def execute_command(command_input):
    command_input_args = command_input.split(" ")

    try:
        # Open a subprocess with the command
        process = subprocess.Popen(command_input_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Communicate with the subprocess (send input, receive output)
        stdout, stderr = process.communicate()

        print(stdout)

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

        # handle cd differently
        if "cd" in command_input:
            input_directory = command_input[3:]
            try:
                os.chdir(input_directory)
            except FileNotFoundError:
                print(f"Directory not found: {input_directory}")

        # handle other commands differently
        else:
            execute_command(command_input)

    return


if __name__ == "__main__":
    startup_shell()