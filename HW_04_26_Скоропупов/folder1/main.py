import first

try:
    import second
except ModuleNotFoundError:
    first.return_file()

    import second
