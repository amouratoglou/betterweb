#!/usr/bin/env python3
from __future__ import annotations
import os, struct, zlib


def png_chunk(chunk_type: bytes, data: bytes) -> bytes:
    return (
        struct.pack(
            ">I", len(data)
        )
        + chunk_type
        + data
        + struct.pack(
            ">I", zlib.crc32(chunk_type + data) & 0xFFFFFFFF
        )
    )


def solid_png(width: int, height: int, rgba=(230, 0, 0, 255)) -> bytes:
    # PNG signature
    out = [b"\x89PNG\r\n\x1a\n"]
    # IHDR
    ihdr = struct.pack(
        ">IIBBBBB",
        width,
        height,
        8,  # bit depth
        6,  # color type RGBA
        0,  # compression
        0,  # filter
        0,  # interlace
    )
    out.append(png_chunk(b"IHDR", ihdr))
    # IDAT: zlib-compressed scanlines (each row starts with filter byte 0)
    r, g, b, a = rgba
    row = bytes([0, r, g, b, a]) * width  # leading 0 filter + pixel RGBA
    raw = row
    for _ in range(height - 1):
        raw += row
    compressed = zlib.compress(raw, 9)
    out.append(png_chunk(b"IDAT", compressed))
    # IEND
    out.append(png_chunk(b"IEND", b""))
    return b"".join(out)


def write_icon(path: str, size: int, rgba=(230, 0, 0, 255)):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(solid_png(size, size, rgba))


def main():
    base = os.path.join(os.path.dirname(__file__), "..", "youtube-hide-rich-sections", "icons")
    write_icon(os.path.join(base, "16.png"), 16, (230, 0, 0, 255))
    write_icon(os.path.join(base, "48.png"), 48, (230, 0, 0, 255))
    write_icon(os.path.join(base, "128.png"), 128, (230, 0, 0, 255))
    print(f"Wrote icons to {base}")


if __name__ == "__main__":
    main()

