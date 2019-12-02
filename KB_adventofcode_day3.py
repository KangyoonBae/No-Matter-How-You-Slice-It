# Using regex to extract all the digits
import re


def process_input_and_calculate(file_name):
    """
        Function to process input and calculate overlaps inches and no overlap ID.

        Parameters
        ----------
        file_name : string
    """

    # Read file object
    with open(file_name, 'r') as fileObject:
        # claimData list
        claim_data_list = []

        # Loop through all the lines
        for line in fileObject:
            # Parse lines, extract all the digits, and put them into a list
            all_the_digits = re.findall(r'\d+', line)

            # Create claim data and append to list
            claim_data_list.append(
                {'claimID': int(all_the_digits[0]), 'left': int(all_the_digits[1]), 'top': int(all_the_digits[2]),
                 'width': int(all_the_digits[3]), 'height': int(all_the_digits[4])})

            # Debug
            # print(claim_data_list)

    # Calculate_overlaps function return track_map.  It will be used for calculate_no_overlaps
    track_map = calculate_overlaps(claim_data_list)

    # Result for calculate_no_overlaps
    print('Claim ID', calculate_no_overlaps(claim_data_list, track_map), 'has no overlapping')


def calculate_overlaps(claim_data_list):
    """
        Function to calculate overlaps
        - Loops through coordinates of area, tracks all of them, counts overlap area, and return total overlap

        Parameters
        ----------
        claim_data_list : List of Dictionary
    """

    # Dictionary to track all the coordinates
    track_map = {}

    # Go through the list of claims
    for claim in claim_data_list:

        # Loops through width an height
        for x in range(claim.get("width")):
            for y in range(claim.get("height")):

                # New coordinate to track
                new_coordinates = (claim.get("left") + x, claim.get("top") + y)

                #
                try:
                    track_map[new_coordinates].append(claim.get("claimID"))
                # Needs a try catch for KeyError for new_coordinates.
                # If track_map doesn't have a key for new_coordinates,
                # then put a List of claimIDs with claimID value and new_coordinates as a key
                except KeyError:
                    track_map[new_coordinates] = [claim.get("claimID")]

    # Counter for overlap
    over_lap_counter = 0

    # Loops through, all the values (claimId list) with key and counts where length of claimId list is more than 1
    for cur_claim_id in track_map.keys():
        if len(track_map[cur_claim_id]) > 1:
            over_lap_counter += 1

    # Print result
    print("There are", over_lap_counter, 'inches overlaps by 2 or more claims')

    # Returns track_map for calculate_no_overlaps
    return track_map


def calculate_no_overlaps(claim_data_list, track_map):
    """
        Function to calculate no overlaps
        - Looping through List of claim data and call helper class to calculate

        Parameters
        ----------
        claim_data_list : List of Dictionary
        track_map : Dictionary of claimID List (Key: Coordinates)
    """

    # Loops through List of Claim data
    for claim in claim_data_list:

        # Calling helper class.  If it returns True, then returns ClaimID
        if calculate_no_overlaps_helper(claim, track_map):
            return claim.get("claimID")


def calculate_no_overlaps_helper(claim, track_map):
    """
        Function to calculate no overlaps
        - Takes claim data and loops through track_map
        - If track_map value contains more than 2 Claim IDs, returns false
        - Case when claim data's all the coordinates contain only one claimID, return true

        Parameters
        ----------
        claim : Dictionary
        track_map : Dictionary of claimID List (Key: Coordinates)
    """

    # Loops through width an height
    for x in range(claim.get("width")):
        for y in range(claim.get("height")):
            new_coordinates = (claim.get("left") + x, claim.get("top") + y)

            # track_map[new_coordinates] value is not single claimID, returns false
            if track_map[new_coordinates] != [claim.get("claimID")]:
                return False
    # Went through all the coordinates.  Returns true
    return True


# Call process_input_and_calculate to start

# Test
# process_input_and_calculate('input_test.txt')
process_input_and_calculate('input.txt')
