import webbrowser


def try_me():
    print('Do you think this is a cool projet ?')
    print('Yes / No')
    answer = input()
    if answer == "Yes":
        print('Thanks <3')
        webbrowser.open('https://www.thisworldthesedays.com/super-cool-project.html')
    else:
        print("You're not cool :(")
        webbrowser.open(
            'https://www.thisworldthesedays.com/super-cool-project.html')

def to_be_tested():
    return True

if __name__ == "__main__":
    try_me()
    to_be_tested()
