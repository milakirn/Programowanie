from cw1 import ReverseWord

def test_palindrome():
    assert ReverseWord("kajak") == "kajak"

def test_isNotPalindrome():
    assert ReverseWord("alamakota") != "alamakota"