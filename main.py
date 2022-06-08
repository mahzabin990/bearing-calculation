from wcb import WCB
from parse_csv import Parser


def calc_back_bearing(forward_bearing) -> WCB:
    """
    This function accepts a parameter called forward_bearing and
    returns the back_bearing.
    steps:
        1. used WCB to make the forward_bearing a Whole Circle Bearing object.
        2. use surveying logics to calculate the back_bearing
        3. return the calculated back_bearing.
        @param forward_bearing: a string in d'm''s''' format or a str/float representing wcb in degree decimal
        @return: back_bearing: a WCB object
    """
    fb = WCB(forward_bearing)
    one_eighty = WCB(180)
    if fb > one_eighty:
        back_bearing = fb - one_eighty
    else:
        back_bearing = fb + one_eighty
    return back_bearing


def get_back_bearings(forward_bearings):
    """
    This function accepts a list of forward_bearings and
    returns a list of back_bearings, using the help of  calc_back_bearing function from above.
    steps:
        1. declare an empty list of back_bearings.
        2. loop through the forward_bearings
        3. in each iteration, use the calc_back_bearing function to calculate
            the back_bearing.
        4. append this back_bearing to your back_bearings list.
    """
    back_bearings = []
    for fb in forward_bearings:
        back_bearing = calc_back_bearing(fb)
        back_bearings.append(back_bearing)

    return back_bearings


def main():
    parser = Parser(file='forward_bearings.csv')
    forward_bearings = parser.forward_bearings
    back_bearings = get_back_bearings(forward_bearings)
    parser.generate_solution(data=back_bearings)
    print('`solution.csv` file is generated.')


if __name__ == '__main__':
    main()
