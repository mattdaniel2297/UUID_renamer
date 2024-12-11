import pyexiv2


print(pyexiv2.exiv2_version_info)

print(pyexiv2.version_info)

metadata = pyexiv2.ImageMetadata('images/photos/bec37a7a97774b27a9e8472a4fe4321d.jpeg')
metadata.read()
# print(metadata.exif_keys)
print(metadata.xmp_keys)
keys = metadata.xmp_keys
if 'Xmp.digiKam.TagsList' in keys:
    print("YES")
    tag = metadata['Xmp.digiKam.TagsList']
    print(tag)
    print(type(tag))
    print(tag.raw_value)
    value = tag.raw_value
    print(type(value))
    value.append('Matt')
    tag.raw_value = value
    metadata.write()