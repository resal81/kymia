"""
This module provides Atom and AtomType classes.
"""


class ImmutableProperty(AttributeError):
    """ Raised when a read-only property is attempted to be changed. """
    pass


class AttributeIsNotSet(ValueError):
    """ Raised when a not-set attribute is requested. """
    pass


class WrongTypeForOverloading(ValueError):
    """ Raised when the expected `other` in special methods is not of the same type. """
    pass


PDB_FORMAT = {
    'ATOM': dict(
        aserial   = slice(6, 11),
        aname     = slice(12, 16),
        alt       = slice(16, 17),
        rname     = slice(17, 21),
        chain     = slice(21, 22),
        rserial   = slice(22, 26),
        coordx    = slice(30, 38),
        coordy    = slice(38, 46),
        coordz    = slice(46, 54),
        occupancy = slice(54, 60),
        bfactor   = slice(60, 66),
        segment   = slice(72, 76),
        element   = slice(76, 78),
        charge    = slice(78, 80)
    )
}


class AtomType:
    def __init__(self, label: str):
        """ AtomType. Once you set an attribute, it becomes read-only. """

        self.__label          = label
        self.__protons        = None
        self.__mass           = None
        self.__lj_dist        = None
        self.__lj_energy      = None
        self.__lj_dist14      = None
        self.__lj_energy14    = None
        self.__charge         = None
        self.__partial_charge = None
        self.__radius         = None

    # ----------------------------
    # laebel
    # ----------------------------

    @property
    def label():
        return self.__label

    @label.setter
    def label(self, _):
        raise ImmutableProperty

    # ----------------------------
    # special methods
    # ----------------------------

    def __eq__(self, other):
        if not isinstance(other, AtomType):
            raise WrongTypeForOverloading

        return self.label == other.label

    def __hash__(self):
        return hash(self.label)


class Atom:
    def __init__(self, name: str, serial: int):
        """ Atom class. Once you set each attribute, it becomes read-only. """

        self.__name          = name
        self.__serial        = serial
        self.__bfactor       = None
        self.__occupancy     = None
        self.__alt_loc       = None
        self.__is_hetero     = None
        self.__type          = None
        self.__source_format = None  # pdb, pqr, ...

    # ----------------------------
    # builders
    # ----------------------------

    @classmethod
    def from_pdb_line(cls, line):
        pass

    @classmethod
    def from_pqr_line(cls, line):
        pass

    # ----------------------------
    # name
    # ----------------------------

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, _):
        raise ImmutableProperty

    # ----------------------------
    # serial
    # ----------------------------

    @property
    def serial(self):
        return self.__serial

    @serial.setter
    def serial(self, _):
        raise ImmutableProperty

    # ----------------------------
    # type
    # ----------------------------

    @property
    def type(self):
        if self.__type is None:
            raise AttributeIsNotSet
        return self.__type

    @type.setter
    def type(self, val):
        if self.__type is not None:
            raise ImmutableProperty

        if isinstance(val, AtomType):
            raise WrongTypeForOverloading

        self.__type = val

    # ----------------------------
    # bfactor
    # ----------------------------

    @property
    def bfactor(self):
        if self.__bfactor is None:
            raise AttributeIsNotSet
        return self.__bfactor

    @bfactor.setter
    def bfactor(self, val: float):
        if self.__bfactor is not None:
            raise ImmutableProperty
        self.__bfactor = val

    # ----------------------------
    # special methods
    # ----------------------------

    def __iter__(self):
        """ Can be used for example in `name, serial = Atom('C', 12)`. """

        return (i for i in (self.name, self.serial))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, self.name, self.serial)

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        if not isinstance(other, Atom):
            raise WrongTypeForOverloading

        cmp = [getattr(self, v) == getattr(other, v) for v in ('name', 'serial', 'type')]
        return all(cmp)

    def __hash__(self):
        return hash(self.name) ^ hash(self.type)




