from copy import deepcopy
import numpy as np

def encode_state_as_string(state):
    '''
    encodes state as a string so it can be used as dictionary key
    '''

    return ','.join(['.'.join([str(disc) for disc in pole]) for pole in state])

def check_state_validity(state):
    '''
    double check validity of randomly generated game state

    state: current game state
    '''
    for pole in state:
        if not (pole[0] == 0 and sorted(pole[1:], reverse=True) == pole[1:]):
            return False
    return True

def generate_random_state(n_discs=4):
    '''
    generate random game state
    
    n_discs: number of discs to play game with
    '''
    while True: 
        state = [[0,],[0,],[0,]]
        for i in range(n_discs, 0, -1):
            pole = np.random.choice([0,1,2])
            state[pole].append(i)
        if check_state_validity(state):
            return state
    
def generate_new_states(state, possible_moves):
    '''
    given current state and list of possible moves, generate list
    of states that would result if those moves were implemented

    state: current game state
    possible moves: list of tuples. first element is index of pole to move from
        second element is index of pole to move to
    '''
    new_states = []
    for from_index, to_index in possible_moves:
        state_copy = deepcopy(state)
        to_move = state_copy[from_index].pop()
        state_copy[to_index].append(to_move)
        new_states.append(state_copy)
    
    return new_states


def get_possible_moves(state):
    '''
    given a current state, generate list
    of all possible moves at that state

    state: current game state
    '''
    possible_moves =[]
    for from_index in range(len(state)):
        for to_index in range(len(state)):
            if from_index != to_index:
                if (state[from_index][-1] < state[to_index][-1] or state[to_index][-1] == 0) \
                    and state[from_index][-1] != 0:
                    possible_moves.append((from_index, to_index))
    return possible_moves


def check_win(state, winning_state):
    '''
    check if current state is winning state

    state: current game state
    winning_state: configuration of winning game state
    '''
    if state == winning_state:
        return True
    return False


def get_configs_h_ahead(state, h, turn_counter, winning_state, 
                                winning_configurations, new_configurations, \
                                subsolutions={}):
    '''
    recursively get all possible board configurations that could result from h moves

    state: current state
    h: horizon counter
    turn counter: num of turns taken
    winning_state: configuration of winning game state 
    new_configurations: list of new configurations resulting from h moves. 
        is continuously appended to each time we reach the end of the recursion
    winning_configurations: maintain a list of winning configurations and their turn counts
    subsolutions: dictionary mapping states to possible subsequent states
    '''

    # check win
    win = check_win(state, winning_state)
    # print(len(subsolutions))

    # if win true, append this configuration to winning configurations
    if win:
        winning_configurations.append((state, turn_counter))
        return new_configurations, winning_configurations, subsolutions

    # if at end of planning horizon, 
    # append resulting configuration to new_configurations
    if h == 0:  
        if state not in new_configurations:  
            new_configurations.append(state)
        return new_configurations, winning_configurations, subsolutions
    
    # otherwise get list of possible moves from this state and begin recursively
    # implementing them
    else:
        state_as_string = encode_state_as_string(state)
        if state_as_string in subsolutions:
            new_states_following_moves = subsolutions[state_as_string]
        else:
            possible_moves = get_possible_moves(state)
            new_states_following_moves = generate_new_states(state, possible_moves)
            subsolutions[state_as_string] = new_states_following_moves

        h -= 1
        turn_counter += 1
        for i, new_state in enumerate(new_states_following_moves):
            new_configurations, winning_configurations, subsolutions = \
            get_configs_h_ahead(new_state, h, turn_counter, winning_state, 
                                        winning_configurations, new_configurations,
                                        subsolutions)

    return new_configurations, winning_configurations, subsolutions