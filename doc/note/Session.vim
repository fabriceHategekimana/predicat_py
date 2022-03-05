let SessionLoad = 1
if &cp | set nocp | endif
let s:cpo_save=&cpo
set cpo&vim
imap <C-G>S <Plug>ISurround
imap <C-G>s <Plug>Isurround
imap <C-S> <Plug>Isurround
inoremap <silent> <Plug>(ale_complete) :ALEComplete
cnoremap <silent> <Plug>(ale_show_completion_menu) <Nop>
inoremap <silent> <Plug>(ale_show_completion_menu) 
inoremap <C-C> 
nnoremap <NL> }
nnoremap  {
nnoremap   .
nnoremap ! :!
nnoremap , ;
nnoremap ; ,
xmap S <Plug>VSurround
omap T" <Plug>(textobj-strings-double_quote-P)
xmap T" <Plug>(textobj-strings-double_quote-P)
nmap T" <Plug>(textobj-strings-double_quote-P)
omap T' <Plug>(textobj-strings-single_quote-P)
xmap T' <Plug>(textobj-strings-single_quote-P)
nmap T' <Plug>(textobj-strings-single_quote-P)
omap T> <Plug>(textobj-strings-balise-P)
xmap T> <Plug>(textobj-strings-balise-P)
nmap T> <Plug>(textobj-strings-balise-P)
omap Tl <Plug>(textobj-strings-liste-P)
xmap Tl <Plug>(textobj-strings-liste-P)
nmap Tl <Plug>(textobj-strings-liste-P)
omap a' <Plug>(textobj-strings-single_quote)
xmap a' <Plug>(textobj-strings-single_quote)
omap a" <Plug>(textobj-strings-liste)
xmap a" <Plug>(textobj-strings-liste)
nmap cS <Plug>CSurround
nmap cs <Plug>Csurround
nnoremap cp :CpL 
nmap ds <Plug>Dsurround
xmap gS <Plug>VgSurround
xmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
onoremap in' :normal f'lvt'
onoremap in" :normal f"lvt"
omap i' <Plug>(textobj-strings-single_quote)
xmap i' <Plug>(textobj-strings-single_quote)
omap i" <Plug>(textobj-strings-liste)
xmap i" <Plug>(textobj-strings-liste)
nnoremap sp :split .
nnoremap tn :LfNewTab
omap t" <Plug>(textobj-strings-double_quote-n)
xmap t" <Plug>(textobj-strings-double_quote-n)
nmap t" <Plug>(textobj-strings-double_quote-n)
omap t' <Plug>(textobj-strings-single_quote-n)
xmap t' <Plug>(textobj-strings-single_quote-n)
nmap t' <Plug>(textobj-strings-single_quote-n)
omap t> <Plug>(textobj-strings-balise-n)
xmap t> <Plug>(textobj-strings-balise-n)
nmap t> <Plug>(textobj-strings-balise-n)
omap tl <Plug>(textobj-strings-liste-n)
xmap tl <Plug>(textobj-strings-liste-n)
nmap tl <Plug>(textobj-strings-liste-n)
nnoremap vp :vsplit .
nmap ySS <Plug>YSsurround
nmap ySs <Plug>YSsurround
nmap yss <Plug>Yssurround
nmap yS <Plug>YSurround
nmap ys <Plug>Ysurround
nnoremap <silent> <Plug>SurroundRepeat .
xnoremap <silent> <Plug>NetrwBrowseXVis :call netrw#BrowseXVis()
nnoremap <silent> <Plug>NetrwBrowseX :call netrw#BrowseX(netrw#GX(),netrw#CheckIfRemote(netrw#GX()))
nnoremap <silent> <Plug>(ale_repeat_selection) :ALERepeatSelection
nnoremap <silent> <Plug>(ale_code_action) :ALECodeAction
nnoremap <silent> <Plug>(ale_rename) :ALERename
nnoremap <silent> <Plug>(ale_import) :ALEImport
nnoremap <silent> <Plug>(ale_documentation) :ALEDocumentation
nnoremap <silent> <Plug>(ale_hover) :ALEHover
nnoremap <silent> <Plug>(ale_find_references) :ALEFindReferences
nnoremap <silent> <Plug>(ale_go_to_type_definition_in_vsplit) :ALEGoToTypeDefinitionIn -vsplit
nnoremap <silent> <Plug>(ale_go_to_type_definition_in_split) :ALEGoToTypeDefinition -split
nnoremap <silent> <Plug>(ale_go_to_type_definition_in_tab) :ALEGoToTypeDefinition -tab
nnoremap <silent> <Plug>(ale_go_to_type_definition) :ALEGoToTypeDefinition
nnoremap <silent> <Plug>(ale_go_to_definition_in_vsplit) :ALEGoToDefinition -vsplit
nnoremap <silent> <Plug>(ale_go_to_definition_in_split) :ALEGoToDefinition -split
nnoremap <silent> <Plug>(ale_go_to_definition_in_tab) :ALEGoToDefinition -tab
nnoremap <silent> <Plug>(ale_go_to_definition) :ALEGoToDefinition
nnoremap <silent> <Plug>(ale_fix) :ALEFix
nnoremap <silent> <Plug>(ale_detail) :ALEDetail
nnoremap <silent> <Plug>(ale_lint) :ALELint
nnoremap <silent> <Plug>(ale_reset_buffer) :ALEResetBuffer
nnoremap <silent> <Plug>(ale_disable_buffer) :ALEDisableBuffer
nnoremap <silent> <Plug>(ale_enable_buffer) :ALEEnableBuffer
nnoremap <silent> <Plug>(ale_toggle_buffer) :ALEToggleBuffer
nnoremap <silent> <Plug>(ale_reset) :ALEReset
nnoremap <silent> <Plug>(ale_disable) :ALEDisable
nnoremap <silent> <Plug>(ale_enable) :ALEEnable
nnoremap <silent> <Plug>(ale_toggle) :ALEToggle
nnoremap <silent> <Plug>(ale_last) :ALELast
nnoremap <silent> <Plug>(ale_first) :ALEFirst
nnoremap <silent> <Plug>(ale_next_wrap_warning) :ALENext -wrap -warning
nnoremap <silent> <Plug>(ale_next_warning) :ALENext -warning
nnoremap <silent> <Plug>(ale_next_wrap_error) :ALENext -wrap -error
nnoremap <silent> <Plug>(ale_next_error) :ALENext -error
nnoremap <silent> <Plug>(ale_next_wrap) :ALENextWrap
nnoremap <silent> <Plug>(ale_next) :ALENext
nnoremap <silent> <Plug>(ale_previous_wrap_warning) :ALEPrevious -wrap -warning
nnoremap <silent> <Plug>(ale_previous_warning) :ALEPrevious -warning
nnoremap <silent> <Plug>(ale_previous_wrap_error) :ALEPrevious -wrap -error
nnoremap <silent> <Plug>(ale_previous_error) :ALEPrevious -error
nnoremap <silent> <Plug>(ale_previous_wrap) :ALEPreviousWrap
nnoremap <silent> <Plug>(ale_previous) :ALEPrevious
onoremap <silent> <Plug>(ale_show_completion_menu) <Nop>
vnoremap <silent> <Plug>(ale_show_completion_menu) <Nop>
nnoremap <silent> <Plug>(ale_show_completion_menu) :call ale#completion#RestoreCompletionOptions()
nnoremap <silent> <Plug>(PrettierCliPath) :PrettierCliPath
nnoremap <silent> <Plug>(PrettierCliVersion) :PrettierCliVersion
nnoremap <silent> <Plug>(PrettierCli) :PrettierCli
nnoremap <silent> <Plug>(PrettierVersion) :PrettierVersion
nnoremap <silent> <Plug>(PrettierPartial) :PrettierPartial
nnoremap <silent> <Plug>(PrettierFragment) :PrettierFragment
nnoremap <silent> <Plug>(PrettierAsync) :PrettierAsync
nnoremap <silent> <Plug>(Prettier) :Prettier
nnoremap <C-J> }
nnoremap <C-K> {
nnoremap <F12> :!clear
nnoremap <F10> :!gedit %
nnoremap <F9> :so $VIMRUNTIME/syntax/hitest.vim
nnoremap <F3> :TagbarToggle
nnoremap <F2> :call Note()
nnoremap <F1> :tabnew ~/.vimrc
inoremap  
imap S <Plug>ISurround
imap s <Plug>Isurround
imap  <Plug>Isurround
inoremap """ "A"
inoremap "" "
inoremap " ""<Left>
inoremap ((( (A)
inoremap (( (
inoremap ( ()<Left>
nnoremap éc yiw:execute "!firefox https://la-conjugaison.nouvelobs.com/du/verbe/".@".".php"
nmap àp <Plug>(Prettier)
nmap àwàm <Plug>VimwikiMakeTomorrowDiaryNote
nmap àwày <Plug>VimwikiMakeYesterdayDiaryNote
nmap àwàt <Plug>VimwikiTabMakeDiaryNote
nmap àwàw <Plug>VimwikiMakeDiaryNote
nmap àwài <Plug>VimwikiDiaryGenerateLinks
nmap àwi <Plug>VimwikiDiaryIndex
nmap àws <Plug>VimwikiUISelect
nmap àwt <Plug>VimwikiTabIndex
nmap àww <Plug>VimwikiIndex
nnoremap éf :call MyFzf()
vmap <silent> éa :call AppendToTextObject(visualmode(), 1)
vmap <silent> éi :call InsertToTextObject(visualmode(), 1)
nmap <silent> éi :set opfunc=InsertToTextObjectg@
nnoremap éq :set opfunc=DoubleQuoteOperatorg@
nmap <silent> éa :set opfunc=AppendToTextObjectg@
nnoremap ékt :g!//d
nnoremap étb :TagbarToggle
nnoremap éns /"
nnoremap éct :Ctags
nnoremap édb :cope
nnoremap èè :call MakefileFunction()
nnoremap élf :!gnome-terminal -- lf %h
nnoremap ésap :!setActualPane
xnoremap éspa :call MakeSpace()
xnoremap àa :ALECodeAction
nnoremap àa :ALECodeAction
map àf :Lf
nnoremap àr :ALERename
nnoremap àh :ALEHover
nnoremap àg :ALEGoToDefinition
inoremap [[[ [A] 
inoremap [[ [
inoremap [ []<Left>
inoremap {{{ {A} 
inoremap {{ { 
inoremap { {}<Left> 
let &cpo=s:cpo_save
unlet s:cpo_save
set autowriteall
set background=dark
set backspace=indent,eol,start
set cindent
set complete=.,w,b,u,t,i,kspell
set fileencodings=ucs-bom,utf-8,default,latin1
set formatlistpat=^\\s*\\%(\\(-\\|\\*\\|+\\)\\|\\(\\C\\%(\\d\\+\\.\\)\\)\\)\\s\\+\\%(\\[\\([\ .oOX-]\\)\\]\\s\\)\\?
set helplang=fr
set ignorecase
set incsearch
set laststatus=2
set matchpairs=(:),{:},[:],<:>
set nomodeline
set omnifunc=syntaxcomplete#Complete
set path=.,/usr/include,,,**
set printoptions=paper:a4
set ruler
set runtimepath=~/.vim,~/.vim/pack/tpope/start/surround,~/.vim/pack/default/start/pythoncomplete,~/vim/tmux-client/,~/.vim/plugged/vimwiki/,~/.vim/plugged/lf.vim/,~/.vim/plugged/AutoComplPop/,~/.vim/plugged/tagbar/,~/.vim/plugged/vim-prettier/,~/.vim/plugged/ale/,~/.vim/plugged/vim-textobj-user/,~/.vim/plugged/swift.vim/,/var/lib/vim/addons,/etc/vim,/usr/share/vim/vimfiles,/usr/share/vim/vim82,/usr/share/vim/vimfiles/after,/etc/vim/after,/var/lib/vim/addons/after,~/.vim/after
set shiftwidth=4
set smartcase
set softtabstop=4
set spelllang=fr_ch,en_us
set splitbelow
set splitright
set statusline=%#Cursor#\ VIM\ \ %#Normal#%{(mode()=='n')?'\ \ NORMAL\ ':''}%#PmenuThumb#%{(mode()=='i')?'\ \ INSERT\ ':''}%#TabLineFill#%{(mode()=='r')?'\ \ REPLACE\ ':''}%#SpellRare#%{(mode()=='v')?'\ \ VISUAL\ ':''}%#LineNr#\ %n\ %#Visual#%#CursorIM#%R%M%#Cursor#%#CursorLine#\ %t\ %=%#LineNr#\ %3l:%-2c\ %#Normal#\ %Y\ %#Cursor#%3p%%\ 
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set noswapfile
set tabstop=4
set timeoutlen=500
set virtualedit=onemore
set wildmenu
set wildmode=list:longest,list:full
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/sessions/predicat/note
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd note.md
edit note.md
argglobal
balt ~/sessions/predicat/note/Trouver\ un\ générateur\ graphique.md
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <expr> <S-Tab> vimwiki#tbl#kbd_shift_tab()
inoremap <buffer> <silent> <S-CR> :VimwikiReturn 2 2
imap <buffer> <C-L><C-M> <Plug>VimwikiListToggle
imap <buffer> <C-L><C-K> <Plug>VimwikiListPrevSymbol
imap <buffer> <C-L><C-J> <Plug>VimwikiListNextSymbol
imap <buffer> <C-T> <Plug>VimwikiIncreaseLvlSingleItem
imap <buffer> <C-D> <Plug>VimwikiDecreaseLvlSingleItem
inoremap <buffer> <C-H> <Left>
inoremap <buffer> <C-L> <Right>
nmap <buffer> 	 <Plug>VimwikiNextLink
vmap <buffer>  <Plug>VimwikiNormalizeLinkVisualCR
nmap <buffer>  <Plug>VimwikiFollowLink
nnoremap <buffer>  :!. ~/sh/cs.sh
vmap <buffer> + <Plug>VimwikiNormalizeLinkVisual
nmap <buffer> + <Plug>VimwikiNormalizeLink
nmap <buffer> - <Plug>VimwikiRemoveHeaderLevel
nmap <buffer> <D-CR> <Plug>VimwikiTabnewLink
nmap <buffer> = <Plug>VimwikiAddHeaderLevel
inoremap <buffer> ééd \begin{tikzpicture}\end{tikzpicture}
nmap <buffer> O <Plug>VimwikiListO
nmap <buffer> [= <Plug>VimwikiGoToPrevSiblingHeader
nmap <buffer> [[ <Plug>VimwikiGoToPrevHeader
nmap <buffer> [u <Plug>VimwikiGoToParentHeader
nmap <buffer> ]= <Plug>VimwikiGoToNextSiblingHeader
nmap <buffer> ]] <Plug>VimwikiGoToNextHeader
nmap <buffer> ]u <Plug>VimwikiGoToParentHeader
vmap <buffer> al <Plug>VimwikiTextObjListChildrenV
omap <buffer> al <Plug>VimwikiTextObjListChildren
vmap <buffer> ac <Plug>VimwikiTextObjColumnV
omap <buffer> ac <Plug>VimwikiTextObjColumn
vmap <buffer> a\ <Plug>VimwikiTextObjTableCellV
omap <buffer> a\ <Plug>VimwikiTextObjTableCell
vmap <buffer> aH <Plug>VimwikiTextObjHeaderSubV
omap <buffer> aH <Plug>VimwikiTextObjHeaderSub
vmap <buffer> ah <Plug>VimwikiTextObjHeaderV
omap <buffer> ah <Plug>VimwikiTextObjHeader
nmap <buffer> gw1 <Plug>VimwikiTableAlignW1
nmap <buffer> gww <Plug>VimwikiTableAlignW
nmap <buffer> gq1 <Plug>VimwikiTableAlignQ1
nmap <buffer> gqq <Plug>VimwikiTableAlignQ
noremap <buffer> <silent> gL1 :VimwikiChangeSymbolInListTo 1.
noremap <buffer> <silent> gl1 :VimwikiChangeSymbolTo 1.
noremap <buffer> <silent> gL+ :VimwikiChangeSymbolInListTo +
noremap <buffer> <silent> gl+ :VimwikiChangeSymbolTo +
noremap <buffer> <silent> gL* :VimwikiChangeSymbolInListTo *
noremap <buffer> <silent> gl* :VimwikiChangeSymbolTo *
noremap <buffer> <silent> gL- :VimwikiChangeSymbolInListTo -
noremap <buffer> <silent> gl- :VimwikiChangeSymbolTo -
nmap <buffer> gL <Plug>VimwikiRemoveCBInList
nmap <buffer> gl <Plug>VimwikiRemoveSingleCB
nmap <buffer> gLR <Plug>VimwikiRenumberAllLists
nmap <buffer> gLr <Plug>VimwikiRenumberAllLists
nmap <buffer> gLL <Plug>VimwikiIncreaseLvlWholeItem
nmap <buffer> gLl <Plug>VimwikiIncreaseLvlWholeItem
nmap <buffer> gLH <Plug>VimwikiDecreaseLvlWholeItem
nmap <buffer> gLh <Plug>VimwikiDecreaseLvlWholeItem
nmap <buffer> gll <Plug>VimwikiIncreaseLvlSingleItem
nmap <buffer> glh <Plug>VimwikiDecreaseLvlSingleItem
vmap <buffer> glp <Plug>VimwikiDecrementListItem
nmap <buffer> glp <Plug>VimwikiDecrementListItem
vmap <buffer> gln <Plug>VimwikiIncrementListItem
nmap <buffer> gln <Plug>VimwikiIncrementListItem
vmap <buffer> glx <Plug>VimwikiToggleRejectedListItem
nmap <buffer> glx <Plug>VimwikiToggleRejectedListItem
nmap <buffer> gnt <Plug>VimwikiNextTask
vmap <buffer> il <Plug>VimwikiTextObjListSingleV
omap <buffer> il <Plug>VimwikiTextObjListSingle
vmap <buffer> ic <Plug>VimwikiTextObjColumnInnerV
omap <buffer> ic <Plug>VimwikiTextObjColumnInner
vmap <buffer> i\ <Plug>VimwikiTextObjTableCellInnerV
omap <buffer> i\ <Plug>VimwikiTextObjTableCellInner
vmap <buffer> iH <Plug>VimwikiTextObjHeaderSubContentV
omap <buffer> iH <Plug>VimwikiTextObjHeaderSubContent
vmap <buffer> ih <Plug>VimwikiTextObjHeaderContentV
omap <buffer> ih <Plug>VimwikiTextObjHeaderContent
nmap <buffer> o <Plug>VimwikiListo
nnoremap <buffer> <silent> <Plug>VimwikiGoToPrevSiblingHeader :call vimwiki#base#goto_sibling(-1)
nnoremap <buffer> <silent> <Plug>VimwikiGoToNextSiblingHeader :call vimwiki#base#goto_sibling(+1)
nnoremap <buffer> <silent> <Plug>VimwikiGoToPrevHeader :call vimwiki#base#goto_prev_header()
nnoremap <buffer> <silent> <Plug>VimwikiGoToNextHeader :call vimwiki#base#goto_next_header()
nnoremap <buffer> <silent> <Plug>VimwikiGoToParentHeader :call vimwiki#base#goto_parent_header()
nnoremap <buffer> <silent> <Plug>VimwikiRemoveHeaderLevel :call vimwiki#base#RemoveHeaderLevel(v:count)
nnoremap <buffer> <silent> <Plug>VimwikiAddHeaderLevel :call vimwiki#base#AddHeaderLevel(v:count)
vnoremap <buffer> <silent> <Plug>VimwikiTextObjListSingleV :call vimwiki#lst#TO_list_item(1, 1)
onoremap <buffer> <silent> <Plug>VimwikiTextObjListSingle :call vimwiki#lst#TO_list_item(1, 0)
vnoremap <buffer> <silent> <Plug>VimwikiTextObjListChildrenV :call vimwiki#lst#TO_list_item(0, 1)
onoremap <buffer> <silent> <Plug>VimwikiTextObjListChildren :call vimwiki#lst#TO_list_item(0, 0)
vnoremap <buffer> <silent> <Plug>VimwikiTextObjColumnInnerV :call vimwiki#base#TO_table_col(1, 1)
onoremap <buffer> <silent> <Plug>VimwikiTextObjColumnInner :call vimwiki#base#TO_table_col(1, 0)
vnoremap <buffer> <silent> <Plug>VimwikiTextObjColumnV :call vimwiki#base#TO_table_col(0, 1)
onoremap <buffer> <silent> <Plug>VimwikiTextObjColumn :call vimwiki#base#TO_table_col(0, 0)
vnoremap <buffer> <silent> <Plug>VimwikiTextObjTableCellInnerV :call vimwiki#base#TO_table_cell(1, 1)
onoremap <buffer> <silent> <Plug>VimwikiTextObjTableCellInner :call vimwiki#base#TO_table_cell(1, 0)
vnoremap <buffer> <silent> <Plug>VimwikiTextObjTableCellV :call vimwiki#base#TO_table_cell(0, 1)
onoremap <buffer> <silent> <Plug>VimwikiTextObjTableCell :call vimwiki#base#TO_table_cell(0, 0)
vnoremap <buffer> <silent> <Plug>VimwikiTextObjHeaderSubContentV :call vimwiki#base#TO_header(1, 1, v:count1)
onoremap <buffer> <silent> <Plug>VimwikiTextObjHeaderSubContent :call vimwiki#base#TO_header(1, 1, v:count1)
vnoremap <buffer> <silent> <Plug>VimwikiTextObjHeaderSubV :call vimwiki#base#TO_header(0, 1, v:count1)
onoremap <buffer> <silent> <Plug>VimwikiTextObjHeaderSub :call vimwiki#base#TO_header(0, 1, v:count1)
vnoremap <buffer> <silent> <Plug>VimwikiTextObjHeaderContentV :call vimwiki#base#TO_header(1, 0, v:count1)
onoremap <buffer> <silent> <Plug>VimwikiTextObjHeaderContent :call vimwiki#base#TO_header(1, 0, v:count1)
vnoremap <buffer> <silent> <Plug>VimwikiTextObjHeaderV :call vimwiki#base#TO_header(0, 0, v:count1)
onoremap <buffer> <silent> <Plug>VimwikiTextObjHeader :call vimwiki#base#TO_header(0, 0, v:count1)
nmap <buffer> <M-Right> <Plug>VimwikiTableMoveColumnRight
nmap <buffer> <M-Left> <Plug>VimwikiTableMoveColumnLeft
nnoremap <buffer> <silent> <Plug>VimwikiTableAlignW1 :VimwikiTableAlignW 2
nnoremap <buffer> <silent> <Plug>VimwikiTableAlignW :VimwikiTableAlignW
nnoremap <buffer> <silent> <Plug>VimwikiTableAlignQ1 :VimwikiTableAlignQ 2
nnoremap <buffer> <silent> <Plug>VimwikiTableAlignQ :VimwikiTableAlignQ
vmap <buffer> <C-@> <Plug>VimwikiToggleListItem
vmap <buffer> <Nul> <Plug>VimwikiToggleListItem
nmap <buffer> <C-@> <Plug>VimwikiToggleListItem
nmap <buffer> <Nul> <Plug>VimwikiToggleListItem
vmap <buffer> <C-Space> <Plug>VimwikiToggleListItem
nmap <buffer> <C-Space> <Plug>VimwikiToggleListItem
nnoremap <buffer> <silent> <Plug>VimwikiListO :call vimwiki#u#count_exe('call vimwiki#lst#kbd_O()')
nnoremap <buffer> <silent> <Plug>VimwikiListo :call vimwiki#u#count_exe('call vimwiki#lst#kbd_o()')
nmap <buffer> <C-Up> <Plug>VimwikiDiaryPrevDay
nmap <buffer> <C-Down> <Plug>VimwikiDiaryNextDay
nmap <buffer> <S-Tab> <Plug>VimwikiPrevLink
nmap <buffer> <BS> <Plug>VimwikiGoBackLink
nmap <buffer> <C-S-CR> <Plug>VimwikiTabnewLink
nmap <buffer> <C-CR> <Plug>VimwikiVSplitLink
nmap <buffer> <S-CR> <Plug>VimwikiSplitLink
nnoremap <buffer> <F8> :call LinkImage()
nnoremap <buffer> <F7> :!zathura %:t:r.pdf &
nnoremap <buffer> <F5> :!bash ~/sh/compmd % 
nnoremap <buffer> <C-P> :!. ~/sh/cs.sh
nnoremap <buffer> <F6> :let g:pane= 
imap <buffer>  <Plug>VimwikiDecreaseLvlSingleItem
inoremap <buffer>  <Left>
inoremap <buffer> <expr> 	 vimwiki#tbl#kbd_tab()
imap <buffer>  <Plug>VimwikiListToggle
imap <buffer>  <Plug>VimwikiListPrevSymbol
imap <buffer> <NL> <Plug>VimwikiListNextSymbol
inoremap <buffer>  <Right>
inoremap <buffer> <silent>  :VimwikiReturn 1 5
imap <buffer>  <Plug>VimwikiIncreaseLvlSingleItem
nmap <buffer> àwr <Plug>VimwikiRenameFile
nmap <buffer> àwd <Plug>VimwikiDeleteFile
nmap <buffer> àwn <Plug>VimwikiGoto
nmap <buffer> àwhh <Plug>Vimwiki2HTMLBrowse
nmap <buffer> àwh <Plug>Vimwiki2HTML
nnoremap <buffer> étg yip:call ToTikzGraph()
nnoremap <buffer> éot 0y$:execute escape("!tmux new-window -c '#{pane_current_path}/".@"."'", "#")
nnoremap <buffer> éei 0y$:call EditImage()
nnoremap <buffer> éoi 0y$:call OpenImage()
nnoremap <buffer> éoP 0y$:execute "!evince ".@"." &"
nnoremap <buffer> éop 0y$:execute "!zathura ".@"." &"
nnoremap <buffer> éol 0y$:execute "!firefox ".@"." &"
nnoremap <buffer> épn :call PythonNotebook()
nnoremap <buffer> és yiw:execute 'term python3 /home/fabrice/script/synonymo.py '.@"
nnoremap <buffer> éd :.!dateI`[A]`
xnoremap <buffer> ém di``<Left>p
nnoremap <buffer> ém Bi`Ea`
nnoremap <buffer> éim i![](images/n)^<Right>a
nnoremap <buffer> éco i``````<Left><Left><Left><Up>
xnoremap <buffer> éb di****2<Left>p
nnoremap <buffer> éb vI**A**
nnoremap <buffer> éta :VimwikiTable
nnoremap <buffer> éru <Plug>VimwikiRenumberList 
nnoremap <buffer> ésr yiw:Search 
nnoremap <buffer> égrn yiw:let @/=@":call SearchFunction2() | GRename 
nnoremap <buffer> érn yiw:Rename 
inoremap <buffer> caption \begin{figure}\end{figure}<Up>\caption{}<Left>
inoremap <buffer> child \child{}<Up>
inoremap <buffer> node \node{}<Left>
inoremap <buffer> tikz \begin{tikzpicture}\end{tikzpicture}<Up>
let &cpo=s:cpo_save
unlet s:cpo_save
setlocal keymap=
setlocal noarabic
setlocal autoindent
setlocal backupcopy=
setlocal balloonexpr=
setlocal nobinary
setlocal nobreakindent
setlocal breakindentopt=
setlocal bufhidden=
setlocal buflisted
setlocal buftype=
setlocal nocindent
setlocal cinkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=
setlocal commentstring=%%%s
setlocal complete=.,w,b,u,t,i,kspell
setlocal concealcursor=
set conceallevel=2
setlocal conceallevel=2
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
set cursorline
setlocal cursorline
setlocal cursorlineopt=both
setlocal define=
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal noexpandtab
if &filetype != 'vimwiki'
setlocal filetype=vimwiki
endif
setlocal fixendofline
setlocal foldcolumn=0
setlocal foldenable
setlocal foldexpr=0
setlocal foldignore=#
setlocal foldlevel=0
setlocal foldmarker={{{,}}}
setlocal foldmethod=manual
setlocal foldminlines=1
setlocal foldnestmax=20
setlocal foldtext=foldtext()
setlocal formatexpr=
setlocal formatoptions=tqn
setlocal formatlistpat=^\\s*\\%(\\(-\\|\\*\\|+\\)\\|\\(\\C\\%(\\d\\+\\.\\)\\)\\)\\s\\+\\%(\\[\\([\ .oOX-]\\)\\]\\s\\)\\?
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=
setlocal includeexpr=
setlocal indentexpr=
setlocal indentkeys=0{,0},0),0],:,0#,!^F,o,O,e
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal listchars=
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:],<:>
setlocal nomodeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=Complete_wikifiles
setlocal path=
setlocal nopreserveindent
setlocal nopreviewwindow
setlocal quoteescape=\\
setlocal noreadonly
setlocal norelativenumber
setlocal norightleft
setlocal rightleftcmd=search
setlocal noscrollbind
setlocal scrolloff=-1
setlocal shiftwidth=4
setlocal noshortname
setlocal showbreak=
setlocal sidescrolloff=-1
setlocal signcolumn=auto
setlocal nosmartindent
setlocal softtabstop=4
setlocal nospell
setlocal spellcapcheck=[.?!]\\_[\\])'\"\	\ ]\\+
setlocal spellfile=
setlocal spelllang=fr_ch,en_us
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=.md
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'vimwiki'
setlocal syntax=vimwiki
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tagfunc=
setlocal tags=./tags,./TAGS,tags,TAGS,~/sessions/predicat/note/.vimwiki_tags
setlocal termwinkey=
setlocal termwinscroll=10000
setlocal termwinsize=
setlocal textwidth=0
setlocal thesaurus=
setlocal noundofile
setlocal undolevels=-123456
setlocal varsofttabstop=
setlocal vartabstop=
setlocal virtualedit=
setlocal wincolor=
setlocal nowinfixheight
setlocal nowinfixwidth
setlocal wrap
setlocal wrapmargin=0
silent! normal! zE
let &fdl = &fdl
let s:l = 1 - ((0 * winheight(0) + 18) / 36)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 1
normal! 0
tabnext 1
badd +8 note.md
badd +7 ~/sessions/predicat/note/Trouver\ un\ générateur\ graphique.md
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOS
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
