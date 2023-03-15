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
        tuple([None, COMP, COMP, COMP, COMP, None]): FOUR_IN_A_ROW_SCORE,

        tuple([None, COMP, COMP, COMP, None, None]): THREE_IN_A_ROW_SCORE,
        tuple([None, None, COMP, COMP, COMP, None]): THREE_IN_A_ROW_SCORE,
        tuple([None, COMP, None, COMP, COMP, None]): THREE_IN_A_ROW_SCORE,
        tuple([None, COMP, COMP, None, COMP, None]): THREE_IN_A_ROW_SCORE,

        tuple([None, None, COMP, None, COMP, None]): OPEN_TWO_SCORE,
        tuple([None, None, COMP, COMP, None, None]): OPEN_TWO_SCORE,
        tuple([None, None, None, COMP, COMP, None]): OPEN_TWO_SCORE,
        tuple([None, COMP, COMP, None, None, None]): OPEN_TWO_SCORE,
        tuple([None, COMP, None, COMP, None, None]): OPEN_TWO_SCORE,
        tuple([None, COMP, None, None, COMP, None]): OPEN_TWO_SCORE,

        tuple([None, COMP, None, None, None, None]): OPEN_ONE_SCORE,
        tuple([None, None, COMP, None, None, None]): OPEN_ONE_SCORE,
        tuple([None, None, None, COMP, None, None]): OPEN_ONE_SCORE,
        tuple([None, None, None, None, COMP, None]): OPEN_ONE_SCORE,
    }

    SCORE_DICT_COMP_5 = {
        tuple([COMP, COMP, COMP, COMP, COMP]): FIVE_IN_A_ROW_SCORE,
        tuple([None, COMP, COMP, COMP, COMP]): BLOCKED_FOUR_SCORE,
        tuple([COMP, None, COMP, COMP, COMP]): BLOCKED_FOUR_SCORE,
        tuple([COMP, COMP, None, COMP, COMP]): BLOCKED_FOUR_SCORE,
        tuple([COMP, COMP, COMP, None, COMP]): BLOCKED_FOUR_SCORE,
        tuple([COMP, COMP, COMP, COMP, None]): BLOCKED_FOUR_SCORE,
    }

    SCORE_DICT_HUMAN_6 = {
        tuple([None, HUMAN, HUMAN, HUMAN, HUMAN, None]): -FOUR_IN_A_ROW_SCORE,
        
        tuple([None, HUMAN, HUMAN, HUMAN, None, None]): -THREE_IN_A_ROW_SCORE,
        tuple([None, None, HUMAN, HUMAN, HUMAN, None]): -THREE_IN_A_ROW_SCORE,
        tuple([None, HUMAN, None, HUMAN, HUMAN, None]): -THREE_IN_A_ROW_SCORE,
        tuple([None, HUMAN, HUMAN, None, HUMAN, None]): -THREE_IN_A_ROW_SCORE,

        tuple([None, None, HUMAN, None, HUMAN, None]): -OPEN_TWO_SCORE,
        tuple([None, None, HUMAN, HUMAN, None, None]): -OPEN_TWO_SCORE,
        tuple([None, None, None, HUMAN, HUMAN, None]): -OPEN_TWO_SCORE,
        tuple([None, HUMAN, HUMAN, None, None, None]): -OPEN_TWO_SCORE,
        tuple([None, HUMAN, None, HUMAN, None, None]): -OPEN_TWO_SCORE,
        tuple([None, HUMAN, None, None, HUMAN, None]): -OPEN_TWO_SCORE,

        tuple([None, HUMAN, None, None, None, None]): -OPEN_ONE_SCORE,
        tuple([None, None, HUMAN, None, None, None]): -OPEN_ONE_SCORE,
        tuple([None, None, None, HUMAN, None, None]): -OPEN_ONE_SCORE,
        tuple([None, None, None, None, HUMAN, None]): -OPEN_ONE_SCORE,
    }

    SCORE_DICT_HUMAN_5 = {
        tuple([HUMAN, HUMAN, HUMAN, HUMAN, HUMAN]): -FIVE_IN_A_ROW_SCORE,
        tuple([None, HUMAN, HUMAN, HUMAN, HUMAN]): -BLOCKED_FOUR_SCORE,
        tuple([HUMAN, None, HUMAN, HUMAN, HUMAN]): -BLOCKED_FOUR_SCORE,
        tuple([HUMAN, HUMAN, None, HUMAN, HUMAN]): -BLOCKED_FOUR_SCORE,
        tuple([HUMAN, HUMAN, HUMAN, None, HUMAN]): -BLOCKED_FOUR_SCORE,
        tuple([HUMAN, HUMAN, HUMAN, HUMAN, None]): -BLOCKED_FOUR_SCORE,
    }