Check Format
Initialize tapes -> GRAPH_TAPE, POWERSET_TAPE, SUBSET_TAPE, TEMP_GRAPH_TAPE, DFS_HISTORY_TAPE, DFS_STACK_TAPE
// POWERSET
WRITE {} to POWERSET_TAPE.head //Empty set
MOVE POWERSET_TAPE.head to the right
WRITE ',' to POWERSET_TAPE.head
RESET GRAPH_TAPE.head to the left most position // To find the links from beginning
MOVE GRAPH_TAPE.head to the right
if GRAPH_TAPE.head.value == "$":
    continue the Algorithm
else: REJECT STATE as there are no strings in the language
    // $ means that is the start of the string
if GRAPH_TAPE is not Null && != n: //the n value is not needed yet.
    MOVE GRAPH_TAPE.head to the right
    for every "|" on GRAPH_TAPE in |^x:
    // Read current edge from tape 1 >> can only be done one at a time
        RESET POWERSET_TAPE.head to the left most position
        // PHASE 1: Copies all sets from tape 2 to tape 3
        While POWERSET_TAPE is not Null:
            for each cell in POWERSET_TAPE:
                MOVE POWERSET_TAPE.head to the right
                WRITE POWERSET_TAPE.head.value to SUBSET_TAPE
                MOVE SUBSET_TAPE.head to the right

        // PHASE 2: This while loop will add the current edge of tape 1 to every subset of tape 3
        while SUBSET_TAPE READS all '}' in }^y:
            // Add current edge of tape 1 to every subset on tape 3 for e.g. (V1,V2,EW)
            // empty set will be ignored
            MOVE SUBSET_TAPE.head to the left && WRITE ',' to SUBSET_TAPE.head if not {} 
            MOVE SUBSET_TAPE.head to the right // currently still reading '}'
            // NOW tape 3 has the correct syntax such as {(SomeRandomEdge),}

            WRITE '(' to SUBSET_TAPE.head && MOVE SUBSET_TAPE.head to the right
            for 5 times COMPUTE: //every 5 cells including commas have a new edge -> V1,V2,EW
                MOVE GRAPH_TAPE.head to the right
                // for e.g. Tape 1 has V1,V2,EW and Tape 2 and tape 3 has {}
                WRITE GRAPH_TAPE.head.value to SUBSET_TAPE.head
                // for e.g. Tape 3 now has {(A,B,1)} 
                MOVE SUBSET_TAPE.head to the right
                // No need to worry about ',' because tape 3 is temporary
                // Tape 3 will always be heading towards '}' so the loop will still iterate
            WRITE ')' to SUBSET_TAPE.head && MOVE SUBSET_TAPE.head to the right

        // PHASE 3: WRITING back all the new sets to tape 2 for e.g.{(A,B,1)} 
        MOVE POWERSET_TAPE.head to the right
        RESET SUBSET_TAPE.head to the left most position
        for every "{" on SUBSET_TAPE:
            for 8 times COMPUTE:
            // every 8 times there is an edge, 8 because of syntax
            // for example Tape 2 now has {}, {(A,B,1)}  
            // 1 -> ( 2 -> A -> 3 -> , 4 -> B 5 -> , 6 -> 1 -> 7 ) -> 8 -> } 
                MOVE SUBSET_TAPE.head to the right
                WRITE SUBSET_TAPE.head.value to POWERSET_TAPE.head
                MOVE POWERSET_TAPE.head to the right
            // Comma is gonna be skipped by the loop because of '{'

for every cell on SUBSET_TAPE: 
    // We can reuse this tape to store the best set of edges
    RESET SUBSET_TAPE.head.value to blank
    RESET SUBSET_TAPE.head to the left most position

// Primary Algorithmic Procedure

// Tape 2 is currently pointing to the last set of the powerset 
// We copied all the data from tape 3 last time
MOVE POWERSET_TAPE.head to the right && WRITE 'W' to POWERSET_TAPE.head.value 
// W indicates weights that we will be calculating and storing
RESET POWERSET_TAPE.head to the left most position
for every subset {}^i on POWERSET_TAPE:
    //PHASE 4: Finding edges and recording them as a temporary graph on Tape 4
    RESET GRAPH_TAPE.head && DFS_HISTORY_TAPE.head to the left most position
    for every cell on GRAPH_TAPE:
        MOVE GRAPH_TAPE.head to the right
        //copying the graph to TEMP_GRAPH_TAPE
        WRITE GRAPH_TAPE.head.value to TEMP_GRAPH_TAPE.head 
        MOVE TEMP_GRAPH_TAPE.head to the right
        //copying the graph to DFS_HISTORY_TAPE to keep track of vertex.visited history
        WRITE GRAPH_TAPE.head.value to DFS_HISTORY_TAPE.head 
        MOVE DFS_HISTORY_TAPE.head to the right

    for each '(X,Y,EW)' edge in subset(skipCells=6): //skip every 6 cells for new edge
         // PHASE 5: Computing Edge Weights
         // subset can have multiple edges due to powerset nature.
        RESET POWERSET_TAPE.head to the leftmost position
        RESET TEMP_GRAPH_TAPE.head to the left most position // for traversing operations
        for every "W" in cells^Z ON POWERSET_TAPE: 
        // Z is 1 because we have only 1 W that represents the start of edge weight counts
            if POWERSET_TAPE.head.value == 'W' ||  POWERSET_TAPE.head.value == '_': // total weight will be after
                MODIFY POWERSET_TAPE.head.value to "@" // so that the next iterations don't pick W (only pick blank)
                MOVE POWERSET_TAPE.head to the left Z times // now we have the edge weight
                // Because we are doing 2 things (UNBOUNDED) on the tape we will need to read the data
                READ POWERSET_TAPE.head.value as edgeWeight // record that cell as a reference  
                MOVE POWERSET_TAPE.head to the right Z+1 times // Z+1 is after W to write data
                // Currently the head is blank
                
                // head is pointing to where it needs already
                for (POWERSET_TAPE.head.value + edgeWeight) times COMPUTE: 
                    // total_weight = total_weight + edge.weight
                    //the head is null (0) so 0 + EW is valid
                    WRITE 1 to POWERSET_TAPE.head.value 
                    MOVE POWERSET_TAPE.head to the right
            // for the loop to continue for the next subset
            MOVE POWERSET_TAPE.head to the left Z + 1 + (POWERSET_TAPE.head.value + edgeWeight) times 
            MOVE POWERSET_TAPE.head 2 times to the right 
            // to skip the extra brackets '),(' in {(A,B,1),(A,B,1)} then the loop will iterate again 6 times

        // PHASE 6: Let's remove the edge
        MOVE POWERSET_TAPE.head 2 times to the left // because after the last subset, there aren't any brackets
        // Now we have the edge weight value from the subset of a powerset
        MOVE TEMP_GRAPH_TAPE.head to the right // Skipping $
        // The point of this loop is to find a specific edge 
        for each '|V1,V2,EW' in edges on TEMP_GRAPH_TAPE(skip=6): // it will skip the cells 6 times
            // comparing the edge weights
            if TEMP_GRAPH_TAPE.head.value == POWERSET_TAPE.head.value: 
                // To have the value of the first verticies
                MOVE POWERSET_TAPE.head && TEMP_GRAPH_TAPE.head to the left 4 times 
                    // Comparing first verticies
                    if TEMP_GRAPH_TAPE.head.value == POWERSET_TAPE.head.value: 
                        // To have the value of the Second verticies
                        MOVE POWERSET_TAPE.head && TEMP_GRAPH_TAPE.head to the right 2 times 
                        // Comparing Second verticies
                        if TEMP_GRAPH_TAPE.head.value == POWERSET_TAPE.head.value: 
                            // removing the edge
                            MOVE TEMP_GRAPH_TAPE.head to the left 3 times // finding the start of the edge '|'
                            for every cell till first "|" on TEMP_GRAPH_TAPE: // Terminate once '|' has been seen
                                EMPTY TEMP_GRAPH_TAPE.head 

    // PHASE 7: Depth-First Search
    RESET TEMP_GRAPH_TAPE.head && DFS_HISTORY_TAPE.head to the left most position
    MOVE TEMP_GRAPH_TAPE.head && DFS_HISTORY_TAPE.head to the right // skip $
    FOR every cell on DFS_HISTORY_TAPE: 
     // Instead of "|" which indicates the start of a string, we put "F" as its vertex history
        if cell == "|": 
            MODIFY DFS_HISTORY_TAPE.head.value to "F" //Vertex 1 visit history of edge 1
        elif cell == ",": //so it will skip the commas before EW to account for the next edge
            MODIFY DFS_HISTORY_TAPE.head.value to "F" //Vertex 2 visit history of edge 1

    MOVE DFS_HISTORY_TAPE.head to the rightmost position + 1 // Move on to the next unused cell
    WRITE "C" to DFS_HISTORY_TAPE.head // To indicate the start of a counter 
    FOR each '|V1,V2,EW' edge^w on TEMP_GRAPH_TAPE(skip=6): 
        FOR each "F" in cells^Y on DFS_HISTORY_TAPE: // Considers each visited vertex
            IF DFS_HISTORY_TAPE.head.value == "F": // If vertex.visited is False
                MODIFY DFS_HISTORY_TAPE.head.value to "T" // Update Vertex.visited to True
                FOR every cell in cells^D on DFS_HISTORY_TAPE:
                    // Increment Counter
                    IF cell == "C": // There is only one 'C', so skip the cells to find C
                    //There could be ones in there already
                        FOR every cell in cells^G on DFS_HISTORY_TAPE(until=_): //find the empty cell
                            MOVE DFS_HISTORY_TAPE.head to the right //Move on to the next unused cell
                            WRITE 1 to DFS_HISTORY_TAPE.head // Keep track and incrementing count with 1's
                MOVE DFS_HISTORY_TAPE.head to the left D + G times // RESET head for future use
                RESET GRAPH_TAPE.head to the left most position
                // USING TAPE 1 HERE to not complicate other tapes
                MOVE GRAPH_TAPE.head to the right 3 times // to get the start vertex
                // Push Start_Vertex onto DFS_STACK_TAPE (our stack). start_vertex is just the first edge
                WRITE (GRAPH_TAPE.head.value) to DFS_STACK_TAPE.head
                // MOVE DFS_STACK_TAPE.head to the right prolly don't need it
                RESET GRAPH_TAPE.head to the left most position

                // NOTE: we only traversed Y times so we have not lost track 
                RESET DFS_HISTORY_TAPE.head to the leftmost position 
                // NOTE: we only traversed w times so we have not lost track 
                RESET TEMP_GRAPH_TAPE.head to the leftmost position 

                while DFS_STACK_TAPE is ! Null: // ! is 'not' // While stack is not empty
                    // for the following 2 loops, we will either find vertex 1 or vertex 2
                    for each "|" on DFS_HISTORY_TAPE:
                        for each "|" on GRAPH_TAPE:// we have start vertex from tape 1
                            MOVE DFS_HISTORY_TAPE.head && GRAPH_TAPE.head to the right// Finding V1
                            // IF tape's 5 vertex 1 == tape's 1 vertex 1
                            if DFS_HISTORY_TAPE.head.value == GRAPH_TAPE.head.value: 
                                    // We now have our current vertex position
                                    continue the Algorithm
                            else: // if it cannot find the current vertex from vertex 1 then find it from the second vertex
                                  // for e.g (V1,V2,EW) is our edge, our current vertex could be in either V1 or V2
                                RESET DFS_HISTORY_TAPE.head && GRAPH_TAPE.head to the leftmost position
                                for each "," on DFS_HISTORY_TAPE:
                                    for each "," on GRAPH_TAPE:// we have start vertex from tape 1
                                        MOVE DFS_HISTORY_TAPE.head && GRAPH_TAPE.head to the right// Finding V2
                                        // IF tape's 5 vertex 2 == tape's 1 vertex 2
                                        if DFS_HISTORY_TAPE.head.value == GRAPH_TAPE.head.value: 
                                                // We now have our current vertex position
                                                continue the Algorithm
                    // If "current_vertex" is not visited:
                    //I am only checking the status of the first vertex of an edge, not the second yet
                    IF DFS_HISTORY_TAPE.head.value == "F": 
                        MODIFY DFS_HISTORY_TAPE.head.value to "T" //Mark it as visited

                    // Pop the top vertex "current_vertex" from DFS_STACK_TAPE
                    MOVE DFS_STACK_TAPE.head to the rightmost position
                    EMPTY DFS_STACK_TAPE.head.value to blank // Pop the vertex
                    ADJUST DFS_STACK_TAPE.head // This will make sure that the right-most position is recalculated
                
                    RESET DFS_HISTORY_TAPE.head to the leftmost position
                    // Read all adjacent vertices of current_vertex
                    for every cell on DFS_HISTORY_TAPE:
                        // tape 1 has the current vertex that guides this part
                        if DFS_HISTORY_TAPE.head.value == GRAPH_TAPE.head.value: 
                            // Reading the second vertex visited history
                            MOVE DFS_HISTORY_TAPE.head to the right  // To read the status of the adjacent vertex
                            // If V is not visited:
                            if DFS_HISTORY_TAPE.head.value == "F":
                                // Push V onto Tape_D (our stack).
                                WRITE (DFS_HISTORY_TAPE.head.value) to DFS_STACK_TAPE.head
                                // END of DFS

            //Move head for the next iterations of loop
            MOVE DFS_HISTORY_TAPE.head to the left Y times 
        MOVE TEMP_GRAPH_TAPE.head to the left W times
    
    // PHASE 8: Checking edge validity and Updating Optimal subset
    RESET GRAPH_TAPE.head to the left most position

    MOVE GRAPH_TAPE.head to the right until (GRAPH_TAPE.head.value == "n") // START OF N
    MOVE DFS_HISTORY_TAPE.head to the right until (GRAPH_TAPE.head.value == "C") // START OF COUNTER
    
    //currently counting
    for every cell on DFS_HISTORY_TAPE:
        // checking compatibility
        MOVE GRAPH_TAPE.head to the right  //stores n
        MOVE DFS_HISTORY_TAPE.head to the right // stores count
    // if n == count
    if GRAPH_TAPE.head == 1 && DFS_HISTORY_TAPE.head == 1:
        MOVE DFS_HISTORY_TAPE.head to the left
        // count > 1
        if DFS_HISTORY_TAPE.head != "@" // then count is greater than 1
            // anything after @ on tape 2 is the total weight
            MOVE POWERSET_TAPE.head to the right till "@" is found
            for every cell on DFS_HISTORY_TAPE:
                MOVE DFS_HISTORY_TAPE.head to the right // Serves as total_weight
                MOVE SUBSET_TAPE.head to the right // Tape 3 will serves as our optimal weight
            MOVE DFS_HISTORY_TAPE.head to the right
            // total_weight > optimal_weight then

            if DFS_HISTORY_TAPE.head == 1: // A continous number of ones signified the total weight
            // We don't need to care about the weight because it is in the set and we have a poweset
                EMPTY SUBSET_TAPE to blank for all cells // RESET tape to store optimal subset
                // store the subset
                for each '(X,Y,EW)' edge in subset {}:
                    //optimal subset
                    WRITE edge subvalues (X,Y,EW) to SUBSET_TAPE.head.value && MOVE SUBSET_TAPE.head to the right 
                    WRITE "," to SUBSET_TAPE.head.value && MOVE SUBSET_TAPE.head to the right
            else:
                continue the Algorithm

    // RESETINGtape 2's head for the next iteration
    MOVE POWERSET_TAPE to next subset {} i

ACCEPT STATE on SUBSET_TAPE // Tape 3 has the optimal subset with minimal weights