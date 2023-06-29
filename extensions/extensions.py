def main():
    user = input("enter file name: ").lower()
    if "." in user:
        split_user = user.split(".")
        extension = split_user[1]

        if extension == "gif" in user:
            print("image/gif")
        elif extension == "jpg" or extension == "jpeg" in user:
            print("image/jpeg")
        elif "png" in user:
            print("image/png")
        elif "pdf" in user:
            print("application/pdf")
        elif "txt" in user:
            print("text/plain")
        elif "zip" in user:
            print("application/zip")
        else:
            print("application/octet-stream")

    else:
        print("application/octet-stream")


main()