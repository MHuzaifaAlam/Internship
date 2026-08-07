#User Configuration Manager that allows users to manage their settings such as theme, 
# language, and notifications. You will implement functions to add, update, delete, and view u

def add_setting(settings,key_value):
    key,value=key_value
    key=key.lower()
    value=value.lower()
    if key in settings:
        return f"the {key} already exist! Cannot add new"
    else:
        settings[key]=value
        return f"{key} addes sucessfully with value{value}"

def update_setting(settings,key_value):
    key,value=key_value
    key=key.lower() 
    value=value.lower()
    if key in settings:
        settings[key]=value
        return f"{key} sucessfully updates with value{value}"
    return f"{key} value not updted didnot find the value in the key "

def delete_setting(setting,key):
    if key in setting:
        del setting[key]
        return f"the {key} is deletes sucessfully ] "
    return f"{key}doesnot exists"

def view_setting(setting,key):
    if not setting:
        return f"No setting is avilable"
    result="Current user settings /" 
    for key,value in setting.items():
        result+=f"{key.capitalize()} : {value} \n"
    return result 

test_settings = {'theme': 'light', 'language': 'english', 'notifications': 'enabled'}
print(add_setting(test_settings,("hello","1")))
print((test_settings,1))