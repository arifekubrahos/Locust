class LogFile():
    def log_error(message):
        with open("ErrorLog.txt", "a") as file:
            file.write(message)
        pass
