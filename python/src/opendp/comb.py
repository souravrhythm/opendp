# Auto-generated. Do not edit.
from opendp._convert import *
from opendp._lib import *
from opendp.mod import *
from opendp.typing import *


def make_chain_mt(
    measurement: Measurement,
    transformation: Transformation
) -> Measurement:
    """Construct the functional composition (`measurement` ○ `transformation`). Returns a Measurement.
    
    :param measurement: outer privatizer
    :type measurement: Measurement
    :param transformation: inner query
    :type transformation: Transformation
    :return: Measurement representing the chained computation.
    :rtype: Measurement
    :raises AssertionError: if an argument's type differs from the expected type
    :raises UnknownTypeError: if a type-argument fails to parse
    :raises OpenDPException: packaged error from the core OpenDP library
    """
    # No type arguments to standardize.
    # Convert arguments to c types.
    measurement = py_to_c(measurement, c_type=Measurement)
    transformation = py_to_c(transformation, c_type=Transformation)
    
    # Call library function.
    function = lib.opendp_comb__make_chain_mt
    function.argtypes = [Measurement, Transformation]
    function.restype = FfiResult
    
    return c_to_py(unwrap(function(measurement, transformation), Measurement))


def make_chain_tt(
    transformation1: Transformation,
    transformation0: Transformation
) -> Transformation:
    """Construct the functional composition (`transformation1` ○ `transformation0`). Returns a Tranformation.
    
    :param transformation1: outer transformation
    :type transformation1: Transformation
    :param transformation0: inner transformation
    :type transformation0: Transformation
    :return: Transformation representing the chained computation.
    :rtype: Transformation
    :raises AssertionError: if an argument's type differs from the expected type
    :raises UnknownTypeError: if a type-argument fails to parse
    :raises OpenDPException: packaged error from the core OpenDP library
    """
    # No type arguments to standardize.
    # Convert arguments to c types.
    transformation1 = py_to_c(transformation1, c_type=Transformation)
    transformation0 = py_to_c(transformation0, c_type=Transformation)
    
    # Call library function.
    function = lib.opendp_comb__make_chain_tt
    function.argtypes = [Transformation, Transformation]
    function.restype = FfiResult
    
    return c_to_py(unwrap(function(transformation1, transformation0), Transformation))


def make_basic_composition(
    measurement0: Measurement,
    measurement1: Measurement
) -> Measurement:
    """Construct the DP composition (`measurement0`, `measurement1`). Returns a Measurement.
    
    :param measurement0: The left member of the resulting 2-tuple.
    :type measurement0: Measurement
    :param measurement1: The right member of the resulting 2-tuple.
    :type measurement1: Measurement
    :return: Measurement representing the composed transformations.
    :rtype: Measurement
    :raises AssertionError: if an argument's type differs from the expected type
    :raises UnknownTypeError: if a type-argument fails to parse
    :raises OpenDPException: packaged error from the core OpenDP library
    """
    # No type arguments to standardize.
    # Convert arguments to c types.
    measurement0 = py_to_c(measurement0, c_type=Measurement)
    measurement1 = py_to_c(measurement1, c_type=Measurement)
    
    # Call library function.
    function = lib.opendp_comb__make_basic_composition
    function.argtypes = [Measurement, Measurement]
    function.restype = FfiResult
    
    return c_to_py(unwrap(function(measurement0, measurement1), Measurement))


def make_population_amplification(
    measurement: Measurement,
    n_population: int,
    DIA: RuntimeTypeDescriptor,
    MO: RuntimeTypeDescriptor
) -> Measurement:
    """Construct an amplified measurement from a `measurement` with privacy amplification by subsampling.
    
    :param measurement: The measurement to amplify.
    :type measurement: Measurement
    :param n_population: Number of records in population.
    :type n_population: int
    :param DIA: atomic input domain
    :type DIA: RuntimeTypeDescriptor
    :param MO: output measure
    :type MO: RuntimeTypeDescriptor
    :return: New measurement with the same function, but an adjusted privacy relation.
    :rtype: Measurement
    :raises AssertionError: if an argument's type differs from the expected type
    :raises UnknownTypeError: if a type-argument fails to parse
    :raises OpenDPException: packaged error from the core OpenDP library
    """
    # Standardize type arguments.
    DIA = RuntimeType.parse(type_name=DIA)
    MO = RuntimeType.parse(type_name=MO)
    
    # Convert arguments to c types.
    measurement = py_to_c(measurement, c_type=Measurement)
    n_population = py_to_c(n_population, c_type=ctypes.c_uint)
    DIA = py_to_c(DIA, c_type=ctypes.c_char_p)
    MO = py_to_c(MO, c_type=ctypes.c_char_p)
    
    # Call library function.
    function = lib.opendp_comb__make_population_amplification
    function.argtypes = [Measurement, ctypes.c_uint, ctypes.c_char_p, ctypes.c_char_p]
    function.restype = FfiResult
    
    return c_to_py(unwrap(function(measurement, n_population, DIA, MO), Measurement))
