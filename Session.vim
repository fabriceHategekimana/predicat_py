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
nnoremap  ;
nnoremap   .
nnoremap ! :!
xmap S <Plug>VSurround
nmap cS <Plug>CSurround
nmap cs <Plug>Csurround
nnoremap cp :CpL 
nmap ds <Plug>Dsurround
xmap gS <Plug>VgSurround
xmap gx <Plug>NetrwBrowseXVis
nmap gx <Plug>NetrwBrowseX
onoremap in' :normal f'lvt'
onoremap in" :normal f"lvt"
nnoremap sp :split .
nnoremap tn :LfNewTab
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
nnoremap <silent> <Plug>(ale_filerename) :ALEFileRename
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
nnoremap <C-N> ;
nnoremap <F2> :call Note()
nnoremap <F1> :tabnew $MYVIMRC
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
nnoremap éco :!gnome-terminal -- tmux new-session ipython
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
nnoremap élF :call NewPane("lf -command ':one'", "extern","-b -h -p 15")
nnoremap élf :call NewPane("~/sh/one", "intern","-b -h -p 15")
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
set background=dark
set backspace=indent,eol,start
set complete=.,w,b,u,t,i,kspell
set fileencodings=ucs-bom,utf-8,default,latin1
set helplang=fr
set ignorecase
set incsearch
set laststatus=2
set matchpairs=(:),{:},[:],<:>
set omnifunc=syntaxcomplete#Complete
set path=.,/usr/include,,,**
set printoptions=paper:a4
set ruler
set runtimepath=~/.vim,~/.vim/pack/tpope/start/surround,~/.vim/pack/default/start/pythoncomplete,~/vim/tmux-client/,~/.vim/plugged/vimwiki/,~/.vim/plugged/lf.vim/,~/.vim/plugged/AutoComplPop/,~/.vim/plugged/tagbar/,~/.vim/plugged/vim-prettier/,~/.vim/plugged/ale/,~/.vim/plugged/swift.vim/,~/.vim/plugged/rainbow_csv/,~/.vim/plugged/vim-hexcolor/,/var/lib/vim/addons,/etc/vim,/usr/share/vim/vimfiles,/usr/share/vim/vim82,/usr/share/vim/vimfiles/after,/etc/vim/after,/var/lib/vim/addons/after,~/.vim/plugged/vim-hexcolor/after,~/.vim/after
set smartcase
set splitbelow
set splitright
set statusline=\ %t\ \ %#Normal#%{(mode()=='n')?'\ \ normal\ ':''}%#PmenuThumb#%{(mode()=='i')?'\ \ insert\ ':''}%#SpellRare#%{(mode()=='v')?'\ \ visual\ ':''}%#MoreMsg#%{(mode()=='c')?'\ \ command\ ':''}%#TabLineFill#%{(mode()=='r')?'\ \ replace\ ':''}%#Search#%m%#CursorLine#%=%#Normal#\ %3l:%-2c\ %#StatusLine#%3p%%\ 
set suffixes=.bak,~,.swp,.o,.info,.aux,.log,.dvi,.bbl,.blg,.brf,.cb,.ind,.idx,.ilg,.inx,.out,.toc
set noswapfile
set timeoutlen=500
set virtualedit=onemore
set wildignore=*.pyc
set wildmenu
set wildmode=list:longest,list:full
set window=28
let s:so_save = &g:so | let s:siso_save = &g:siso | setg so=0 siso=0 | setl so=-1 siso=-1
let v:this_session=expand("<sfile>:p")
silent only
silent tabonly
cd ~/sessions/predicat
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
argglobal
%argdel
$argadd cli.py
edit cli.py
let s:save_splitbelow = &splitbelow
let s:save_splitright = &splitright
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
let &splitbelow = s:save_splitbelow
let &splitright = s:save_splitright
wincmd t
let s:save_winminheight = &winminheight
let s:save_winminwidth = &winminwidth
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 73 + 74) / 148)
exe 'vert 2resize ' . ((&columns * 74 + 74) / 148)
argglobal
let s:cpo_save=&cpo
set cpo&vim
inoremap <buffer> <C-H> <Left>
inoremap <buffer> <C-L> <Right>
xnoremap <buffer> <NL> }
xnoremap <buffer>  {
nnoremap <buffer> gnc /```python
xnoremap <buffer> <silent> <F5> y:call PasteToPane()
nnoremap <buffer> <silent> <F5> :term python3 %
nnoremap <buffer> <silent> <F4> :call TmuxSplit("ipython --no-autoindent", "-v")
nnoremap <buffer> <silent> <F3> yip:call PasteToPane()
nnoremap <buffer> <Right> :call SendKeys("eog", "Right")
nnoremap <buffer> <Left> :call SendKeys("eog", "Left")
xnoremap <buffer> <C-K> {
xnoremap <buffer> <C-J> }
nnoremap <buffer> <F6> :call ChangeTargetPane()
inoremap <buffer>  <Left>
inoremap <buffer>  <Right>
nnoremap <buffer> <silent> ée yy:call PasteToPane()
nnoremap <buffer> éoi yy:call OpenImage()
nnoremap <buffer> és yiw:call SendToPane(@".".shape")
nnoremap <buffer> éh yiw:call SendToPane(@".".head()")
nnoremap <buffer> év yiw:call PasteToPane()
nnoremap <buffer> éog :!myfeh -R 10 images/ &
nnoremap <buffer> éoG :!firefox images/. &
nnoremap <buffer> éwa :call SendToPane("whos ndarray")
nnoremap <buffer> éwd :call SendToPane("whos DataFrame")
nnoremap <buffer> éwf :call SendToPane("whos function")
nnoremap <buffer> éw :call SendToPane("whos")
nnoremap <buffer> éfm :call SendToPane("from functionModule import *")
nnoremap <buffer> éd ^xx 
xnoremap <buffer> éd :normal ^xx
xnoremap <buffer> éc :normal I# 
nnoremap <buffer> éc ^i# 
nnoremap <buffer> ésr yiw:Search 
nnoremap <buffer> égrn yiw:let @/=@":call SearchFunction2() | GRename 
nnoremap <buffer> érn yiw:Rename 
inoremap <buffer> def  def ():F(i
inoremap <buffer> npde np.linalg.det()<Left>
inoremap <buffer> npdo np.dot(,_)<Left><Left><Left>
inoremap <buffer> npa np.array([])<Left><Left>
inoremap <buffer> print print()<Left>
inoreabbr <buffer> class class ():def __init__(self):#code<Up><Up><Up><Left><Left><Left>
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
setlocal cinkeys=0{,0},0),0],:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=b:#,fb:-
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i,kspell
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
set cursorline
setlocal cursorline
setlocal cursorlineopt=both
setlocal define=^\\s*\\(def\\|class\\)
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
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
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(substitute(substitute(v:fname,b:grandparent_match,b:grandparent_sub,''),b:parent_match,b:parent_sub,''),b:child_match,b:child_sub,'g')
setlocal indentexpr=GetPythonIndent(v:lnum)
setlocal indentkeys=0{,0},0),0],:,!^F,o,O,e,<:>,=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=python3\ -m\ pydoc
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal listchars=
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:],<:>
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=python3complete#Complete
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
setlocal spelllang=en
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=.py
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tagfunc=
setlocal tags=
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
let s:l = 9 - ((6 * winheight(0) + 13) / 27)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 9
normal! 0
wincmd w
argglobal
if bufexists("UnitTest.py") | buffer UnitTest.py | else | edit UnitTest.py | endif
nnoremap <buffer> gnc /```python
let s:cpo_save=&cpo
set cpo&vim
nnoremap <buffer> <F6> :call ChangeTargetPane()
xnoremap <buffer> <silent> <F5> y:call PasteToPane()
nnoremap <buffer> <silent> <F5> :term python3 %
nnoremap <buffer> <silent> <F4> :call TmuxSplit("ipython --no-autoindent", "-v")
nnoremap <buffer> <silent> <F3> yip:call PasteToPane()
nnoremap <buffer> <Right> :call SendKeys("eog", "Right")
nnoremap <buffer> <Left> :call SendKeys("eog", "Left")
nnoremap <buffer> <silent> ée yy:call PasteToPane()
nnoremap <buffer> éoi yy:call OpenImage()
nnoremap <buffer> és yiw:call SendToPane(@".".shape")
nnoremap <buffer> éh yiw:call SendToPane(@".".head()")
nnoremap <buffer> év yiw:call PasteToPane()
nnoremap <buffer> éog :!myfeh -R 10 images/ &
nnoremap <buffer> éoG :!firefox images/. &
nnoremap <buffer> éwa :call SendToPane("whos ndarray")
nnoremap <buffer> éwd :call SendToPane("whos DataFrame")
nnoremap <buffer> éwf :call SendToPane("whos function")
nnoremap <buffer> éw :call SendToPane("whos")
nnoremap <buffer> éfm :call SendToPane("from functionModule import *")
nnoremap <buffer> éd ^xx 
xnoremap <buffer> éd :normal ^xx
xnoremap <buffer> éc :normal I# 
nnoremap <buffer> éc ^i# 
inoremap <buffer> def  def ():F(i
inoremap <buffer> npde np.linalg.det()<Left>
inoremap <buffer> npdo np.dot(,_)<Left><Left><Left>
inoremap <buffer> npa np.array([])<Left><Left>
inoremap <buffer> print print()<Left>
inoreabbr <buffer> class class ():def __init__(self):#code<Up><Up><Up><Left><Left><Left>
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
setlocal cinkeys=0{,0},0),0],:,!^F,o,O,e
setlocal cinoptions=
setlocal cinwords=if,else,while,do,for,switch
setlocal colorcolumn=
setlocal comments=b:#,fb:-
setlocal commentstring=#\ %s
setlocal complete=.,w,b,u,t,i,kspell
setlocal concealcursor=
setlocal conceallevel=0
setlocal completefunc=
setlocal nocopyindent
setlocal cryptmethod=
setlocal nocursorbind
setlocal nocursorcolumn
set cursorline
setlocal cursorline
setlocal cursorlineopt=both
setlocal define=^\\s*\\(def\\|class\\)
setlocal dictionary=
setlocal nodiff
setlocal equalprg=
setlocal errorformat=
setlocal expandtab
if &filetype != 'python'
setlocal filetype=python
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
setlocal formatoptions=tcq
setlocal formatlistpat=^\\s*\\d\\+[\\]:.)}\\t\ ]\\s*
setlocal formatprg=
setlocal grepprg=
setlocal iminsert=0
setlocal imsearch=-1
setlocal include=^\\s*\\(from\\|import\\)
setlocal includeexpr=substitute(substitute(substitute(v:fname,b:grandparent_match,b:grandparent_sub,''),b:parent_match,b:parent_sub,''),b:child_match,b:child_sub,'g')
setlocal indentexpr=GetPythonIndent(v:lnum)
setlocal indentkeys=0{,0},0),0],:,!^F,o,O,e,<:>,=elif,=except
setlocal noinfercase
setlocal iskeyword=@,48-57,_,192-255
setlocal keywordprg=python3\ -m\ pydoc
setlocal nolinebreak
setlocal nolisp
setlocal lispwords=
setlocal nolist
setlocal listchars=
setlocal makeencoding=
setlocal makeprg=
setlocal matchpairs=(:),{:},[:],<:>
setlocal modeline
setlocal modifiable
setlocal nrformats=bin,octal,hex
set number
setlocal number
setlocal numberwidth=4
setlocal omnifunc=python3complete#Complete
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
setlocal spelllang=en
setlocal spelloptions=
setlocal statusline=
setlocal suffixesadd=.py
setlocal noswapfile
setlocal synmaxcol=3000
if &syntax != 'python'
setlocal syntax=python
endif
setlocal tabstop=4
setlocal tagcase=
setlocal tagfunc=
setlocal tags=
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
let s:l = 5 - ((4 * winheight(0) + 13) / 27)
if s:l < 1 | let s:l = 1 | endif
keepjumps exe s:l
normal! zt
keepjumps 5
normal! 0
lcd ~/sessions/predicat
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 73 + 74) / 148)
exe 'vert 2resize ' . ((&columns * 74 + 74) / 148)
tabnext 1
badd +0 ~/sessions/predicat/cli.py
badd +0 ~/sessions/predicat/UnitTest.py
if exists('s:wipebuf') && len(win_findbuf(s:wipebuf)) == 0
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 shortmess=filnxtToOS
let &winminheight = s:save_winminheight
let &winminwidth = s:save_winminwidth
let s:sx = expand("<sfile>:p:r")."x.vim"
if filereadable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &g:so = s:so_save | let &g:siso = s:siso_save
nohlsearch
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
