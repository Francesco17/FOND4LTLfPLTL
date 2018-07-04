
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTION_KEY ADL_KEY AND_KEY DEFINE_KEY DOMAIN_KEY EFFECT_KEY EQUALITY_KEY EQUALS EXISTS_KEY FORALL_KEY HYPHEN IMPLY_KEY LPAREN NAME ND_KEY NOT_KEY ONEOF_KEY OR_KEY PARAMETERS_KEY PRECONDITION_KEY PREDICATES_KEY REQUIREMENTS_KEY RPAREN STRIPS_KEY TYPES_KEY TYPING_KEY VARIABLE WHEN_KEYpddl : domaindomain : LPAREN DEFINE_KEY domain_def require_def types_def predicates_def action_def_lst RPARENdomain_def : LPAREN DOMAIN_KEY NAME RPARENrequire_def : LPAREN REQUIREMENTS_KEY require_key_lst RPARENrequire_key_lst : require_key require_key_lst\n                           | require_keyrequire_key : STRIPS_KEY\n                       | EQUALITY_KEY\n                       | TYPING_KEY\n                       | ADL_KEY\n                       | ND_KEYtypes_def : LPAREN TYPES_KEY names_lst RPARENnames_lst : NAME names_lst\n                     | NAMEpredicates_def : LPAREN PREDICATES_KEY predicate_def_lst RPARENpredicate_def_lst : predicate_def predicate_def_lst\n                             | predicate_defpredicate_def : LPAREN NAME typed_variables_lst RPAREN\n                         | LPAREN NAME RPARENaction_def_lst : action_def action_def_lst\n                          | action_defaction_def : LPAREN ACTION_KEY NAME parameters_def precond_def effects_def RPARENparameters_def : PARAMETERS_KEY LPAREN typed_variables_lst RPAREN\n                          | PARAMETERS_KEY LPAREN RPARENprecond_def : PRECONDITION_KEY LPAREN formula RPARENformula : literal\n                   | AND_KEY formula_lst\n                   | OR_KEY formula_lst\n                   | NOT_KEY formula\n                   | IMPLY_KEY formula formula\n                   | EXISTS_KEY LPAREN typed_variables_lst RPAREN formula\n                   | FORALL_KEY LPAREN typed_variables_lst RPAREN formula\n                   | LPAREN AND_KEY formula_lst RPAREN\n                   | LPAREN OR_KEY formula_lst RPAREN\n                   | LPAREN NOT_KEY formula RPAREN\n                   | LPAREN IMPLY_KEY formula formula RPAREN\n                   | LPAREN literal RPAREN\n                   | LPAREN EXISTS_KEY LPAREN typed_variables_lst RPAREN formula RPAREN\n                   | LPAREN FORALL_KEY LPAREN typed_variables_lst RPAREN formula RPARENformula_lst : formula formula_lst\n                       | formulaeffects_def : EFFECT_KEY LPAREN one_eff_formula RPARENone_eff_formula : literal\n                           | AND_KEY one_eff_formula_lst\n                           | ONEOF_KEY atomic_eff_lst\n                           | LPAREN ONEOF_KEY atomic_eff_lst RPAREN\n                           | LPAREN WHEN_KEY formula atomic_eff RPAREN\n                           | LPAREN FORALL_KEY LPAREN typed_variables_lst RPAREN atomic_eff RPAREN\n                           | LPAREN FORALL_KEY LPAREN typed_variables_lst RPAREN LPAREN WHEN_KEY formula atomic_eff RPAREN RPARENone_eff_formula_lst : one_eff_formula one_eff_formula_lst\n                               | one_eff_formulaatomic_eff_lst : atomic_eff atomic_eff_lst\n                          | atomic_effatomic_eff : literal\n                      | AND_KEY literal_lst\n                      | LPAREN AND_KEY literal_lst RPARENliteral_lst : literal literal_lst\n                       | literal literal : LPAREN NOT_KEY predicate RPAREN\n                   | predicatepredicate : LPAREN NAME variables_lst RPAREN\n                     | LPAREN EQUALS VARIABLE VARIABLE RPAREN\n                     | LPAREN NAME RPAREN\n                     | NAME variables_lst\n                     | EQUALS VARIABLE VARIABLE\n                     | NAMEtyped_variables_lst : variables_lst HYPHEN type typed_variables_lst\n                               | variables_lst HYPHEN typevariables_lst : VARIABLE variables_lst\n                         | VARIABLEtype : NAME'
    
_lr_action_items = {'LPAREN':([0,4,6,9,13,14,24,25,29,32,33,37,42,46,48,50,51,53,55,60,61,65,66,67,69,70,71,72,73,74,75,76,77,82,83,84,86,87,88,89,91,92,96,97,98,99,100,103,105,106,107,108,112,113,114,115,116,117,121,124,125,129,131,132,135,137,143,144,145,146,147,148,149,150,151,155,157,158,159,163,165,166,167,168,169,170,171,172,173,178,179,180,181,182,185,],[3,5,8,12,23,-3,30,-4,35,30,-12,35,-15,-19,-70,56,-18,-69,61,66,67,-22,80,85,-26,67,67,67,67,101,102,-60,-66,-43,80,118,67,67,121,67,126,127,-27,67,-28,-29,67,-64,118,67,138,139,-44,80,-45,118,-54,85,85,67,-37,-63,-40,-30,-65,118,-50,-52,-55,85,85,-33,-34,-35,-59,-61,67,67,-46,-57,-36,67,67,-62,-31,-32,-47,176,-56,-38,-39,67,-48,118,-49,]),'$end':([1,2,39,],[0,-1,-2,]),'DEFINE_KEY':([3,],[4,]),'DOMAIN_KEY':([5,],[7,]),'NAME':([7,22,28,35,38,48,52,53,61,66,67,69,70,71,72,73,76,77,80,82,83,84,85,86,87,88,89,96,97,98,99,100,103,105,106,108,112,113,114,115,116,117,118,121,124,125,129,131,132,135,137,139,143,144,145,146,147,148,149,150,151,155,157,158,159,163,165,166,167,168,169,170,171,172,173,176,178,179,180,181,182,185,],[10,28,28,41,44,-70,58,-69,77,77,93,-26,77,77,77,77,-60,-66,109,-43,77,77,109,77,77,77,77,-27,77,-28,-29,77,-64,77,77,77,-44,77,-45,77,-54,77,109,93,77,-37,-63,-40,-30,-65,77,109,-50,-52,-55,77,77,-33,-34,-35,-59,-61,77,77,-46,-57,-36,77,77,-62,-31,-32,-47,77,-56,109,-38,-39,77,-48,77,-49,]),'REQUIREMENTS_KEY':([8,],[11,]),'RPAREN':([10,15,16,17,18,19,20,21,26,27,28,31,32,34,36,37,40,41,43,45,46,48,51,53,56,57,58,59,62,64,65,68,69,76,77,81,82,90,93,96,97,98,99,103,109,111,112,113,114,115,116,119,120,122,123,125,128,129,131,132,133,134,135,136,140,141,143,144,145,146,148,149,150,151,152,153,154,155,156,159,160,161,162,163,164,165,168,169,170,171,173,174,175,177,178,179,181,183,184,185,],[14,25,-6,-7,-8,-9,-10,-11,-5,33,-14,39,-21,-13,42,-17,-20,46,-16,51,-19,-70,-18,-69,63,-68,-71,65,79,-67,-22,95,-26,-60,-66,111,-43,125,129,-27,-41,-28,-29,-64,129,-42,-44,-51,-45,-53,-54,148,149,150,151,-37,155,-63,-40,-30,157,158,-65,159,151,155,-50,-52,-55,-58,-33,-34,-35,-59,165,166,167,-61,168,-46,171,172,168,-57,173,-36,-62,-31,-32,-47,-56,178,179,181,-38,-39,-48,184,185,-49,]),'STRIPS_KEY':([11,16,17,18,19,20,21,],[17,17,-7,-8,-9,-10,-11,]),'EQUALITY_KEY':([11,16,17,18,19,20,21,],[18,18,-7,-8,-9,-10,-11,]),'TYPING_KEY':([11,16,17,18,19,20,21,],[19,19,-7,-8,-9,-10,-11,]),'ADL_KEY':([11,16,17,18,19,20,21,],[20,20,-7,-8,-9,-10,-11,]),'ND_KEY':([11,16,17,18,19,20,21,],[21,21,-7,-8,-9,-10,-11,]),'TYPES_KEY':([12,],[22,]),'PREDICATES_KEY':([23,],[29,]),'ACTION_KEY':([30,],[38,]),'VARIABLE':([41,48,56,57,58,77,78,93,94,101,102,104,109,110,126,127,130,138,142,],[48,48,48,48,-71,48,104,48,130,48,48,135,48,142,48,48,156,48,162,]),'PARAMETERS_KEY':([44,],[50,]),'HYPHEN':([47,48,53,],[52,-70,-69,]),'AND_KEY':([48,53,61,66,67,69,70,71,72,73,76,77,82,83,84,86,87,88,89,96,97,98,99,100,103,105,106,112,113,114,115,116,118,121,124,125,129,131,132,135,137,143,144,145,146,148,149,150,151,155,157,158,159,163,165,166,167,168,169,170,171,172,173,176,178,179,180,181,182,185,],[-70,-69,70,83,86,-26,70,70,70,70,-60,-66,-43,83,117,70,70,70,70,-27,70,-28,-29,70,-64,117,70,-44,83,-45,117,-54,147,86,70,-37,-63,-40,-30,-65,117,-50,-52,-55,-58,-33,-34,-35,-59,-61,70,70,-46,-57,-36,70,70,-62,-31,-32,-47,117,-56,147,-38,-39,70,-48,117,-49,]),'OR_KEY':([48,53,61,67,69,70,71,72,73,76,77,86,87,88,89,96,97,98,99,100,103,106,121,124,125,129,131,132,135,148,149,150,151,155,157,158,165,166,167,168,169,170,178,179,180,],[-70,-69,71,87,-26,71,71,71,71,-60,-66,71,71,71,71,-27,71,-28,-29,71,-64,71,87,71,-37,-63,-40,-30,-65,-33,-34,-35,-59,-61,71,71,-36,71,71,-62,-31,-32,-38,-39,71,]),'NOT_KEY':([48,53,61,67,69,70,71,72,73,76,77,80,85,86,87,88,89,96,97,98,99,100,103,106,118,121,124,125,129,131,132,135,148,149,150,151,155,157,158,165,166,167,168,169,170,176,178,179,180,],[-70,-69,72,88,-26,72,72,72,72,-60,-66,108,108,72,72,72,72,-27,72,-28,-29,72,-64,72,108,88,72,-37,-63,-40,-30,-65,-33,-34,-35,-59,-61,72,72,-36,72,72,-62,-31,-32,108,-38,-39,72,]),'IMPLY_KEY':([48,53,61,67,69,70,71,72,73,76,77,86,87,88,89,96,97,98,99,100,103,106,121,124,125,129,131,132,135,148,149,150,151,155,157,158,165,166,167,168,169,170,178,179,180,],[-70,-69,73,89,-26,73,73,73,73,-60,-66,73,73,73,73,-27,73,-28,-29,73,-64,73,89,73,-37,-63,-40,-30,-65,-33,-34,-35,-59,-61,73,73,-36,73,73,-62,-31,-32,-38,-39,73,]),'EXISTS_KEY':([48,53,61,67,69,70,71,72,73,76,77,86,87,88,89,96,97,98,99,100,103,106,121,124,125,129,131,132,135,148,149,150,151,155,157,158,165,166,167,168,169,170,178,179,180,],[-70,-69,74,91,-26,74,74,74,74,-60,-66,74,74,74,74,-27,74,-28,-29,74,-64,74,91,74,-37,-63,-40,-30,-65,-33,-34,-35,-59,-61,74,74,-36,74,74,-62,-31,-32,-38,-39,74,]),'FORALL_KEY':([48,53,61,67,69,70,71,72,73,76,77,80,86,87,88,89,96,97,98,99,100,103,106,121,124,125,129,131,132,135,148,149,150,151,155,157,158,165,166,167,168,169,170,178,179,180,],[-70,-69,75,92,-26,75,75,75,75,-60,-66,107,75,75,75,75,-27,75,-28,-29,75,-64,75,92,75,-37,-63,-40,-30,-65,-33,-34,-35,-59,-61,75,75,-36,75,75,-62,-31,-32,-38,-39,75,]),'EQUALS':([48,53,61,66,67,69,70,71,72,73,76,77,80,82,83,84,85,86,87,88,89,96,97,98,99,100,103,105,106,108,112,113,114,115,116,117,118,121,124,125,129,131,132,135,137,139,143,144,145,146,147,148,149,150,151,155,157,158,159,163,165,166,167,168,169,170,171,172,173,176,178,179,180,181,182,185,],[-70,-69,78,78,94,-26,78,78,78,78,-60,-66,110,-43,78,78,110,78,78,78,78,-27,78,-28,-29,78,-64,78,78,78,-44,78,-45,78,-54,78,110,94,78,-37,-63,-40,-30,-65,78,110,-50,-52,-55,78,78,-33,-34,-35,-59,-61,78,78,-46,-57,-36,78,78,-62,-31,-32,-47,78,-56,110,-38,-39,78,-48,78,-49,]),'ONEOF_KEY':([48,53,66,76,77,80,82,83,103,112,113,114,115,116,129,135,143,144,145,146,151,155,159,163,168,171,173,181,185,],[-70,-69,84,-60,-66,105,-43,84,-64,-44,84,-45,-53,-54,-63,-65,-50,-52,-55,-58,-59,-61,-46,-57,-62,-47,-56,-48,-49,]),'PRECONDITION_KEY':([49,63,79,],[55,-24,-23,]),'EFFECT_KEY':([54,95,],[60,-25,]),'WHEN_KEY':([80,176,],[106,180,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'pddl':([0,],[1,]),'domain':([0,],[2,]),'domain_def':([4,],[6,]),'require_def':([6,],[9,]),'types_def':([9,],[13,]),'require_key_lst':([11,16,],[15,26,]),'require_key':([11,16,],[16,16,]),'predicates_def':([13,],[24,]),'names_lst':([22,28,],[27,34,]),'action_def_lst':([24,32,],[31,40,]),'action_def':([24,32,],[32,32,]),'predicate_def_lst':([29,37,],[36,43,]),'predicate_def':([29,37,],[37,37,]),'typed_variables_lst':([41,56,57,101,102,126,127,138,],[45,62,64,133,134,153,154,161,]),'variables_lst':([41,48,56,57,77,93,101,102,109,126,127,138,],[47,53,47,47,103,128,47,47,141,47,47,47,]),'parameters_def':([44,],[49,]),'precond_def':([49,],[54,]),'type':([52,],[57,]),'effects_def':([54,],[59,]),'formula':([61,70,71,72,73,86,87,88,89,97,100,106,124,157,158,166,167,180,],[68,97,97,99,100,97,97,122,124,97,132,137,152,169,170,174,175,182,]),'literal':([61,66,67,70,71,72,73,83,84,86,87,88,89,97,100,105,106,113,115,117,121,124,137,146,147,157,158,166,167,172,180,182,],[69,82,90,69,69,69,69,82,116,69,69,69,69,69,69,116,69,82,116,146,90,69,116,146,146,69,69,69,69,116,69,116,]),'predicate':([61,66,67,70,71,72,73,83,84,86,87,88,89,97,100,105,106,108,113,115,117,121,124,137,146,147,157,158,166,167,172,180,182,],[76,76,76,76,76,76,76,76,76,76,76,123,76,76,76,76,76,140,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'one_eff_formula':([66,83,113,],[81,113,113,]),'formula_lst':([70,71,86,87,97,],[96,98,119,120,131,]),'one_eff_formula_lst':([83,113,],[112,143,]),'atomic_eff_lst':([84,105,115,],[114,136,144,]),'atomic_eff':([84,105,115,137,172,182,],[115,115,115,160,177,183,]),'literal_lst':([117,146,147,],[145,163,164,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> pddl","S'",1,None,None,None),
  ('pddl -> domain','pddl',1,'p_pddl','parser.py',23),
  ('domain -> LPAREN DEFINE_KEY domain_def require_def types_def predicates_def action_def_lst RPAREN','domain',8,'p_domain','parser.py',27),
  ('domain_def -> LPAREN DOMAIN_KEY NAME RPAREN','domain_def',4,'p_domain_def','parser.py',31),
  ('require_def -> LPAREN REQUIREMENTS_KEY require_key_lst RPAREN','require_def',4,'p_require_def','parser.py',35),
  ('require_key_lst -> require_key require_key_lst','require_key_lst',2,'p_require_key_lst','parser.py',39),
  ('require_key_lst -> require_key','require_key_lst',1,'p_require_key_lst','parser.py',40),
  ('require_key -> STRIPS_KEY','require_key',1,'p_require_key','parser.py',47),
  ('require_key -> EQUALITY_KEY','require_key',1,'p_require_key','parser.py',48),
  ('require_key -> TYPING_KEY','require_key',1,'p_require_key','parser.py',49),
  ('require_key -> ADL_KEY','require_key',1,'p_require_key','parser.py',50),
  ('require_key -> ND_KEY','require_key',1,'p_require_key','parser.py',51),
  ('types_def -> LPAREN TYPES_KEY names_lst RPAREN','types_def',4,'p_types_def','parser.py',55),
  ('names_lst -> NAME names_lst','names_lst',2,'p_names_lst','parser.py',59),
  ('names_lst -> NAME','names_lst',1,'p_names_lst','parser.py',60),
  ('predicates_def -> LPAREN PREDICATES_KEY predicate_def_lst RPAREN','predicates_def',4,'p_predicates_def','parser.py',69),
  ('predicate_def_lst -> predicate_def predicate_def_lst','predicate_def_lst',2,'p_predicate_def_lst','parser.py',73),
  ('predicate_def_lst -> predicate_def','predicate_def_lst',1,'p_predicate_def_lst','parser.py',74),
  ('predicate_def -> LPAREN NAME typed_variables_lst RPAREN','predicate_def',4,'p_predicate_def','parser.py',81),
  ('predicate_def -> LPAREN NAME RPAREN','predicate_def',3,'p_predicate_def','parser.py',82),
  ('action_def_lst -> action_def action_def_lst','action_def_lst',2,'p_action_def_lst','parser.py',89),
  ('action_def_lst -> action_def','action_def_lst',1,'p_action_def_lst','parser.py',90),
  ('action_def -> LPAREN ACTION_KEY NAME parameters_def precond_def effects_def RPAREN','action_def',7,'p_action_def','parser.py',97),
  ('parameters_def -> PARAMETERS_KEY LPAREN typed_variables_lst RPAREN','parameters_def',4,'p_parameters_def','parser.py',101),
  ('parameters_def -> PARAMETERS_KEY LPAREN RPAREN','parameters_def',3,'p_parameters_def','parser.py',102),
  ('precond_def -> PRECONDITION_KEY LPAREN formula RPAREN','precond_def',4,'p_precond_def','parser.py',109),
  ('formula -> literal','formula',1,'p_formula','parser.py',113),
  ('formula -> AND_KEY formula_lst','formula',2,'p_formula','parser.py',114),
  ('formula -> OR_KEY formula_lst','formula',2,'p_formula','parser.py',115),
  ('formula -> NOT_KEY formula','formula',2,'p_formula','parser.py',116),
  ('formula -> IMPLY_KEY formula formula','formula',3,'p_formula','parser.py',117),
  ('formula -> EXISTS_KEY LPAREN typed_variables_lst RPAREN formula','formula',5,'p_formula','parser.py',118),
  ('formula -> FORALL_KEY LPAREN typed_variables_lst RPAREN formula','formula',5,'p_formula','parser.py',119),
  ('formula -> LPAREN AND_KEY formula_lst RPAREN','formula',4,'p_formula','parser.py',120),
  ('formula -> LPAREN OR_KEY formula_lst RPAREN','formula',4,'p_formula','parser.py',121),
  ('formula -> LPAREN NOT_KEY formula RPAREN','formula',4,'p_formula','parser.py',122),
  ('formula -> LPAREN IMPLY_KEY formula formula RPAREN','formula',5,'p_formula','parser.py',123),
  ('formula -> LPAREN literal RPAREN','formula',3,'p_formula','parser.py',124),
  ('formula -> LPAREN EXISTS_KEY LPAREN typed_variables_lst RPAREN formula RPAREN','formula',7,'p_formula','parser.py',125),
  ('formula -> LPAREN FORALL_KEY LPAREN typed_variables_lst RPAREN formula RPAREN','formula',7,'p_formula','parser.py',126),
  ('formula_lst -> formula formula_lst','formula_lst',2,'p_formula_lst','parser.py',162),
  ('formula_lst -> formula','formula_lst',1,'p_formula_lst','parser.py',163),
  ('effects_def -> EFFECT_KEY LPAREN one_eff_formula RPAREN','effects_def',4,'p_effects_def','parser.py',170),
  ('one_eff_formula -> literal','one_eff_formula',1,'p_one_eff_formula','parser.py',186),
  ('one_eff_formula -> AND_KEY one_eff_formula_lst','one_eff_formula',2,'p_one_eff_formula','parser.py',187),
  ('one_eff_formula -> ONEOF_KEY atomic_eff_lst','one_eff_formula',2,'p_one_eff_formula','parser.py',188),
  ('one_eff_formula -> LPAREN ONEOF_KEY atomic_eff_lst RPAREN','one_eff_formula',4,'p_one_eff_formula','parser.py',189),
  ('one_eff_formula -> LPAREN WHEN_KEY formula atomic_eff RPAREN','one_eff_formula',5,'p_one_eff_formula','parser.py',190),
  ('one_eff_formula -> LPAREN FORALL_KEY LPAREN typed_variables_lst RPAREN atomic_eff RPAREN','one_eff_formula',7,'p_one_eff_formula','parser.py',191),
  ('one_eff_formula -> LPAREN FORALL_KEY LPAREN typed_variables_lst RPAREN LPAREN WHEN_KEY formula atomic_eff RPAREN RPAREN','one_eff_formula',11,'p_one_eff_formula','parser.py',192),
  ('one_eff_formula_lst -> one_eff_formula one_eff_formula_lst','one_eff_formula_lst',2,'p_one_eff_formula_lst','parser.py',210),
  ('one_eff_formula_lst -> one_eff_formula','one_eff_formula_lst',1,'p_one_eff_formula_lst','parser.py',211),
  ('atomic_eff_lst -> atomic_eff atomic_eff_lst','atomic_eff_lst',2,'p_atomic_eff_lst','parser.py',218),
  ('atomic_eff_lst -> atomic_eff','atomic_eff_lst',1,'p_atomic_eff_lst','parser.py',219),
  ('atomic_eff -> literal','atomic_eff',1,'p_atomic_eff','parser.py',226),
  ('atomic_eff -> AND_KEY literal_lst','atomic_eff',2,'p_atomic_eff','parser.py',227),
  ('atomic_eff -> LPAREN AND_KEY literal_lst RPAREN','atomic_eff',4,'p_atomic_eff','parser.py',228),
  ('literal_lst -> literal literal_lst','literal_lst',2,'p_literal_lst','parser.py',243),
  ('literal_lst -> literal','literal_lst',1,'p_literal_lst','parser.py',244),
  ('literal -> LPAREN NOT_KEY predicate RPAREN','literal',4,'p_literal','parser.py',251),
  ('literal -> predicate','literal',1,'p_literal','parser.py',252),
  ('predicate -> LPAREN NAME variables_lst RPAREN','predicate',4,'p_predicate','parser.py',259),
  ('predicate -> LPAREN EQUALS VARIABLE VARIABLE RPAREN','predicate',5,'p_predicate','parser.py',260),
  ('predicate -> LPAREN NAME RPAREN','predicate',3,'p_predicate','parser.py',261),
  ('predicate -> NAME variables_lst','predicate',2,'p_predicate','parser.py',262),
  ('predicate -> EQUALS VARIABLE VARIABLE','predicate',3,'p_predicate','parser.py',263),
  ('predicate -> NAME','predicate',1,'p_predicate','parser.py',264),
  ('typed_variables_lst -> variables_lst HYPHEN type typed_variables_lst','typed_variables_lst',4,'p_typed_variables_lst','parser.py',280),
  ('typed_variables_lst -> variables_lst HYPHEN type','typed_variables_lst',3,'p_typed_variables_lst','parser.py',281),
  ('variables_lst -> VARIABLE variables_lst','variables_lst',2,'p_variables_lst','parser.py',288),
  ('variables_lst -> VARIABLE','variables_lst',1,'p_variables_lst','parser.py',289),
  ('type -> NAME','type',1,'p_type','parser.py',296),
]
