# Create Class 
class Employee:

    # Initializing 
    def _init_(self):
        print('Employee created')

    # Calling destructor 
    def _del_(self):
        print("Destructor called")

def Create_obj():
    print('Making object...')
    obj = Employee()
    print('function end...')
    return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')
