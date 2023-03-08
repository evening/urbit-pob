import mmh3


def _f(j: int, key: int) -> int:
    raku = [0xB76D5EED, 0xEE281300, 0x85BCAE01, 0x4B387AF7]
    lo, hi = key & 0xFF, (key & 0xFF00) // 0x100
    return mmh3.hash(bytes([lo, hi]), raku[j], signed=False)


def _loop_hi_lo_init(v):
    lo = v & 0xFFFFFFFF
    hi = v & 0xFFFFFFFF00000000
    return hi, lo


def _feis(m: int) -> int:
    c = _fe(4, 65535, 65536, m)
    return c if c < 0xFFFFFFFF else _fe(4, 65535, 65536, c)


def _fe(r: int, a: int, b: int, m: int) -> int:
    right, left = divmod(m, a)
    return _fe_loop(r, a, b, 1, left, right)


def _fe_loop(r: int, a: int, b: int, j: int, ell: int, arr: int):
    if j > r:
        if r % 2 != 0 or arr == a:
            return (a * arr) + ell
        return (a * ell) + arr
    eff = _f(j - 1, arr)
    tmp = ell + eff
    use_value = b if j % 2 == 0 else a
    tmp = tmp % use_value
    return _fe_loop(r, a, b, j + 1, arr, tmp)


def _fen_loop(a: int, b: int, j: int, ell: int, arr: int) -> int:
    if j < 1:
        return (a * arr) + ell
    eff = _f(j - 1, ell)
    use_value = b if j % 2 == 0 else a
    tmp = (arr + use_value - (eff % use_value)) % use_value
    return _fen_loop(a, b, j - 1, tmp, ell)


def _fen(r: int, a: int, b: int, m: int) -> int:
    ale, ahh = divmod(m, a)
    if r % 2 == 1:
        ale, ahh = ahh, ale
    return _fen_loop(a, b, r, ale, ahh)


def _tail(v: int) -> int:
    c = _fen(4, 65535, 65536, v)
    return c if c < 0xFFFFFFFF else _fen(4, 65535, 65536, c)


def fein(pyn: int) -> int:
    hi, lo = _loop_hi_lo_init(pyn)
    if 0x10000 <= pyn <= 0xFFFFFFFF:
        return 0x10000 + _feis(pyn - 0x10000)
    if 0x100000000 <= pyn <= 0xFFFFFFFFFFFFFFFF:
        return hi | fein(lo)
    return pyn


def fynd(cry: int) -> int:
    hi, lo = _loop_hi_lo_init(cry)
    if 0x10000 <= cry <= 0xFFFFFFFF:
        return 0x10000 + _tail(cry - 0x10000)
    if 0x100000000 <= cry <= 0xFFFFFFFFFFFFFFFF:
        return hi | fynd(lo)
    return cry
