import logging
from rdiffweb.controller import Controller, flash
from rdiffweb.tools.i18n import ugettext as _

_logger = logging.getLogger(__name__)

def render_preferences_panel(self, panel_id, action=None, **kwargs):  # @UnusedVariable
    # Handle action
    ssh_form = SshForm()
    delete_ssh_form = DeleteSshForm()

    if action == "add" and ssh_form.is_submitted():
        self._add_key(action, ssh_form)
    elif action == 'delete' and delete_ssh_form.is_submitted():
        self._delete_key(action, delete_ssh_form)
