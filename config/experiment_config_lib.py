import itertools
import string

class ControllerConfig(object):
  _port_gen = itertools.count(8888)

  def __init__(self, cmdline="", address="127.0.0.1", port=None):
    '''
    Store metadata for the controller.
      - cmdline is an array of command line tokens.

        Note: if you need to pass in the address and port to controller's
        command line, use the aliases __address__ and __port__ to have the
        values interpolated automatically
      - address and port are the sockets switches will bind to
    '''
    if cmdline == "":
      raise RuntimeError("Must specify boot parameters.")
    self.cmdline_string = cmdline
    self.address = address
    if not port:
      port = self._port_gen.next()
    self.port = port
    if "pox" in self.cmdline_string:
      self.name = "pox"
    self.cmdline = map(lambda(x): string.replace(x, "__port__", str(port)),
                       map(lambda(x): string.replace(x, "__address__",
                                                     str(address)), cmdline.split()))

  @property
  def uuid(self):
    return (self.address, self.port)

  def __repr__(self):
    return self.__class__.__name__  + "(cmdline=\"" + self.cmdline_string +\
           "\",address=\"" + self.address + "\",port=" + self.port.__repr__() + ")"