"""
CC3 Student Submission
Name: Sid Amarnath
"""

from typing import List, Tuple


def calculate(participants: List[str], character_details: List[Tuple[str, str, int]]) \
        -> List[Tuple[str, int]]:
    """
    Calculates each participants power score. 
    :param participants: contains the names of each participant in the tournament in the order they are lined up. 
        May contain duplicates.
    : param character_details: contains the English and Japanese name of each character, 
        along with the power level of the associated character
    :return: Tuple of participants name and final power score.
    """

    # ! Runtime Complexity -> O(n * m)
    # ! Spacetime Complexity -> O(n + m) 

    english_to_japanese = {}
    japanese_to_english = {}
    power_levels = []
    output_list = []

    for participant in participants:
        for character in character_details:
            # name is english
            if 65 <= ord(participant[0]) <= 122:
                if participant == character[0]:
                    english_to_japanese[participant] = character[1]
                    japanese_to_english[character[1]] = participant
                    power_levels.append(character[2])
                if participant == character[1]:
                    english_to_japanese[participant] = character[0]
                    japanese_to_english[character[0]] = participant
                    power_levels.append(character[2])
            # name is japanese
            else:
                if participant == character[0]:
                    japanese_to_english[participant] = character[1]
                    english_to_japanese[character[1]] = participant
                    power_levels.append(character[2])
                
                if participant == character[1]:
                    japanese_to_english[participant] = character[0]
                    english_to_japanese[character[0]] = participant
                    power_levels.append(character[2])
    
    
    for i in range(len(power_levels)):
        power_level_score = 0
        for j in range(i + 1, len(power_levels)):
            if power_levels[i] >= power_levels[j]:
                power_level_score += power_levels[j]
            else:
                break
        
        # participants name is english
        if 65 <= ord(participants[i][0]) <= 122:
            if power_levels[i] > 9000:
                output_list.append((english_to_japanese[participants[i]], power_level_score))
            else:
                output_list.append((participants[i], power_level_score))
        # participants name is japanese
        else:
            if power_levels[i] > 9000:
                output_list.append((participants[i], power_level_score))
            else:
                output_list.append((japanese_to_english[participants[i]], power_level_score))
    
    return output_list
                





