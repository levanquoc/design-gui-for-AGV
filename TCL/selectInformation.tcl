#############################################################################
# Generated by PAGE version 5.5
#  in conjunction with Tcl version 8.6
#  Nov 04, 2020 12:40:33 PM +07  platform: Linux
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
        -menu "$top.m46" -background #234e70 -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 592x173+88+70
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
    wm title $top "Select Information"
    vTcl:DefineAlias "$top" "SELECTINFORMATION" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    menu $top.m46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    button $top.but47 \
        -activebackground #f9f9f9 -activeforeground black -background #fbf8be \
        -command pinInformation \
        -font {-family {DejaVu Sans} -size 13 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black -text Battery 
    vTcl:DefineAlias "$top.but47" "pinInformation" vTcl:WidgetProc "SELECTINFORMATION" 1
    button $top.but48 \
        -activebackground #f9f9f9 -activeforeground black -background #fbf8be \
        -command machinevisionInformation \
        -font {-family {DejaVu Sans} -size 13 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) -highlightcolor black \
        -text {Machine Vision} 
    vTcl:DefineAlias "$top.but48" "machinevisionButton" vTcl:WidgetProc "SELECTINFORMATION" 1
    button $top.but49 \
        -activebackground #f9f9f9 -activeforeground black -background #d2302c \
        -command eixt -font TkDefaultFont -foreground #f7f7f9 \
        -highlightcolor black -text Exit 
    vTcl:DefineAlias "$top.but49" "exitButton" vTcl:WidgetProc "SELECTINFORMATION" 1
    label $top.lab45 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) 
    vTcl:DefineAlias "$top.lab45" "Label1" vTcl:WidgetProc "SELECTINFORMATION" 1
    label $top.lab46 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) 
    vTcl:DefineAlias "$top.lab46" "Label2" vTcl:WidgetProc "SELECTINFORMATION" 1
    label $top.lab47 \
        -background $vTcl(actual_gui_bg) -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) 
    vTcl:DefineAlias "$top.lab47" "Label3" vTcl:WidgetProc "SELECTINFORMATION" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but47 \
        -in $top -x 0 -relx 0.135 -y 0 -rely 0.286 -width 131 -relwidth 0 \
        -height 71 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 0 -relx 0.524 -y 0 -rely 0.286 -width 141 -relwidth 0 \
        -height 71 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 0 -relx 0.878 -y 0 -width 71 -relwidth 0 -height 31 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 0 -relx 0.355 -y 0 -rely 0.376 -width 0 -relwidth 0.032 \
        -height 0 -relheight 0.22 -anchor nw -bordermode ignore 
    place $top.lab46 \
        -in $top -x 0 -relx 0.63 -y 0 -rely 0.694 -width 0 -relwidth 0.032 \
        -height 0 -relheight 0.15 -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 0 -relx 0.574 -y 0 -rely 0.809 -width 0 -relwidth 0.15 \
        -height 0 -relheight 0.035 -anchor nw -bordermode ignore 
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

