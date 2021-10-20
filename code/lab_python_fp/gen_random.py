import random


def gen_random(num_count, min, max):
    for i in range(num_count):
        i = random.randint(min, max)
        yield i


a = gen_random(4, 8, 12)

if __name__ == '__main__':
    print(list(a))