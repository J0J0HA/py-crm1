"""Test the VersionRange class and related functions."""

from crm1.helpers.versions import (
    Version,
    VersionEndMode,
    VersionRange,
    range_from_maven_string,
)


class TestVersionRange:
    def test_from_string(self):
        range1 = VersionRange.from_string("[1.0,2.0.1)")
        assert range1.lower == Version.from_string("1.0")
        assert range1.lower_mode == VersionEndMode.INCLUSIVE
        assert range1.upper == Version.from_string("2.0.1")
        assert range1.upper_mode == VersionEndMode.EXCLUSIVE

        range2 = VersionRange.from_string("(1.0,]")
        assert range2.lower == Version.from_string("1.0")
        assert range2.lower_mode == VersionEndMode.EXCLUSIVE
        assert range2.upper is None
        assert range2.upper_mode == VersionEndMode.INCLUSIVE

    def test_contains(self):
        vers1 = Version.from_string("1.0")
        vers2 = Version.from_string("2.0.1")
        vers3 = Version.from_string("20.1")
        range1 = VersionRange.from_string("[1.0,2.0.1)")

        assert vers1 in range1
        assert vers2 not in range1
        assert vers3 not in range1

        range2 = VersionRange.from_string("(1.0,]")
        assert vers1 not in range2
        assert vers2 in range2
        assert vers3 in range2
        
    def test_to_string(self):
        range1 = VersionRange.from_string("[1.0,2.0.1)")
        assert str(range1) == "[1.0.0,2.0.1)"
        
        range2 = VersionRange.from_string("(1.0,]")
        assert str(range2) == "(1.0.0,)"
        
        range3 = VersionRange.from_string("(,1.0]")
        assert str(range3) == "(,1.0.0]"
        
        range4 = VersionRange.from_string("(,)")
        assert str(range4) == "(,)"
        
        range5 = VersionRange.from_string("1.0")
        assert str(range5) == "1.0.0"
        
    def test_from_maven_string(self):
        assert str(range_from_maven_string(">=1.0")) == "[1.0.0,)"
        assert str(range_from_maven_string(">1.0")) == "(1.0.0,)"
        assert str(range_from_maven_string("<1.0")) == "(,1.0.0)"
        assert str(range_from_maven_string("<=1.0")) == "(,1.0.0]"
        assert str(range_from_maven_string("1.0")) == "1.0.0"
        assert str(range_from_maven_string("*")) == "(,)"
    
    def test_checks(self):
        v1 = Version.from_string("1.0")
        v2 = Version.from_string("1.0.0")
        v3 = Version.from_string("1.0.1")
        
        assert v1 == v2
        assert v1 < v3
        assert v3 > v1
        assert v1 != v3
        assert v1 <= v2
        assert v1 <= v3
        assert v3 >= v1
        assert v3 >= v2
        assert v1 >= v2
        
    def test_less_than(self):
        v_1_0_0_r1_22 = Version.from_string("1.0.0-r1+22")
        v_1_0_0_r1_33 = Version.from_string("1.0.0-r1+33")
        v_1_0_0_r2_22 = Version.from_string("1.0.0-r2+22")
        
        assert v_1_0_0_r1_22 == v_1_0_0_r1_33
        assert v_1_0_0_r1_22 < v_1_0_0_r2_22
        assert v_1_0_0_r1_33 < v_1_0_0_r2_22
        
        v_1_0_0_alpha_1 = Version.from_string("1.0.0-alpha.1")
        v_1_0_0_alpha_2 = Version.from_string("1.0.0-alpha.2")
        v_1_0_0_beta_1 = Version.from_string("1.0.0-beta.1")
        
        assert v_1_0_0_alpha_1 < v_1_0_0_alpha_2
        assert v_1_0_0_alpha_1 < v_1_0_0_beta_1
        assert v_1_0_0_alpha_2 < v_1_0_0_beta_1
        
        v_1_0_0 = Version.from_string("1.0.0")
        v_1_0_1 = Version.from_string("1.0.1")
        v_1_1_0 = Version.from_string("1.1.0")
        
        assert v_1_0_0 < v_1_0_1
        assert v_1_0_0 < v_1_1_0
        assert v_1_0_1 < v_1_1_0
        
        v_1_0_0_r_a = Version.from_string("1.0.0-r.a")
        v_1_0_0_r_1 = Version.from_string("1.0.0-r.1")
        
        assert v_1_0_0_r_a > v_1_0_0_r_1        
        
