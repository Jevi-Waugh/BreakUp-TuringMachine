Check Format //0(1)
Initialize tapes -> GRAPH_TAPE, POWERSET_TAPE, SUBSET_TAPE, TEMP_GRAPH_TAPE, DFS_HISTORY_TAPE, DFS_STACK_TAPE//0(1)
WRITE {} to POWERSET_TAPE.head //0(1)
MOVE POWERSET_TAPE.head to the right//0(1)
WRITE ',' to POWERSET_TAPE.head//0(1)
RESET GRAPH_TAPE.head to the left most position//0(1)
MOVE GRAPH_TAPE.head to the right//0(1)
if GRAPH_TAPE.head.value == "$"://0(1)
    continue the Algorithm//0(1)
else://0(1)
    REJECT STATE as there are no strings in the language//0(1)
if GRAPH_TAPE is not Null && != n://0(1)
    MOVE GRAPH_TAPE.head to the right//0(1)
    // All above is O(1)
    // Time complexity
    for every "|" on GRAPH_TAPE in |^x: //O(n)
        RESET POWERSET_TAPE.head to the left most position//0(1)

        // Powerset Time complexity
        While POWERSET_TAPE is not Null: // O(2^n)
            for each cell in POWERSET_TAPE://0(1)
                MOVE POWERSET_TAPE.head to the right//0(1)
                WRITE POWERSET_TAPE.head.value to SUBSET_TAPE//0(1)
                MOVE SUBSET_TAPE.head to the right//0(1)

        // Subset Tape Time complexity
        while SUBSET_TAPE READS all '}' in }^y: // O(2^n-1)
   
            MOVE SUBSET_TAPE.head to the left && WRITE ',' to SUBSET_TAPE.head if not {} //0(1)
            MOVE SUBSET_TAPE.head to the right//0(1)
            WRITE '(' to SUBSET_TAPE.head && MOVE SUBSET_TAPE.head to the right//0(1)
            // Time complexity
            for 5 times COMPUTE: //0(5) -> 0(1)
                MOVE GRAPH_TAPE.head to the right//0(1)
                WRITE GRAPH_TAPE.head.value to SUBSET_TAPE.head//0(1)
                MOVE SUBSET_TAPE.head to the right//0(1)

            WRITE ')' to SUBSET_TAPE.head && MOVE SUBSET_TAPE.head to the right//0(1)

        MOVE POWERSET_TAPE.head to the right//0(1)
        RESET SUBSET_TAPE.head to the left most position//0(1)
        // Time complexity
        for every "{" on SUBSET_TAPE:
            // Time complexity
            for 8 times COMPUTE: //0(8) -> 0(1)
                MOVE SUBSET_TAPE.head to the right//0(1)
                WRITE SUBSET_TAPE.head.value to POWERSET_TAPE.head//0(1)
                MOVE POWERSET_TAPE.head to the right//0(1)
// Time complexity
for every cell on SUBSET_TAPE: // O(2^n-1)
    RESET SUBSET_TAPE.head.value to blank//0(1)
    RESET SUBSET_TAPE.head to the left most position//0(1)


MOVE POWERSET_TAPE.head to the right && WRITE 'W' to POWERSET_TAPE.head.value //0(1)
RESET POWERSET_TAPE.head to the left most position //0(1)
// Time complexity
for every subset {}^i on POWERSET_TAPE: // O(2^n)
    RESET GRAPH_TAPE.head && DFS_HISTORY_TAPE.head to the left most position //0(1)
    // Time complexity
    for every cell on GRAPH_TAPE: //0(n)
        MOVE GRAPH_TAPE.head to the right //0(1)
        WRITE GRAPH_TAPE.head.value to TEMP_GRAPH_TAPE.head //0(1)
        MOVE TEMP_GRAPH_TAPE.head to the right //0(1)
        WRITE GRAPH_TAPE.head.value to DFS_HISTORY_TAPE.head //0(1)
        MOVE DFS_HISTORY_TAPE.head to the right //0(1)
    // Time complexity
    for each '(X,Y,EW)' edge in subset(skipCells=6):// maximum edge in subset is 0(n)
        RESET POWERSET_TAPE.head to the leftmost position //0(1)
        RESET TEMP_GRAPH_TAPE.head to the left most position //0(1)
        // Time complexity
        for every "W" in cells^Z ON POWERSET_TAPE: // O(2^n)
            if POWERSET_TAPE.head.value == 'W' ||  POWERSET_TAPE.head.value == '_': //0(1)
                MODIFY POWERSET_TAPE.head.value to "@" //0(1)
                MOVE POWERSET_TAPE.head to the left Z times //0(1)
                READ POWERSET_TAPE.head.value as edgeWeight  //0(1)
                MOVE POWERSET_TAPE.head to the right Z+1 times // 0(Z+1)
                // Time complexity
                for (POWERSET_TAPE.head.value + edgeWeight) times COMPUTE: // 0(1)
                    WRITE 1 to POWERSET_TAPE.head.value  //0(1)
                    MOVE POWERSET_TAPE.head to the right //0(1)
            MOVE POWERSET_TAPE.head to the left Z + 1 + (POWERSET_TAPE.head.value + edgeWeight) times // 0(1)
            MOVE POWERSET_TAPE.head 2 times to the right // 0(1)

        MOVE POWERSET_TAPE.head 2 times to the left // 0(1)
        MOVE TEMP_GRAPH_TAPE.head to the right // 0(1)
        // Time complexity
        for each '|V1,V2,EW' in edges on TEMP_GRAPH_TAPE(skip=6): // 0(n)

            if TEMP_GRAPH_TAPE.head.value == POWERSET_TAPE.head.value: // 0(1)
                MOVE POWERSET_TAPE.head && TEMP_GRAPH_TAPE.head to the left 4 times // 0(1)
                    if TEMP_GRAPH_TAPE.head.value == POWERSET_TAPE.head.value: // 0(1)
                        MOVE POWERSET_TAPE.head && TEMP_GRAPH_TAPE.head to the right 2 times // 0(1)
                        if TEMP_GRAPH_TAPE.head.value == POWERSET_TAPE.head.value: // 0(1)
                            // Time complexity
                            for every cell till first "|" on TEMP_GRAPH_TAPE: // 0(n)
                                EMPTY TEMP_GRAPH_TAPE.head // 0(1)

    RESET TEMP_GRAPH_TAPE.head && DFS_HISTORY_TAPE.head to the left most position // 0(1)
    MOVE TEMP_GRAPH_TAPE.head && DFS_HISTORY_TAPE.head to the right // 0(1)
    // Time complexity
    FOR every cell on DFS_HISTORY_TAPE: // 0(n)
        if cell == "|": // 0(1)
            MODIFY DFS_HISTORY_TAPE.head.value to "F" // 0(1)
        elif cell == ",": // 0(1)
            MODIFY DFS_HISTORY_TAPE.head.value to "F" // 0(1)
    
    MOVE DFS_HISTORY_TAPE.head to the rightmost position + 1 // 0(1)
    WRITE "C" to DFS_HISTORY_TAPE.head // 0(1)
    // Time complexity
    FOR each '|V1,V2,EW' edge^w on TEMP_GRAPH_TAPE(skip=6): // 0(n)
        // Time complexity
        FOR each "F" in cells^Y on DFS_HISTORY_TAPE: // 0(n)
            IF DFS_HISTORY_TAPE.head.value == "F": // 0(1)
                MODIFY DFS_HISTORY_TAPE.head.value to "T" // 0(1)
                // Time complexity
                FOR every cell in cells^D on DFS_HISTORY_TAPE:// 0(n)
                    IF cell == "C": // 0(1)
                        // Time complexity
                        FOR every cell in cells^G on DFS_HISTORY_TAPE(until=_): // 0(n)
                            MOVE DFS_HISTORY_TAPE.head to the right // 0(1)
                            WRITE 1 to DFS_HISTORY_TAPE.head // 0(1)
                MOVE DFS_HISTORY_TAPE.head to the left D + G times // 0(D) + 0(G)
                RESET GRAPH_TAPE.head to the left most position // 0(1)
                MOVE GRAPH_TAPE.head to the right 3 times // 0(1)
                WRITE (GRAPH_TAPE.head.value) to DFS_STACK_TAPE.head // 0(1)
                RESET GRAPH_TAPE.head to the left most position // 0(1)
                RESET DFS_HISTORY_TAPE.head to the leftmost position // 0(1)
                RESET TEMP_GRAPH_TAPE.head to the leftmost position // 0(1)

                // Time complexity
                for each "|" on DFS_HISTORY_TAPE: // 0(n)
                    // Time complexity
                    for each "|" on GRAPH_TAPE: // 0(n)
                        MOVE DFS_HISTORY_TAPE.head && GRAPH_TAPE.head to the right // 0(1)
                        if DFS_HISTORY_TAPE.head.value == GRAPH_TAPE.head.value:  // 0(1)
                                continue the Algorithm // 0(1)
                        else:  // 0(1)
                            RESET DFS_HISTORY_TAPE.head && GRAPH_TAPE.head to the leftmost position // 0(1)
                            // Time complexity
                            for each "," on DFS_HISTORY_TAPE: // 0(n)
                                for each "," on GRAPH_TAPE: // 0(n)
                                    MOVE DFS_HISTORY_TAPE.head && GRAPH_TAPE.head to the right // 0(1)
                                    if DFS_HISTORY_TAPE.head.value == GRAPH_TAPE.head.value:  // 0(1)
                                            continue the Algorithm // 0(1)
                IF DFS_HISTORY_TAPE.head.value == "F":  // 0(1)
                    MODIFY DFS_HISTORY_TAPE.head.value to "T" // 0(1)
                MOVE DFS_STACK_TAPE.head to the rightmost position // 0(1)
                EMPTY DFS_STACK_TAPE.head.value to blank // 0(1)
                ADJUST DFS_STACK_TAPE.head // 0(1)
            
                RESET DFS_HISTORY_TAPE.head to the leftmost position // 0(1)
                // Time complexity
                for every cell on DFS_HISTORY_TAPE:  // 0(n)
                    if DFS_HISTORY_TAPE.head.value == GRAPH_TAPE.head.value:  // 0(1)
                        MOVE DFS_HISTORY_TAPE.head to the right // 0(1)
                        if DFS_HISTORY_TAPE.head.value == "F": // 0(1)
                            WRITE (DFS_HISTORY_TAPE.head.value) to DFS_STACK_TAPE.head // 0(1)
            MOVE DFS_HISTORY_TAPE.head to the left Y times  // 0(Y)
        MOVE TEMP_GRAPH_TAPE.head to the left W times // 0(W)
    RESET GRAPH_TAPE.head to the left most position  // 0(1)

    MOVE GRAPH_TAPE.head to the right until (GRAPH_TAPE.head.value == "n") // 0(n)
    MOVE DFS_HISTORY_TAPE.head to the right until (GRAPH_TAPE.head.value == "C") // 0(n)
    // Time complexity
    for every cell on DFS_HISTORY_TAPE:// 0(n)
        MOVE GRAPH_TAPE.head to the right // 0(1)
        MOVE DFS_HISTORY_TAPE.head to the right // 0(1)

    if GRAPH_TAPE.head == 1 && DFS_HISTORY_TAPE.head == 1: // 0(1)
        MOVE DFS_HISTORY_TAPE.head to the left // 0(1)
    
        if DFS_HISTORY_TAPE.head != "@": // 0(1)
            MOVE POWERSET_TAPE.head to the right till "@" is found // 0(1)
            // Time complexity
            for every cell on DFS_HISTORY_TAPE: // 0(n)
                MOVE DFS_HISTORY_TAPE.head to the right // 0(1)
                MOVE SUBSET_TAPE.head to the right // 0(1)
            MOVE DFS_HISTORY_TAPE.head to the right // 0(1)
            
            if DFS_HISTORY_TAPE.head == 1: // 0(1)
                EMPTY SUBSET_TAPE to blank for all cells // 0(n)
                // Time complexity
                for each '(X,Y,EW)' edge in subset {}: // 0(n)
                    WRITE edge subvalues (X,Y,EW) to SUBSET_TAPE.head.value && MOVE SUBSET_TAPE.head to the right // 0(1)
                    WRITE "," to SUBSET_TAPE.head.value && MOVE SUBSET_TAPE.head to the right // 0(1)
            else: // 0(1)
                continue the Algorithm // 0(1)

    MOVE POWERSET_TAPE to next subset {} i // 0(1)

ACCEPT STATE on SUBSET_TAPE // 0(1)