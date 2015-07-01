"""
This module provides Atom and AtomType classes.
"""


class AtomImmutableProperty(AttributeError):
    """ This is raised when a read-only property is
        attempted to be changed.
    """

PDB_FORMAT = {
    'ATOM': dict(
        aserial=slice(6, 11),
        aname=slice(12, 16),
        alt=slice(16, 17),
        rname=slice(17, 21),
        chain=slice(21, 22),
        rserial=slice(22, 26),
        coordx=slice(30, 38),
        coordy=slice(38, 46),
        coordz=slice(46, 54),
        occupancy=slice(54, 60),
        bfactor=slice(60, 66),
        segment=slice(72, 76),
        element=slice(76, 78),
        charge=slice(78, 80)
    )
}


class AtomType:
    def __init__(self, label: str):
        """ AtomType. Once you set an attribute, it becomes read-only. """

        self._label = label
        self._protons = None
        self._mass = None
        self._lj_dist = None
        self._lj_energy = None
        self._lj_dist14 = None
        self._lj_energy14 = None
        self._charge = None
        self._partial_charge = None
        self._radius = None


class Atom:
    def __init__(self, name: str, serial: int):
        """ Atom class. Once you set each attribute, it becomes read-only. """

        self._name = name
        self._serial = serial
        self._bfactor = None
        self._occupancy = None
        self._alt_loc = None
        self._is_hetero = None
        self._type = None

        self._source_format = None  # pdb, pqr, ...

    # -------------
    # builders
    # -------------

    @classmethod
    def from_pdb_line(cls, line):
        pass

    @classmethod
    def from_pqr_line(cls, line):
        pass

    # -------------
    # name
    # -------------

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _):
        raise AtomImmutableProperty("name is already set.")

    @name.deleter
    def name(self):
        raise AttributeError("name cannot be deleted")

    # -------------
    # bfactor
    # -------------
    @property
    def bfactor(self):
        if self._bfactor is None:
            raise ValueError("bfactor has not been set")
        return self._bfactor

    @bfactor.setter
    def bfactor(self, val: float):
        if self._bfactor is not None:
            raise AttributeError("bfactor is already set.")
        self._bfactor = val

    @bfactor.deleter
    def bfactor(self):
        raise AttributeError("bfactor cannot be deleted")
