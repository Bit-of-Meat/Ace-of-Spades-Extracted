# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\shlex

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_come_froms ::= \e__come_froms COME_FROM . 
_come_froms ::= _come_froms . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_FORWARD come_froms
_ifstmts_jump ::= c_stmts_opt . JUMP_FORWARD come_froms
_ifstmts_jump ::= c_stmts_opt JUMP_FORWARD . come_froms
_ifstmts_jump ::= c_stmts_opt JUMP_FORWARD come_froms . 
_ifstmts_jump ::= return_if_stmts . 
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
attribute ::= expr . LOAD_ATTR
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
break ::= BREAK_LOOP . 
buildclass ::= LOAD_CONST . expr mkfunc CALL_FUNCTION_0 BUILD_CLASS
buildclass ::= LOAD_CONST expr . mkfunc CALL_FUNCTION_0 BUILD_CLASS
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= continues . 
c_stmts ::= lastc_stmt . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . expr CALL_FUNCTION_1
call ::= expr . expr expr CALL_FUNCTION_2
call ::= expr CALL_FUNCTION_0 . 
call ::= expr expr . CALL_FUNCTION_1
call ::= expr expr . expr CALL_FUNCTION_2
call ::= expr expr CALL_FUNCTION_1 . 
call ::= expr expr expr . CALL_FUNCTION_2
call ::= expr expr expr CALL_FUNCTION_2 . 
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
classdefdeco2 ::= LOAD_CONST . expr mkfunc CALL_FUNCTION_0 BUILD_CLASS
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
continue ::= JUMP_BACK . JUMP_ABSOLUTE
continues ::= _stmts . lastl_stmt continue
continues ::= _stmts lastl_stmt . continue
continues ::= continue . 
continues ::= lastl_stmt . continue
continues ::= lastl_stmt continue . 
delete ::= expr . DELETE_ATTR
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
else_suitec ::= c_stmts . 
else_suitel ::= l_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= and . 
expr ::= attribute . 
expr ::= bin_op . 
expr ::= call . 
expr ::= compare . 
expr ::= or . 
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
expr_jt ::= expr jmp_true . 
for ::= SETUP_LOOP . expr for_iter store for_block POP_BLOCK \e__come_froms
for ::= SETUP_LOOP . expr for_iter store for_block POP_BLOCK _come_froms
for ::= SETUP_LOOP expr . for_iter store for_block POP_BLOCK \e__come_froms
for ::= SETUP_LOOP expr . for_iter store for_block POP_BLOCK _come_froms
forelselaststmt ::= SETUP_LOOP . expr for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP . expr for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmt ::= SETUP_LOOP expr . for_iter store for_block POP_BLOCK else_suitec \e__come_froms
forelselaststmt ::= SETUP_LOOP expr . for_iter store for_block POP_BLOCK else_suitec _come_froms
forelselaststmtl ::= SETUP_LOOP . expr for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP . expr for_iter store for_block POP_BLOCK else_suitel _come_froms
forelselaststmtl ::= SETUP_LOOP expr . for_iter store for_block POP_BLOCK else_suitel \e__come_froms
forelselaststmtl ::= SETUP_LOOP expr . for_iter store for_block POP_BLOCK else_suitel _come_froms
forelsestmt ::= SETUP_LOOP . expr for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP . expr for_iter store for_block POP_BLOCK else_suite _come_froms
forelsestmt ::= SETUP_LOOP expr . for_iter store for_block POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr . for_iter store for_block POP_BLOCK else_suite _come_froms
genexpr_func ::= LOAD_FAST . FOR_ITER store comp_iter JUMP_BACK
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
ifelsestmtl ::= testexpr c_stmts_opt . CONTINUE else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . JUMP_BACK else_suitel
ifelsestmtl ::= testexpr c_stmts_opt CONTINUE . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt JUMP_BACK . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt JUMP_BACK else_suitel . 
ifelsestmtr ::= testexpr . return_if_stmts COME_FROM returns
ifelsestmtr ::= testexpr return_if_stmts . COME_FROM returns
ifelsestmtr ::= testexpr return_if_stmts COME_FROM . returns
iflaststmt ::= testexpr . c_stmts_opt JUMP_ABSOLUTE
iflaststmt ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE
iflaststmt ::= testexpr c_stmts_opt . JUMP_ABSOLUTE
iflaststmt ::= testexpr c_stmts_opt JUMP_ABSOLUTE . 
iflaststmtl ::= testexpr . c_stmts
iflaststmtl ::= testexpr . c_stmts_opt JUMP_BACK
iflaststmtl ::= testexpr \e_c_stmts_opt . JUMP_BACK
iflaststmtl ::= testexpr c_stmts . 
iflaststmtl ::= testexpr c_stmts_opt . JUMP_BACK
iflaststmtl ::= testexpr c_stmts_opt JUMP_BACK . 
ifstmt ::= testexpr . _ifstmts_jump
ifstmt ::= testexpr . return_if_stmts COME_FROM
ifstmt ::= testexpr . return_stmts COME_FROM
ifstmt ::= testexpr _ifstmts_jump . 
ifstmt ::= testexpr return_if_stmts . COME_FROM
ifstmt ::= testexpr return_if_stmts COME_FROM . 
ifstmt ::= testexpr return_stmts . COME_FROM
ifstmt ::= testexpr return_stmts COME_FROM . 
import ::= LOAD_CONST . LOAD_CONST alias
import_from ::= LOAD_CONST . LOAD_CONST IMPORT_NAME importlist POP_TOP
import_from_star ::= LOAD_CONST . LOAD_CONST IMPORT_NAME IMPORT_STAR
importmultiple ::= LOAD_CONST . LOAD_CONST alias imports_cont
jmp_false ::= POP_JUMP_IF_FALSE . 
jmp_true ::= POP_JUMP_IF_TRUE . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= lastl_stmt . 
l_stmts_opt ::= l_stmts . 
lastc_stmt ::= ifelsestmtc . 
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
list ::= expr . expr BUILD_LIST_2
list ::= expr expr . BUILD_LIST_2
mkfunc ::= expr . LOAD_CODE MAKE_FUNCTION_1
mkfunc ::= expr . expr LOAD_CODE MAKE_FUNCTION_2
mkfunc ::= expr . expr expr LOAD_CODE MAKE_FUNCTION_3
mkfunc ::= expr expr . LOAD_CODE MAKE_FUNCTION_2
mkfunc ::= expr expr . expr LOAD_CODE MAKE_FUNCTION_3
mkfunc ::= expr expr expr . LOAD_CODE MAKE_FUNCTION_3
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
or ::= expr_jt . expr \e_come_from_opt
or ::= expr_jt . expr come_from_opt
or ::= expr_jt expr . come_from_opt
or ::= expr_jt expr \e_come_from_opt . 
or ::= expr_jt expr come_from_opt . 
print_item ::= expr . PRINT_ITEM_CONT
print_item ::= expr PRINT_ITEM_CONT . 
print_items ::= print_item . 
print_items ::= print_items . print_item
print_items_nl_stmt ::= expr . PRINT_ITEM \e_print_items_opt PRINT_NEWLINE_CONT
print_items_nl_stmt ::= expr . PRINT_ITEM print_items_opt PRINT_NEWLINE_CONT
print_items_nl_stmt ::= expr PRINT_ITEM . print_items_opt PRINT_NEWLINE_CONT
print_items_nl_stmt ::= expr PRINT_ITEM \e_print_items_opt . PRINT_NEWLINE_CONT
print_items_nl_stmt ::= expr PRINT_ITEM \e_print_items_opt PRINT_NEWLINE_CONT . 
print_items_nl_stmt ::= expr PRINT_ITEM print_items_opt . PRINT_NEWLINE_CONT
print_items_nl_stmt ::= expr PRINT_ITEM print_items_opt PRINT_NEWLINE_CONT . 
print_items_opt ::= print_items . 
print_items_stmt ::= expr . PRINT_ITEM \e_print_items_opt
print_items_stmt ::= expr . PRINT_ITEM print_items_opt
print_items_stmt ::= expr PRINT_ITEM . print_items_opt
print_items_stmt ::= expr PRINT_ITEM \e_print_items_opt . 
print_items_stmt ::= expr PRINT_ITEM print_items_opt . 
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
return ::= return_expr RETURN_VALUE . 
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr RETURN_END_IF . 
return_if_stmts ::= _stmts . return_if_stmt
return_if_stmts ::= return_if_stmt . 
return_stmt ::= return . 
return_stmts ::= _stmts . return_stmt
return_stmts ::= _stmts return_stmt . 
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
sstmt ::= return . RETURN_LAST
sstmt ::= stmt . 
stmt ::= assign . 
stmt ::= break . 
stmt ::= call_stmt . 
stmt ::= continue . 
stmt ::= ifelsestmtc . 
stmt ::= ifstmt . 
stmt ::= print_items_nl_stmt . 
stmt ::= print_items_stmt . 
stmt ::= return . 
stmt ::= while1stmt . 
stmt ::= whilestmt . 
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
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOPX_2 BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOPX_2 BINARY_SUBSCR
testexpr ::= testfalse . 
testexpr ::= testtrue . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testtrue ::= expr . jmp_true
testtrue ::= expr jmp_true . 
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr BUILD_TUPLE_3
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr BUILD_TUPLE_3
tuple ::= expr expr expr . BUILD_TUPLE_3
unary_convert ::= expr . UNARY_CONVERT
unary_not ::= expr . UNARY_NOT
unary_op ::= expr . unary_operator
unpack ::= UNPACK_SEQUENCE_2 . store store
unpack ::= UNPACK_SEQUENCE_2 store . store
unpack ::= UNPACK_SEQUENCE_2 store store . 
while1elsestmt ::= SETUP_LOOP . l_stmts JUMP_BACK POP_BLOCK else_suitel COME_FROM
while1elsestmt ::= SETUP_LOOP . l_stmts JUMP_BACK else_suitel COME_FROM
while1elsestmt ::= SETUP_LOOP l_stmts . JUMP_BACK POP_BLOCK else_suitel COME_FROM
while1elsestmt ::= SETUP_LOOP l_stmts . JUMP_BACK else_suitel COME_FROM
while1elsestmt ::= SETUP_LOOP l_stmts JUMP_BACK . POP_BLOCK else_suitel COME_FROM
while1elsestmt ::= SETUP_LOOP l_stmts JUMP_BACK . else_suitel COME_FROM
while1elsestmt ::= SETUP_LOOP l_stmts JUMP_BACK POP_BLOCK . else_suitel COME_FROM
while1stmt ::= SETUP_LOOP . l_stmts_opt CONTINUE COME_FROM
while1stmt ::= SETUP_LOOP . l_stmts_opt JUMP_BACK COME_FROM
while1stmt ::= SETUP_LOOP . l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM
while1stmt ::= SETUP_LOOP . returns COME_FROM
while1stmt ::= SETUP_LOOP . returns pb_come_from
while1stmt ::= SETUP_LOOP \e_l_stmts_opt . CONTINUE COME_FROM
while1stmt ::= SETUP_LOOP \e_l_stmts_opt . JUMP_BACK COME_FROM
while1stmt ::= SETUP_LOOP \e_l_stmts_opt . JUMP_BACK POP_BLOCK COME_FROM
while1stmt ::= SETUP_LOOP l_stmts_opt . CONTINUE COME_FROM
while1stmt ::= SETUP_LOOP l_stmts_opt . JUMP_BACK COME_FROM
while1stmt ::= SETUP_LOOP l_stmts_opt . JUMP_BACK POP_BLOCK COME_FROM
while1stmt ::= SETUP_LOOP l_stmts_opt JUMP_BACK . COME_FROM
while1stmt ::= SETUP_LOOP l_stmts_opt JUMP_BACK . POP_BLOCK COME_FROM
while1stmt ::= SETUP_LOOP l_stmts_opt JUMP_BACK POP_BLOCK . COME_FROM
while1stmt ::= SETUP_LOOP l_stmts_opt JUMP_BACK POP_BLOCK COME_FROM . 
whileelsestmt ::= SETUP_LOOP . testexpr \e_l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= SETUP_LOOP . testexpr l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= SETUP_LOOP testexpr . l_stmts_opt JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= SETUP_LOOP testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= SETUP_LOOP testexpr l_stmts_opt . JUMP_BACK POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= SETUP_LOOP testexpr l_stmts_opt JUMP_BACK . POP_BLOCK else_suitel COME_FROM
whileelsestmt ::= SETUP_LOOP testexpr l_stmts_opt JUMP_BACK POP_BLOCK . else_suitel COME_FROM
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
whilestmt ::= SETUP_LOOP testexpr . l_stmts_opt JUMP_BACK JUMP_BACK POP_BLOCK \e__come_froms
whilestmt ::= SETUP_LOOP testexpr . l_stmts_opt JUMP_BACK JUMP_BACK POP_BLOCK _come_froms
whilestmt ::= SETUP_LOOP testexpr . l_stmts_opt JUMP_BACK POP_BLOCK \e__come_froms
whilestmt ::= SETUP_LOOP testexpr . l_stmts_opt JUMP_BACK POP_BLOCK _come_froms
whilestmt ::= SETUP_LOOP testexpr . returns \e__come_froms POP_BLOCK COME_FROM
whilestmt ::= SETUP_LOOP testexpr . returns _come_froms POP_BLOCK COME_FROM
whilestmt ::= SETUP_LOOP testexpr \e_l_stmts_opt . JUMP_BACK JUMP_BACK POP_BLOCK \e__come_froms
whilestmt ::= SETUP_LOOP testexpr \e_l_stmts_opt . JUMP_BACK JUMP_BACK POP_BLOCK _come_froms
whilestmt ::= SETUP_LOOP testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK \e__come_froms
whilestmt ::= SETUP_LOOP testexpr \e_l_stmts_opt . JUMP_BACK POP_BLOCK _come_froms
whilestmt ::= SETUP_LOOP testexpr l_stmts_opt . JUMP_BACK JUMP_BACK POP_BLOCK \e__come_froms
whilestmt ::= SETUP_LOOP testexpr l_stmts_opt . JUMP_BACK JUMP_BACK POP_BLOCK _come_froms
whilestmt ::= SETUP_LOOP testexpr l_stmts_opt . JUMP_BACK POP_BLOCK \e__come_froms
whilestmt ::= SETUP_LOOP testexpr l_stmts_opt . JUMP_BACK POP_BLOCK _come_froms
whilestmt ::= SETUP_LOOP testexpr l_stmts_opt JUMP_BACK . JUMP_BACK POP_BLOCK \e__come_froms
whilestmt ::= SETUP_LOOP testexpr l_stmts_opt JUMP_BACK . JUMP_BACK POP_BLOCK _come_froms
whilestmt ::= SETUP_LOOP testexpr l_stmts_opt JUMP_BACK . POP_BLOCK \e__come_froms
whilestmt ::= SETUP_LOOP testexpr l_stmts_opt JUMP_BACK . POP_BLOCK _come_froms
whilestmt ::= SETUP_LOOP testexpr l_stmts_opt JUMP_BACK POP_BLOCK . _come_froms
whilestmt ::= SETUP_LOOP testexpr l_stmts_opt JUMP_BACK POP_BLOCK \e__come_froms . 
whilestmt ::= SETUP_LOOP testexpr l_stmts_opt JUMP_BACK POP_BLOCK _come_froms . 
with ::= expr . SETUP_WITH POP_TOP \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH WITH_CLEANUP END_FINALLY
with ::= expr . SETUP_WITH POP_TOP suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH WITH_CLEANUP END_FINALLY
withasstmt ::= expr . SETUP_WITH store \e_suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH WITH_CLEANUP END_FINALLY
withasstmt ::= expr . SETUP_WITH store suite_stmts_opt POP_BLOCK LOAD_CONST COME_FROM_WITH WITH_CLEANUP END_FINALLY
yield ::= expr . YIELD_VALUE
Instruction context:
-> 
 L. 166       500  LOAD_FAST             0  'self'
                 503  LOAD_ATTR             7  'state'
                 506  LOAD_FAST             0  'self'
                 509  LOAD_ATTR            16  'quotes'
                 512  COMPARE_OP            6  in
                 515  POP_JUMP_IF_FALSE   712  'to 712'
import os.path, sys
from collections import deque
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

__all__ = [
 'shlex', 'split']

class shlex:

    def __init__(self, instream=None, infile=None, posix=False):
        if isinstance(instream, basestring):
            instream = StringIO(instream)
        if instream is not None:
            self.instream = instream
            self.infile = infile
        else:
            self.instream = sys.stdin
            self.infile = None
        self.posix = posix
        if posix:
            self.eof = None
        else:
            self.eof = ''
        self.commenters = '#'
        self.wordchars = 'abcdfeghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
        if self.posix:
            self.wordchars += b'\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd8\xd9\xda\xdb\xdc\xdd\xde'
        self.whitespace = ' \t\r\n'
        self.whitespace_split = False
        self.quotes = '\'"'
        self.escape = '\\'
        self.escapedquotes = '"'
        self.state = ' '
        self.pushback = deque()
        self.lineno = 1
        self.debug = 0
        self.token = ''
        self.filestack = deque()
        self.source = None
        if self.debug:
            print 'shlex: reading from %s, line %d' % (
             self.instream, self.lineno)
        return

    def push_token(self, tok):
        if self.debug >= 1:
            print 'shlex: pushing token ' + repr(tok)
        self.pushback.appendleft(tok)

    def push_source(self, newstream, newfile=None):
        if isinstance(newstream, basestring):
            newstream = StringIO(newstream)
        self.filestack.appendleft((self.infile, self.instream, self.lineno))
        self.infile = newfile
        self.instream = newstream
        self.lineno = 1
        if self.debug:
            if newfile is not None:
                print 'shlex: pushing to file %s' % (self.infile,)
            else:
                print 'shlex: pushing to stream %s' % (self.instream,)
        return

    def pop_source(self):
        self.instream.close()
        self.infile, self.instream, self.lineno = self.filestack.popleft()
        if self.debug:
            print 'shlex: popping to %s, line %d' % (
             self.instream, self.lineno)
        self.state = ' '

    def get_token(self):
        if self.pushback:
            tok = self.pushback.popleft()
            if self.debug >= 1:
                print 'shlex: popping token ' + repr(tok)
            return tok
        raw = self.read_token()
        if self.source is not None:
            while raw == self.source:
                spec = self.sourcehook(self.read_token())
                if spec:
                    newfile, newstream = spec
                    self.push_source(newstream, newfile)
                raw = self.get_token()

        while raw == self.eof:
            if not self.filestack:
                return self.eof
            self.pop_source()
            raw = self.get_token()

        if self.debug >= 1:
            if raw != self.eof:
                print 'shlex: token=' + repr(raw)
            else:
                print 'shlex: token=EOF'
        return raw

    def read_token--- This code section failed: ---

 L. 121         0  LOAD_GLOBAL           0  'False'
                3  STORE_FAST            1  'quoted'

 L. 122         6  LOAD_CONST               ' '
                9  STORE_FAST            2  'escapedstate'

 L. 123        12  SETUP_LOOP         1269  'to 1284'
               15  LOAD_GLOBAL           1  'True'
               18  POP_JUMP_IF_FALSE  1283  'to 1283'

 L. 124        21  LOAD_FAST             0  'self'
               24  LOAD_ATTR             2  'instream'
               27  LOAD_ATTR             3  'read'
               30  LOAD_CONST               1
               33  CALL_FUNCTION_1       1  None
               36  STORE_FAST            3  'nextchar'

 L. 125        39  LOAD_FAST             3  'nextchar'
               42  LOAD_CONST               '\n'
               45  COMPARE_OP            2  ==
               48  POP_JUMP_IF_FALSE    70  'to 70'

 L. 126        51  LOAD_FAST             0  'self'
               54  LOAD_ATTR             4  'lineno'
               57  LOAD_CONST               1
               60  BINARY_ADD       
               61  LOAD_FAST             0  'self'
               64  STORE_ATTR            4  'lineno'
               67  JUMP_FORWARD          0  'to 70'
             70_0  COME_FROM            67  '67'

 L. 127        70  LOAD_FAST             0  'self'
               73  LOAD_ATTR             5  'debug'
               76  LOAD_CONST               3
               79  COMPARE_OP            5  >=
               82  POP_JUMP_IF_FALSE   120  'to 120'

 L. 128        85  LOAD_CONST               'shlex: in state'
               88  PRINT_ITEM       
               89  LOAD_GLOBAL           6  'repr'
               92  LOAD_FAST             0  'self'
               95  LOAD_ATTR             7  'state'
               98  CALL_FUNCTION_1       1  None
              101  PRINT_ITEM_CONT  

 L. 129       102  LOAD_CONST               'I see character:'
              105  PRINT_ITEM       
              106  LOAD_GLOBAL           6  'repr'
              109  LOAD_FAST             3  'nextchar'
              112  CALL_FUNCTION_1       1  None
              115  PRINT_ITEM_CONT  
              116  PRINT_NEWLINE_CONT
              117  JUMP_FORWARD          0  'to 120'
            120_0  COME_FROM           117  '117'

 L. 130       120  LOAD_FAST             0  'self'
              123  LOAD_ATTR             7  'state'
              126  LOAD_CONST               None
              129  COMPARE_OP            8  is
              132  POP_JUMP_IF_FALSE   148  'to 148'

 L. 131       135  LOAD_CONST               ''
              138  LOAD_FAST             0  'self'
              141  STORE_ATTR            9  'token'

 L. 132       144  BREAK_LOOP       
              145  JUMP_BACK            15  'to 15'

 L. 133       148  LOAD_FAST             0  'self'
              151  LOAD_ATTR             7  'state'
              154  LOAD_CONST               ' '
              157  COMPARE_OP            2  ==
              160  POP_JUMP_IF_FALSE   500  'to 500'

 L. 134       163  LOAD_FAST             3  'nextchar'
              166  POP_JUMP_IF_TRUE    182  'to 182'

 L. 135       169  LOAD_CONST               None
              172  LOAD_FAST             0  'self'
              175  STORE_ATTR            7  'state'

 L. 136       178  BREAK_LOOP       
              179  JUMP_ABSOLUTE      1280  'to 1280'

 L. 137       182  LOAD_FAST             3  'nextchar'
              185  LOAD_FAST             0  'self'
              188  LOAD_ATTR            10  'whitespace'
              191  COMPARE_OP            6  in
              194  POP_JUMP_IF_FALSE   254  'to 254'

 L. 138       197  LOAD_FAST             0  'self'
              200  LOAD_ATTR             5  'debug'
              203  LOAD_CONST               2
              206  COMPARE_OP            5  >=
              209  POP_JUMP_IF_FALSE   220  'to 220'

 L. 139       212  LOAD_CONST               'shlex: I see whitespace in whitespace state'
              215  PRINT_ITEM       
              216  PRINT_NEWLINE_CONT
              217  JUMP_FORWARD          0  'to 220'
            220_0  COME_FROM           217  '217'

 L. 140       220  LOAD_FAST             0  'self'
              223  LOAD_ATTR             9  'token'
              226  POP_JUMP_IF_TRUE    244  'to 244'
              229  LOAD_FAST             0  'self'
              232  LOAD_ATTR            11  'posix'
              235  POP_JUMP_IF_FALSE    15  'to 15'
              238  LOAD_FAST             1  'quoted'
            241_0  COME_FROM           235  '235'
            241_1  COME_FROM           226  '226'
              241  POP_JUMP_IF_FALSE    15  'to 15'

 L. 141       244  BREAK_LOOP       
              245  JUMP_ABSOLUTE       497  'to 497'

 L. 143       248  CONTINUE             15  'to 15'
              251  JUMP_ABSOLUTE      1280  'to 1280'

 L. 144       254  LOAD_FAST             3  'nextchar'
              257  LOAD_FAST             0  'self'
              260  LOAD_ATTR            12  'commenters'
              263  COMPARE_OP            6  in
              266  POP_JUMP_IF_FALSE   301  'to 301'

 L. 145       269  LOAD_FAST             0  'self'
              272  LOAD_ATTR             2  'instream'
              275  LOAD_ATTR            13  'readline'
              278  CALL_FUNCTION_0       0  None
              281  POP_TOP          

 L. 146       282  LOAD_FAST             0  'self'
              285  LOAD_ATTR             4  'lineno'
              288  LOAD_CONST               1
              291  BINARY_ADD       
              292  LOAD_FAST             0  'self'
              295  STORE_ATTR            4  'lineno'
              298  JUMP_ABSOLUTE      1280  'to 1280'

 L. 147       301  LOAD_FAST             0  'self'
              304  LOAD_ATTR            11  'posix'
              307  POP_JUMP_IF_FALSE   343  'to 343'
              310  LOAD_FAST             3  'nextchar'
              313  LOAD_FAST             0  'self'
              316  LOAD_ATTR            14  'escape'
              319  COMPARE_OP            6  in
            322_0  COME_FROM           307  '307'
              322  POP_JUMP_IF_FALSE   343  'to 343'

 L. 148       325  LOAD_CONST               'a'
              328  STORE_FAST            2  'escapedstate'

 L. 149       331  LOAD_FAST             3  'nextchar'
              334  LOAD_FAST             0  'self'
              337  STORE_ATTR            7  'state'
              340  JUMP_ABSOLUTE      1280  'to 1280'

 L. 150       343  LOAD_FAST             3  'nextchar'
              346  LOAD_FAST             0  'self'
              349  LOAD_ATTR            15  'wordchars'
              352  COMPARE_OP            6  in
              355  POP_JUMP_IF_FALSE   379  'to 379'

 L. 151       358  LOAD_FAST             3  'nextchar'
              361  LOAD_FAST             0  'self'
              364  STORE_ATTR            9  'token'

 L. 152       367  LOAD_CONST               'a'
              370  LOAD_FAST             0  'self'
              373  STORE_ATTR            7  'state'
              376  JUMP_ABSOLUTE      1280  'to 1280'

 L. 153       379  LOAD_FAST             3  'nextchar'
              382  LOAD_FAST             0  'self'
              385  LOAD_ATTR            16  'quotes'
              388  COMPARE_OP            6  in
              391  POP_JUMP_IF_FALSE   427  'to 427'

 L. 154       394  LOAD_FAST             0  'self'
              397  LOAD_ATTR            11  'posix'
              400  POP_JUMP_IF_TRUE    415  'to 415'

 L. 155       403  LOAD_FAST             3  'nextchar'
              406  LOAD_FAST             0  'self'
              409  STORE_ATTR            9  'token'
              412  JUMP_FORWARD          0  'to 415'
            415_0  COME_FROM           412  '412'

 L. 156       415  LOAD_FAST             3  'nextchar'
              418  LOAD_FAST             0  'self'
              421  STORE_ATTR            7  'state'
              424  JUMP_ABSOLUTE      1280  'to 1280'

 L. 157       427  LOAD_FAST             0  'self'
              430  LOAD_ATTR            17  'whitespace_split'
              433  POP_JUMP_IF_FALSE   457  'to 457'

 L. 158       436  LOAD_FAST             3  'nextchar'
              439  LOAD_FAST             0  'self'
              442  STORE_ATTR            9  'token'

 L. 159       445  LOAD_CONST               'a'
              448  LOAD_FAST             0  'self'
              451  STORE_ATTR            7  'state'
              454  JUMP_ABSOLUTE      1280  'to 1280'

 L. 161       457  LOAD_FAST             3  'nextchar'
              460  LOAD_FAST             0  'self'
              463  STORE_ATTR            9  'token'

 L. 162       466  LOAD_FAST             0  'self'
              469  LOAD_ATTR             9  'token'
              472  POP_JUMP_IF_TRUE    490  'to 490'
              475  LOAD_FAST             0  'self'
              478  LOAD_ATTR            11  'posix'
              481  POP_JUMP_IF_FALSE    15  'to 15'
              484  LOAD_FAST             1  'quoted'
            487_0  COME_FROM           481  '481'
            487_1  COME_FROM           472  '472'
              487  POP_JUMP_IF_FALSE    15  'to 15'

 L. 163       490  BREAK_LOOP       
              491  JUMP_ABSOLUTE      1280  'to 1280'

 L. 165       494  CONTINUE             15  'to 15'
              497  JUMP_BACK            15  'to 15'

 L. 166       500  LOAD_FAST             0  'self'
              503  LOAD_ATTR             7  'state'
              506  LOAD_FAST             0  'self'
              509  LOAD_ATTR            16  'quotes'
              512  COMPARE_OP            6  in
              515  POP_JUMP_IF_FALSE   712  'to 712'

 L. 167       518  LOAD_GLOBAL           1  'True'
              521  STORE_FAST            1  'quoted'

 L. 168       524  LOAD_FAST             3  'nextchar'
              527  POP_JUMP_IF_TRUE    565  'to 565'

 L. 169       530  LOAD_FAST             0  'self'
              533  LOAD_ATTR             5  'debug'
              536  LOAD_CONST               2
              539  COMPARE_OP            5  >=
              542  POP_JUMP_IF_FALSE   553  'to 553'

 L. 170       545  LOAD_CONST               'shlex: I see EOF in quotes state'
              548  PRINT_ITEM       
              549  PRINT_NEWLINE_CONT
              550  JUMP_FORWARD          0  'to 553'
            553_0  COME_FROM           550  '550'

 L. 172       553  LOAD_GLOBAL          18  'ValueError'
              556  LOAD_CONST               'No closing quotation'
              559  RAISE_VARARGS_2       2  None
              562  JUMP_FORWARD          0  'to 565'
            565_0  COME_FROM           562  '562'

 L. 173       565  LOAD_FAST             3  'nextchar'
              568  LOAD_FAST             0  'self'
              571  LOAD_ATTR             7  'state'
              574  COMPARE_OP            2  ==
              577  POP_JUMP_IF_FALSE   630  'to 630'

 L. 174       580  LOAD_FAST             0  'self'
              583  LOAD_ATTR            11  'posix'
              586  POP_JUMP_IF_TRUE    618  'to 618'

 L. 175       589  LOAD_FAST             0  'self'
              592  LOAD_ATTR             9  'token'
              595  LOAD_FAST             3  'nextchar'
              598  BINARY_ADD       
              599  LOAD_FAST             0  'self'
              602  STORE_ATTR            9  'token'

 L. 176       605  LOAD_CONST               ' '
              608  LOAD_FAST             0  'self'
              611  STORE_ATTR            7  'state'

 L. 177       614  BREAK_LOOP       
              615  JUMP_ABSOLUTE       709  'to 709'

 L. 179       618  LOAD_CONST               'a'
              621  LOAD_FAST             0  'self'
              624  STORE_ATTR            7  'state'
              627  JUMP_ABSOLUTE      1280  'to 1280'

 L. 180       630  LOAD_FAST             0  'self'
              633  LOAD_ATTR            11  'posix'
              636  POP_JUMP_IF_FALSE   693  'to 693'
              639  LOAD_FAST             3  'nextchar'
              642  LOAD_FAST             0  'self'
              645  LOAD_ATTR            14  'escape'
              648  COMPARE_OP            6  in
              651  POP_JUMP_IF_FALSE   693  'to 693'

 L. 181       654  LOAD_FAST             0  'self'
              657  LOAD_ATTR             7  'state'
              660  LOAD_FAST             0  'self'
              663  LOAD_ATTR            19  'escapedquotes'
              666  COMPARE_OP            6  in
            669_0  COME_FROM           651  '651'
            669_1  COME_FROM           636  '636'
              669  POP_JUMP_IF_FALSE   693  'to 693'

 L. 182       672  LOAD_FAST             0  'self'
              675  LOAD_ATTR             7  'state'
              678  STORE_FAST            2  'escapedstate'

 L. 183       681  LOAD_FAST             3  'nextchar'
              684  LOAD_FAST             0  'self'
              687  STORE_ATTR            7  'state'
              690  JUMP_ABSOLUTE      1280  'to 1280'

 L. 185       693  LOAD_FAST             0  'self'
              696  LOAD_ATTR             9  'token'
              699  LOAD_FAST             3  'nextchar'
              702  BINARY_ADD       
              703  LOAD_FAST             0  'self'
              706  STORE_ATTR            9  'token'
              709  JUMP_BACK            15  'to 15'

 L. 186       712  LOAD_FAST             0  'self'
              715  LOAD_ATTR             7  'state'
              718  LOAD_FAST             0  'self'
              721  LOAD_ATTR            14  'escape'
              724  COMPARE_OP            6  in
              727  POP_JUMP_IF_FALSE   863  'to 863'

 L. 187       730  LOAD_FAST             3  'nextchar'
              733  POP_JUMP_IF_TRUE    771  'to 771'

 L. 188       736  LOAD_FAST             0  'self'
              739  LOAD_ATTR             5  'debug'
              742  LOAD_CONST               2
              745  COMPARE_OP            5  >=
              748  POP_JUMP_IF_FALSE   759  'to 759'

 L. 189       751  LOAD_CONST               'shlex: I see EOF in escape state'
              754  PRINT_ITEM       
              755  PRINT_NEWLINE_CONT
              756  JUMP_FORWARD          0  'to 759'
            759_0  COME_FROM           756  '756'

 L. 191       759  LOAD_GLOBAL          18  'ValueError'
              762  LOAD_CONST               'No escaped character'
              765  RAISE_VARARGS_2       2  None
              768  JUMP_FORWARD          0  'to 771'
            771_0  COME_FROM           768  '768'

 L. 194       771  LOAD_FAST             2  'escapedstate'
              774  LOAD_FAST             0  'self'
              777  LOAD_ATTR            16  'quotes'
              780  COMPARE_OP            6  in
              783  POP_JUMP_IF_FALSE   835  'to 835'

 L. 195       786  LOAD_FAST             3  'nextchar'
              789  LOAD_FAST             0  'self'
              792  LOAD_ATTR             7  'state'
              795  COMPARE_OP            3  !=
              798  POP_JUMP_IF_FALSE   835  'to 835'
              801  LOAD_FAST             3  'nextchar'
              804  LOAD_FAST             2  'escapedstate'
              807  COMPARE_OP            3  !=
            810_0  COME_FROM           798  '798'
            810_1  COME_FROM           783  '783'
              810  POP_JUMP_IF_FALSE   835  'to 835'

 L. 196       813  LOAD_FAST             0  'self'
              816  LOAD_ATTR             9  'token'
              819  LOAD_FAST             0  'self'
              822  LOAD_ATTR             7  'state'
              825  BINARY_ADD       
              826  LOAD_FAST             0  'self'
              829  STORE_ATTR            9  'token'
              832  JUMP_FORWARD          0  'to 835'
            835_0  COME_FROM           832  '832'

 L. 197       835  LOAD_FAST             0  'self'
              838  LOAD_ATTR             9  'token'
              841  LOAD_FAST             3  'nextchar'
              844  BINARY_ADD       
              845  LOAD_FAST             0  'self'
              848  STORE_ATTR            9  'token'

 L. 198       851  LOAD_FAST             2  'escapedstate'
              854  LOAD_FAST             0  'self'
              857  STORE_ATTR            7  'state'
              860  JUMP_BACK            15  'to 15'

 L. 199       863  LOAD_FAST             0  'self'
              866  LOAD_ATTR             7  'state'
              869  LOAD_CONST               'a'
              872  COMPARE_OP            2  ==
              875  POP_JUMP_IF_FALSE    15  'to 15'

 L. 200       878  LOAD_FAST             3  'nextchar'
              881  POP_JUMP_IF_TRUE    897  'to 897'

 L. 201       884  LOAD_CONST               None
              887  LOAD_FAST             0  'self'
              890  STORE_ATTR            7  'state'

 L. 202       893  BREAK_LOOP       
              894  JUMP_ABSOLUTE      1280  'to 1280'

 L. 203       897  LOAD_FAST             3  'nextchar'
              900  LOAD_FAST             0  'self'
              903  LOAD_ATTR            10  'whitespace'
              906  COMPARE_OP            6  in
              909  POP_JUMP_IF_FALSE   978  'to 978'

 L. 204       912  LOAD_FAST             0  'self'
              915  LOAD_ATTR             5  'debug'
              918  LOAD_CONST               2
              921  COMPARE_OP            5  >=
              924  POP_JUMP_IF_FALSE   935  'to 935'

 L. 205       927  LOAD_CONST               'shlex: I see whitespace in word state'
              930  PRINT_ITEM       
              931  PRINT_NEWLINE_CONT
              932  JUMP_FORWARD          0  'to 935'
            935_0  COME_FROM           932  '932'

 L. 206       935  LOAD_CONST               ' '
              938  LOAD_FAST             0  'self'
              941  STORE_ATTR            7  'state'

 L. 207       944  LOAD_FAST             0  'self'
              947  LOAD_ATTR             9  'token'
              950  POP_JUMP_IF_TRUE    968  'to 968'
              953  LOAD_FAST             0  'self'
              956  LOAD_ATTR            11  'posix'
              959  POP_JUMP_IF_FALSE    15  'to 15'
              962  LOAD_FAST             1  'quoted'
            965_0  COME_FROM           959  '959'
            965_1  COME_FROM           950  '950'
              965  POP_JUMP_IF_FALSE    15  'to 15'

 L. 208       968  BREAK_LOOP       
              969  JUMP_ABSOLUTE      1277  'to 1277'

 L. 210       972  CONTINUE             15  'to 15'
              975  JUMP_ABSOLUTE      1280  'to 1280'

 L. 211       978  LOAD_FAST             3  'nextchar'
              981  LOAD_FAST             0  'self'
              984  LOAD_ATTR            12  'commenters'
              987  COMPARE_OP            6  in
              990  POP_JUMP_IF_FALSE  1077  'to 1077'

 L. 212       993  LOAD_FAST             0  'self'
              996  LOAD_ATTR             2  'instream'
              999  LOAD_ATTR            13  'readline'
             1002  CALL_FUNCTION_0       0  None
             1005  POP_TOP          

 L. 213      1006  LOAD_FAST             0  'self'
             1009  LOAD_ATTR             4  'lineno'
             1012  LOAD_CONST               1
             1015  BINARY_ADD       
             1016  LOAD_FAST             0  'self'
             1019  STORE_ATTR            4  'lineno'

 L. 214      1022  LOAD_FAST             0  'self'
             1025  LOAD_ATTR            11  'posix'
             1028  POP_JUMP_IF_FALSE  1277  'to 1277'

 L. 215      1031  LOAD_CONST               ' '
             1034  LOAD_FAST             0  'self'
             1037  STORE_ATTR            7  'state'

 L. 216      1040  LOAD_FAST             0  'self'
             1043  LOAD_ATTR             9  'token'
             1046  POP_JUMP_IF_TRUE   1064  'to 1064'
             1049  LOAD_FAST             0  'self'
             1052  LOAD_ATTR            11  'posix'
             1055  POP_JUMP_IF_FALSE    15  'to 15'
             1058  LOAD_FAST             1  'quoted'
           1061_0  COME_FROM          1055  '1055'
           1061_1  COME_FROM          1046  '1046'
             1061  POP_JUMP_IF_FALSE    15  'to 15'

 L. 217      1064  BREAK_LOOP       
             1065  JUMP_ABSOLUTE      1074  'to 1074'

 L. 219      1068  CONTINUE             15  'to 15'
             1071  JUMP_ABSOLUTE      1277  'to 1277'
             1074  JUMP_ABSOLUTE      1280  'to 1280'

 L. 220      1077  LOAD_FAST             0  'self'
             1080  LOAD_ATTR            11  'posix'
             1083  POP_JUMP_IF_FALSE  1113  'to 1113'
             1086  LOAD_FAST             3  'nextchar'
             1089  LOAD_FAST             0  'self'
             1092  LOAD_ATTR            16  'quotes'
             1095  COMPARE_OP            6  in
           1098_0  COME_FROM          1083  '1083'
             1098  POP_JUMP_IF_FALSE  1113  'to 1113'

 L. 221      1101  LOAD_FAST             3  'nextchar'
             1104  LOAD_FAST             0  'self'
             1107  STORE_ATTR            7  'state'
             1110  JUMP_ABSOLUTE      1280  'to 1280'

 L. 222      1113  LOAD_FAST             0  'self'
             1116  LOAD_ATTR            11  'posix'
             1119  POP_JUMP_IF_FALSE  1155  'to 1155'
             1122  LOAD_FAST             3  'nextchar'
             1125  LOAD_FAST             0  'self'
             1128  LOAD_ATTR            14  'escape'
             1131  COMPARE_OP            6  in
           1134_0  COME_FROM          1119  '1119'
             1134  POP_JUMP_IF_FALSE  1155  'to 1155'

 L. 223      1137  LOAD_CONST               'a'
             1140  STORE_FAST            2  'escapedstate'

 L. 224      1143  LOAD_FAST             3  'nextchar'
             1146  LOAD_FAST             0  'self'
             1149  STORE_ATTR            7  'state'
             1152  JUMP_ABSOLUTE      1280  'to 1280'

 L. 225      1155  LOAD_FAST             3  'nextchar'
             1158  LOAD_FAST             0  'self'
             1161  LOAD_ATTR            15  'wordchars'
             1164  COMPARE_OP            6  in
             1167  POP_JUMP_IF_TRUE   1194  'to 1194'
             1170  LOAD_FAST             3  'nextchar'
             1173  LOAD_FAST             0  'self'
             1176  LOAD_ATTR            16  'quotes'
             1179  COMPARE_OP            6  in
             1182  POP_JUMP_IF_TRUE   1194  'to 1194'

 L. 226      1185  LOAD_FAST             0  'self'
             1188  LOAD_ATTR            17  'whitespace_split'
           1191_0  COME_FROM          1182  '1182'
           1191_1  COME_FROM          1167  '1167'
             1191  POP_JUMP_IF_FALSE  1213  'to 1213'

 L. 227      1194  LOAD_FAST             0  'self'
             1197  LOAD_ATTR             9  'token'
             1200  LOAD_FAST             3  'nextchar'
             1203  BINARY_ADD       
             1204  LOAD_FAST             0  'self'
             1207  STORE_ATTR            9  'token'
             1210  JUMP_ABSOLUTE      1280  'to 1280'

 L. 229      1213  LOAD_FAST             0  'self'
             1216  LOAD_ATTR            20  'pushback'
             1219  LOAD_ATTR            21  'appendleft'
             1222  LOAD_FAST             3  'nextchar'
             1225  CALL_FUNCTION_1       1  None
             1228  POP_TOP          

 L. 230      1229  LOAD_FAST             0  'self'
             1232  LOAD_ATTR             5  'debug'
             1235  LOAD_CONST               2
             1238  COMPARE_OP            5  >=
             1241  POP_JUMP_IF_FALSE  1252  'to 1252'

 L. 231      1244  LOAD_CONST               'shlex: I see punctuation in word state'
             1247  PRINT_ITEM       
             1248  PRINT_NEWLINE_CONT
             1249  JUMP_FORWARD          0  'to 1252'
           1252_0  COME_FROM          1249  '1249'

 L. 232      1252  LOAD_CONST               ' '
             1255  LOAD_FAST             0  'self'
             1258  STORE_ATTR            7  'state'

 L. 233      1261  LOAD_FAST             0  'self'
             1264  LOAD_ATTR             9  'token'
             1267  POP_JUMP_IF_FALSE    15  'to 15'

 L. 234      1270  BREAK_LOOP       
             1271  JUMP_ABSOLUTE      1280  'to 1280'

 L. 236      1274  CONTINUE             15  'to 15'
             1277  JUMP_BACK            15  'to 15'
             1280  JUMP_BACK            15  'to 15'
             1283  POP_BLOCK        
           1284_0  COME_FROM            12  '12'

 L. 237      1284  LOAD_FAST             0  'self'
             1287  LOAD_ATTR             9  'token'
             1290  STORE_FAST            4  'result'

 L. 238      1293  LOAD_CONST               ''
             1296  LOAD_FAST             0  'self'
             1299  STORE_ATTR            9  'token'

 L. 239      1302  LOAD_FAST             0  'self'
             1305  LOAD_ATTR            11  'posix'
             1308  POP_JUMP_IF_FALSE  1339  'to 1339'
             1311  LOAD_FAST             1  'quoted'
             1314  UNARY_NOT        
             1315  POP_JUMP_IF_FALSE  1339  'to 1339'
             1318  LOAD_FAST             4  'result'
             1321  LOAD_CONST               ''
             1324  COMPARE_OP            2  ==
           1327_0  COME_FROM          1315  '1315'
           1327_1  COME_FROM          1308  '1308'
             1327  POP_JUMP_IF_FALSE  1339  'to 1339'

 L. 240      1330  LOAD_CONST               None
             1333  STORE_FAST            4  'result'
             1336  JUMP_FORWARD          0  'to 1339'
           1339_0  COME_FROM          1336  '1336'

 L. 241      1339  LOAD_FAST             0  'self'
             1342  LOAD_ATTR             5  'debug'
             1345  LOAD_CONST               1
             1348  COMPARE_OP            4  >
             1351  POP_JUMP_IF_FALSE  1386  'to 1386'

 L. 242      1354  LOAD_FAST             4  'result'
             1357  POP_JUMP_IF_FALSE  1378  'to 1378'

 L. 243      1360  LOAD_CONST               'shlex: raw token='
             1363  LOAD_GLOBAL           6  'repr'
             1366  LOAD_FAST             4  'result'
             1369  CALL_FUNCTION_1       1  None
             1372  BINARY_ADD       
             1373  PRINT_ITEM       
             1374  PRINT_NEWLINE_CONT
             1375  JUMP_ABSOLUTE      1386  'to 1386'

 L. 245      1378  LOAD_CONST               'shlex: raw token=EOF'
             1381  PRINT_ITEM       
             1382  PRINT_NEWLINE_CONT
             1383  JUMP_FORWARD          0  'to 1386'
           1386_0  COME_FROM          1383  '1383'

 L. 246      1386  LOAD_FAST             4  'result'
             1389  RETURN_VALUE     

Parse error at or near `LOAD_FAST' instruction at offset 500

    def sourcehook(self, newfile):
        if newfile[0] == '"':
            newfile = newfile[1:-1]
        if isinstance(self.infile, basestring) and not os.path.isabs(newfile):
            newfile = os.path.join(os.path.dirname(self.infile), newfile)
        return (
         newfile, open(newfile, 'r'))

    def error_leader(self, infile=None, lineno=None):
        if infile is None:
            infile = self.infile
        if lineno is None:
            lineno = self.lineno
        return '"%s", line %d: ' % (infile, lineno)

    def __iter__(self):
        return self

    def next(self):
        token = self.get_token()
        if token == self.eof:
            raise StopIteration
        return token


def split(s, comments=False, posix=True):
    lex = shlex(s, posix=posix)
    lex.whitespace_split = True
    if not comments:
        lex.commenters = ''
    return list(lex)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        lexer = shlex()
    else:
        file = sys.argv[1]
        lexer = shlex(open(file), file)
    while 1:
        tt = lexer.get_token()
        if tt:
            print 'Token: ' + repr(tt)
        else:
            break
