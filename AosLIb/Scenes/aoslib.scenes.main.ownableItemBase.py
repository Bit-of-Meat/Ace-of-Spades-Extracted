# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: C:\TeamCity\buildAgent\work\dc8eb0b1d2cf198a\Main\client\standalone\build\pyi.win32\run_obfuscated\out00-PYZ.pyz\aoslib.scenes.main.ownableItemBase

-- Stacks of completed symbols:
START ::= |- stmts . 
_come_froms ::= \e__come_froms . COME_FROM
_ifstmts_jump ::= \e_c_stmts_opt . JUMP_FORWARD come_froms
_ifstmts_jump ::= c_stmts_opt . JUMP_FORWARD come_froms
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
c_stmts ::= _stmts . 
c_stmts ::= _stmts . lastc_stmt
c_stmts_opt ::= c_stmts . 
call ::= expr . CALL_FUNCTION_0
call ::= expr . expr CALL_FUNCTION_1
call ::= expr . expr expr CALL_FUNCTION_2
call ::= expr . expr expr expr CALL_FUNCTION_3
call ::= expr . expr expr expr expr CALL_FUNCTION_4
call ::= expr . expr expr expr expr expr expr expr expr CALL_FUNCTION_8
call ::= expr . expr kwarg CALL_FUNCTION_257
call ::= expr CALL_FUNCTION_0 . 
call ::= expr expr . CALL_FUNCTION_1
call ::= expr expr . expr CALL_FUNCTION_2
call ::= expr expr . expr expr CALL_FUNCTION_3
call ::= expr expr . expr expr expr CALL_FUNCTION_4
call ::= expr expr . expr expr expr expr expr expr expr CALL_FUNCTION_8
call ::= expr expr . kwarg CALL_FUNCTION_257
call ::= expr expr CALL_FUNCTION_1 . 
call ::= expr expr expr . CALL_FUNCTION_2
call ::= expr expr expr . expr CALL_FUNCTION_3
call ::= expr expr expr . expr expr CALL_FUNCTION_4
call ::= expr expr expr . expr expr expr expr expr expr CALL_FUNCTION_8
call ::= expr expr expr expr . CALL_FUNCTION_3
call ::= expr expr expr expr . expr CALL_FUNCTION_4
call ::= expr expr expr expr . expr expr expr expr expr CALL_FUNCTION_8
call_stmt ::= expr . POP_TOP
call_stmt ::= expr POP_TOP . 
classdefdeco1 ::= expr . classdefdeco1 CALL_FUNCTION_1
classdefdeco1 ::= expr . classdefdeco2 CALL_FUNCTION_1
come_from_opt ::= COME_FROM . 
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
continues ::= continue . 
continues ::= lastl_stmt . continue
continues ::= lastl_stmt continue . 
delete ::= expr . DELETE_ATTR
delete_subscript ::= expr . expr DELETE_SUBSCR
delete_subscript ::= expr expr . DELETE_SUBSCR
dict ::= BUILD_MAP_1 . kv3
dict ::= BUILD_MAP_1 kv3 . 
else_suitel ::= l_stmts . 
expr ::= LOAD_CONST . 
expr ::= LOAD_FAST . 
expr ::= LOAD_GLOBAL . 
expr ::= and . 
expr ::= attribute . 
expr ::= call . 
expr ::= compare . 
expr ::= dict . 
expr ::= get_iter . 
expr ::= list . 
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
for ::= SETUP_LOOP expr for_iter store for_block . POP_BLOCK \e__come_froms
for ::= SETUP_LOOP expr for_iter store for_block . POP_BLOCK _come_froms
for_block ::= \e_l_stmts_opt . JUMP_ABSOLUTE JUMP_BACK JUMP_BACK
for_block ::= \e_l_stmts_opt . JUMP_BACK
for_block ::= \e_l_stmts_opt . _come_froms JUMP_BACK
for_block ::= \e_l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt . JUMP_ABSOLUTE JUMP_BACK JUMP_BACK
for_block ::= l_stmts_opt . JUMP_BACK
for_block ::= l_stmts_opt . _come_froms JUMP_BACK
for_block ::= l_stmts_opt JUMP_BACK . 
for_block ::= l_stmts_opt \e__come_froms . JUMP_BACK
for_block ::= l_stmts_opt \e__come_froms JUMP_BACK . 
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
forelsestmt ::= SETUP_LOOP expr for_iter store for_block . POP_BLOCK else_suite \e__come_froms
forelsestmt ::= SETUP_LOOP expr for_iter store for_block . POP_BLOCK else_suite _come_froms
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
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr . c_stmts_opt JUMP_FORWARD else_suite come_froms
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr \e_c_stmts_opt . JUMP_FORWARD else_suite come_froms
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_ABSOLUTE else_suitec
ifelsestmtc ::= testexpr c_stmts_opt . JUMP_FORWARD else_suite come_froms
ifelsestmtl ::= testexpr . c_stmts_opt CONTINUE else_suitel
ifelsestmtl ::= testexpr . c_stmts_opt JUMP_BACK else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . CONTINUE else_suitel
ifelsestmtl ::= testexpr \e_c_stmts_opt . JUMP_BACK else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . CONTINUE else_suitel
ifelsestmtl ::= testexpr c_stmts_opt . JUMP_BACK else_suitel
ifelsestmtl ::= testexpr c_stmts_opt JUMP_BACK . else_suitel
ifelsestmtl ::= testexpr c_stmts_opt JUMP_BACK else_suitel . 
ifelsestmtr ::= testexpr . return_if_stmts COME_FROM returns
ifelsestmtr ::= testexpr return_if_stmts . COME_FROM returns
ifelsestmtr ::= testexpr return_if_stmts COME_FROM . returns
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
jmp_false ::= POP_JUMP_IF_FALSE . 
kv3 ::= expr . expr STORE_MAP
kv3 ::= expr expr . STORE_MAP
kv3 ::= expr expr STORE_MAP . 
l_stmts ::= _stmts . 
l_stmts ::= _stmts . lastl_stmt
l_stmts ::= continues . 
l_stmts ::= lastl_stmt . 
l_stmts_opt ::= l_stmts . 
lastl_stmt ::= ifelsestmtl . 
lastl_stmt ::= iflaststmtl . 
list ::= BUILD_LIST_0 . 
list ::= expr . expr expr expr BUILD_LIST_4
list ::= expr expr . expr expr BUILD_LIST_4
list ::= expr expr expr . expr BUILD_LIST_4
list ::= expr expr expr expr . BUILD_LIST_4
list ::= expr expr expr expr BUILD_LIST_4 . 
list_comp ::= BUILD_LIST_0 . list_iter
mkfunc ::= expr . expr expr expr expr expr expr expr LOAD_CODE MAKE_FUNCTION_8
mkfunc ::= expr expr . expr expr expr expr expr expr LOAD_CODE MAKE_FUNCTION_8
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
raise_stmt3 ::= expr . expr expr RAISE_VARARGS_3
raise_stmt3 ::= expr expr . expr RAISE_VARARGS_3
ret_and ::= expr . JUMP_IF_FALSE_OR_POP return_expr_or_cond COME_FROM
ret_or ::= expr . JUMP_IF_TRUE_OR_POP return_expr_or_cond COME_FROM
return ::= return_expr . RETURN_VALUE
return_expr ::= expr . 
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA
return_expr_lambda ::= return_expr . RETURN_VALUE_LAMBDA LAMBDA_MARKER
return_if_stmt ::= return_expr . RETURN_END_IF
return_if_stmt ::= return_expr RETURN_END_IF . 
return_if_stmts ::= _stmts . return_if_stmt
return_if_stmts ::= return_if_stmt . 
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
store ::= unpack . 
store_subscript ::= expr . expr STORE_SUBSCR
subscript ::= expr . expr BINARY_SUBSCR
subscript ::= expr expr . BINARY_SUBSCR
subscript2 ::= expr . expr DUP_TOPX_2 BINARY_SUBSCR
subscript2 ::= expr expr . DUP_TOPX_2 BINARY_SUBSCR
testexpr ::= testfalse . 
testfalse ::= expr . jmp_false
testfalse ::= expr jmp_false . 
testtrue ::= expr . jmp_true
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
   
 L. 110       115  CONTINUE             63  'to 63'
                 118  JUMP_BACK            63  'to 63'
->               121  JUMP_BACK            63  'to 63'
                 124  POP_BLOCK        
               125_0  COME_FROM            50  '50'
from aoslib.scenes.main.listPanelItemBase import ListPanelItemBase
from aoslib import strings
from aoslib.text import draw_text_with_size_validation, draw_text_with_alignment_and_size_validation, medium_aldo_ui_font
from aoslib.gui import gl, TextButton
from shared.constants import A1055
from shared.constants_shop import DLC_APPID_LIST
from shared.steam import SteamActivateGameOverlayToStore, SteamIsDemoRunning
import playlists

class OwnableItemBase(ListPanelItemBase):

    def initialize(self, name, dlc_manager, selectable_when_unowned=False, owned=None, playlist_id=None, pack_name='', filename=None, uid=None, custom_map=False, author=''):
        super(OwnableItemBase, self).initialize(name, uid=uid)
        self.filename = filename
        self.dlc_manager = dlc_manager
        self.custom_map = custom_map
        self.author = author
        if playlist_id is not None:
            self.demo = playlists.play_lists_by_id[playlist_id].demo
        else:
            self.demo = True
        self.show_unowned = show_as_unowned(name)
        if owned is not None:
            self.owned = owned
        else:
            self.owned = owns_info(name, dlc_manager, self.demo)
        self.selectable_when_unowned = selectable_when_unowned
        self.pack_name = pack_name
        if not self.owned:
            dlc_manager.append_dlc_installed_callback(self.on_dlc_installed)
        return

    def close(self):
        if not self.owned:
            self.dlc_manager.remove_dlc_installed_callback(self.on_dlc_installed)

    def draw_name(self):
        gl.glColor4f(1.0, 1.0, 1.0, 1.0)
        text_width = self.width - self.pad * 2
        text_height = self.height - self.pad * 2
        x = self.get_text_x_position()
        y = self.get_text_y_position()
        if self.owned or self.selectable_when_unowned:
            colour = self.text_colour
        else:
            colour = A1055
        if self.name != 'Untitled UGC':
            text = self.name
        else:
            text = self.filename
        draw_text_with_size_validation(text, x, y, text_width, text_height, colour, self.font, self.center_text)
        if not self.owned or self.show_unowned:
            colour = A1055
            draw_text_with_alignment_and_size_validation(strings.NOT_OWNED, x, y, text_width - self.pad_x * 2, text_height, colour, medium_aldo_ui_font, 'right')
        gl.glColor4f(1.0, 1.0, 1.0, 1.0)

    def is_selectable(self):
        return super(OwnableItemBase, self).is_selectable() and (self.owned or self.selectable_when_unowned)

    def on_dlc_installed(self, dlc_manager):
        previously_owned = self.owned
        self.owned = owns_info(self.name, dlc_manager, self.demo)
        if not previously_owned and self.owned:
            dlc_manager.remove_dlc_installed_callback(self.on_dlc_installed)


def owns_info--- This code section failed: ---

 L. 100         0  LOAD_GLOBAL           0  'SteamIsDemoRunning'
                3  CALL_FUNCTION_0       0  None
                6  POP_JUMP_IF_FALSE    13  'to 13'

 L. 101         9  LOAD_FAST             2  'demo'
               12  RETURN_END_IF    
             13_0  COME_FROM             6  '6'

 L. 102        13  BUILD_MAP_1           1  None

 L. 103        16  LOAD_CONST               'Alcatraz'
               19  LOAD_CONST               'CityOfChicago'
               22  LOAD_GLOBAL           1  'strings'
               25  LOAD_ATTR             2  'TC_TITLE'
               28  LOAD_GLOBAL           1  'strings'
               31  LOAD_ATTR             3  'VIP_MODE_TITLE'
               34  BUILD_LIST_4          4 
               37  LOAD_CONST               'mafia'
               40  STORE_MAP        
               41  STORE_FAST            3  'dlc_to_info'

 L. 105        44  BUILD_LIST_0          0 
               47  STORE_FAST            4  'required_dlc'

 L. 106        50  SETUP_LOOP           72  'to 125'
               53  LOAD_FAST             3  'dlc_to_info'
               56  LOAD_ATTR             4  'iteritems'
               59  CALL_FUNCTION_0       0  None
               62  GET_ITER         
               63  FOR_ITER             58  'to 124'
               66  UNPACK_SEQUENCE_2     2 
               69  STORE_FAST            5  'dlc'
               72  STORE_FAST            6  'info_list'

 L. 107        75  LOAD_FAST             0  'info'
               78  LOAD_FAST             6  'info_list'
               81  COMPARE_OP            6  in
               84  POP_JUMP_IF_FALSE    63  'to 63'

 L. 108        87  LOAD_FAST             5  'dlc'
               90  LOAD_FAST             4  'required_dlc'
               93  COMPARE_OP            7  not-in
             96_0  COME_FROM            84  '84'
               96  POP_JUMP_IF_FALSE    63  'to 63'

 L. 109        99  LOAD_FAST             4  'required_dlc'
              102  LOAD_ATTR             5  'append'
              105  LOAD_FAST             5  'dlc'
              108  CALL_FUNCTION_1       1  None
              111  POP_TOP          
              112  JUMP_BACK            63  'to 63'

 L. 110       115  CONTINUE             63  'to 63'
              118  JUMP_BACK            63  'to 63'
              121  JUMP_BACK            63  'to 63'
              124  POP_BLOCK        
            125_0  COME_FROM            50  '50'

 L. 111       125  SETUP_LOOP           33  'to 161'
              128  LOAD_FAST             4  'required_dlc'
              131  GET_ITER         
              132  FOR_ITER             25  'to 160'
              135  STORE_FAST            5  'dlc'

 L. 112       138  LOAD_FAST             1  'dlc_manager'
              141  LOAD_ATTR             6  'is_installed_dlc'
              144  LOAD_FAST             5  'dlc'
              147  CALL_FUNCTION_1       1  None
              150  POP_JUMP_IF_TRUE    132  'to 132'

 L. 113       153  LOAD_GLOBAL           7  'False'
              156  RETURN_END_IF    
            157_0  COME_FROM           150  '150'
              157  JUMP_BACK           132  'to 132'
              160  POP_BLOCK        
            161_0  COME_FROM           125  '125'

 L. 114       161  LOAD_GLOBAL           8  'True'
              164  RETURN_VALUE     
               -1  RETURN_LAST      

Parse error at or near `JUMP_BACK' instruction at offset 121


def show_as_unowned(info):
    if not SteamIsDemoRunning():
        return False
    if info in playlists.mapinfo.map_info:
        map_info = playlists.mapinfo.map_info[info]
        return not map_info['demo']
