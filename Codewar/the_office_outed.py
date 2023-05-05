#Given an object (meet) containing team member names as keys, and their happiness rating out of 10 as the value, you need to assess the overall happiness rating of the group. If <= 5, return 'Get Out Now!'. Else return 'Nice Work Champ!'.
#Happiness rating will be total score / number of people in the room.
def assess_happiness(meet, boss):
    total_score = sum(meet.values()) + (boss * 2)
    num_people = len(meet) + 1
    avg_score = total_score / num_people
    
    if avg_score <= 5:
        return 'Get Out Now!'
    else:
        return 'Nice Work Champ!'
