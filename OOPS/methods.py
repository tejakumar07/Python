# 1️⃣ Instance Method (Normal Method)

# Uses self, works with instance attributes.

'''
class Example:
    def instance_method(self):
        return f"Called on {self}"

obj = Example()
print(obj.instance_method())  # ✅ Called on instance

❌ Cannot be called directly on the class:

print(Example.instance_method())  # ❌ ERROR: Needs an instance

'''

# 2️⃣ Class Method (@classmethod)

# 💡 Uses self, works with instance attributes.

'''
class Example:
    class_variable = "Hello"

    @classmethod
    def class_method(cls):
        return f"Class method called, class_variable = {cls.class_variable}"

print(Example.class_method())  # ✅ Can be called on class

✅ Also works on an instance:
obj = Example()
print(obj.class_method())  # ✅ Can be called on instance too

'''

# 3️⃣ Static Method (@staticmethod)

# Does not use self or cls, just a normal function inside the class.

'''
class Example:
    @staticmethod
    def static_method():
        return "Static method called"

print(Example.static_method())  # ✅ Can be called on class

✅ Also works on an instance:

obj = Example()
print(obj.static_method())  # ✅ Can be called on instance too

'''

# 4️⃣ Other Method Types

# 🔹 @property (Getter)
# Allows accessing methods like an attribute.
# Read-only property

'''
class Example:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name  # No need for () when calling!

obj = Example("Alice")
print(obj.name)  # ✅ No parentheses needed

🔹 @name.setter (Setter)
Allows modifying the property value.

class Example:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

obj = Example("Alice")
obj.name = "Bob"  # ✅ Setter modifies name
print(obj.name)  # ✅ Bob

'''

class Example:
    class_variable = "Class Variable"

    def __init__(self, name):
        self.name = name  # Instance variable

    # Instance Method (uses self)
    def instance_method(self):
        return f"Called on {self.name}"

    # Class Method (uses cls)
    @classmethod
    def class_method(cls):
        return f"Class method, class_variable = {cls.class_variable}"

    # Static Method (does not use self or cls)
    @staticmethod
    def static_method():
        return "This is a static method"

    # Property (getter)
    @property
    def name_upper(self):
        return self.name.upper()

    # Property (setter)
    @name_upper.setter
    def name_upper(self, new_name):
        self.name = new_name.lower()

# ✅ Calling methods
obj = Example("Alice")
print(obj.instance_method())  # Instance method
print(Example.class_method())  # Class method
print(obj.class_method())  # Class method (on instance)
print(Example.static_method())  # Static method
print(obj.name_upper)  # Property (getter)
obj.name_upper = "BOB"  # Property (setter)
print(obj.name)  # Bob