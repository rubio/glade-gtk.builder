import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

widget = Gtk.Box()
print(dir(widget.props))
