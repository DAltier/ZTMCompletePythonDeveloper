# short circuiting

is_friend = True
is_user = True

# if is_friend is True, the "or" skips checking the is_user and defaults to "True"
if is_friend or is_user:
    print('best friends forever')
    
# if is_friends is False, the "and" skips checking the is_user and defaults to "False"
if is_friend and is_user:
    print('best friends forever')