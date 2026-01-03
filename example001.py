import numpy as np

def main():
    # create a 1D array
    a = np.array([1, 2, 3, 4])
    print("a:", a)

    # elementwise operations
    print("a * 2:", a * 2)
    print("a + 5:", a + 5)

    # reshape to 2x2 and matrix multiply
    b = a.reshape((2, 2))
    print("b:\n", b)
    print("b @ b.T:\n", b @ b.T)

    # basic statistics
    print("mean:", a.mean(), "std:", a.std())

    # random array (repeatable)
    rng = np.random.default_rng(0)
    r = rng.normal(size=(3, 3))
    print("random 3x3:\n", r)

if __name__ == "__main__":
    main()