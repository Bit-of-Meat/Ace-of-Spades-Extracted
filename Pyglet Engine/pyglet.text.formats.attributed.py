# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\pyglet.text.formats.attributed
__docformat__ = 'restructuredtext'
__version__ = '$Id: $'
import operator, parser, re, token, pyglet
_pattern = re.compile('\n    (?P<escape_hex>\\{\\#x(?P<escape_hex_val>[0-9a-fA-F]+)\\})\n  | (?P<escape_dec>\\{\\#(?P<escape_dec_val>[0-9]+)\\})\n  | (?P<escape_lbrace>\\{\\{)\n  | (?P<escape_rbrace>\\}\\})\n  | (?P<attr>\\{\n        (?P<attr_name>[^ \\{\\}]+)\\s+\n        (?P<attr_val>[^\\}]+)\\})\n  | (?P<nl_hard1>\\n(?=[ \\t]))\n  | (?P<nl_hard2>\\{\\}\\n)\n  | (?P<nl_soft>\\n(?=\\S))\n  | (?P<nl_para>\\n\\n+)\n  | (?P<text>[^\\{\\}\\n]+)\n    ', re.VERBOSE | re.DOTALL)

class AttributedTextDecoder(pyglet.text.DocumentDecoder):

    def decode(self, text, location=None):
        self.doc = pyglet.text.document.FormattedDocument()
        self.length = 0
        self.attributes = {}
        next_trailing_space = True
        trailing_newline = True
        for m in _pattern.finditer(text):
            group = m.lastgroup
            trailing_space = True
            if group == 'text':
                t = m.group('text')
                self.append(t)
                trailing_space = t.endswith(' ')
                trailing_newline = False
            elif group == 'nl_soft':
                if not next_trailing_space:
                    self.append(' ')
                trailing_newline = False
            elif group in ('nl_hard1', 'nl_hard2'):
                self.append('\n')
                trailing_newline = True
            elif group == 'nl_para':
                self.append(m.group('nl_para'))
                trailing_newline = True
            elif group == 'attr':
                try:
                    ast = parser.expr(m.group('attr_val'))
                    if self.safe(ast):
                        val = eval(ast.compile())
                    else:
                        val = None
                except (parser.ParserError, SyntaxError):
                    val = None

                name = m.group('attr_name')
                if name[0] == '.':
                    if trailing_newline:
                        self.attributes[name[1:]] = val
                    else:
                        self.doc.set_paragraph_style(self.length, self.length, {name[1:]: val})
                else:
                    self.attributes[name] = val
            elif group == 'escape_dec':
                self.append(unichr(int(m.group('escape_dec_val'))))
            elif group == 'escape_hex':
                self.append(unichr(int(m.group('escape_hex_val'), 16)))
            elif group == 'escape_lbrace':
                self.append('{')
            elif group == 'escape_rbrace':
                self.append('}')
            next_trailing_space = trailing_space

        return self.doc

    def append(self, text):
        self.doc.insert_text(self.length, text, self.attributes)
        self.length += len(text)
        self.attributes.clear()

    _safe_names = ('True', 'False', 'None')

    def safe(self, ast):
        tree = ast.totuple()
        return self.safe_node(tree)

    def safe_node(self, node):
        if token.ISNONTERMINAL(node[0]):
            return reduce(operator.and_, map(self.safe_node, node[1:]))
        else:
            if node[0] == token.NAME:
                return node[1] in self._safe_names
            return True
# okay decompiling out\pyglet.text.formats.attributed.pyc
