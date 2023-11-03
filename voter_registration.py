"""Program that creates Voter Registration if person using the program is eligible"""

# create boolean values to set up while loops to check logic further in the program
CONTINUE_PROMPT = True
STATE_VALIDATION = True
ZIP_VALIDATION = True

# Introduces the user to Voter Registration
print("******************************************************\n"
      "Welcome to the Python Voter Registration Application.")

# while loop to run the program until break
while CONTINUE_PROMPT:
    # Asks for first name and if they want to continue
    first_name = input("Enter your first name:")
    prompt = input("Do you want to continue with Voter Registration?(Yes/No)")
    if "no" in prompt or "No" in prompt or "NO" in prompt:
        break
    # Asks for last name and if they want to continue
    last_name = input("Enter your last name:")
    prompt = input("Do you want to continue with Voter Registration?")
    if "no" in prompt or "No" in prompt or "NO" in prompt:
        break
    # Asks for age and verifies the age between 18 and 120 and then asks if they want to continue
    age = int(input("What is your age:"))
    if age < 18:
        print("Error! Must be at least 18 to vote")
        break
    if age > 120:
        print("Error! Invalid age")
        break
    prompt = input("Do you want to continue with Voter Registration?")
    if "no" in prompt or "No" in prompt or "NO" in prompt:
        break
    # Asks if they are a citizen and confirms they are and asks if user wants to continue
    citizen = input("Are you a U.S. Citizen:")
    if "no" in citizen or "No" in citizen or "NO" in citizen:
        print("Error! Must be a U.S. Citizen to vote")
        break
    prompt = input("Do you want to continue with Voter Registration?")
    if "no" in prompt or "No" in prompt or "NO" in prompt:
        break
    # Creates a while loop to get a state abbreviation until proper abbreviation is detected
    while STATE_VALIDATION:
        # list of valid states
        valid_states = ['AL', 'AK', 'AS', 'AZ', 'AR', 'CA', 'CO', 'CT',
                        'DE', 'DC', 'FL', 'GA', 'GU', 'HI', 'ID', 'IL',
                        'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA',
                        'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH',
                        'NJ', 'NM', 'NY', 'NC', 'ND', 'MP', 'OH', 'OK',
                        'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX',
                        'UT', 'VT', 'VI', 'VA', 'WA', 'WV', 'WI', 'WY']
        # State input
        state = input("What state do you live in: \nUse abbreviations ex. VA, CO, MD, Etc.")
        # Verifies the length of the abbreviation
        if len(state) != 2:
            print("Error! please enter valid state abbreviation")
            state = input("What state do you live in: \nUse abbreviations ex. VA, CO, MD, Etc.")
        # Makes sure the abbreviation is in the list
        if state not in valid_states:
            print("Error! Entered an invalid state abbreviation please try again")
            state = input("What state do you live in: \nUse abbreviations ex. VA, CO, MD, Etc.")
        # If the length and the state is valid then the while loop ends
        if len(state) and state in valid_states:
            STATE_VALIDATION = False
    # Prompts user if they want to continue
    prompt = input("Do you want to continue with Voter Registration?")
    if "no" in prompt or "No" in prompt or "NO" in prompt:
        break
    # Zip code loop until a valid zip code is entered
    while ZIP_VALIDATION:
        # asks for zipcode
        zipcode = input("Enter your Zipcode:")
        # if zip code is not 5 digits then user is asked to enter it again else the loop ends
        if len(zipcode) != 5:
            print("Error! Invalid Zipcode please enter 5 digits")
            zipcode = input("Enter your Zipcode:")
        else:
            ZIP_VALIDATION = False
    # Prints all the information using an f-string.
    print(f"Thank your for registering to vote here is the information "
          f"we have received.\nName: {first_name} {last_name}\nAge: {age}\n"
          f"U.S. Citizen: {citizen}\nState: {state}\nZipcode: {zipcode}")

    break
