from user import *

class Privileges ( ) :

    def __init__ ( self ,privileges='can add user'):
        self.privileges = [ ]
        self.privileges.append ( privileges )

    def show_privilege ( self ) :
        print('User Admin has following privileges:')
        for privilege in self.privileges :
            print('-' ,privilege.title())


class Admin ( User ) :

    def __init__ ( self , first_name , last_name  ) :
        super().__init__ ( first_name , last_name )
        self.privileges = Privileges ( )

    def store_privilege ( self , privilege) :
        self.privileges.privileges.append(privilege)

