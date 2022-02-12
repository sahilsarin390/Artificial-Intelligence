def vacuum_world():

    goal = {'A': '0', 'B': '0'}
    cost = 0

    location = input("Enter Location of Vacuum: ")

    status = input("Enter status of " + location + ": ")
    status_compl = input("Enter status of other room: ")
    print("Initial Location Condition" + str(goal))

    if location == 'A':

        print("Vacuum is placed in Location A")
        if status == '1':
            print("Location A is Dirty.")
            goal['A'] = '0'
            cost += 1
            print("Cost for CLEANING A " + str(cost))
            print("Location A has been Cleaned.")

            if status_compl == '1':

                print("Location B is Dirty.")
                print("Moving right to the Location B. ")
                cost += 1
                print("Cost for moving right" + str(cost))

                goal['B'] = '0'
                cost += 1
                print("Cost for cleaning " + str(cost))
                print("Location B has been Cleaned. ")
            else:
                print("No action" + str(cost))

                print("Location B is already clean.")

        if status == '0':
            print("Location A is already clean ")
            if status_compl == '1':
                print("Location B is Dirty.")
                print("Moving right to the Location B. ")
                cost += 1
                print("COST for moving right " + str(cost))
                goal['B'] = '0'
                cost += 1
                print("Cost for cleaning" + str(cost))
                print("Location B has been Cleaned. ")
            else:
                print("No action " + str(cost))
                print(cost)

                print("Location B is already clean.")

    else:
        print("Vacuum is placed in location B")

        if status == '1':
            print("Location B is Dirty.")

            goal['B'] = '0'
            cost += 1
            print("COST for CLEANING " + str(cost))
            print("Location B has been Cleaned.")

            if status_compl == '1':

                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1
                print("COST for moving LEFT" + str(cost))

                goal['A'] = '0'
                cost += 1
                print("COST for cleaning " + str(cost))
                print("Location A has been Cleaned.")

        else:
            print(cost)

            print("Location B is already clean.")

            if status_compl == '1':
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                cost += 1
                print("COST for moving LEFT " + str(cost))
                goal['A'] = '0'
                cost += 1
                print("Cost for cleaning " + str(cost))
                print("Location A has been Cleaned. ")
            else:
                print("No action " + str(cost))
                print("Location A is already clean.")

    print("GOAL STATE: ")
    print(goal)
    print("Performance Measurement: " + str(cost))


vacuum_world()
