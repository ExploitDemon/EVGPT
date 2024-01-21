from handler import ApiHandler


def main():
    api_handler = ApiHandler()
    data = api_handler.get_data()

    odds = data["results"][0]["odds"]
    for odd in odds:
        print(odd)

    print(data["results"][0]["team1name"])
    print(data["results"][0]["team2name"])


if __name__ == "__main__":
    main()
