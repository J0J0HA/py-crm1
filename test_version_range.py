"""Test the VersionRange class and related functions."""

from crm1.helpers.versions import Version, VersionRange, range_from_maven_string


range1 = VersionRange.from_string("[1.0,2.0.1)")
print(range1.lower, range1.lower_mode)
# 1.0.0 VersionEndMode.INCLUSIVE
print(range1.upper, range1.upper_mode)
# 2.0.1 VersionEndMode.EXCLUSIVE

range2 = VersionRange.from_string("(1.0,]")
print(range2.lower, range2.lower_mode)
# 1.0.0 VersionEndMode.EXCLUSIVE
print(range2.upper, range2.upper_mode)
# None VersionEndMode.INCLUSIVE

vers1 = Version.from_string("1.0")
vers2 = Version.from_string("2.0.1")
vers3 = Version.from_string("20.1")

print(vers1 in range1)
# True
print(vers2 in range1)
# False
print(vers3 in range1)
# False
print(vers1 in range2)
# False
print(vers2 in range2)
# True
print(vers3 in range2)
# True


print(str(range_from_maven_string(">=1.0")))
# [1.0.0,)
print(str(range_from_maven_string(">1.0")))
# (1.0.0,)
print(str(range_from_maven_string("<1.0")))
# (,1.0.0)
print(str(range_from_maven_string("<=1.0")))
# (,1.0.0]
print(str(range_from_maven_string("1.0")))
# 1.0.0
print(str(range_from_maven_string("*")))
# (,)