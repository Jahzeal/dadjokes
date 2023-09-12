
import requests
# import pyfiglet
# from termcolor import colored
try:
#     header = pyfiglet.figlet_format("DAD JOKES 3000")
#     header = colored(header, color="magenta")
#     print(header)
    jw = "https://icanhazdadjoke.com/search"
    while True:
        ques = input("do you want another joke ? ")
        if ques == "yes":
            ask = input("let me tell you a joke ! Give me a topic: ")
            limited = input("what limit !")
            response = requests.get(jw,headers={"Accept": "application/json"},
                        params={"term": ask,"limit": limited})
            data = (response.json())
            num_jokes =(len(data["results"]))
            if num_jokes >= 1:
                 print(data["results"])
            else:
                num_jokes == 0
                print(f"they are no jokes for {ask}")
        else:
            print("bye")
            break
except Exception:
    print("oops you are not connected to the internet")