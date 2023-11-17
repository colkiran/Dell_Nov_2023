
def outerFun(fnc):
    def helper(amt):
        print("Logging into the server......")
        fnc(amt)                # callback
        print("Logging out of the server......")
        print("-" * 60)

    return helper

@outerFun               # deposit = outerFun(deposit)
def deposit(amt):
    print(f"Amount {amt} credited into the account......")


deposit(50000)

# decorator to calculate the time taken by a function to execute.....
