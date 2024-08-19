# Python Program

print("Hello World")

'''@overload def print(*values: object,
          sep: str | None = " ",
          end: str | None = "\n",
          file: SupportsWrite[str] | None = None,
          flush: Literal[False] = False) -> None

Prints the values to a stream, or to sys. stdout by default.

sep
string inserted between values, default a space.
end
string appended after the last value, default a newline.
file
a file-like object (stream); defaults to the current sys. stdout.
flush
whether to forcibly flush the stream.
print(*values, sep=" ", end="\n", file=None, flush=False)` on docs. python. org '''

print("Hi", "pc", 123, sep="?", end="_")
print("pc")
