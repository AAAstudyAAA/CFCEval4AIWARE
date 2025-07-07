import logging
from rdiffweb.controller import Controller, flash
from rdiffweb.tools.i18n import ugettext as _

def render_preferences_panel(self, panel_id, action=None, **kwargs):  # @UnusedVariable

    # Handle action
    ssh_form = SshForm()

    # vulnerable
    if action == "add":
        self._add_key(action, ssh_form)
    elif action == 'delete':
        # vulnerable
        self._delete_key(action, DeleteSshForm())
