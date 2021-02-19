import requests
import json

def build_board(string):
    """Build board from string"""
    if len(string) != 16:
        print("Error. Must enter 4*4 grid (16 characters)")
        return
    board = [[*string[0:4]], [*string[4:8]], [*string[8:12]], [*string[12:16]]]
    print(board)
    boggle_solver(string)

def boggle_solver(string):
    base_url = 'http://api.codebox.org.uk/boggle/'
    url = base_url + string
    print(url)
    response = requests.get(url)
    print(response)
    data = response.json()
    json_formatted_str = json.dumps(data, indent=2)
    print(json_formatted_str)

if __name__ == '__main__':
    val = input("Enter your value: ")
    # val = "SERSPATGLINESERS"
    build_board(val)


