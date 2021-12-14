from __future__ import annotations

import numpy as np
import pytest

from dask_awkward.utils import assert_eq

from .helpers import (  # noqa: F401
    line_delim_records_file,
    load_records_eager,
    load_records_lazy,
)


def test_ufunc_add(line_delim_records_file) -> None:  # noqa: F811
    daa = load_records_lazy(line_delim_records_file).analysis.x1
    caa = load_records_eager(line_delim_records_file).analysis.x1
    a1 = daa + 2
    a2 = caa + 2
    assert_eq(a1, a2)


def test_ufunc_sin(line_delim_records_file) -> None:  # noqa: F811
    daa = load_records_lazy(line_delim_records_file).analysis.x1
    caa = load_records_eager(line_delim_records_file).analysis.x1
    a1 = np.sin(daa)
    a2 = np.sin(caa)
    assert_eq(a1, a2)


@pytest.mark.parametrize("f", [np.add.accumulate, np.add.reduce])
def test_ufunc_method_raise(line_delim_records_file, f) -> None:  # noqa: F811
    daa = load_records_lazy(line_delim_records_file).analysis.x1
    with pytest.raises(NotImplementedError, match="Array ufunc supports only method"):
        f(daa, daa)
