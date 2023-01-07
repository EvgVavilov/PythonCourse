

def generate_power(exponent):
    def power(base):
        return str(exponent) + str(base)
    return power

print(generate_power(2)(4))
# raise_two = generate_power(2)
# raise_three = generate_power(3)

# p1 = raise_two(4)
# p2 = raise_three(5)
# print(p1)
# print(p2)
# print(raise_two)
# print(raise_three)
# help(raise_two)
# print(type(raise_two))
# print(type(raise_three))


