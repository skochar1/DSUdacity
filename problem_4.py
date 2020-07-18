#Active Directory
#In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

class Group(object):
    id_counter = 1
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        self.id = Group.id_counter
        Group.id_counter += 1
        
    #Group.add_group(parent, child)
    #parent.add_group(child)
    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
      
    def get_id(self):
        return self.id


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

#Write a function that provides an efficient look up of whether the user is in a group.

"""
(a) To check if a user is part of a group, we first
look to see if the user is in the users list for 
that group.

(b) If not, then we repeat for every group
in that group's group list.
"""
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    return helper(user, group, {})
    
    
def helper(user, group, seen):
    seen[group.get_id()] = True
    
    if user in group.get_users():
        return True
    
    groups = group.get_groups()  
    for grp in groups:
        if grp.get_id() not in seen:
            is_in_grp = helper(user, grp, seen)
            if is_in_grp:
                return True
    return False