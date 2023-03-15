class Constants:
    COMP = 1
    HUMAN = -1
    
    FIVE_IN_A_ROW_SCORE = 10000
    FOUR_IN_A_ROW_SCORE = 1000
    BLOCKED_FOUR_SCORE = 150
    THREE_IN_A_ROW_SCORE = 100
    OPEN_TWO_SCORE = 10
    OPEN_ONE_SCORE = 1

    SCORE_DICT_COMP_6 = {
        (None, COMP, COMP, COMP, COMP, None): FOUR_IN_A_ROW_SCORE,

        (None, COMP, COMP, COMP, None, None): THREE_IN_A_ROW_SCORE,
        (None, None, COMP, COMP, COMP, None): THREE_IN_A_ROW_SCORE,
        (None, COMP, None, COMP, COMP, None): THREE_IN_A_ROW_SCORE,
        (None, COMP, COMP, None, COMP, None): THREE_IN_A_ROW_SCORE,

        (None, None, COMP, None, COMP, None): OPEN_TWO_SCORE,
        (None, None, COMP, COMP, None, None): OPEN_TWO_SCORE,
        (None, None, None, COMP, COMP, None): OPEN_TWO_SCORE,
        (None, COMP, COMP, None, None, None): OPEN_TWO_SCORE,
        (None, COMP, None, COMP, None, None): OPEN_TWO_SCORE,
        (None, COMP, None, None, COMP, None): OPEN_TWO_SCORE,

        (None, COMP, None, None, None, None): OPEN_ONE_SCORE,
        (None, None, COMP, None, None, None): OPEN_ONE_SCORE,
        (None, None, None, COMP, None, None): OPEN_ONE_SCORE,
        (None, None, None, None, COMP, None): OPEN_ONE_SCORE,
    }

    SCORE_DICT_COMP_5 = {
        (COMP, COMP, COMP, COMP, COMP): FIVE_IN_A_ROW_SCORE,
        (None, COMP, COMP, COMP, COMP): BLOCKED_FOUR_SCORE,
        (COMP, None, COMP, COMP, COMP): BLOCKED_FOUR_SCORE,
        (COMP, COMP, None, COMP, COMP): BLOCKED_FOUR_SCORE,
        (COMP, COMP, COMP, None, COMP): BLOCKED_FOUR_SCORE,
        (COMP, COMP, COMP, COMP, None): BLOCKED_FOUR_SCORE,
    }

    SCORE_DICT_HUMAN_6 = {
        (None, HUMAN, HUMAN, HUMAN, HUMAN, None): -FOUR_IN_A_ROW_SCORE,
        
        (None, HUMAN, HUMAN, HUMAN, None, None): -THREE_IN_A_ROW_SCORE,
        (None, None, HUMAN, HUMAN, HUMAN, None): -THREE_IN_A_ROW_SCORE,
        (None, HUMAN, None, HUMAN, HUMAN, None): -THREE_IN_A_ROW_SCORE,
        (None, HUMAN, HUMAN, None, HUMAN, None): -THREE_IN_A_ROW_SCORE,

        (None, None, HUMAN, None, HUMAN, None): -OPEN_TWO_SCORE,
        (None, None, HUMAN, HUMAN, None, None): -OPEN_TWO_SCORE,
        (None, None, None, HUMAN, HUMAN, None): -OPEN_TWO_SCORE,
        (None, HUMAN, HUMAN, None, None, None): -OPEN_TWO_SCORE,
        (None, HUMAN, None, HUMAN, None, None): -OPEN_TWO_SCORE,
        (None, HUMAN, None, None, HUMAN, None): -OPEN_TWO_SCORE,

        (None, HUMAN, None, None, None, None): -OPEN_ONE_SCORE,
        (None, None, HUMAN, None, None, None): -OPEN_ONE_SCORE,
        (None, None, None, HUMAN, None, None): -OPEN_ONE_SCORE,
        (None, None, None, None, HUMAN, None): -OPEN_ONE_SCORE,
    }

    SCORE_DICT_HUMAN_5 = {
        (HUMAN, HUMAN, HUMAN, HUMAN, HUMAN): -FIVE_IN_A_ROW_SCORE,
        (None, HUMAN, HUMAN, HUMAN, HUMAN): -BLOCKED_FOUR_SCORE,
        (HUMAN, None, HUMAN, HUMAN, HUMAN): -BLOCKED_FOUR_SCORE,
        (HUMAN, HUMAN, None, HUMAN, HUMAN): -BLOCKED_FOUR_SCORE,
        (HUMAN, HUMAN, HUMAN, None, HUMAN): -BLOCKED_FOUR_SCORE,
        (HUMAN, HUMAN, HUMAN, HUMAN, None): -BLOCKED_FOUR_SCORE,
    }