#############################################################################
# Generated by PAGE version 5.5
#  in conjunction with Tcl version 8.6
#  Nov 03, 2020 01:53:34 PM +07  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}



    menu .pop48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 1 
    vTcl:DefineAlias ".pop48" "Popupmenu1" vTcl:WidgetProc "" 1

proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m50" -background $vTcl(actual_gui_bg) \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 735x228+55+14
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "LOGIN" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    labelframe $top.lab46 \
        \
        -font {-family {DejaVu Sans} -size 20 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground black -text LOGIN -background #7A88C0 -height 231 \
        -highlightcolor black -width 756 
    vTcl:DefineAlias "$top.lab46" "login" vTcl:WidgetProc "LOGIN" 1
    set site_3_0 $top.lab46
    label $site_3_0.lab47 \
        -activebackground #f9f9f9 -activeforeground #ffffff \
        -background #080a5e \
        -font {-family {DejaVu Sans} -size 20 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #eb2188 -highlightcolor #ffffff -text USERNAME 
    vTcl:DefineAlias "$site_3_0.lab47" "userNameLabel" vTcl:WidgetProc "LOGIN" 1
    entry $site_3_0.ent48 \
        -background white \
        -font {-family {ＭＳ ゴシック} -size 24 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 224 
    vTcl:DefineAlias "$site_3_0.ent48" "userNameEntry" vTcl:WidgetProc "LOGIN" 1
    label $site_3_0.lab45 \
        -activebackground #f9f9f9 -activeforeground black -background #080a5e \
        -font {-family {DejaVu Sans} -size 20 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #eb2188 -highlightcolor black -text PASSWORD 
    vTcl:DefineAlias "$site_3_0.lab45" "passWordLabel" vTcl:WidgetProc "LOGIN" 1
    entry $site_3_0.ent46 \
        -background white \
        -font {-family {ＭＳ ゴシック} -size 24 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -show * -width 224 
    vTcl:DefineAlias "$site_3_0.ent46" "passWordEntry" vTcl:WidgetProc "LOGIN" 1
    button $site_3_0.but48 \
        -activebackground #f9f9f9 -activeforeground black -background #4a141e \
        -command login \
        -font {-family {DejaVu Sans} -size 24 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #e2b144 -highlightcolor black -pady 0 -text LOGIN 
    vTcl:DefineAlias "$site_3_0.but48" "loginButton" vTcl:WidgetProc "LOGIN" 1
    button $site_3_0.but49 \
        -activebackground #f9f9f9 -activeforeground black -background #d2302c \
        -command quitLogin \
        -font {-family {Segoe UI} -size 24 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #f9f7f7 -highlightcolor black -pady 0 -text EXIT 
    vTcl:DefineAlias "$site_3_0.but49" "exitButton" vTcl:WidgetProc "LOGIN" 1
    button $site_3_0.but45 \
        -activebackground #f9f9f9 -activeforeground black -background #4a141e \
        -command reset \
        -font {-family {DejaVu Sans} -size 24 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #e2b144 -highlightcolor black -text RESET 
    vTcl:DefineAlias "$site_3_0.but45" "resetButton" vTcl:WidgetProc "LOGIN" 1
    place $site_3_0.lab47 \
        -in $site_3_0 -x 0 -relx 0.109 -y 0 -rely 0.184 -width 0 \
        -relwidth 0.264 -height 0 -relheight 0.194 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent48 \
        -in $site_3_0 -x 0 -relx 0.381 -y 0 -rely 0.171 -width 224 \
        -relwidth 0 -height 47 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab45 \
        -in $site_3_0 -x 0 -relx 0.107 -y 0 -rely 0.469 -width 0 \
        -relwidth 0.264 -height 0 -relheight 0.197 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent46 \
        -in $site_3_0 -x 0 -relx 0.381 -y 0 -rely 0.459 -width 224 \
        -relwidth 0 -height 47 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but48 \
        -in $site_3_0 -x 0 -relx 0.185 -y 0 -rely 0.697 -width 157 \
        -relwidth 0 -height 54 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but49 \
        -in $site_3_0 -x 0 -relx 0.635 -y 0 -rely 0.693 -width 147 \
        -relwidth 0 -height 54 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but45 \
        -in $site_3_0 -x 0 -relx 0.423 -y 0 -rely 0.706 -width 131 \
        -relwidth 0 -height 51 -relheight 0 -anchor nw -bordermode ignore 
    menu $top.m50 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab46 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1.029 -height 0 \
        -relheight 1.013 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

