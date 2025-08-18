class StudentManager: 
    def __init__(self):
        self.students = []

    def add(self, list_id : int, new_student : str) -> None:
        """
        Adds a new student to the specified list.
        
        Parameters:
        -----
        list_id (int): The ID of the list to which the student will be added.
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
        
        self.students[list_id].append(new_student.lower())

    def sort_students_alphabetically(self):
        """
        Sorts the internal student list by surname, then by name,
        using the list's sort() method.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Raises
        -------
        Exception: If an error occurs during sorting.

        Examples
        --------
        >>> sort_students_alphabetically([{"name": "Mario", "surname": "Rossi"}, {"name": "Luca", "surname": "Bianchi"}])
        >>> # Result: Student list sorted by surname and name.
        """

        try:
            self.students.sort(key=lambda s: (s["surname"].lower(), s["name"].lower()))
            print("Student list sorted successfully")

        except Exception as e:
            print("Error while sorting the student list:", e)

    def search(self, list_id : int, student_name : str) -> bool:
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
        return student_name.lower() in self.students[list_id]