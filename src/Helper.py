from src.Event import Event
import requests
import os
import sys


class Helper():

    @staticmethod
    def print_header() -> None:
        print("")
        print(r"     _       _                 _         __ _  __     _    ")
        print(r"    / \   __| |_   _____ _ __ | |_ ___  / _| |/ /___ | |_  ")
        print(r"   / _ \ / _` \ \ / / _ \ '_ \| __/ _ \| |_| ' // _ \| __| ")
        print(r"  / ___ \ (_| |\ V /  __/ | | | || (_) |  _| . \ (_) | |   ")
        print(r" /_/   \_\__,_| \_/ \___|_| |_|\__\___/|_| |_|\_\___/ \__| ")
        print("")

    @staticmethod
    def retrieve_challenge_input(url, login_cookie=sys.argv[1]) -> list:
        Event("Retrieving the challenge input...")
        cookie = {"session": login_cookie}
        try:
            response = requests.get(url, cookies=cookie)
        except Exception as e:
            message = "Getting the challenge input from " + url + \
                    "went wrong. Error message: " + str(e)
            Event(message=message, is_error=True, exit=True)
        Event("Done!", is_success=True)
        return response.content.decode("utf-8").split("\n")


# Print header upon import
Helper.print_header()
