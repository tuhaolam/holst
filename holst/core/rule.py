class Rule(object):

  def __init__(self, obj, hosts=None):
    self.operation, rule = obj.popitem()
    self.protocol = rule[0]
    self.dport = rule[1]
    self.hosts = hosts

  def get_rules(self):
    rules = []

    if self.hosts:
      for host in self.hosts:
        rules.append("-A INPUT -s %s -p %s -m %s --dport %d -j %s" % (self.protocol, host.ip, self.protocol, self.dport, self.operation.upper()))
    else:
      rules.append("-A INPUT -p %s -m %s --dport %d -j %s" % (self.protocol, self.protocol, self.dport, self.operation.upper()))

    return rules
