from jsonschema import validate

# A sample schema, like what we'd get from json.load()
schema = {  
   "$schema":"http://json-schema.org/schema#",
   "required":[  
      "games",
      "range_end",
      "range_start",
      "total_games",
      "unique_users"
   ],
   "type":"object",
   "properties":{  
      "range_end":{  
         "type":"string"
      },
      "range_start":{  
         "type":"string"
      },
      "games":{  
         "items":{  
            "required":[  
               "added",
               "card_history",
               "coin",
               "duration",
               "hero",
               "hero_deck",
               "id",
               "legend",
               "mode",
               "note",
               "opponent",
               "opponent_deck",
               "rank",
               "region",
               "result",
               "user_hash"
            ],
            "type":"object",
            "properties":{  
               "note":{  
                  "type":"null"
               },
               "added":{  
                  "type":"string"
               },
               "hero":{  
                  "type":"string"
               },
               "region":{  
                  "type":"string"
               },
               "rank":{  
                  "type":[  
                     "integer",
                     "null"
                  ]
               },
               "legend":{  
                  "type":[  
                     "integer",
                     "null"
                  ]
               },
               "opponent_deck":{  
                  "type":[  
                     "null",
                     "string"
                  ]
               },
               "card_history":{  
                  "items":{  
                     "required":[  
                        "card",
                        "player",
                        "turn"
                     ],
                     "type":"object",
                     "properties":{  
                        "player":{  
                           "type":"string"
                        },
                        "card":{  
                           "required":[  
                              "id",
                              "mana",
                              "name"
                           ],
                           "type":"object",
                           "properties":{  
                              "mana":{  
                                 "type":[  
                                    "integer",
                                    "null"
                                 ]
                              },
                              "id":{  
                                 "type":"string"
                              },
                              "name":{  
                                 "type":"string"
                              }
                           }
                        },
                        "turn":{  
                           "type":"integer"
                        }
                     }
                  },
                  "type":"array"
               },
               "user_hash":{  
                  "type":"string"
               },
               "duration":{  
                  "type":[  
                     "integer",
                     "null"
                  ]
               },
               "hero_deck":{  
                  "type":[  
                     "null",
                     "string"
                  ]
               },
               "mode":{  
                  "type":"string"
               },
               "opponent":{  
                  "type":"string"
               },
               "coin":{  
                  "type":"boolean"
               },
               "id":{  
                  "type":"integer"
               },
               "result":{  
                  "type":"string"
               }
            }
         },
         "type":"array"
      },
      "unique_users":{  
         "type":"integer"
      },
      "total_games":{  
         "type":"integer"
      }
   }
}


# If no exception is raised by validate(), the instance is valid.
a = validate({
  "range_start": "2016-06-01T00:00:00Z",
  "range_end": "2016-07-01T00:00:00Z",
  "unique_users": 38,
  "total_games": 7950,
  "games": [
    {
      "user_hash": "853B97737D848AE2F22D60931C888CB3",
      "region": "Europe",
      "id": 33262529,
      "mode": "ranked",
      "hero": "Warrior",
      "hero_deck": "Dragon",
      "opponent": "Shaman",
      "opponent_deck": "Midrange",
      "coin": True,
      "result": "loss",
      "duration": 761,
      "rank": 6,
      "legend": None,
      "note": None,
      "added": "2016-06-28T17:57:45Z",
      "card_history": [
        {
          "player": "opponent",
          "turn": 1,
          "card": {
            "id": "LOE_018",
            "name": "Tunnel Trogg",
            "mana": 1
          }
        },
        {
          "player": "me",
          "turn": 1,
          "card": {
            "id": "GAME_005",
            "name": "The Coin",
            "mana": None
          }
        },
        {
          "player": "me",
          "turn": 1,
          "card": {
            "id": "CS2_106",
            "name": "Fiery War Axe",
            "mana": 2
          }
        },
        {
          "player": "me",
          "turn": 2,
          "card": {
            "id": "OG_314",
            "name": "Blood To Ichor",
            "mana": 1
          }
        },
        {
          "player": "opponent",
          "turn": 3,
          "card": {
            "id": "EX1_248",
            "name": "Feral Spirit",
            "mana": 3
          }
        },
        {
          "player": "me",
          "turn": 3,
          "card": {
            "id": "LOE_022",
            "name": "Fierce Monkey",
            "mana": 3
          }
        },
        {
          "player": "opponent",
          "turn": 4,
          "card": {
            "id": "EX1_565",
            "name": "Flametongue Totem",
            "mana": 2
          }
        },
        {
          "player": "me",
          "turn": 4,
          "card": {
            "id": "NEW1_011",
            "name": "Kor'kron Elite",
            "mana": 4
          }
        },
        {
          "player": "opponent",
          "turn": 5,
          "card": {
            "id": "AT_052",
            "name": "Totem Golem",
            "mana": 2
          }
        },
        {
          "player": "opponent",
          "turn": 5,
          "card": {
            "id": "OG_028",
            "name": "Thing from Below",
            "mana": 6
          }
        },
        {
          "player": "me",
          "turn": 5,
          "card": {
            "id": "OG_149",
            "name": "Ravaging Ghoul",
            "mana": 3
          }
        },
        {
          "player": "me",
          "turn": 5,
          "card": {
            "id": "CS2_108",
            "name": "Execute",
            "mana": 1
          }
        },
        {
          "player": "opponent",
          "turn": 6,
          "card": {
            "id": "EX1_008",
            "name": "Argent Squire",
            "mana": 1
          }
        },
        {
          "player": "opponent",
          "turn": 6,
          "card": {
            "id": "OG_024",
            "name": "Flamewreathed Faceless",
            "mana": 4
          }
        },
        {
          "player": "me",
          "turn": 6,
          "card": {
            "id": "NEW1_011",
            "name": "Kor'kron Elite",
            "mana": 4
          }
        },
        {
          "player": "me",
          "turn": 6,
          "card": {
            "id": "CS2_106",
            "name": "Fiery War Axe",
            "mana": 2
          }
        },
        {
          "player": "opponent",
          "turn": 7,
          "card": {
            "id": "AT_046",
            "name": "Tuskarr Totemic",
            "mana": 3
          }
        },
        {
          "player": "opponent",
          "turn": 7,
          "card": {
            "id": "CS2_045",
            "name": "Rockbiter Weapon",
            "mana": 1
          }
        },
        {
          "player": "me",
          "turn": 7,
          "card": {
            "id": "BRM_034",
            "name": "Blackwing Corruptor",
            "mana": 5
          }
        },
        {
          "player": "opponent",
          "turn": 8,
          "card": {
            "id": "AT_053",
            "name": "Ancestral Knowledge",
            "mana": 2
          }
        },
        {
          "player": "opponent",
          "turn": 8,
          "card": {
            "id": "LOE_018",
            "name": "Tunnel Trogg",
            "mana": 1
          }
        },
        {
          "player": "opponent",
          "turn": 8,
          "card": {
            "id": "AT_052",
            "name": "Totem Golem",
            "mana": 2
          }
        },
        {
          "player": "me",
          "turn": 8,
          "card": {
            "id": "BRM_034",
            "name": "Blackwing Corruptor",
            "mana": 5
          }
        },
        {
          "player": "opponent",
          "turn": 9,
          "card": {
            "id": "OG_028",
            "name": "Thing from Below",
            "mana": 6
          }
        },
        {
          "player": "me",
          "turn": 9,
          "card": {
            "id": "EX1_284",
            "name": "Azure Drake",
            "mana": 5
          }
        },
        {
          "player": "me",
          "turn": 9,
          "card": {
            "id": "AT_017",
            "name": "Twilight Guardian",
            "mana": 4
          }
        },
        {
          "player": "opponent",
          "turn": 10,
          "card": {
            "id": "CS2_045",
            "name": "Rockbiter Weapon",
            "mana": 1
          }
        },
        {
          "player": "opponent",
          "turn": 10,
          "card": {
            "id": "AT_094",
            "name": "Flame Juggler",
            "mana": 2
          }
        },
        {
          "player": "me",
          "turn": 10,
          "card": {
            "id": "LOE_076",
            "name": "Sir Finley Mrrgglton",
            "mana": 1
          }
        },
        {
          "player": "me",
          "turn": 10,
          "card": {
            "id": "OG_314",
            "name": "Blood To Ichor",
            "mana": 1
          }
        },
        {
          "player": "me",
          "turn": 10,
          "card": {
            "id": "BRM_024",
            "name": "Drakonid Crusher",
            "mana": 6
          }
        },
        {
          "player": "opponent",
          "turn": 11,
          "card": {
            "id": "EX1_238",
            "name": "Lightning Bolt",
            "mana": 1
          }
        },
        {
          "player": "me",
          "turn": 11,
          "card": {
            "id": "AT_017",
            "name": "Twilight Guardian",
            "mana": 4
          }
        },
        {
          "player": "opponent",
          "turn": 12,
          "card": {
            "id": "EX1_248",
            "name": "Feral Spirit",
            "mana": 3
          }
        },
        {
          "player": "me",
          "turn": 12,
          "card": {
            "id": "OG_312",
            "name": "N'Zoth's First Mate",
            "mana": 1
          }
        },
        {
          "player": "opponent",
          "turn": 13,
          "card": {
            "id": "AT_087",
            "name": "Argent Horserider",
            "mana": 3
          }
        },
        {
          "player": "me",
          "turn": 13,
          "card": {
            "id": "OG_149",
            "name": "Ravaging Ghoul",
            "mana": 3
          }
        },
        {
          "player": "opponent",
          "turn": 14,
          "card": {
            "id": "EX1_238",
            "name": "Lightning Bolt",
            "mana": 1
          }
        }
      ]
    },
    {
      "user_hash": "853B97737D848AE2F22D60931C888CB3",
      "region": "Europe",
      "id": 33261034,
      "mode": "ranked",
      "hero": "Warrior",
      "hero_deck": "Dragon",
      "opponent": "Hunter",
      "opponent_deck": "Midrange",
      "coin": True,
      "result": "loss",
      "duration": 349,
      "rank": 6,
      "legend": None,
      "note": None,
      "added": "2016-06-28T17:44:53Z",
      "card_history": [
        {
          "player": "me",
          "turn": 1,
          "card": {
            "id": "GAME_005",
            "name": "The Coin",
            "mana": None
          }
        },
        {
          "player": "me",
          "turn": 1,
          "card": {
            "id": "AT_071",
            "name": "Alexstrasza's Champion",
            "mana": 2
          }
        },
        {
          "player": "opponent",
          "turn": 2,
          "card": {
            "id": "AT_058",
            "name": "King's Elekk",
            "mana": 2
          }
        },
        {
          "player": "me",
          "turn": 2,
          "card": {
            "id": "CS2_106",
            "name": "Fiery War Axe",
            "mana": 2
          }
        },
        {
          "player": "opponent",
          "turn": 3,
          "card": {
            "id": "EX1_536",
            "name": "Eaglehorn Bow",
            "mana": 3
          }
        },
        {
          "player": "opponent",
          "turn": 4,
          "card": {
            "id": "OG_216",
            "name": "Infested Wolf",
            "mana": 4
          }
        },
        {
          "player": "me",
          "turn": 4,
          "card": {
            "id": "OG_149",
            "name": "Ravaging Ghoul",
            "mana": 3
          }
        },
        {
          "player": "me",
          "turn": 4,
          "card": {
            "id": "LOE_076",
            "name": "Sir Finley Mrrgglton",
            "mana": 1
          }
        },
        {
          "player": "opponent",
          "turn": 5,
          "card": {
            "id": "EX1_028",
            "name": "Stranglethorn Tiger",
            "mana": 5
          }
        },
        {
          "player": "me",
          "turn": 5,
          "card": {
            "id": "BRM_034",
            "name": "Blackwing Corruptor",
            "mana": 5
          }
        },
        {
          "player": "opponent",
          "turn": 6,
          "card": {
            "id": "EX1_539",
            "name": "Kill Command",
            "mana": 3
          }
        },
        {
          "player": "opponent",
          "turn": 6,
          "card": {
            "id": "AT_058",
            "name": "King's Elekk",
            "mana": 2
          }
        },
        {
          "player": "opponent",
          "turn": 6,
          "card": {
            "id": "OG_179",
            "name": "Fiery Bat",
            "mana": 1
          }
        },
        {
          "player": "me",
          "turn": 6,
          "card": {
            "id": "AT_017",
            "name": "Twilight Guardian",
            "mana": 4
          }
        },
        {
          "player": "me",
          "turn": 6,
          "card": {
            "id": "NEW1_023",
            "name": "Faerie Dragon",
            "mana": 2
          }
        },
        {
          "player": "opponent",
          "turn": 7,
          "card": {
            "id": "DS1_070",
            "name": "Houndmaster",
            "mana": 4
          }
        },
        {
          "player": "opponent",
          "turn": 7,
          "card": {
            "id": "OG_179",
            "name": "Fiery Bat",
            "mana": 1
          }
        },
        {
          "player": "me",
          "turn": 7,
          "card": {
            "id": "OG_314",
            "name": "Blood To Ichor",
            "mana": 1
          }
        },
        {
          "player": "me",
          "turn": 7,
          "card": {
            "id": "OG_314",
            "name": "Blood To Ichor",
            "mana": 1
          }
        },
        {
          "player": "me",
          "turn": 7,
          "card": {
            "id": "NEW1_011",
            "name": "Kor'kron Elite",
            "mana": 4
          }
        },
        {
          "player": "opponent",
          "turn": 8,
          "card": {
            "id": "EX1_534",
            "name": "Savannah Highmane",
            "mana": 6
          }
        },
        {
          "player": "opponent",
          "turn": 8,
          "card": {
            "id": "BRM_013",
            "name": "Quick Shot",
            "mana": 2
          }
        },
        {
          "player": "me",
          "turn": 8,
          "card": {
            "id": "EX1_298",
            "name": "Ragnaros the Firelord",
            "mana": 8
          }
        },
        {
          "player": "opponent",
          "turn": 9,
          "card": {
            "id": "OG_216",
            "name": "Infested Wolf",
            "mana": 4
          }
        },
        {
          "player": "opponent",
          "turn": 9,
          "card": {
            "id": "NEW1_041",
            "name": "Stampeding Kodo",
            "mana": 5
          }
        },
        {
          "player": "me",
          "turn": 9,
          "card": {
            "id": "EX1_604",
            "name": "Frothing Berserker",
            "mana": 3
          }
        },
        {
          "player": "me",
          "turn": 9,
          "card": {
            "id": "OG_149",
            "name": "Ravaging Ghoul",
            "mana": 3
          }
        }
      ]
    }
  ]
}, schema)


print a