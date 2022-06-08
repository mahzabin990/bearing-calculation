class WCB:
    """
    This class definesWhole Circle Bearing or WCB from a specific formatted string or float.
    It can perform calculations on WCB, like adding or subtracting two or more
    whole circle bearings with addition to comparing between two or more WCB objects.
    The constractor accepts one argument dms.
    * dms stands for degree minute second
    dms can be a
    1. string: say you have a wcb of 130 degree 20 minutes.
        you would pass it in wcb as "130'20''"
    2. if you want to pass the degree in decimals you can pass
        that as integer or float, like 130.666 or 140 etc.

    Example Usage:
        Let's say you have a whole circle bearing of 120 degree 28 minutes.
        If you want to perform calculations on it, you have to make a WCB object
        out of it. Because without a WCB object, python can't understand what 120
        degree 28 minute is!
        So how do you make it?
        well you can represent 120 degree 28 minute as a string formatted in this
        way: you will use one apostrophe (') to represent a degree and two
        apostrophe ('') to represent a minute.
        so 120 degree 28 minutes become: 120'28''
        wrap this in quotes ("") to make a python string so: "120'28''"
        Now you can make a WCB out of it simply calling: WCB("120'28''")

        You can also pass decimal degrees like 257.83832 degrees to WCB so the
        call would be: WCB(257.83832)

        Now you perform calculations with it like:
            WCB("120'28''") - WCB(180)
        would subtract 180 degree from 120 degree 28 minute.
    """
    DEGREE_NOTATION = "'"
    MINUTE_NOTATION = "''"
    SECOND_NOTATION = "'''"
    MINUTE_FACTOR = 60
    SECOND_FACTOR = 3600

    def __init__(self, dms):
        """
        dms stands for degree minute second

        @param dms: can be a string or float or int representing whole circle bearing. If string is passed it should be
        specified in d'm''s''' format.
        """
        if type(dms) == str:
            self.wcb_format = dms
        elif type(dms) in [int, float]:
            self.wcb_format = self.decimal_to_string(dms)

    @property
    def degree(self):
        if self.DEGREE_NOTATION in self.wcb_format:
            index_end = self.wcb_format.find(self.DEGREE_NOTATION)
            return float(self.wcb_format[:index_end])
        return 0

    @property
    def minute(self):
        if self.MINUTE_NOTATION in self.wcb_format:
            index_start = self.wcb_format.find(self.DEGREE_NOTATION) + len(self.DEGREE_NOTATION)
            index_end = self.wcb_format.find(self.MINUTE_NOTATION)
            return float(self.wcb_format[index_start:index_end])
        return 0

    @property
    def second(self):
        if self.SECOND_NOTATION in self.wcb_format:
            index_start = self.wcb_format.find(self.MINUTE_NOTATION) + len(self.MINUTE_NOTATION)
            index_end = self.wcb_format.find(self.SECOND_NOTATION)
            return float(self.wcb_format[index_start:index_end])
        return 0

    @property
    def decimal_degree(self):
        return self.degree + (self.minute / self.MINUTE_FACTOR) + (self.second / self.SECOND_FACTOR)

    @classmethod
    def get_dms_from_decimal_degree(cls, decimal_deg):
        degree = int(decimal_deg)  # whole degree
        minute_decimal = (decimal_deg - degree) * cls.MINUTE_FACTOR
        minute = int(minute_decimal)  # whole minute
        second_decimal = (minute_decimal - minute) * cls.MINUTE_FACTOR
        second = round(second_decimal, 2)  # second to 2 place
        return degree, minute, second

    @classmethod
    def decimal_to_string(cls, decimal_deg):
        degree, minute, second = cls.get_dms_from_decimal_degree(decimal_deg)
        string = f"{degree}{cls.DEGREE_NOTATION}{minute}{cls.MINUTE_NOTATION}{second}{cls.SECOND_NOTATION}"
        return string

    def __repr__(self):
        return f"{self.wcb_format}"

    def __str__(self):
        return f"{self.wcb_format}"

    def __add__(self, other):
        result = self.decimal_degree + other.decimal_degree
        return WCB(self.decimal_to_string(result))

    def __sub__(self, other):
        result = abs(self.decimal_degree - other.decimal_degree)
        return WCB(self.decimal_to_string(result))

    def __eq__(self, other):
        return self.decimal_degree == other.decimal_degree

    def __ge__(self, other):
        return self.decimal_degree >= other.decimal_degree

    def __gt__(self, other):
        return self.decimal_degree > other.decimal_degree

    def __le__(self, other):
        return self.decimal_degree <= other.decimal_degree

    def __lt__(self, other):
        return self.decimal_degree < other.decimal_degree
