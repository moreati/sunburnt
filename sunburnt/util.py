import re

_valid_patt = re.compile(u'[^\u0020-\uD7FF\x09\x0A\x0D'
                         u'\uE000-\uFFFD\U00010000-\U0010FFFF]', re.U)

def strip_invalid_xml_chars(s, substitute=u''):
    r'''Replace characters in a unicode string s that are forbidden by XML 1.0

    XML 1.0 only a allows a subset of Unicode characters in an XML document.
    Others (e.g. U+0000, U+0013) are invalid - they may not be included
    regardless of encoding or escaping. Valid characters are U+0009, U+000A,
    U+000D, U+0020-U+D7FF, U+E000-U+FFFD, U+10000-U+10FFFF.

    See <http://www.w3.org/TR/2008/PER-xml-20080205/#charsets>
    >>> strip_invalid_xml_chars(u'a\x00bc\x13d\tef\n ghi')
    u'abcd\tef\n ghi'
    '''
    return _valid_patt.sub(substitute, s)
