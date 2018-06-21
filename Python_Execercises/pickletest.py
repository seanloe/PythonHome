import pickle

a_list = { "mimi":23,"loe_family":{"sean":45,"cynthia":42},"jacky":41}

#with open('haha.pickle','wb') as f:
#    pickle.dump(a_list,f)
with open('haha.pickle','rb') as f:
    my_dict = pickle.load(f)
print(my_dict)
