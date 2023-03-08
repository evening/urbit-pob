# urbit-pob

A python implementation of [urbit-ob](https://github.com/urbit/urbit-ob)

### Install

Run `pip install urbitob`

### Module Use

The library exposes two families of functions:

* `patp / patp_to_num / patp_to_hex / hex_to_patp / is_valid_patp`
* `patq / patq_to_num / patq_to_hex / hex_to_patq / is_valid_patq`

As well as:

* `clan`, for determining the ship class of a `@p` value
* `sein`, for determining the parent of a `@p` value
* `eq_patq`, for comparing `@q` values for equality
* `is_valid_pat`, for a faster/weaker check of `@p` or `@q`-ness that only
  validates syllables (and not proper dash formatting)

### Example Usage

```py
>>> import urbitob as ob
>>> ob.patp(0)
'~zod'
>>> ob.patp_to_num('~nidsut-tomdun')
15663360
>>> ob.hex_to_patq(010203)
'~doznec-binwes'
>>> ob.patq_to_hex('~marned-wismul-nilsev-botnyt')
'01ca0e51d20462f3'
>>> ob.is_valid_patp('~marned-wismul-nilsev-botnyt')
True
>>> ob.clan('~marzod')
'star'
>>> ob.sein('~marzod')
'~zod'
```

### Testing

A simple `python -m unittest` will run the test suite.
