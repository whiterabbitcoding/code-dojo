# For the ng practical test


class MovingTotal:
    structure = []
    moving_totals = []
    current_index = 0

    def generate(self):
        if len(self.structure) < 3:
            return None
        else:
            for i in range(0, len(self.structure) - 2):
                print(i)
                self.moving_totals.append(sum(self.structure[i : i + 3]))
                self.current_index += 1

        print(self.moving_totals)

    def append(self, numbers):
        """
        :param numbers: (list) The list of numbers.
        """
        self.structure = self.structure + numbers
        self.moving_totals = []
        for i in range(self.current_index, self.current_index + len(numbers)):
            sub_array = self.structure[i - 2 : i + 1]
            print(sub_array)
            print(self.moving_totals)
            self.moving_totals.append(sum(sub_array))
            self.current_index += 1

        # self.generate()

    def contains(self, total):
        """
        :param total: (int) The total to check for.
        :returns: (bool) If MovingTotal contains the total.
        """
        return True if total in self.moving_totals else False


if __name__ == "__main__":
    movingtotal = MovingTotal()

    movingtotal.append([1, 2, 3, 4])
    # movingtotal.generate()
    movingtotal.append([5])
    print(movingtotal.contains(6))
    print(movingtotal.contains(9))
    print(movingtotal.contains(12))
    assert movingtotal.contains(9) is True
    assert movingtotal.contains(12) is True
    assert movingtotal.contains(7) is False
    print(movingtotal.contains(7))
