# I would recommend always using parenthese
# to indicate start and end  of tuple
# even though parenthese are optional
# Explicit is better than implicit.
zoo = ('python', 'elephant', 'penguin')
print('No of Animals in the zoo: ', len(zoo))

new_zoo= 'monkey', 'camel', zoo #perentheses not required   but are good idea
print('Number of cages in the new zoo is: ', len(new_zoo))
print('All Animals in the New zoo are: ', new_zoo)
print('Animals brought from old zoo were: ', new_zoo[2])
print('Last Animal brought from old zoo was: ', new_zoo[2][2])
print('Number of Animals in the new zoo is ', len(new_zoo)-1+len(new_zoo[2]))