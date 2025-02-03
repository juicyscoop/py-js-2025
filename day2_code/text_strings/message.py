def message(slovnik):
    # "movie", "name", "role"
    # any, all
    # if any(key not in slovnik for key in required_keys):
    #   return None
    data = {}
    if (f"na{data['vloz_tenhle_datopvy_bod_do_jmena']}" not in slovnik) or ("movie" not in slovnik) or ("role" not in slovnik):
        return None
    result = f'''
    In {slovnik['movie']},
    {slovnik["name"]}
    is
    {slovnik["role"]}
    '''
    #  "In movie, name is a role."
    return result

res = message({
    "movie": "Harry Potter",
    "name": "Daniel Radcliffe",
    "role": "Wizard",
    "movie_data": {
        "movie_gross": "100 000 USD",
        "movie_profit": "10 000 USD"
    }
})
print(res)


