from moving import generate_new_states, get_possible_moves, check_win, \
generate_random_state, get_configs_h_ahead
from strategies import choose_agent_zero, choose_agent_one, choose_agent_two
import numpy as np

def play_hanoi(h=4, agent=0, n_discs=4, max_turns=10000, win_context=0, subsolutions={}):
    
    turn_counter = 0
    win = False
    current_state = generate_random_state(n_discs)

    winning_state = None
    last_choice = None
    
    # if win context is 0, winning state is tower in random location
    if win_context == 0:
        winning_pole = np.random.choice([0,1,2])
        winning_state = [[0],[0],[0]]
        winning_state[winning_pole] += [i for i in range(n_discs,0,-1)]


    # if win context is 1, winning state is random configuration
    elif win_context == 1:
        while not winning_state:
            candidate_state = generate_random_state()
            if candidate_state != current_state:
                winning_state = candidate_state

    # for sanity checks, if win _context == 3 all discs start on first pole
    # and winning state has all_discs on last pole
    elif win_context == 2:
        current_state = [[0]+[i for i in range(n_discs, 0, -1)],[0],[0]]
        winning_state = [[0],[0],[0]+[i for i in range(n_discs, 0, -1)]]

    # begin the game loop, which will end once winning state 
    # reached or maxed out turns
    while not win and turn_counter <= max_turns:
        new_configurations = []
        winning_configurations = []
        if "subsolutions" not in locals():
            subsolutions = {}
        # recursively move until end of planning horizon
        new_configurations, winning_configurations, subsolutions \
                 = get_configs_h_ahead(current_state, h, turn_counter,
                                                winning_state, winning_configurations, 
                                                new_configurations, 
                                                subsolutions)

        # end game if win detected
        if len(winning_configurations):
            return sorted(winning_configurations, key=lambda e: e[1])[0][1], subsolutions

        else:
            turn_counter += h
        
        # different possible strategies for choosing moves
        if agent == 0:
            choice = choose_agent_zero(current_state, new_configurations, winning_state)
        elif agent == 1:
            choice = choose_agent_one(current_state, new_configurations, winning_state)
        elif agent == 2:
            choice = choose_agent_two(current_state, new_configurations, winning_state)
        
        current_state = choice
        
    return turn_counter, subsolutions