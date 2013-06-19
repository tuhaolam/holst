from rule import Rule

class Service():
  def __init__(self, name, service):
    self.rules = []
    self.name = name

    if "rules" in service:
      if type(service["rules"]) is dict:
        self.rule_template = [service["rules"]]
      else:
        self.rule_template = service["rules"]

  def create_rules(self, chain_name, hosts=None):

    for rule in self.rule_template:
      self.rules.append(Rule(rule, chain_name, hosts))

    return self.rules

  def get_chain(self):
    chains = []

    for rule_obj in self.rule_template:
      operation = rule_obj.keys()[0]
      rule = rule_obj.get(operation)

      if len(rule) == 2:
        chains.append("-A INPUT -p %s -m %s --dport %d -m state --state NEW -j %s" % (rule[0], rule[0], rule[1], self.name))
      else:
        chains.append("-A INPUT -p %s -m multiport --dports %s -m state --state NEW -j %s" % (rule[0], ",".join(map(str,rule[1:])), self.name))

    return chains
