from code_844_backspace_string_compare import Solution

def test_example_1():
    s = Solution()
    assert s.backspaceCompare("ab#c", "ad#c") == True

def test_example_2():
    s = Solution()
    assert s.backspaceCompare("ab##", "c#d#") == True

def test_example_3():
    s = Solution()
    assert s.backspaceCompare("a#c", "b") == False

def test_failed_101():
    s = Solution()
    assert s.backspaceCompare("y#fo##f", "y#f#o##f") == True