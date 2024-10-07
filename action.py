"""action.py

Module for encapsulating actions and effects in the game.
"""
from typing import Type

import entities


class Action:
    """An action that can be taken in the game.

    Actions affect the stats of the actor, or another entity acted upon.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def apply_effect(self, stat: entities.Stats) -> None:
        """Applies the effect of this action to the given stat.
        This method must be overridden by subclasses.
        """
        raise NotImplementedError


class SelfAction(Action):
    """SelfActions apply their effects to the actor's stats."""


class OtherAction(Action):
    """OtherActions apply their effects to the target's stats."""


class _TakeDamage(SelfAction):
    """Takes damage from the target.
    This is a private action that is invoked by other actions only.
    """
    def __init__(self, value: int):
        super().__init__("take damage", "takes damage")
        self.value = value

    def apply_effect(self, stat: entities.Stats) -> None:
        # Deal damage to shield first
        while stat.shield:  # is not 0
            self.value -= 1
            stat.shield -= 1
        # Remaining damage is dealt to hp
        while self.value and stat.hp:  # is not 0
            self.value -= 1
            stat.hp -= 1


class Adaptation(SelfAction):
    """Adapt to an enemy's weaknesses. The effect is applied to the actor's
    stats."""

    def __init__(self):
        super().__init__(name="adaptation", description="Adapt to the enemy's weaknesses")

    def apply_effect(self, stat: entities.Stats) -> None:
        stat.attack += 2


class Defend(SelfAction):
    """Defend against an attack. The effect is applied to the actor's stats."""

    def __init__(self):
        super().__init__(name="defend", description="it defends")

    def apply_effect(self, stat: entities.Stats) -> None:
        stat.shield += stat.maxhp // 2


class Heal(SelfAction):
    """Heal the actor."""

    def __init__(self, value: int):
        super().__init__("heal", f"heal {value} hp")
        self.value = value

    def apply_effect(self, stat: entities.Stats) -> None:
        while self.value and stat.hp < stat.maxhp:
            stat.hp += 1
            self.value -= 1
        self.value = 0


class Hit(OtherAction):
    """An attack upon another entity. the effect is applied to the other
    entity's stats.
    """

    def __init__(self, damage: int):
        super().__init__(name="hit", description="it hits")
        self.damage = damage

    def apply_effect(self, stat: entities.Stats) -> None:
        _TakeDamage(self.damage).apply_effect(stat)


class IntegrationOneDotFive(SelfAction):
    """Increase the polynomial degree of the monster's attack."""

    def __init__(self):
        super().__init__(name="integration x1.5", description="enemys polynomial degree increases, amplifying stats by 1.5x")

    def apply_effect(self, stat: entities.Stats) -> None:
        stat.attack += stat.attack // 2
        Heal(stat.hp // 2).apply_effect(stat)


class Sacrifice(SelfAction):
    """Sacrifice the actor's hp to increase attack."""
    def __init__(self, value: int):
        super().__init__(name="sacrifice", description="you slit your hand dripping blood")
        self.value = value

    def apply_effect(self, stat: entities.Stats) -> None:
        while stat.hp > 1 and self.value:
            self.value -= 1
            stat.hp -= 1
        self.value = 0


class SlamDunk(OtherAction):
    """Lebron Dunks on the enemy. The effect is applied to the other entity's
    stats."""

    def __init__(self, damage: int):
        super().__init__(name="slamdunk", description="lebron dunks on you aura -1000")
        self.damage = damage

    def apply_effect(self, stat: entities.Stats) -> None:
        _TakeDamage(self.damage).apply_effect(stat)
        stat.sanity -= 1


class Trip(SelfAction):
    """Trip on one's own feet. The effect is applied to the actor's stats."""

    def __init__(self):
        super().__init__(name="trip", description="it falls onto the ground")

    def apply_effect(self, stat: entities.Stats) -> None:
        # Damage is dealt directly to hp, bypassing shields
        stat.hp -= 1


def get(name: str):
    """A getter method for the action class"""
    if name == "adaptation":
        return Adaptation
    elif name == "defend":
        return Defend
    elif name == "heal":
        return Heal
    elif name == "hit":
        return Hit
    elif name == "integration x1.5":
        return IntegrationOneDotFive
    elif name == "sacrifice":
        return Sacrifice
    elif name == "slamdunk":
        return SlamDunk
    elif name == "take damage":
        return _TakeDamage
    elif name == "trip":
        return Trip
    raise ValueError(f"{name}: Invalid action")