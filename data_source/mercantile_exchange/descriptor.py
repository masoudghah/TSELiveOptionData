class Token:
    def __set_name__(self, owner, name):
        self.storage_name = name

    def __set__(self, instance, value: str):
        if isinstance(value, str) and len(value) > 1:
            instance.__dict__[self.storage_name] = value
        else:
            msg = f'Invalid value ({value}) for {self.storage_name}: must be a string with length greater than 1.'
            raise ValueError(msg)

    def __get__(self, instance, owner):
        if instance:
            return instance.__dict__.get(self.storage_name, None)
        return self
