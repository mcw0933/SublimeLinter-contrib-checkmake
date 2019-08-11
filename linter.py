"""Subclass to call checkmake for linting Makefiles"""
from SublimeLinter.lint import Linter


class MakefileLinter(Linter):
    """Subclass to call checkmake for linting Makefiles"""
    cmd = 'checkmake $file_on_disk'
    regex = (
        r'^  (?: .*$|(?P<code>[a-z0-9]+) +(?P<message>[\w" ]{29}) +(?P<line>\d+))'
    )
    defaults = {
        'selector': 'source.makefile'
    }
    tempfile_suffix = '-'

    def split_match(self, match):
        """Override split_match to set line number 0s to line 1,
          subtract 2 from other line numbers due to line number bug"""

        (match, line, col, error, warning, message, near) = super().split_match(match)
        if message:
            if line > 0:
                line = line - 2
            else:
                line = 1

        return (match, line, col, error, warning, message, near)
