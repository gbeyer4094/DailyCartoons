def main():
    print("The main function is running")
    print("The __name__ parameter is " + __name__)


if __name__ == "__main__":
    main()
else:
    print("The main function is not running")
    print("The __name__ parameter is " + __name__)
