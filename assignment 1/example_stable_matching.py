preffered_ranking_men = {
'Ryan' : ['Lizzy', 'Sarah', 'Zoey', 'Daniella'],
'Joe' : ['Sarah', 'Lizzy', 'Daniella', 'Zoey'],
'Blake' : ['Sarah', 'Daniella', 'Zoey', 'Lizzy'],
'Connor' : ['Lizzy', 'Sarah', 'Zoey', 'Daniella'],
}

preffered_ranking_women = {
'Lizzy' : ['Ryan', 'Blake', 'Joe', 'Connor'],
'Sarah' : ['Ryan', 'Blake', 'Connor', 'Joe'],
'Zoey' : ['Connor', 'Joe', 'Ryan', 'Blake'],
'Daniella' : ['Ryan', 'Joe', 'Connor', 'Blake'],
}
 
tentative_matches = [] # To keep track of the tentative matchings
free_men = [man for man in list(preffered_ranking_men.keys())] # Initialize the list of free men
 
def stableMatch():
    while len(free_men) > 0:
        for man in free_men:
            begin_matching(man)
 
def begin_matching(man):
    print(f"Dealing with {man}")
    for woman in preffered_ranking_men[man]:
        taken_match = [pairing for pairing in tentative_matches if woman in pairing]
 
        if not taken_match:
            tentative_matches.append([man, woman])
            free_men.remove(man)
            print(f"{man} is tentatively matched to {woman}")
            break
 
        else:
            print(f"{woman} is already matched")
            current_partner = preffered_ranking_women[woman].index(taken_match[0][0])
            potential_partner = preffered_ranking_women[woman].index(man)

            if potential_partner < current_partner:
                print(f"{man} is more preffered than {taken_match[0][0]}")
                print(f"Unpair {taken_match[0][0]} and {woman}. Now, {man} is tentatively matched to {woman}")
                
                # the potential guy is matched and the current guy is now free
                free_men.remove(man)
                free_men.append(taken_match[0][0])
                
                taken_match[0][0] = man
                break
            else:
                print(f"{woman} is satisfied with {taken_match[0][0]}")
 
            if __name__ == '__main__':
                stableMatch()
                print("\nFINAL PAIRINGS : ")
                print(*tentative_matches) # print out the final list of matchings

stableMatch()