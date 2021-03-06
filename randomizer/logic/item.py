from enum import IntEnum
import random


class Item(IntEnum):
  BOMBS = 0x00
  WOOD_SWORD = 0x01
  WHITE_SWORD = 0x02
  MAGICAL_SWORD = 0x03
  BAIT = 0x04
  RECORDER = 0x05
  BLUE_CANDLE = 0x06
  RED_CANDLE = 0x07
  WOOD_ARROWS = 0x08
  SILVER_ARROWS = 0x09
  BOW = 0x0A
  MAGICAL_KEY = 0x0B
  RAFT = 0x0C
  LADDER = 0x0D
  NOTHING = 0x0E
  FIVE_RUPEES = 0x0F
  WAND = 0x10
  BOOK = 0x11
  BLUE_RING = 0x12
  RED_RING = 0x13
  POWER_BRACELET = 0x14
  LETTER = 0x15
  COMPASS = 0x16
  MAP = 0x17
  RUPEE = 0x18
  KEY = 0x19
  HEART_CONTAINER = 0x1A
  TRIFORCE = 0x1B
  MAGICAL_SHIELD = 0x1C
  BOOMERANG = 0x1D
  MAGICAL_BOOMERANG = 0x1E
  BLUE_POTION = 0x1F
  RED_POTION = 0x20
  SINGLE_HEART = 0x22
  OVERWORLD_NO_ITEM = 0x3F
  # Not actual codes -- only for Inventory class
  TRIFORCE_OF_POWER_PLACEHOLDER_ITEM = 0x3D
  KIDNAPPED_PLACEHOLDER_ITEM = 0x3E

  def IsMajorItem(self) -> bool:
    return self in [
        Item.WOOD_SWORD, Item.WHITE_SWORD, Item.MAGICAL_SWORD, Item.RECORDER, Item.BLUE_CANDLE,
        Item.RED_CANDLE, Item.WOOD_ARROWS, Item.SILVER_ARROWS, Item.BOW, Item.MAGICAL_KEY,
        Item.RAFT, Item.LADDER, Item.WAND, Item.BOOK, Item.BLUE_RING, Item.RED_RING,
        Item.POWER_BRACELET, Item.LETTER, Item.HEART_CONTAINER, Item.BOOMERANG,
        Item.MAGICAL_BOOMERANG, Item.BAIT
    ]

  def IsAnIncrementalUpgradeItem(self) -> bool:
    return self in [
        Item.WOOD_SWORD, Item.WHITE_SWORD, Item.MAGICAL_SWORD, Item.BLUE_CANDLE, Item.RED_CANDLE,
        Item.WOOD_ARROWS, Item.SILVER_ARROWS, Item.BLUE_RING, Item.RED_RING, Item.BOOMERANG,
        Item.MAGICAL_BOOMERANG
    ]

  def IsSwordOrWand(self) -> bool:
    return self in [Item.WOOD_SWORD, Item.WHITE_SWORD, Item.MAGICAL_SWORD, Item.WAND]
