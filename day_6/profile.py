def create_profile () :
    profile ={ }
    i = 0
    while i < 1 :
        prompt = input('Do you wish to continue : ').lower().strip()
        if prompt == 'no' :
            break
        elif prompt != 'yes' :
            continue 
        first_name = input ('Enter the first name : ').title().strip()
        profile['First Name'] = first_name
        last_name = input ('Enter the last name : ').title().strip()
        profile['Last Name'] = last_name
        i += 1
        while True :
            message = input('Do you have additional details : ').lower().strip()
            if message == 'no' :
                break
            elif message != 'yes' :
                continue 
            detail_key = input ('Enter the additonal key : ').title().strip()
            detail_value = input ('Enter the addiotnal value : ').title().strip()
            profile[detail_key] = detail_value
    return profile
