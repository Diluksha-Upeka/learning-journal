# Computers cannot directly store Python objects like dictionaries or lists.
# Hard disks can store only bytes (0s and 1s).

# student_data = { "id" : 101} will not work

# SERIALIZATION
# Converting Python objects into a byte stream
# Python Dict -> JSON text -> Saved as bytes on disk

# DESERIALIZATION
# Converting byte stream back into Python objects
# Bytes on disk -> JSON text -> Python Dict

# json.dump() -> Python -> JSON -> file
# json.load() -> file -> JSON -> Python

# Limitations of JSON:
# - Can only represent basic data types (no custom objects)
# - Does not support complex data structures like sets or tuples
# - Cannot store Functions or methods

# Json is universal for all programming languages
# Easy to read and write for humans and machines

# Simple structured data - > JSON
# Tables only -> CSV
# Complex structured data -> XML
# Large scalable systems -> Databases