class Constants:
    COMP = 1
    HUMAN = -1
    
    SCORE_DICT_COMP_6 = {
        tuple([None, COMP, COMP, COMP, COMP, None]): 1000,

        tuple([None, COMP, COMP, COMP, None, None]): 100,
        tuple([None, None, COMP, COMP, COMP, None]): 100,
        tuple([None, COMP, None, COMP, COMP, None]): 100,
        tuple([None, COMP, COMP, None, COMP, None]): 100,

        tuple([None, None, COMP, None, COMP, None]): 10,
        tuple([None, None, COMP, COMP, None, None]): 10,
        tuple([None, None, None, COMP, COMP, None]): 10,
        tuple([None, COMP, COMP, None, None, None]): 10,
        tuple([None, COMP, None, COMP, None, None]): 10,
        tuple([None, COMP, None, None, COMP, None]): 10,

        tuple([None, COMP, None, None, None, None]): 1,
        tuple([None, None, COMP, None, None, None]): 1,
        tuple([None, None, None, COMP, None, None]): 1,
        tuple([None, None, None, None, COMP, None]): 1,
    }

    SCORE_DICT_COMP_5 = {
        tuple([COMP, COMP, COMP, COMP, COMP]): 10000,
        tuple([None, COMP, COMP, COMP, COMP]): 150,
        tuple([COMP, None, COMP, COMP, COMP]): 150,
        tuple([COMP, COMP, None, COMP, COMP]): 150,
        tuple([COMP, COMP, COMP, None, COMP]): 150,
        tuple([COMP, COMP, COMP, COMP, None]): 150,
    }

    SCORE_DICT_HUMAN_6 = {
        tuple([None, HUMAN, HUMAN, HUMAN, HUMAN, None]): -1000,
        
        tuple([None, HUMAN, HUMAN, HUMAN, None, None]): -100,
        tuple([None, None, HUMAN, HUMAN, HUMAN, None]): -100,
        tuple([None, HUMAN, None, HUMAN, HUMAN, None]): -100,
        tuple([None, HUMAN, HUMAN, None, HUMAN, None]): -100,

        tuple([None, None, HUMAN, None, HUMAN, None]): -10,
        tuple([None, None, HUMAN, HUMAN, None, None]): -10,
        tuple([None, None, None, HUMAN, HUMAN, None]): -10,
        tuple([None, HUMAN, HUMAN, None, None, None]): -10,
        tuple([None, HUMAN, None, HUMAN, None, None]): -10,
        tuple([None, HUMAN, None, None, HUMAN, None]): -10,

        tuple([None, HUMAN, None, None, None, None]): -1,
        tuple([None, None, HUMAN, None, None, None]): -1,
        tuple([None, None, None, HUMAN, None, None]): -1,
        tuple([None, None, None, None, HUMAN, None]): -1,
    }

    SCORE_DICT_HUMAN_5 = {
        tuple([HUMAN, HUMAN, HUMAN, HUMAN, HUMAN]): -10000,
        tuple([None, HUMAN, HUMAN, HUMAN, HUMAN]): -150,
        tuple([HUMAN, None, HUMAN, HUMAN, HUMAN]): -150,
        tuple([HUMAN, HUMAN, None, HUMAN, HUMAN]): -150,
        tuple([HUMAN, HUMAN, HUMAN, None, HUMAN]): -150,
        tuple([HUMAN, HUMAN, HUMAN, HUMAN, None]): -150,
    }