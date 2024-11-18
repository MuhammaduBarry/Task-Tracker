def task(id: int, description: str, status: str, createdAt: str, updatedAt: str):
    """Create a new task

    Args:
        id (int): id
        description (str): description
        status (str): status
        createdAt (str): createdAt
        updatedAt (str): updatedAt

    Returns:
        dict: returns a new dict
    """
    new_task = {
        "id": id,
        "description": description,
        "status": status,
        "createdAt": createdAt,
        "updatedAt": updatedAt
    }

    return new_task
