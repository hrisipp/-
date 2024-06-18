immutable_var_tuple_ = 13, 'Hello', True
print(immutable_var_tuple_)
#immutable_var_tuple_[0] = 200 (нельзя изменить, потому что программа выдает TypeError)
mutable_list = [1, 15, 'hello']
mutable_list[0] = 13
print(mutable_list)