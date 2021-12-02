from typing import List, Union, Dict
from abc import ABC, abstractmethod

with open('input', 'r') as fd:
    lines = [line.strip() for line in fd.readlines()]


class GenericRule(ABC):
    @abstractmethod
    def validate(self, s: str) -> Union[None, List[str]]:
        pass


ALL_RULES: Dict[str, GenericRule] = {}


class CharRule(GenericRule):
    def __init__(self, char: str):
        self.value = char

    def validate(self, s: str) -> Union[None, List[str]]:
        if s.startswith(self.value):
            return [s[len(self.value):]]
        return None


class ChainRule(GenericRule):
    def __init__(self, chain_rules: List[str]):
        self.rules = chain_rules

    def validate(self, s: str) -> Union[None, List[str]]:
        matches = []
        if len(self.rules) == 0:
            return [s]
        possibilities = ALL_RULES[self.rules[0]].validate(s)
        if possibilities is None:
            return None
        for p in possibilities:
            result = ChainRule(self.rules[1:]).validate(p)
            if result is not None:
                matches += result
        if len(matches) > 0:
            return matches
        return None


class OrRule(GenericRule):
    def __init__(self, or_rules: List[str]):
        self.rules: List[GenericRule] = [make_rule(subrule) for subrule in or_rules]

    def __str__(self):
        return ' | '.join(str(rule) for rule in self.rules)

    def validate(self, s: str) -> Union[None, List[str]]:
        matches = []
        for rule in self.rules:
            validation = rule.validate(s)
            if validation is not None:
                matches += validation
        if len(matches) > 0:
            return matches
        return None


def make_rule(text_raw: str) -> GenericRule:
    text = text_raw.strip()
    if '"' in text:
        return CharRule(text.replace('"', ''))
    elif '|' not in text:
        return ChainRule(text.split())
    return OrRule(text.split('|'))


def matches_rule_zero(s: str) -> bool:
    result = ALL_RULES['0'].validate(s)
    return result is not None and '' in result


# A1
matching_lines = 0
for line in lines:
    if ':' in line:
        rule_split = line.split(':')
        rule_id, rule_text = rule_split[0], rule_split[1]
        ALL_RULES[rule_id] = make_rule(rule_text)
    elif len(line) > 0:
        matching_lines += 1 if matches_rule_zero(line) else 0
print(matching_lines)


# A2
matching_lines = 0
ALL_RULES['8'] = make_rule('42 | 42 8')
ALL_RULES['11'] = make_rule('42 31 | 42 11 31')
for line in lines:
    if ':' not in line and len(line) > 0:
        matching_lines += 1 if matches_rule_zero(line) else 0
print(matching_lines)
