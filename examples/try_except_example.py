def  convert_string_to_int(string):
    try:
        return int(string)
    except ValueError:
        return None
    except TypeError:
        print("Encountered type error!")
        return "a"
    finally:
        print("I always get executed!")
