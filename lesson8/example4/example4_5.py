# from first_package import inner_element
# import first_package

# print(inner_element.CONSTANT_5)

# print(first_package.CONSTANT_5)

# from second_package import module1

import second_package

from second_package.package_3.package_5 import example_deep_3

if __name__ == '__main__':
    print(second_package.inner_variable)
    print(example_deep_3.item)
