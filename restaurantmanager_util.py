def parse_line(line):
    """
    Parses a single line of the yelp file, keeping some of the
    data, and throwing away the rest.
    """
    line = line.strip('\n')
    values = line.split('|')
    
    result = [ values[0], \
               values[1], \
               values[2], \
               values[3], \
               ]
    return result


def read_restaurants(filename):
    """
    Parses the given filename containing yelp data and
    returns a list of restaurants. Each item is a list containing 
    restaurant information.
    """
    restaurants = []
    for line in open(filename):
        new_r = parse_line(line)
        restaurants.append(new_r)
    return restaurants