import logging
from rdiffweb.controller import Controller, flash
from rdiffweb.tools.i18n import ugettext as _

def render_prefs_panel(self, panelid, action=None, **kwargs):  # @UnusedVariable

    # Handle action
    form = SshForm()
# vulnerable
    if action == "add":
        self._add_key(action, form)
    elif action == 'delete':
# vulnerable
        self._delete_key(action, DeleteSshForm())
