"""Subclass to call checkmake for linting Makefiles"""
from SublimeLinter.lint import Linter


class MakefileLinter(Linter):
    """Subclass to call checkmake for linting Makefiles"""
    cmd = 'checkmake --format="{{.LineNumber}}:{{.Rule}}:{{printf \"%s\n\" .Violation}}" $file_on_disk'
    regex = (
        r'^(?:(?P<line>\d+):(?P<code>[a-z0-9]+):(?P<message>.*))'
    )
    defaults = {
        'selector': 'source.makefile'
    }
    tempfile_suffix = '-'
