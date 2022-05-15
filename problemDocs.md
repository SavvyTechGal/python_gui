# Documentation of Problems
Details of problems encountered throughout the project and how they were solved

## Example Format:
# Problem 1 - Savana Hughes - Occurred 05/04/22
    Description: Layout of components were conflicting with aspects each contributor had created. 
    Solution: Created a Grid Layout system for our gui, so that each component can be added to a specifc row/col of the main window. Each component can have its own defined layout, as long as it is inserted in the main window grid at the appropriate location. 

# Problem 2 - Moris Goldshtein - Occurred 05/04/22
    Description: In GridLayout, spanning 3 columns for the music track slider created a limitation for increasing the width of the slider. If a user friendly size was used, the MainWindow changed size along with the widths of the buttons above the slider. 
    Solution: Spanning 5 columns starting at col 0 gives far more leeway for increasing the width of the slider as we now cannot go beyond the width of the layout without causing the same problem, which would not be intended anyway. The only caveat is to make sure that a selected width prevents the slider from touching the labels next to it, which has been done. 

# Problem 3 - Moris Goldshtein - Occurred 05/11/22
    Description: The Wave library that provides a means for extracting raw sound data for the procedure of generating a Matplot display wave for a song does not work for mp3 files. Only wav files work, but mp3 files need to be supported.
    Solution: Research revealed that the pydub library has a function that extracts raw sound data from mp3 files. It has been imported for the implementation.
