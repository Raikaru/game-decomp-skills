# GameCube / Wii / PowerPC Functional Notes

- Use DOL/REL analysis for behavior and system boundaries, not copied implementation.
- Watch C++ ABI behavior, object lifecycle, small data, floating point, scheduler assumptions, and asset/archive formats.
- Keep platform services separate so later PC-port work can use `functional-decomp-port`.
- Record provenance for signatures, SDK-like names, and public docs.
