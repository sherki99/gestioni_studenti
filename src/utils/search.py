def search(list_id : int, student_name : str, student_lists : list[list]) -> bool:
    """
    Searches for a student in the specified list by name.
    
    Parameters:
    -----
    list_id (int): The ID of the list to search in.
    student_name (str): The name of the student to search for.
    student_lists (list[list]): A list containing all student lists.

    Returns:
    -----
    bool: True if the student is found, False otherwise.

    Examples:
    ---------
    >>> student_lists = [["Alice", "Bob"], ["Charlie"]]
    >>> search(0, "David", student_lists)
    False
    >>> search(1, "Charlie", student_lists)
    True
    """
    return student_name.lower() in student_lists[list_id]