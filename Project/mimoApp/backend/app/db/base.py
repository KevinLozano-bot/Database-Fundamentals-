from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    """
    A base class for all SQLAlchemy models.

    This class is used as a base class for all models in the application. By inheriting from this class,
    models will automatically have an `id` field and a dynamically generated `__tablename__` attribute.

    Attributes:
        - id (int): A primary key field for the model (automatically generated).
        - __name__ (str): The name of the model class (used to dynamically generate `__tablename__`).
    
    Methods:
        - __tablename__: A method that generates the table name based on the model class name.
    """
    # Automatically generates an `id` field for the model, which will be the primary key
    id: int
    __name__: str

    @declared_attr
    def __tablename__(self) -> str:
        """
        Dynamically generates the table name based on the model's class name.

        This method uses the name of the model class (which is stored in `self.__class__.__name__`)
        and converts it to lowercase. This ensures that the table name is automatically derived 
        from the class name.

        Returns:
            str: The generated table name for the model.
        """
        return self.__class__.__name__.lower()
