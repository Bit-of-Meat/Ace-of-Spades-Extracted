# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.frontend.mapsPanel

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_FORWARD come_froms
_ifstmts_jump ::= c_stmts_opt . JUMP_FORWARD come_froms
_ifstmts_jump ::= c_stmts_opt JUMP_FORWARD . come_froms
_ifstmts_jump ::= c_stmts_opt JUMP_FORWARD come_froms . 
_stmts ::= _stmts . stmt
_stmts ::= _stmts stmt . 
_stmts ::= stmt . 
and ::= expr . JUMP_IF_FALSE_OR_POP expr COME_FROM
and ::= expr . jmp_false expr \e_come_from_opt
and ::= expr . jmp_false expr come_from_opt
and ::= expr jmp_false . expr \e_come_from_opt
and ::= expr jmp_false . expr come_from_opt
and ::= expr jmp_false expr . come_from_opt
and ::= expr jmp_false expr \e_come_from_opt . 
and ::= expr jmp_false expr come_from_opt . 
assert ::= assert_expr . jmp_true LOAD_ASSERT RAISE_VARARGS_1
assert ::= assert_expr jmp_true . LOAD_ASSERT RAISE_VARARGS_1
assert2 ::= assert_expr . jmp_true LOAD_ASSERT expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert2 ::= assert_expr jmp_true . LOAD_ASSERT expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_expr ::= assert_expr_and . 
assert_expr ::= assert_expr_or . 
assert_expr ::= expr . 
assert_expr_and ::= assert_expr . jmp_false expr
assert_expr_and ::= assert_expr jmp_false . expr
assert_expr_and ::= assert_expr jmp_false expr . 
assert_expr_or ::= assert_expr . jmp_true expr
assert_expr_or ::= assert_expr jmp_true . expr
assert_expr_or ::= assert_expr jmp_true expr . 
assign ::= expr . DUP_TOP designList
assign ::= expr . store
assign ::= expr store . 
assign2 ::= expr . expr ROT_TWO store store
assign2 ::= expr expr . ROT_TWO store store
assign3 ::= expr . expr expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr . expr ROT_THREE ROT_TWO store store store
assign3 ::= expr expr expr . ROT_THREE ROT_TWO store store store
attribute ::= expr . GET_ITER
attribute ::= expr . LOAD_ATTR
attribute ::= expr GET_ITER . 
attribute ::= expr LOAD_ATTR . 
aug_assign1 ::= expr . expr inplace_op ROT_FOUR STORE_SLICE+3
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SLICE+1
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SLICE+2
aug_assign1 ::= expr . expr inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr . expr inplace_op ROT_TWO STORE_SLICE+0
aug_assign1 ::= expr . expr inplace_op store
aug_assign1 ::= expr expr . inplace_op ROT_FOUR STORE_SLICE+3
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SLICE+1
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SLICE+2
aug_assign1 ::= expr expr . inplace_op ROT_THREE STORE_SUBSCR
aug_assign1 ::= expr expr . inplace_op ROT_TWO STORE_SLICE+0
aug_assign1 ::= expr expr . inplace_op store
aug_assign2 ::= expr . DUP_TOP LOAD_ATTR expr inplace_op ROT_TWO STORE_ATTR
bin_op ::= expr . expr binary_operator
bin_op ::= expr expr . binary_operator
bin_op ::= expr expr binary_operator . 
binary_operator ::= BINARY_ADD . 
buildclass ::= LOAD_CONST . expr mkfunc CALL_FUNCTION_0 BUILD_CLASS
buildclass ::= LOAD_CONST expr . mkfunc CALL_FUNCTION_0 BUILD_CLASS
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= continues . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . expr CALL_FUNCTION_1
call ::= expr . expr expr CALL_FUNCTION_2
call ::= expr . expr expr expr expr expr CALL_FUNCTION_5
call ::= expr . expr expr expr expr expr kwarg CALL_FUNCTION_261
call ::= expr . expr expr kwarg kwarg kwarg kwarg kwarg CALL_FUNCTION_1282
call ::= expr . expr kwarg CALL_FUNCTION_257
call ::= expr . expr kwarg kwarg kwarg CALL_FUNCTION_769
call ::= expr CALL_FUNCTION_0 . 
call ::= expr expr . CALL_FUNCTION_1
call ::= expr expr . expr CALL_FUNCTION_2
call ::= expr expr . expr expr expr expr CALL_FUNCTION_5
call ::= expr expr . expr expr expr expr kwarg CALL_FUNCTION_261
call ::= expr expr . expr kwarg kwarg kwarg kwarg kwarg CALL_FUNCTION_1282
call ::= expr expr . kwarg CALL_FUNCTION_257
call ::= expr expr . kwarg kwarg kwarg CALL_FUNCTION_769
call ::= expr expr CALL_FUNCTION_1 . 
call ::= expr expr expr . CALL_FUNCTION_2
call ::= expr expr expr . expr expr expr CALL_FUNCTION_5
call ::= expr expr expr . expr expr expr kwarg CALL_FUNCTION_261
call ::= expr expr expr . kwarg kwarg kwarg kwarg kwarg CALL_FUNCTION_1282
call ::= expr expr expr CALL_FUNCTION_2 . 
call ::= expr expr expr expr . expr expr CALL_FUNCTION_5
call ::= expr expr expr expr . expr expr kwarg CALL_FUNCTION_261
call ::= expr expr expr expr expr . expr CALL_FUNCTION_5
call ::= expr expr expr expr expr . expr kwarg CALL_FUNCTION_261
call ::= expr expr expr expr expr expr . CALL_FUNCTION_5
call ::= expr expr expr expr expr expr . kwarg CALL_FUNCTION_261
call ::= expr expr expr expr expr expr kwarg . CALL_FUNCTION_261
call ::= expr expr expr kwarg . kwarg kwarg kwarg kwarg CALL_FUNCTION_1282
call ::= expr expr expr kwarg kwarg . kwarg kwarg kwarg CALL_FUNCTION_1282
call ::= expr expr kwarg . CALL_FUNCTION_257
call ::= expr expr kwarg . kwarg kwarg CALL_FUNCTION_769
call ::= expr expr kwarg kwarg . kwarg CALL_FUNCTION_769
call ::= expr expr kwarg kwarg kwarg . CALL_FUNCTION_769
call ::= expr expr kwarg kwarg kwarg CALL_FUNCTION_769 . 
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
classdefdeco2 ::= LOAD_CONST . expr mkfunc CALL_FUNCTION_0 BUILD_CLASS
classdefdeco2 ::= LOAD_CONST expr . mkfunc CALL_FUNCTION_0 BUILD_CLASS
come_from_opt ::= COME_FROM . 
come_froms ::= COME_FROM . 
come_froms ::= come_froms . COME_FROM
compare ::= compare_single . 
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP \e__come_froms
compare_chained ::= expr . compare_chained1 ROT_TWO POP_TOP _come_froms
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained1 COME_FROM
compare_chained1 ::= expr . DUP_TOP ROT_THREE COMPARE_OP JUMP_IF_FALSE_OR_POP compare_chained2 COME_FROM
compare_single ::= expr . expr COMPARE_OP
compare_single ::= expr expr . COMPARE_OP
compare_single ::= expr expr COMPARE_OP . 
continue ::= CONTINUE . 
continues ::= _stmts . lastl_stmt continue
continues ::= _stmts lastl_stmt . continue
continues ::= continue . 
continues ::= lastl_stmt . continue
continues ::= lastl_stmt continue . 
delete ::= expr . DELETE_ATTR
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
else_suitec ::= c_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= and . 
expr ::= attribute . 
expr ::= bin_op . 
expr ::= call . 
expr ::= compare . 
expr ::= get_iter . 
expr ::= list . 
expr ::= or . 
expr ::= subscript . 
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
for ::= SETUP_LOOP . expr for_iter store for_block POP_BLOCK \e__come_froms
for ::= SETUP_LOOP . expr for_iter store for_block POP_BLOCK _come_froms
for ::= SETUP_LOOP expr . for_iter store for_block POP_BLOCK \e__come_froms
for ::= SETUP_LOOP expr . for_iter store for_block POP_BLOCK _come_froms
for ::= SETUP_LOOP expr for_iter . store for_block POP_BLOCK \e__come_froms
for ::= SETUP_LOOP expr for_iter . store for_block POP_BLOCK _come_froms
for ::= SETUP_LOOP expr for_iter store . for_block POP_BLOCK \e__come_froms
for ::= SETUP_LOOP expr for_iter store . for_block POP_BLOCK _come_froms
for_block ::= \e_l_stmts_opt . JUMP_ABSOLUTE JUMP_BACK JUMP_BACK
for_block ::= \e_l_stmts_opt . JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt . JUMP_ABSOLUTE JUMP_BACK JUMP_BACK
for_block ::= l_stmts_opt . JUMP_BACK
for_block ::= l_stmts_opt . _come_froms JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_iter ::= GET_ITER . COME_FROM FOR_ITER
for_iter ::= GET_ITER . FOR_ITER
for_iter ::= GET_ITER FOR_ITER . 
forelselaststmtl ::= SETUP_LOOP . expr for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP . expr for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr . for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr . for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr for_iter . store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr for_iter . store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr for_iter store . for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr for_iter store . for_block POP_BLOCK else_suitel _come_froms
forelsestmt ::= SETUP_LOOP . expr for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP . expr for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr . for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr . for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr for_iter . store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr for_iter . store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr for_iter store . for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr for_iter store . for_block POP_BLOCK else_suite _come_froms
genexpr_func ::= LOAD_FAST . FOR_ITER store comp_iter JUMP_BACK
get_iter ::= expr . GET_ITER
get_iter ::= expr GET_ITER . 
if_exp ::= expr . jmp_false expr JUMP_ABSOLUTE expr
if_exp ::= expr . jmp_false expr JUMP_FORWARD expr COME_FROM
if_exp ::= expr jmp_false . expr JUMP_ABSOLUTE expr
if_exp ::= expr jmp_false . expr JUMP_FORWARD expr COME_FROM
if_exp ::= expr jmp_false expr . JUMP_ABSOLUTE expr
if_exp ::= expr jmp_false expr . JUMP_FORWARD expr COME_FROM
if_exp_lambda ::= expr . jmp_false expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_lambda ::= expr jmp_false expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not ::= expr . jmp_true expr _jump expr COME_FROM
if_exp_not ::= expr jmp_true . expr _jump expr COME_FROM
if_exp_not ::= expr jmp_true expr . _jump expr COME_FROM
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true . expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_not_lambda ::= expr jmp_true expr . return_if_lambda return_stmt_lambda LAMBDA_MARKER
if_exp_true ::= expr . JUMP_FORWARD expr COME_FROM
ifelsestmt ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite come_froms
ifelsestmt ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite come_froms
ifelsestmt ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite come_froms
ifelsestmt ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite come_froms
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite come_froms
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite come_froms
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite come_froms
ifelsestmtc ::= testexpr c_stmts_opt JUMP_ABSOLUTE . else_suitec
ifelsestmtc ::= testexpr c_stmts_opt JUMP_ABSOLUTE else_suitec . 
ifelsestmtc ::= testexpr c_stmts_opt JUMP_FORWARD . else_suite come_froms
ifelsestmtl ::= testexpr . c_stmts_opt CONTINUE else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt JUMP_BACK else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . CONTINUE else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . JUMP_BACK else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt CONTINUE . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . CONTINUE else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . JUMP_BACK else_suitel
ifelsestmtl ::= testexpr c_stmts_opt CONTINUE . else_suitel
ifelsestmtr ::= testexpr . return_if_stmts COME_FROM returns
iflaststmt ::= testexpr . c_stmts_opt JUMP_ABSOLUTE
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE
iflaststmt ::= testexpr c_stmts_opt . JUMP_ABSOLUTE
iflaststmt ::= testexpr c_stmts_opt JUMP_ABSOLUTE . 
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts_opt JUMP_BACK
iflaststmtl ::= testexpr \e_c_stmts_opt . JUMP_BACK
iflaststmtl ::= testexpr c_stmts . 
iflaststmtl ::= testexpr c_stmts_opt . JUMP_BACK
ifstmt ::= testexpr . _ifstmts_jump
ifstmt ::= testexpr . return_if_stmts COME_FROM
ifstmt ::= testexpr . return_stmts COME_FROM
ifstmt ::= testexpr _ifstmts_jump . 
import ::= LOAD_CONST . LOAD_CONST alias
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
kwarg ::= LOAD_CONST . expr
kwarg ::= LOAD_CONST expr . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= continues . 
l_stmts ::= lastl_stmt . 
l_stmts_opt ::= l_stmts . 
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
list ::= BUILD_LIST_0 . 
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr BUILD_LIST_1 . 
list ::= expr expr . BUILD_LIST_2
list ::= expr expr BUILD_LIST_2 . 
list_comp ::= BUILD_LIST_0 . list_iter
mkfunc ::= expr . LOAD_CODE MAKE_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= expr_jt . expr \e_come_from_opt
or ::= expr_jt . expr come_from_opt
or ::= expr_jt expr . come_from_opt
or ::= expr_jt expr \e_come_from_opt . 
or ::= expr_jt expr come_from_opt . 
print_items_nl_stmt ::= expr . PRINT_ITEM \e_print_items_opt PRINT_NEWLINE_CONT
print_items_nl_stmt ::= expr . PRINT_ITEM print_items_opt PRINT_NEWLINE_CONT
print_items_stmt ::= expr . PRINT_ITEM \e_print_items_opt
print_items_stmt ::= expr . PRINT_ITEM print_items_opt
print_nl_to ::= expr . PRINT_NEWLINE_TO
print_to ::= expr . print_to_items POP_TOP
print_to_nl ::= expr . print_to_items PRINT_NEWLINE_TO
raise_stmt1 ::= expr . RAISE_VARARGS_1
raise_stmt2 ::= expr . expr RAISE_VARARGS_2
raise_stmt2 ::= expr expr . RAISE_VARARGS_2
raise_stmt3 ::= expr . expr expr RAISE_VARARGS_3
raise_stmt3 ::= expr expr . expr RAISE_VARARGS_3
raise_stmt3 ::= expr expr expr . RAISE_VARARGS_3
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_VALUE
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmts ::= _stmts . return_if_stmt
return_stmts ::= _stmts . return_stmt
returns ::= _stmts . return
slice0 ::= expr . DUP_TOP SLICE+0
slice0 ::= expr . SLICE+0
slice1 ::= expr . expr DUP_TOPX_2 SLICE+1
slice1 ::= expr . expr SLICE+1
slice1 ::= expr expr . DUP_TOPX_2 SLICE+1
slice1 ::= expr expr . SLICE+1
slice2 ::= expr . expr DUP_TOPX_2 SLICE+2
slice2 ::= expr . expr SLICE+2
slice2 ::= expr expr . DUP_TOPX_2 SLICE+2
slice2 ::= expr expr . SLICE+2
slice3 ::= expr . expr expr DUP_TOPX_3 SLICE+3
slice3 ::= expr . expr expr SLICE+3
slice3 ::= expr expr . expr DUP_TOPX_3 SLICE+3
slice3 ::= expr expr . expr SLICE+3
slice3 ::= expr expr expr . DUP_TOPX_3 SLICE+3
slice3 ::= expr expr expr . SLICE+3
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= call_stmt . 
stmt ::= continue . 
stmt ::= ifstmt . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= expr . STORE_SLICE+0
store ::= expr . expr STORE_SLICE+1
store ::= expr . expr STORE_SLICE+2
store ::= expr . expr expr STORE_SLICE+3
store ::= expr STORE_ATTR . 
store ::= expr expr . STORE_SLICE+1
store ::= expr expr . STORE_SLICE+2
store ::= expr expr . expr STORE_SLICE+3
store ::= expr expr expr . STORE_SLICE+3
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript ::= expr expr BINARY_SUBSCR . 
subscript2 ::= expr . expr DUP_TOPX_2 BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOPX_2 BINARY_SUBSCR
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
unary_convert ::= expr . UNARY_CONVERT
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_2 . store store
unpack ::= UNPACK_SEQUENCE_2 store . store
unpack ::= UNPACK_SEQUENCE_2 store store . 
while1elsestmt ::= SETUP_LOOP . l_stmts JUMP_BACK POP_BLOCK else_suitel COME_FROM
while1elsestmt ::= SETUP_LOOP . l_stmts JUMP_BACK else_suitel COME_FROM
while1stmt ::= SETUP_LOOP . l_stmts_opt CONTINUE COME_FROM
while1stmt ::= SETUP_LOOP . l_stmts_opt JUMP_BACK COME_FROM
while1stmt ::= SETUP_LOOP . l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM
while1stmt ::= SETUP_LOOP . returns COME_FROM
while1stmt ::= SETUP_LOOP . returns pb_come_from
while1stmt ::= SETUP_LOOP \e_l_stmts_opt . CONTINUE COME_FROM
while1stmt ::= SETUP_LOOP \e_l_stmts_opt . JUMP_BACK COME_FROM
while1stmt ::= SETUP_LOOP \e_l_stmts_opt . JUMP_BACK POP_BLOCK COME_FROM
whileelsestmt ::= SETUP_LOOP . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= SETUP_LOOP . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whilestmt ::= SETUP_LOOP . testexpr \e_l_stmts_opt JUMP_BACK JUMP_BACK POP_BLOCK \e__come_froms
whilestmt ::= SETUP_LOOP . testexpr \e_l_stmts_opt JUMP_BACK JUMP_BACK POP_BLOCK _come_froms
whilestmt ::= SETUP_LOOP . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK \e__come_froms
whilestmt ::= SETUP_LOOP . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK _come_froms
whilestmt ::= SETUP_LOOP . testexpr l_stmts_opt JUMP_BACK JUMP_BACK POP_BLOCK \e__come_froms
whilestmt ::= SETUP_LOOP . testexpr l_stmts_opt JUMP_BACK JUMP_BACK POP_BLOCK _come_froms
whilestmt ::= SETUP_LOOP . testexpr l_stmts_opt JUMP_BACK POP_BLOCK \e__come_froms
whilestmt ::= SETUP_LOOP . testexpr l_stmts_opt JUMP_BACK POP_BLOCK _come_froms
whilestmt ::= SETUP_LOOP . testexpr returns \e__come_froms POP_BLOCK COME_FROM
whilestmt ::= SETUP_LOOP . testexpr returns _come_froms POP_BLOCK COME_FROM
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH WITH_CLEANUP END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH WITH_CLEANUP END_FINALLY
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH WITH_CLEANUP END_FINALLY
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH WITH_CLEANUP END_FINALLY
yield ::= expr . YIELD_VALUE
Instruction context:
   
 L. 158       375  CONTINUE            265  'to 265'
->               378  JUMP_FORWARD        103  'to 484'
from aoslib.scenes.frontend.listPanelBase import ListPanelBase
from aoslib.scenes.frontend.expandableListPanel import ExpandableListPanel
from aoslib.scenes.main.mapListItem import MapListItem
from aoslib.scenes.main.ownableItemBase import OwnableItemBase
from aoslib.scenes.main.categoryListItem import CategoryListItem
from aoslib.scenes.frontend.lobbyPanelBase import LobbyPanelBase
from aoslib.scenes.main.matchSettings import get_string_as_list, get_list_items_as_string, generate_ugc_map_filename_from_lobby, generate_ugc_map_filename, generate_ugc_map_title
from aoslib import strings
from aoslib.scenes import MenuScene
from aoslib.gui import SliderOption
from shared.constants_matchmaking import A2665
from shared.steam import SteamGetLobbyData, SteamSetLobbyData, SteamAmITheLobbyOwner, SteamGetSubscribedContentTitle
from shared.hud_constants import ROW_DARK_GREY_COLOUR, ROW_GREY_COLOUR
from aoslib.ugc_data import get_available_game_modes, get_map_baseplate, get_hosted_ugc_map_names, get_subscribed_ugc_map_names
from shared.constants_gamemode import A2450
from aoslib.ugc_data import get_ugc_data_from_file
import playlists

class MapsPanel(LobbyPanelBase):

    def __init__(self, manager, ugc_mode=False):
        self.ugc_mode = ugc_mode
        super(MapsPanel, self).__init__(manager)

    def initialize(self):
        super(MapsPanel, self).initialize()
        self.expandable_list_panel = ExpandableListPanel(self.manager)
        self.maps = {}
        self.original_maps = []

    def initialise_ui(self, lobby_id, x, y, width, height):
        super(MapsPanel, self).initialise_ui(lobby_id, x, y, width, height)
        self.elements.append(self.expandable_list_panel)
        self.select_all_text = strings.SELECT_ALL
        self.expandable_list_panel.initialise_ui(strings.MAPS, x, y, width, height, has_header=True)
        self.expandable_list_panel.center_header_text = True
        self.expandable_list_panel.add_on_item_selected_handler(self.on_row_selected, 0)
        self.__initialise()

    def close(self):
        for row in [ row for row in self.expandable_list_panel.rows if hasattr(row, 'close') ]:
            row.close()

        return super(MapsPanel, self).close()

    def __initialise(self):
        self.generate_maps_lists_per_dlc()
        self.populate_playlist()
        self.expandable_list_panel.scrollbar.set_scroll(0)

    def set_content_visibility(self, visible):
        super(MapsPanel, self).set_content_visibility(visible)
        if not SteamAmITheLobbyOwner():
            return
        if visible:
            self.__initialise()

    def generate_maps_lists_per_dlc(self):
        game_modes_string = SteamGetLobbyData(self.lobby_id, 'PLAYLIST')
        if self.ugc_mode and game_modes_string != 'ugc':
            game_modes_string = 'ugc'
        map_rotation_string = SteamGetLobbyData(self.lobby_id, 'MAP_ROTATION_FILENAME')
        game_modes = get_string_as_list(game_modes_string)
        self.original_maps = get_string_as_list(map_rotation_string)
        self.maps.clear()
        for id in A2665:
            self.maps[id] = {}

        self.maps['SAVED_MAPS'] = {}
        self.maps['SUBSCRIBED_MAPS'] = {}
        self.maps['TEMPLATES'] = {}
        for map_name, map_info in playlists.mapinfo.map_info.iteritems():
            valid_map = False
            for mode in game_modes:
                if mode == 'cctf':
                    test_mode = 'ctf'
                else:
                    test_mode = mode
                if test_mode not in map_info['invalid_modes']:
                    valid_map = True
                    break

            if valid_map:
                selected = map_name in self.original_maps
                if map_info['classic']:
                    self.maps['A2362'][map_name] = selected
                elif map_info['mafia']:
                    self.maps['MAFIA_PACK'][map_name] = selected
                else:
                    if 'Baseplate' in map_name:
                        self.maps['TEMPLATES'][map_name] = selected
                    else:
                        self.maps['STANDARD'][map_name] = selected
            hosted_ugc_map_names = get_hosted_ugc_map_names()
            subscribed_ugc_map_names = get_subscribed_ugc_map_names()
            if not self.ugc_mode:
                for map_name in subscribed_ugc_map_names:
                    if A2450[game_modes[0]] not in get_available_game_modes(map_name, True) and not self.ugc_mode:
                        continue
                    selected = map_name in self.original_maps or map_name == self.manager.hosted_ugc_map_filename
                    self.maps['SUBSCRIBED_MAPS'][map_name] = selected

            for map_name in hosted_ugc_map_names:
                if map_name in subscribed_ugc_map_names:
                    continue
                if A2450[game_modes[0]] not in get_available_game_modes(map_name) and not self.ugc_mode:
                    continue
                selected = map_name in self.original_maps or map_name == self.manager.hosted_ugc_map_filename
                self.maps['SAVED_MAPS'][map_name] = selected

    def populate_playlist--- This code section failed: ---

 L. 122         0  LOAD_FAST             0  'self'
                3  LOAD_ATTR             0  'expandable_list_panel'
                6  LOAD_ATTR             1  'reset_list'
                9  CALL_FUNCTION_0       0  None
               12  POP_TOP          

 L. 123        13  LOAD_CONST               None
               16  STORE_FAST            1  'row_name_to_select'

 L. 125        19  LOAD_CONST               'SAVED_MAPS'
               22  BUILD_LIST_1          1 
               25  LOAD_CONST               'SUBSCRIBED_MAPS'
               28  BUILD_LIST_1          1 
               31  BINARY_ADD       
               32  LOAD_GLOBAL           3  'A2665'
               35  BINARY_ADD       
               36  LOAD_CONST               'TEMPLATES'
               39  BUILD_LIST_1          1 
               42  BINARY_ADD       
               43  STORE_FAST            2  'packs'

 L. 126        46  LOAD_GLOBAL           4  'SteamGetLobbyData'
               49  LOAD_FAST             0  'self'
               52  LOAD_ATTR             5  'lobby_id'
               55  LOAD_CONST               'MAP_ROTATION_FILENAME'
               58  CALL_FUNCTION_2       2  None
               61  STORE_FAST            3  'current_map_selected'

 L. 128        64  SETUP_LOOP          517  'to 584'
               67  LOAD_FAST             2  'packs'
               70  GET_ITER         
               71  FOR_ITER            509  'to 583'
               74  STORE_FAST            4  'pack_name'

 L. 129        77  LOAD_FAST             4  'pack_name'
               80  LOAD_FAST             0  'self'
               83  LOAD_ATTR             6  'maps'
               86  LOAD_ATTR             7  'keys'
               89  CALL_FUNCTION_0       0  None
               92  COMPARE_OP            7  not-in
               95  POP_JUMP_IF_FALSE   104  'to 104'

 L. 130        98  CONTINUE             71  'to 71'
              101  JUMP_FORWARD          0  'to 104'
            104_0  COME_FROM           101  '101'

 L. 132       104  LOAD_FAST             0  'self'
              107  LOAD_ATTR             6  'maps'
              110  LOAD_FAST             4  'pack_name'
              113  BINARY_SUBSCR    
              114  STORE_FAST            5  'maps'

 L. 134       117  LOAD_FAST             4  'pack_name'
              120  LOAD_CONST               'SAVED_MAPS'
              123  COMPARE_OP            2  ==
              126  POP_JUMP_IF_TRUE    141  'to 141'
              129  LOAD_FAST             4  'pack_name'
              132  LOAD_CONST               'SUBSCRIBED_MAPS'
              135  COMPARE_OP            2  ==
            138_0  COME_FROM           126  '126'
              138  POP_JUMP_IF_FALSE   165  'to 165'
              141  LOAD_GLOBAL           8  'len'
              144  LOAD_FAST             5  'maps'
              147  CALL_FUNCTION_1       1  None
              150  LOAD_CONST               0
              153  COMPARE_OP            2  ==
            156_0  COME_FROM           138  '138'
              156  POP_JUMP_IF_FALSE   165  'to 165'

 L. 135       159  CONTINUE             71  'to 71'
              162  JUMP_FORWARD          0  'to 165'
            165_0  COME_FROM           162  '162'

 L. 137       165  LOAD_GLOBAL           9  'CategoryListItem'
              168  LOAD_GLOBAL          10  'strings'
              171  LOAD_ATTR            11  'get_by_id'
              174  LOAD_FAST             4  'pack_name'
              177  CALL_FUNCTION_1       1  None
              180  LOAD_CONST               'is_expandable'
              183  LOAD_GLOBAL          12  'True'
              186  LOAD_CONST               'sub_row_colours'
              189  LOAD_GLOBAL          13  'ROW_GREY_COLOUR'
              192  LOAD_GLOBAL          14  'ROW_DARK_GREY_COLOUR'
              195  BUILD_LIST_2          2 
              198  LOAD_CONST               'sort_order'
              201  LOAD_FAST             2  'packs'
              204  LOAD_ATTR            15  'index'
              207  LOAD_FAST             4  'pack_name'
              210  CALL_FUNCTION_1       1  None
              213  CALL_FUNCTION_769   769  None
              216  STORE_FAST            6  'categoryItem'

 L. 138       219  LOAD_GLOBAL          16  'False'
              222  LOAD_FAST             6  'categoryItem'
              225  STORE_ATTR           17  'center_text'

 L. 139       228  LOAD_GLOBAL          12  'True'
              231  STORE_FAST            7  'available_map'

 L. 140       234  BUILD_LIST_0          0 
              237  STORE_FAST            8  'map_items'

 L. 145       240  LOAD_GLOBAL          16  'False'
              243  STORE_FAST            9  'custom_map'

 L. 146       246  LOAD_CONST               ''
              249  STORE_FAST           10  'author'

 L. 147       252  SETUP_LOOP          306  'to 561'
              255  LOAD_FAST             5  'maps'
              258  LOAD_ATTR            18  'iteritems'
              261  CALL_FUNCTION_0       0  None
              264  GET_ITER         
              265  FOR_ITER            292  'to 560'
              268  UNPACK_SEQUENCE_2     2 
              271  STORE_FAST           11  'map_filename'
              274  STORE_FAST           12  'selected'

 L. 148       277  LOAD_FAST             4  'pack_name'
              280  LOAD_CONST               'SAVED_MAPS'
              283  COMPARE_OP            2  ==
              286  POP_JUMP_IF_FALSE   381  'to 381'

 L. 149       289  LOAD_GLOBAL          19  'get_ugc_data_from_file'
              292  LOAD_FAST            11  'map_filename'
              295  CALL_FUNCTION_1       1  None
              298  STORE_FAST           13  'data'

 L. 151       301  LOAD_FAST            13  'data'
              304  LOAD_CONST               None
              307  COMPARE_OP            9  is-not
              310  POP_JUMP_IF_FALSE   265  'to 265'
              313  LOAD_CONST               'title'
              316  LOAD_FAST            13  'data'
              319  COMPARE_OP            6  in
            322_0  COME_FROM           310  '310'
              322  POP_JUMP_IF_FALSE   265  'to 265'

 L. 152       325  LOAD_FAST            13  'data'
              328  LOAD_CONST               'title'
              331  BINARY_SUBSCR    
              332  STORE_FAST           14  'display_map_name'

 L. 153       335  LOAD_FAST            11  'map_filename'
              338  STORE_FAST           15  'filename'

 L. 154       341  LOAD_GLOBAL          12  'True'
              344  STORE_FAST            9  'custom_map'

 L. 155       347  LOAD_CONST               'author'
              350  LOAD_FAST            13  'data'
              353  COMPARE_OP            6  in
              356  POP_JUMP_IF_FALSE   378  'to 378'

 L. 156       359  LOAD_FAST            13  'data'
              362  LOAD_CONST               'author'
              365  BINARY_SUBSCR    
              366  STORE_FAST           10  'author'
              369  JUMP_ABSOLUTE       378  'to 378'
              372  JUMP_ABSOLUTE       484  'to 484'

 L. 158       375  CONTINUE            265  'to 265'
              378  JUMP_FORWARD        103  'to 484'

 L. 159       381  LOAD_FAST             4  'pack_name'
              384  LOAD_CONST               'SUBSCRIBED_MAPS'
              387  COMPARE_OP            2  ==
              390  POP_JUMP_IF_FALSE   436  'to 436'

 L. 160       393  LOAD_GLOBAL          19  'get_ugc_data_from_file'
              396  LOAD_FAST            11  'map_filename'
              399  CALL_FUNCTION_1       1  None
              402  POP_TOP          

 L. 161       403  LOAD_GLOBAL          20  'SteamGetSubscribedContentTitle'
              406  LOAD_FAST            11  'map_filename'
              409  CALL_FUNCTION_1       1  None
              412  STORE_FAST           14  'display_map_name'

 L. 162       415  LOAD_FAST            11  'map_filename'
              418  STORE_FAST           15  'filename'

 L. 163       421  LOAD_GLOBAL          12  'True'
              424  STORE_FAST            9  'custom_map'

 L. 164       427  LOAD_CONST               ''
              430  STORE_FAST           10  'author'
              433  JUMP_FORWARD         48  'to 484'

 L. 167       436  LOAD_FAST            11  'map_filename'
              439  STORE_FAST           15  'filename'

 L. 168       442  LOAD_FAST            11  'map_filename'
              445  STORE_FAST           14  'display_map_name'

 L. 169       448  LOAD_FAST             4  'pack_name'
              451  LOAD_CONST               'TEMPLATES'
              454  COMPARE_OP            2  ==
              457  POP_JUMP_IF_FALSE   484  'to 484'

 L. 170       460  LOAD_GLOBAL          12  'True'
              463  STORE_FAST            9  'custom_map'

 L. 171       466  LOAD_GLOBAL          10  'strings'
              469  LOAD_ATTR            11  'get_by_id'
              472  LOAD_FAST            11  'map_filename'
              475  CALL_FUNCTION_1       1  None
              478  STORE_FAST           14  'display_map_name'
              481  JUMP_FORWARD          0  'to 484'
            484_0  COME_FROM           481  '481'
            484_1  COME_FROM           433  '433'
            484_2  COME_FROM           378  '378'

 L. 173       484  LOAD_GLOBAL          21  'OwnableItemBase'
              487  LOAD_FAST            14  'display_map_name'
              490  LOAD_FAST             0  'self'
              493  LOAD_ATTR            22  'manager'
              496  LOAD_ATTR            23  'dlc_manager'
              499  LOAD_CONST               'pack_name'
              502  LOAD_FAST             4  'pack_name'
              505  LOAD_CONST               'filename'
              508  LOAD_FAST            15  'filename'
              511  LOAD_CONST               'uid'
              514  LOAD_FAST            11  'map_filename'
              517  LOAD_CONST               'custom_map'
              520  LOAD_FAST             9  'custom_map'
              523  LOAD_CONST               'author'
              526  LOAD_FAST            10  'author'
              529  CALL_FUNCTION_1282  1282  None
              532  STORE_FAST           16  'mapItem'

 L. 174       535  LOAD_GLOBAL          16  'False'
              538  LOAD_FAST            16  'mapItem'
              541  STORE_ATTR           17  'center_text'

 L. 175       544  LOAD_FAST             8  'map_items'
              547  LOAD_ATTR            24  'append'
              550  LOAD_FAST            16  'mapItem'
              553  CALL_FUNCTION_1       1  None
              556  POP_TOP          
              557  JUMP_BACK           265  'to 265'
              560  POP_BLOCK        
            561_0  COME_FROM           252  '252'

 L. 176       561  LOAD_FAST             0  'self'
              564  LOAD_ATTR             0  'expandable_list_panel'
              567  LOAD_ATTR            25  'add_list_item'
              570  LOAD_FAST             6  'categoryItem'
              573  LOAD_FAST             8  'map_items'
              576  CALL_FUNCTION_2       2  None
              579  POP_TOP          
              580  JUMP_BACK            71  'to 71'
              583  POP_BLOCK        
            584_0  COME_FROM            64  '64'

 L. 178       584  LOAD_FAST             0  'self'
              587  LOAD_ATTR             0  'expandable_list_panel'
              590  LOAD_ATTR            26  'on_scroll'
              593  LOAD_CONST               0
              596  LOAD_CONST               'silent'
              599  LOAD_GLOBAL          12  'True'
              602  CALL_FUNCTION_257   257  None
              605  POP_TOP          

 L. 180       606  LOAD_FAST             3  'current_map_selected'
              609  LOAD_CONST               None
              612  COMPARE_OP            9  is-not
              615  POP_JUMP_IF_FALSE   655  'to 655'

 L. 181       618  LOAD_FAST             0  'self'
              621  LOAD_ATTR             0  'expandable_list_panel'
              624  LOAD_ATTR            27  'select_row_with_uid'
              627  LOAD_FAST             3  'current_map_selected'
              630  CALL_FUNCTION_1       1  None
              633  STORE_FAST           17  'row'

 L. 182       636  LOAD_FAST             0  'self'
              639  LOAD_ATTR            28  'on_row_selected'
              642  LOAD_CONST               0
              645  LOAD_FAST            17  'row'
              648  CALL_FUNCTION_2       2  None
              651  POP_TOP          
              652  JUMP_FORWARD          0  'to 655'
            655_0  COME_FROM           652  '652'
              655  LOAD_CONST               None
              658  RETURN_VALUE     

Parse error at or near `JUMP_FORWARD' instruction at offset 378

    def on_row_selected(self, index, row):
        if row is None:
            print 'Chosen map row could not be selected'
            return
        else:
            if type(row) is CategoryListItem:
                return
            if not SteamAmITheLobbyOwner():
                return
            if row.filename is None or row.filename == '':
                map_rotation_name = row.name
            else:
                map_rotation_name = row.filename
            new_title = row.name
            SteamSetLobbyData('Custom_UGC_Map', str(row.custom_map))
            if row.custom_map:
                SteamSetLobbyData('Custom_UGC_Map_Author', row.author)
            else:
                SteamSetLobbyData('Custom_UGC_Map_Author', '')
            if len(self.maps['SAVED_MAPS']) + len(self.maps['SUBSCRIBED_MAPS']) > 0 or row.pack_name == 'TEMPLATES':
                if row.pack_name == 'SAVED_MAPS' or row.pack_name == 'SUBSCRIBED_MAPS':
                    self.manager.hosted_ugc_map_filename = map_rotation_name
                else:
                    if row.pack_name == 'TEMPLATES':
                        new_title = generate_ugc_map_title(row.name)
                        filename = generate_ugc_map_filename_from_lobby(self.lobby_id)
                        self.manager.hosted_ugc_map_filename = filename
                    else:
                        new_title = row.name
            SteamSetLobbyData('MAP_ROTATION_ORIGINAL_TITLE', row.name)
            SteamSetLobbyData('MAP_ROTATION_FILENAME', map_rotation_name)
            SteamSetLobbyData('MAP_ROTATION_NEW_TITLE', new_title)
            return

    def draw(self):
        super(MapsPanel, self).draw()
