import json


class Q:
    def __init__(self, **params):
        self._params = params
        self.complete_string = ''

    def __or__(self, other):
        temp_str = ' OR '

        if 'invert' in other._params:
            temp_str = temp_str + ' NOT '
            del other._params['invert']

        temp = other._params

        if self.complete_string:  # if str == '' don't run
            self.complete_string += temp_str

        if not self.complete_string:
            self.complete_string += str(self._params) + temp_str + str(temp)
        else:
            self.complete_string += str(temp)

        return self

    def __and__(self, other):

        temp_str = ' AND '

        if 'invert' in other._params:
            temp_str = temp_str + ' NOT '
            del other._params['invert']

        temp = other._params

        if self.complete_string:  # if str == '' don't run
            self.complete_string += temp_str

        if not self.complete_string:
            self.complete_string += str(self._params) + temp_str + str(temp)
        else:
            self.complete_string += str(temp)

        return self

    def __invert__(self):
        self._params['invert'] = True
        return self

    def __str__(self):
        return self.complete_string


filter = Q()
filter = (Q(first_name='John') | Q(last_name='Gonzalez')) & ~Q(first_name='John2') & ~Q(last_name='Gonzale2')
# filter |= ~Q(stuff=True)
# filter |= Q(age=42)

# filter = Q()
# filter &= Q(first_name='John2')
# filter &= Q(last_name='Gonzalez2')
# filter &= Q(stuff=True)
# filter &= Q(age=42)

# filter != Q(dwada w)
print(str(filter))
# print(filter2)
