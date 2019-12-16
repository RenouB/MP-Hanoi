from copy import deepcopy
import numpy as np

def choose_agent_zero(current_state, new_configurations, winning_state):
    '''
    agent zero plans h steps ahea dand then chooses configuration with 
    highest number of discs in the correct location
    curren_state: current game state
    new_configurations: list of configurations resulting from h moves
    winning_state: configuration of winning state
    '''
    
    # score each new config
    config_scores = []
    for config in new_configurations:
        score = 0
        for i in range(len(config)):        
            config_as_set = set([disc for disc in config[i] if disc != 0])
            winning_as_set = set([disc for disc in winning_state[i] if disc != 0])
            score += len(config_as_set.intersection(winning_as_set))
        config_scores.append(score)
    
    # get the two highest config scores
    max_two_scores = sorted(list(set(config_scores)), reverse=True)[:2]
    highest_scoring_configs = [i for i, config  in enumerate(new_configurations) \
                                     if config_scores[i] == max_two_scores[0] and \
                                     config != current_state]

    # in the even that there is only one highest scoring state that is the same
    # as the current state, we choose from set of second highest scoring states
    if len(highest_scoring_configs) == 0:
        highest_scoring_configs = [i for i, config  in enumerate(new_configurations) \
                                     if config_scores[i] == max_two_scores[1] and \
                                     config != current_state]

    # in the event that there are many highest scoring states, we randomly choose one
    choice = np.random.choice(highest_scoring_configs, 1)[0]
    best_state = new_configurations[choice]
    return best_state


def choose_agent_one(current_state, new_configurations, winning_state):
    '''
    agent one plans h steps ahead, attempting to place largest misplaced disk
    in correct position

    current_state: current game state
    new_configurations: list of configuratinos resulting from h moves
    winning_state: configuration of winning state
    '''

    # find pole locations of each disc, in current_state and winning_state
    # then find which discs are in correct locations
    positions_in_current_state = []
    positions_in_winning_state = []
    correct_positions = []
    for disc in range(1,5):
        for pole_index in range(len(current_state)):
            if disc in current_state[pole_index]:
                positions_in_current_state.append((disc, pole_index))
            if disc in winning_state[pole_index]:
                positions_in_winning_state.append((disc, pole_index))
    misplaced_disks = set(positions_in_winning_state).difference(set(positions_in_current_state))
    largest_misplaced_disc, desired_location = sorted(list(misplaced_disks), reverse=True)[0]

    # get all configurations where largest misplaced disk is in correct spot
    valable_configurations = [config for config in new_configurations \
                                 if largest_misplaced_disc in config[desired_location]]
    # if there aren't any, resort to strategy of agent 1
    if len(valable_configurations) == 0:
        valable_configurations = new_configurations

    # now we must choose the highest scoring among these options. In our case
    # we choose the config with highest number of discs in correct location
    
    return choose_agent_zero(current_state, valable_configurations, winning_state)


def choose_agent_two(current_state, new_configurations, winning_state):
    '''
    agent two is identical to agent one, except tries to put
     randomly chosen disc in its correct location
    '''
    positions_in_current_state = []
    positions_in_winning_state = []
    correct_positions = []
    for disc in range(1,5):
        for pole_index in range(len(current_state)):
            if disc in current_state[pole_index]:
                positions_in_current_state.append((disc, pole_index))
            if disc in winning_state[pole_index]:
                positions_in_winning_state.append((disc, pole_index))
    
    misplaced_disks = set(positions_in_winning_state).difference(set(positions_in_current_state))
    misplaced_disks = list(misplaced_disks)
    random_index = np.random.choice([i for i in range(len(misplaced_disks))], 1)[0]
    disc_to_move, desired_location = misplaced_disks[random_index]


    valable_configurations = [config for config in new_configurations \
                                 if disc_to_move in config[desired_location]]
    # if there aren't any, resort to strategy of agent 1
    if len(valable_configurations) == 0:
        valable_configurations = new_configurations

    return choose_agent_zero(current_state, valable_configurations, winning_state)

