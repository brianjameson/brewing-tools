

class BrewingCalculators:
    def __init__(self):
        pass

    # Returns weigted average of worts of varying volumes and gravities
    def weightedWort(self, volume_list=[1.0], gravity_list=[1.0]):

        # Ensure both lists have the same number of elements before proceeding with calculation
        if len(volume_list) != len(gravity_list):
            return None

        # Catch division by zero
        total_volume = float(sum(volume_list))
        if total_volume == 0:
            return None

        # Multiply corresponding list elements together (similar to SUMPRODUCT in MS Excel)
        # Returns a weighted average
        sumproduct = 0
        for i in range(len(volume_list)):
            sumproduct += (float(volume_list[i]) * float(gravity_list[i]))

        weighted_average = sumproduct/total_volume
        return '{0:.3f}'.format(weighted_average)
