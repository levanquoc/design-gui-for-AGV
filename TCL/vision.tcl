#############################################################################
# Generated by PAGE version 5.5
#  in conjunction with Tcl version 8.6
#  Nov 04, 2020 03:35:32 PM +07  platform: Linux
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

proc vTclWindow.top48 {base} {
    global vTcl
    if {$base == ""} {
        set base .top48
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m49" -background #f0a07c -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 455x290+163+53
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 785 450
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Vision Information"
    vTcl:DefineAlias "$top" "visionInformation" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    menu $top.m49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    label $top.lab50 \
        -activebackground #f9f9f9 -activeforeground black -background #4a274f \
        -font {-family {DejaVu Sans} -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightcolor black -text {Camera ID} 
    vTcl:DefineAlias "$top.lab50" "Label1" vTcl:WidgetProc "visionInformation" 1
    label $top.lab51 \
        -activebackground #f9f9f9 -activeforeground black -background #4a274f \
        -font {-family {DejaVu Sans} -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightcolor black -text {Software Version} 
    vTcl:DefineAlias "$top.lab51" "Label2" vTcl:WidgetProc "visionInformation" 1
    label $top.lab52 \
        -activebackground #f9f9f9 -activeforeground black -background #4a274f \
        -font {-family {DejaVu Sans} -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightcolor black -text {Model Vison Name} 
    vTcl:DefineAlias "$top.lab52" "Label3" vTcl:WidgetProc "visionInformation" 1
    label $top.lab53 \
        -activebackground #f9f9f9 -activeforeground black -background #4a274f \
        -font {-family {DejaVu Sans} -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightcolor black -text {Deepstream Version} 
    vTcl:DefineAlias "$top.lab53" "Label4" vTcl:WidgetProc "visionInformation" 1
    label $top.lab54 \
        -activebackground #f9f9f9 -activeforeground black -background #ffffff \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black 
    vTcl:DefineAlias "$top.lab54" "cameraID" vTcl:WidgetProc "visionInformation" 1
    label $top.lab55 \
        -activebackground #f9f9f9 -activeforeground black -background #ffffff \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black 
    vTcl:DefineAlias "$top.lab55" "software_version" vTcl:WidgetProc "visionInformation" 1
    label $top.lab56 \
        -activebackground #f9f9f9 -activeforeground black -background #ffffff \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black 
    vTcl:DefineAlias "$top.lab56" "deepstream_version" vTcl:WidgetProc "visionInformation" 1
    label $top.lab57 \
        -activebackground #f9f9f9 -activeforeground black -background #ffffff \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightcolor black 
    vTcl:DefineAlias "$top.lab57" "model_vision_name" vTcl:WidgetProc "visionInformation" 1
    button $top.but58 \
        -activebackground #f9f9f9 -activeforeground black -background #d2302c \
        -command exit \
        -font {-family {DejaVu Sans} -size 13 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #f7f7f9 -highlightcolor black -text EXIT 
    vTcl:DefineAlias "$top.but58" "exitButton" vTcl:WidgetProc "visionInformation" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab50 \
        -in $top -x 0 -relx 0.044 -y 0 -rely 0.034 -width 0 -relwidth 0.484 \
        -height 0 -relheight 0.138 -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 0 -relx 0.044 -y 0 -rely 0.214 -width 0 -relwidth 0.484 \
        -height 0 -relheight 0.138 -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 0 -relx 0.048 -y 0 -rely 0.593 -width 0 -relwidth 0.484 \
        -height 0 -relheight 0.138 -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 0 -relx 0.044 -y 0 -rely 0.403 -width 0 -relwidth 0.484 \
        -height 0 -relheight 0.138 -anchor nw -bordermode ignore 
    place $top.lab54 \
        -in $top -x 0 -relx 0.558 -y 0 -rely 0.038 -width 0 -relwidth 0.352 \
        -height 0 -relheight 0.138 -anchor nw -bordermode ignore 
    place $top.lab55 \
        -in $top -x 0 -relx 0.56 -y 0 -rely 0.231 -width 0 -relwidth 0.352 \
        -height 0 -relheight 0.138 -anchor nw -bordermode ignore 
    place $top.lab56 \
        -in $top -x 0 -relx 0.563 -y 0 -rely 0.414 -width 0 -relwidth 0.352 \
        -height 0 -relheight 0.138 -anchor nw -bordermode ignore 
    place $top.lab57 \
        -in $top -x 0 -relx 0.56 -y 0 -rely 0.593 -width 0 -relwidth 0.352 \
        -height 0 -relheight 0.138 -anchor nw -bordermode ignore 
    place $top.but58 \
        -in $top -x 0 -relx 0.842 -y 0 -rely 0.817 -width 71 -relwidth 0 \
        -height 51 -relheight 0 -anchor nw -bordermode ignore 
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
Window show .top48 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

