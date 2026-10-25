# KB-013 — Attack base damage / Concussive Runes / Repulsion exception

- scope: Path of Exile 2, current patch reference 0.5.5e
- researched: 2026-10-25
- status: NEEDS_RETEST
- confidence: high for generic attack rule; medium/low for weapon-independent exception
- category: mechanics / skills

## Core rules
1. OFFICIAL (Mark_GGG, 2026-10-23/24): Base attack damage normally comes from the equipped Martial Weapon. Attack skills specify a percentage of that base (100% may be omitted).
2. DATA_VERIFIED (PoE2DB): Concussive Runes supports Attacks, triggering Runic Shockwave when the supported Attack Heavy Stuns; trigger requires enough Runic Ward. Runic Shockwave has 130–531% of base attack damage at gem levels 1–20, 2 m radius, cannot cause stun buildup, and copies the supported gem's level.
3. DATA_VERIFIED (PoE2DB): Repulsion Wave is an Attack whose description explicitly states that its physical attack damage is NOT based on weapon damage and provides its own base physical damage values.
4. UNRESOLVED: The developer's generic statement does not explicitly explain what Concussive Runes' Runic Shockwave uses as its damage source when triggered via Repulsion Wave with a wand, staff, or no Martial Weapon. Forum users disagree. Do not assert that the wave inherits Repulsion's independent base damage or that it deals zero damage until tested.

## Computation / adjudication
- Normal martial-weapon attack (illustrative, not a full damage formula):
  attack_base_range = equipped_martial_weapon_base_range × attack_skill_base_damage_percentage.
- For Runic Shockwave, first confirm the heavy-stun trigger and Runic Ward cost; then identify which base damage source its separate triggered attack actually uses; only then apply eligible increases/more and enemy mitigation.
- A triggered effect's own skill damage percentage is NOT evidence that it inherits the triggering skill's final hit damage.
- Exceptional attacks explicitly independent of weapon damage require a separate calculation branch.

## Misconceptions
- 'All attacks use weapon damage' — false as a universal statement; Repulsion Wave is a text-level exception.
- 'Runic Shockwave 531% of base = 531% of the triggering hit' — not established.
- 'Concussive Runes always triggers on any hit' — false; requires Heavy Stun and sufficient Runic Ward.
- 'The GGG reply proves the wand/Repulsion case' — false; generic reply did not answer that special case.

## Reproducible experiment
1. Hold constant character level, supported gem level, passive tree, support setup, enemy type, and Runic Ward.
2. Trigger Concussive Runes through Repulsion Wave while equipping: (A) wand, (B) martial weapon with low base damage, (C) martial weapon with high base damage.
3. Confirm Heavy Stun and separate Runic Shockwave damage event from Repulsion Wave; compare hit ranges over repeated trials.
4. Change Repulsion Wave's gem level independently of weapon base and track whether the triggered damage changes; separately vary attack-damage and spell-damage modifiers.
5. Record tooltip and actual hit damage; control crits, enemy armour/resistances, exposure, shock and other buffs.
6. Mark each observation by patch; do not infer from a single combat event.

## Practical impact
- BD: A Concussive Runes damage build should not select wand vs martial weapon based on the unsupported assumption that Repulsion's independent base damage is inherited.
- Crafting: Prioritize martial-weapon damage affixes only after confirming the damage source of the actual triggered skill.
- Farm: Heavy Stun uptime, Ward sustainability and trigger frequency may limit effective damage; no reliable farm ranking follows from tooltip % alone.

## Sources
- GGG official developer reply: https://www.pathofexile.com/forum/view-thread/4011598
- PoE2DB Concussive Runes: https://poe2db.tw/us/Concussive_Runes
- PoE2DB Repulsion: https://poe2db.tw/us/Repulsion
- PoE2 Wiki weapon rule: https://www.poe2wiki.net/wiki/Weapon

## Next verification
Determine whether Concussive Runes uses Martial Weapon base, Repulsion Wave independent base, or another fallback when no Martial Weapon is equipped; quantify the effect of gem levels and damage modifiers.
