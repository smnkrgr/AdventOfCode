from src.Event import Event
import requests
import os


class Helper():

    def __init__(self):
        self.print_header()

    def print_header(self) -> None:
        print("")
        print(r"     _       _                 _         __ _  __     _    ")
        print(r"    / \   __| |_   _____ _ __ | |_ ___  / _| |/ /___ | |_  ")
        print(r"   / _ \ / _` \ \ / / _ \ '_ \| __/ _ \| |_| ' // _ \| __| ")
        print(r"  / ___ \ (_| |\ V /  __/ | | | || (_) |  _| . \ (_) | |   ")
        print(r" /_/   \_\__,_| \_/ \___|_| |_|\__\___/|_| |_|\_\___/ \__| ")
        print("")

    @staticmethod
    def retrieve_challenge_input(uri) -> list:
        Event("Retrieving the challenge input...")
        try:
            response = requests.get(uri)
        except Exception as e:
            message = "Getting the challenge input from " + url + \
                    "went wrong..."
            Event(message=message, is_error=True, exit=True)
        Event("Done!", is_success=True)

