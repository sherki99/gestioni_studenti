def add(list_id, new_student, student_lists):
    """
    Adds a new student to the specified list.
    
    Parameters:
    -----
    list_id (str): The ID of the list to which the student will be added.
    new_student (str): A string containing the student's name and surname.
    student_lists (list[list]): A list containing all student lists.
    
    Returns:
    -----
    list[list]: The updated list of student lists with the new student added.
    
    Examples:
    ---------
    >>> student_lists = [["Alice", "Bob"], ["Charlie"]]
    >>> add(0, "David", student_lists)
    [['Alice', 'Bob', 'David'], ['Charlie']]
    """
    
    student_lists[list_id].append(new_student)
    return student_lists