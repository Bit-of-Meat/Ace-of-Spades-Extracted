# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\urlparse

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
assert2 ::= assert_expr . jmp_true LOAD_ASSERT expr CALL_FUNCTION_1 RAISE_VARARGS_1
assert_expr ::= assert_expr_and . 
assert_expr ::= expr . 
assert_expr_and ::= assert_expr . jmp_false expr
assert_expr_and ::= assert_expr jmp_false . expr
assert_expr_and ::= assert_expr jmp_false expr . 
assert_expr_or ::= assert_expr . jmp_true expr
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
binary_operator ::= BINARY_MODULO . 
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts ::= _stmts lastc_stmt . 
c_stmts ::= continues . 
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . expr CALL_FUNCTION_1
call ::= expr . expr expr CALL_FUNCTION_2
call ::= expr . expr expr expr CALL_FUNCTION_3
call ::= expr . expr expr expr expr expr CALL_FUNCTION_5
call ::= expr . expr expr expr expr expr expr CALL_FUNCTION_6
call ::= expr expr . CALL_FUNCTION_1
call ::= expr expr . expr CALL_FUNCTION_2
call ::= expr expr . expr expr CALL_FUNCTION_3
call ::= expr expr . expr expr expr expr CALL_FUNCTION_5
call ::= expr expr . expr expr expr expr expr CALL_FUNCTION_6
call ::= expr expr CALL_FUNCTION_1 . 
call ::= expr expr expr . CALL_FUNCTION_2
call ::= expr expr expr . expr CALL_FUNCTION_3
call ::= expr expr expr . expr expr expr CALL_FUNCTION_5
call ::= expr expr expr . expr expr expr expr CALL_FUNCTION_6
call ::= expr expr expr CALL_FUNCTION_2 . 
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
continues ::= _stmts lastl_stmt continue . 
continues ::= continue . 
continues ::= lastl_stmt . continue
del_expr ::= expr . 
delete ::= del_expr . DELETE_SLICE+0
delete ::= del_expr . del_expr DELETE_SLICE+1
delete ::= del_expr . del_expr DELETE_SLICE+2
delete ::= del_expr . del_expr del_expr DELETE_SLICE+3
delete ::= del_expr del_expr . DELETE_SLICE+1
delete ::= del_expr del_expr . DELETE_SLICE+2
delete ::= del_expr del_expr . del_expr DELETE_SLICE+3
delete ::= del_expr del_expr del_expr . DELETE_SLICE+3
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
expr ::= list_comp . 
expr ::= tuple . 
expr ::= unary_not . 
expr_jitop ::= expr . JUMP_IF_TRUE_OR_POP
expr_jt ::= expr . jmp_true
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
if_exp_not_lambda ::= expr . jmp_true expr return_if_lambda return_stmt_lambda LAMBDA_MARKER
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
jmp_false ::= POP_JUMP_IF_FALSE . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= _stmts lastl_stmt . 
l_stmts ::= continues . 
l_stmts ::= lastl_stmt . 
l_stmts_opt ::= l_stmts . 
lastc_stmt ::= iflaststmt . 
lastl_stmt ::= iflaststmtl . 
lc_body ::= expr . LIST_APPEND
lc_body ::= expr LIST_APPEND . 
list ::= BUILD_LIST_0 . 
list ::= expr . BUILD_LIST_1
list ::= expr . expr BUILD_LIST_2
list ::= expr expr . BUILD_LIST_2
list_comp ::= BUILD_LIST_0 . list_iter
list_comp ::= BUILD_LIST_0 list_iter . 
list_for ::= expr . for_iter store list_iter JUMP_BACK
list_for ::= expr for_iter . store list_iter JUMP_BACK
list_for ::= expr for_iter store . list_iter JUMP_BACK
list_for ::= expr for_iter store list_iter . JUMP_BACK
list_for ::= expr for_iter store list_iter JUMP_BACK . 
list_if ::= expr . jmp_false list_iter
list_if_not ::= expr . jmp_true list_iter
list_iter ::= lc_body . 
list_iter ::= list_for . 
mkfunc ::= expr . LOAD_CODE MAKE_FUNCTION_1
mkfunc ::= expr . expr LOAD_CODE MAKE_FUNCTION_2
mkfunc ::= expr expr . LOAD_CODE MAKE_FUNCTION_2
mkfuncdeco ::= expr . mkfuncdeco CALL_FUNCTION_1
mkfuncdeco ::= expr . mkfuncdeco0 CALL_FUNCTION_1
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
raise_stmt2 ::= expr expr RAISE_VARARGS_2 . 
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
stmt ::= raise_stmt2 . 
stmts ::= sstmt . 
stmts ::= stmts . sstmt
stmts ::= stmts sstmt . 
store ::= STORE_FAST . 
store ::= expr . STORE_ATTR
store ::= expr . STORE_SLICE+0
store ::= expr . expr STORE_SLICE+1
store ::= expr . expr STORE_SLICE+2
store ::= expr . expr expr STORE_SLICE+3
store ::= expr expr . STORE_SLICE+1
store ::= expr expr . STORE_SLICE+2
store ::= expr expr . expr STORE_SLICE+3
store_subscript ::= expr . expr STORE_SUBSCR
store_subscript ::= expr expr . STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOPX_2 BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOPX_2 BINARY_SUBSCR
testexpr ::= testfalse . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testtrue ::= expr . jmp_true
tuple ::= expr . BUILD_TUPLE_1
tuple ::= expr . expr BUILD_TUPLE_2
tuple ::= expr . expr expr expr expr BUILD_TUPLE_5
tuple ::= expr . expr expr expr expr expr BUILD_TUPLE_6
tuple ::= expr BUILD_TUPLE_1 . 
tuple ::= expr expr . BUILD_TUPLE_2
tuple ::= expr expr . expr expr expr BUILD_TUPLE_5
tuple ::= expr expr . expr expr expr expr BUILD_TUPLE_6
tuple ::= expr expr expr . expr expr BUILD_TUPLE_5
tuple ::= expr expr expr . expr expr expr BUILD_TUPLE_6
unary_convert ::= expr . UNARY_CONVERT
unary_not ::= expr . UNARY_NOT
unary_not ::= expr UNARY_NOT . 
unary_op ::= expr . unary_operator
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
   
 L. 422       178  CONTINUE             69  'to 69'
->               181  JUMP_FORWARD          0  'to 184'
               184_0  COME_FROM           181  '181'
import re
__all__ = [
 'urlparse', 'urlunparse', 'urljoin', 'urldefrag', 
 'urlsplit', 'urlunsplit', 
 'parse_qs', 'parse_qsl']
uses_relative = [
 'ftp', 'http', 'gopher', 'nntp', 'imap', 
 'wais', 'file', 'https', 'shttp', 
 'mms', 
 'prospero', 'rtsp', 'rtspu', '', 'sftp', 
 'svn', 'svn+ssh']
uses_netloc = ['ftp', 'http', 'gopher', 'nntp', 'telnet', 
 'imap', 'wais', 'file', 'mms', 
 'https', 'shttp', 
 'snews', 'prospero', 'rtsp', 'rtspu', 'rsync', '', 
 'svn', 
 'svn+ssh', 'sftp', 'nfs', 'git', 'git+ssh']
uses_params = ['ftp', 'hdl', 'prospero', 'http', 'imap', 
 'https', 'shttp', 'rtsp', 'rtspu', 
 'sip', 'sips', 
 'mms', '', 'sftp', 'tel']
non_hierarchical = [
 'gopher', 'hdl', 'mailto', 'news', 
 'telnet', 'wais', 'imap', 'snews', 
 'sip', 'sips']
uses_query = ['http', 'wais', 'imap', 'https', 'shttp', 'mms', 
 'gopher', 'rtsp', 'rtspu', 
 'sip', 'sips', '']
uses_fragment = ['ftp', 'hdl', 'http', 'gopher', 'news', 
 'nntp', 'wais', 'https', 'shttp', 
 'snews', 
 'file', 'prospero', '']
scheme_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-.'
MAX_CACHE_SIZE = 20
_parse_cache = {}

def clear_cache():
    _parse_cache.clear()


class ResultMixin(object):

    @property
    def username(self):
        netloc = self.netloc
        if '@' in netloc:
            userinfo = netloc.rsplit('@', 1)[0]
            if ':' in userinfo:
                userinfo = userinfo.split(':', 1)[0]
            return userinfo
        return

    @property
    def password(self):
        netloc = self.netloc
        if '@' in netloc:
            userinfo = netloc.rsplit('@', 1)[0]
            if ':' in userinfo:
                return userinfo.split(':', 1)[1]
        return

    @property
    def hostname(self):
        netloc = self.netloc.split('@')[-1]
        if '[' in netloc and ']' in netloc:
            return netloc.split(']')[0][1:].lower()
        else:
            if ':' in netloc:
                return netloc.split(':')[0].lower()
            else:
                if netloc == '':
                    return
                return netloc.lower()

            return

    @property
    def port(self):
        netloc = self.netloc.split('@')[-1].split(']')[-1]
        if ':' in netloc:
            port = netloc.split(':')[1]
            if port:
                port = int(port, 10)
                if 0 <= port <= 65535:
                    return port
        return


from collections import namedtuple

class SplitResult(namedtuple('SplitResult', 'scheme netloc path query fragment'), ResultMixin):
    __slots__ = ()

    def geturl(self):
        return urlunsplit(self)


class ParseResult(namedtuple('ParseResult', 'scheme netloc path params query fragment'), ResultMixin):
    __slots__ = ()

    def geturl(self):
        return urlunparse(self)


def urlparse(url, scheme='', allow_fragments=True):
    tuple = urlsplit(url, scheme, allow_fragments)
    scheme, netloc, url, query, fragment = tuple
    if scheme in uses_params and ';' in url:
        url, params = _splitparams(url)
    else:
        params = ''
    return ParseResult(scheme, netloc, url, params, query, fragment)


def _splitparams(url):
    if '/' in url:
        i = url.find(';', url.rfind('/'))
        if i < 0:
            return (url, '')
    else:
        i = url.find(';')
    return (
     url[:i], url[i + 1:])


def _splitnetloc(url, start=0):
    delim = len(url)
    for c in '/?#':
        wdelim = url.find(c, start)
        if wdelim >= 0:
            delim = min(delim, wdelim)

    return (
     url[start:delim], url[delim:])


def urlsplit(url, scheme='', allow_fragments=True):
    allow_fragments = bool(allow_fragments)
    key = (url, scheme, allow_fragments, type(url), type(scheme))
    cached = _parse_cache.get(key, None)
    if cached:
        return cached
    else:
        if len(_parse_cache) >= MAX_CACHE_SIZE:
            clear_cache()
        netloc = query = fragment = ''
        i = url.find(':')
        if i > 0:
            if url[:i] == 'http':
                scheme = url[:i].lower()
                url = url[i + 1:]
                if url[:2] == '//':
                    netloc, url = _splitnetloc(url, 2)
                    if '[' in netloc and ']' not in netloc or ']' in netloc and '[' not in netloc:
                        raise ValueError('Invalid IPv6 URL')
                if allow_fragments and '#' in url:
                    url, fragment = url.split('#', 1)
                if '?' in url:
                    url, query = url.split('?', 1)
                v = SplitResult(scheme, netloc, url, query, fragment)
                _parse_cache[key] = v
                return v
            for c in url[:i]:
                if c not in scheme_chars:
                    break
            else:
                rest = url[i + 1:]
                if not rest or any(c not in '0123456789' for c in rest):
                    scheme, url = url[:i].lower(), rest
        if url[:2] == '//':
            netloc, url = _splitnetloc(url, 2)
            if '[' in netloc and ']' not in netloc or ']' in netloc and '[' not in netloc:
                raise ValueError('Invalid IPv6 URL')
        if allow_fragments and '#' in url:
            url, fragment = url.split('#', 1)
        if '?' in url:
            url, query = url.split('?', 1)
        v = SplitResult(scheme, netloc, url, query, fragment)
        _parse_cache[key] = v
        return v


def urlunparse(data):
    scheme, netloc, url, params, query, fragment = data
    if params:
        url = '%s;%s' % (url, params)
    return urlunsplit((scheme, netloc, url, query, fragment))


def urlunsplit(data):
    scheme, netloc, url, query, fragment = data
    if netloc or scheme and scheme in uses_netloc and url[:2] != '//':
        if url and url[:1] != '/':
            url = '/' + url
        url = '//' + (netloc or '') + url
    if scheme:
        url = scheme + ':' + url
    if query:
        url = url + '?' + query
    if fragment:
        url = url + '#' + fragment
    return url


def urljoin(base, url, allow_fragments=True):
    if not base:
        return url
    if not url:
        return base
    bscheme, bnetloc, bpath, bparams, bquery, bfragment = urlparse(base, '', allow_fragments)
    scheme, netloc, path, params, query, fragment = urlparse(url, bscheme, allow_fragments)
    if scheme != bscheme or scheme not in uses_relative:
        return url
    if scheme in uses_netloc:
        if netloc:
            return urlunparse((scheme, netloc, path,
             params, query, fragment))
        netloc = bnetloc
    if path[:1] == '/':
        return urlunparse((scheme, netloc, path,
         params, query, fragment))
    if not path and not params:
        path = bpath
        params = bparams
        if not query:
            query = bquery
        return urlunparse((scheme, netloc, path,
         params, query, fragment))
    segments = bpath.split('/')[:-1] + path.split('/')
    if segments[-1] == '.':
        segments[-1] = ''
    while '.' in segments:
        segments.remove('.')

    while 1:
        i = 1
        n = len(segments) - 1
        while 1:
            if i < n:
                if segments[i] == '..' and segments[i - 1] not in ('', '..'):
                    del segments[i - 1:i + 1]
                    break
                i = i + 1
        else:
            break

    if segments == ['', '..']:
        segments[-1] = ''
    elif len(segments) >= 2 and segments[-1] == '..':
        segments[(-2):] = [
         '']
    return urlunparse((scheme, netloc, ('/').join(segments),
     params, query, fragment))


def urldefrag(url):
    if '#' in url:
        s, n, p, a, q, frag = urlparse(url)
        defrag = urlunparse((s, n, p, a, q, ''))
        return (
         defrag, frag)
    else:
        return (
         url, '')


try:
    unicode
except NameError:

    def _is_unicode(x):
        return 0


else:

    def _is_unicode(x):
        return isinstance(x, unicode)


_hexdig = '0123456789ABCDEFabcdef'
_hextochr = dict((a + b, chr(int(a + b, 16))) for a in _hexdig for b in _hexdig)
_asciire = re.compile('([\x00-\x7f]+)')

def unquote(s):
    if _is_unicode(s):
        if '%' not in s:
            return s
        bits = _asciire.split(s)
        res = [bits[0]]
        append = res.append
        for i in range(1, len(bits), 2):
            append(unquote(str(bits[i])).decode('latin1'))
            append(bits[i + 1])

        return ('').join(res)
    bits = s.split('%')
    if len(bits) == 1:
        return s
    res = [
     bits[0]]
    append = res.append
    for item in bits[1:]:
        try:
            append(_hextochr[item[:2]])
            append(item[2:])
        except KeyError:
            append('%')
            append(item)

    return ('').join(res)


def parse_qs(qs, keep_blank_values=0, strict_parsing=0):
    dict = {}
    for name, value in parse_qsl(qs, keep_blank_values, strict_parsing):
        if name in dict:
            dict[name].append(value)
        else:
            dict[name] = [
             value]

    return dict


def parse_qsl--- This code section failed: ---

 L. 409         0  BUILD_LIST_0          0 
                3  LOAD_FAST             0  'qs'
                6  LOAD_ATTR             0  'split'
                9  LOAD_CONST               '&'
               12  CALL_FUNCTION_1       1  None
               15  GET_ITER         
               16  FOR_ITER             34  'to 53'
               19  STORE_FAST            3  's1'
               22  LOAD_FAST             3  's1'
               25  LOAD_ATTR             0  'split'
               28  LOAD_CONST               ';'
               31  CALL_FUNCTION_1       1  None
               34  GET_ITER         
               35  FOR_ITER             12  'to 50'
               38  STORE_FAST            4  's2'
               41  LOAD_FAST             4  's2'
               44  LIST_APPEND           3  None
               47  JUMP_BACK            35  'to 35'
               50  JUMP_BACK            16  'to 16'
               53  STORE_FAST            5  'pairs'

 L. 410        56  BUILD_LIST_0          0 
               59  STORE_FAST            6  'r'

 L. 411        62  SETUP_LOOP          223  'to 288'
               65  LOAD_FAST             5  'pairs'
               68  GET_ITER         
               69  FOR_ITER            215  'to 287'
               72  STORE_FAST            7  'name_value'

 L. 412        75  LOAD_FAST             7  'name_value'
               78  UNARY_NOT        
               79  POP_JUMP_IF_FALSE    95  'to 95'
               82  LOAD_FAST             2  'strict_parsing'
               85  UNARY_NOT        
             86_0  COME_FROM            79  '79'
               86  POP_JUMP_IF_FALSE    95  'to 95'

 L. 413        89  CONTINUE             69  'to 69'
               92  JUMP_FORWARD          0  'to 95'
             95_0  COME_FROM            92  '92'

 L. 414        95  LOAD_FAST             7  'name_value'
               98  LOAD_ATTR             0  'split'
              101  LOAD_CONST               '='
              104  LOAD_CONST               1
              107  CALL_FUNCTION_2       2  None
              110  STORE_FAST            8  'nv'

 L. 415       113  LOAD_GLOBAL           1  'len'
              116  LOAD_FAST             8  'nv'
              119  CALL_FUNCTION_1       1  None
              122  LOAD_CONST               2
              125  COMPARE_OP            3  !=
              128  POP_JUMP_IF_FALSE   184  'to 184'

 L. 416       131  LOAD_FAST             2  'strict_parsing'
              134  POP_JUMP_IF_FALSE   156  'to 156'

 L. 417       137  LOAD_GLOBAL           2  'ValueError'
              140  LOAD_CONST               'bad query field: %r'
              143  LOAD_FAST             7  'name_value'
              146  BUILD_TUPLE_1         1 
              149  BINARY_MODULO    
              150  RAISE_VARARGS_2       2  None
              153  JUMP_FORWARD          0  'to 156'
            156_0  COME_FROM           153  '153'

 L. 419       156  LOAD_FAST             1  'keep_blank_values'
              159  POP_JUMP_IF_FALSE    69  'to 69'

 L. 420       162  LOAD_FAST             8  'nv'
              165  LOAD_ATTR             3  'append'
              168  LOAD_CONST               ''
              171  CALL_FUNCTION_1       1  None
              174  POP_TOP          
              175  JUMP_ABSOLUTE       184  'to 184'

 L. 422       178  CONTINUE             69  'to 69'
              181  JUMP_FORWARD          0  'to 184'
            184_0  COME_FROM           181  '181'

 L. 423       184  LOAD_GLOBAL           1  'len'
              187  LOAD_FAST             8  'nv'
              190  LOAD_CONST               1
              193  BINARY_SUBSCR    
              194  CALL_FUNCTION_1       1  None
              197  POP_JUMP_IF_TRUE    206  'to 206'
              200  LOAD_FAST             1  'keep_blank_values'
            203_0  COME_FROM           197  '197'
              203  POP_JUMP_IF_FALSE    69  'to 69'

 L. 424       206  LOAD_GLOBAL           4  'unquote'
              209  LOAD_FAST             8  'nv'
              212  LOAD_CONST               0
              215  BINARY_SUBSCR    
              216  LOAD_ATTR             5  'replace'
              219  LOAD_CONST               '+'
              222  LOAD_CONST               ' '
              225  CALL_FUNCTION_2       2  None
              228  CALL_FUNCTION_1       1  None
              231  STORE_FAST            9  'name'

 L. 425       234  LOAD_GLOBAL           4  'unquote'
              237  LOAD_FAST             8  'nv'
              240  LOAD_CONST               1
              243  BINARY_SUBSCR    
              244  LOAD_ATTR             5  'replace'
              247  LOAD_CONST               '+'
              250  LOAD_CONST               ' '
              253  CALL_FUNCTION_2       2  None
              256  CALL_FUNCTION_1       1  None
              259  STORE_FAST           10  'value'

 L. 426       262  LOAD_FAST             6  'r'
              265  LOAD_ATTR             3  'append'
              268  LOAD_FAST             9  'name'
              271  LOAD_FAST            10  'value'
              274  BUILD_TUPLE_2         2 
              277  CALL_FUNCTION_1       1  None
              280  POP_TOP          
              281  JUMP_BACK            69  'to 69'
              284  JUMP_BACK            69  'to 69'
              287  POP_BLOCK        
            288_0  COME_FROM            62  '62'

 L. 428       288  LOAD_FAST             6  'r'
              291  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `JUMP_FORWARD' instruction at offset 181
