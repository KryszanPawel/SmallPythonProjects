import fileinput


def define_file() -> list:
    """Extracts lines from input file"""
    # extract lines from input file
    # and contain strings in list without "\n" and "\r".
    file_input = [line.replace('\n', '').replace('\r', '')
                  for line in fileinput.input()]
    # as farther modernization of code, I would add exception handling of empty
    # or invalid input file
    return file_input


class Permutation:
    """Returns the lowest cost of permutation using .result method"""

    def __init__(self, file: list):
        """ Initializes Permutation Object with path to .in file """
        self.file = file
        self.number_of_elephants = int(self.file[0])
        # list of elephants masses
        self.mass_list = [int(mass) for mass in self.file[1].split(' ')]
        # actual arrangement
        self.actual_position = [int(inline_position) - 1
                                for inline_position in self.file[2].split(' ')]
        # target arrangement
        self.target_position = [int(inline_position) - 1
                                for inline_position in self.file[3].split(' ')]
        # define permutation
        self.permutation_list = self.create_permutation()
        # creates permutation cycles
        self.cycles = self.define_cycles()
        # list of cycles parameters and min weight
        self.cycles_parameters, self.minimum_weight = self.define_cycles_parameters()
        # lowest cost of rearrangement
        self.result = self.calculate_result()

    def create_permutation(self) -> list:
        """Returns list of permutation values"""
        permutation = [0 for _ in range(self.number_of_elephants)]
        for i in range(self.number_of_elephants):
            permutation[self.target_position[i]] = self.actual_position[i]
        return permutation

    def define_cycles(self) -> list:
        """Defines permutation cycles"""
        # array of booleans to define end of cycle
        end_cycle = [False for _ in range(self.number_of_elephants)]
        # list of cycles
        cycles = [[] for _ in range(self.number_of_elephants)]
        # number of permutation cycles
        cycle_counter = 0
        for i in range(self.number_of_elephants):
            if not end_cycle[i]:
                cycle_counter += 1
                elephant_index = i
                while not end_cycle[elephant_index]:
                    end_cycle[elephant_index] = True
                    cycles[cycle_counter - 1].append(elephant_index)
                    elephant_index = self.permutation_list[elephant_index]
        # delete cycles with zero or one elephant, cost = 0
        cycles = [cycle for cycle in cycles if len(cycle) > 1]
        return cycles

    def define_cycles_parameters(self) -> tuple:
        """Returns List of dictionaries with parameters of
        permutation cycles and min weight in elephant
        mass_list"""
        minimum_weight = min(self.mass_list)
        parameters = []
        for i, cycle in enumerate(self.cycles):
            sum_in_cycle_i = 0
            minimal_weight_in_cycle_i = float('inf')
            for elephant in cycle:
                sum_in_cycle_i += self.mass_list[elephant]
                minimal_weight_in_cycle_i = min(minimal_weight_in_cycle_i, self.mass_list[elephant])
            parameters_for_cycle_i = {'sum_in_cycle_i': sum_in_cycle_i,
                                      'min_weight_in_cycle_i': minimal_weight_in_cycle_i,
                                      'length_of_cycle_i': len(self.cycles[i])}
            parameters.append(parameters_for_cycle_i)
        return parameters, minimum_weight

    def calculate_result(self) -> int:
        """Returns the lowest value of permutation cost"""
        result = 0
        for i in range(len(self.cycles)):
            method_1_cycle_i = self.cycles_parameters[i]['sum_in_cycle_i'] + \
                               (self.cycles_parameters[i]['length_of_cycle_i'] - 2) * \
                               self.cycles_parameters[i]['min_weight_in_cycle_i']
            method_2_cycle_i = self.cycles_parameters[i]['sum_in_cycle_i'] + \
                               self.cycles_parameters[i]['min_weight_in_cycle_i'] + \
                               (self.cycles_parameters[i]['length_of_cycle_i'] + 1) * \
                               self.minimum_weight
            result += min(method_1_cycle_i, method_2_cycle_i)
        return result


if __name__ == "__main__":
    solver = Permutation(define_file())
    print(solver.result)
