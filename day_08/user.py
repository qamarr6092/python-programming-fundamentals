class User ( ) :

    def __init__ ( self, first_name , last_name ) :
        self.first_name = first_name.title().strip()
        self.last_name =  last_name.title( ).strip( )
        self.login_attempts = 0

    def increment_login_attempts ( self ) :
        self.login_attempts += 1
    
    def reset_login_attempts ( self ) :
        self.login_attempts = 0

    def describe_user ( self ) :
        print('User Information' )
        print('First Name :' ,self.first_name)
        print('Last Name :' , self.last_name )
        print('Login attempts =' ,self.login_attempts )

